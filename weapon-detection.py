import cv2
import imutils
import datetime

# Load cascade
gun_cascade = cv2.CascadeClassifier(
    r"C:\Users\HP\Desktop\python-projects\cascade.xml"
)

if gun_cascade.empty():
    print("Error: Could not load cascade.xml")
    exit()

# Start webcam
camera = cv2.VideoCapture(0)

gun_exist = False
detection_count = 0
DETECTION_THRESHOLD = 8  # consecutive frames required

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to capture frame")
        break

    frame = imutils.resize(frame, width=500)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Improve contrast
    gray = cv2.equalizeHist(gray)

    # Light blur to reduce noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    guns = gun_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=12,
        minSize=(150, 150)
    )

    valid_detections = []

    for (x, y, w, h) in guns:
        area = w * h

        # Ignore tiny detections
        if area < 25000:
            continue

        valid_detections.append((x, y, w, h))

    # Consecutive-frame validation
    if len(valid_detections) > 0:
        detection_count += 1
    else:
        detection_count = 0
        gun_exist = False

    if detection_count >= DETECTION_THRESHOLD and not gun_exist:
        gun_exist = True
        print(
            f"Gun detected at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

    # Draw rectangles only for valid detections
    for (x, y, w, h) in valid_detections:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Gun",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f"Detection Count: {detection_count}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

    cv2.imshow("Gun Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()