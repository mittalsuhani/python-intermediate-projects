import cv2 # OpenCV library for computer vision tasks

a = cv2.VideoCapture(0) # Initialize video capture from the default camera (index 0)

# recognize that the camera may not be available or accessible, so we check if it opened successfully
if not a.isOpened():
    print("Cannot open camera")
    exit()
# Load the Haar cascade for frontal face detection. 
# #The path is constructed using OpenCV's built-in data directory for cascades.
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Check if the cascade was loaded successfully. If the file is missing or the path is incorrect, it will be empty.
if face_cascade.empty():
    print("Cascade file not loaded")
    exit()

# infinite loop to continuously capture frames from the webcam and perform face detection
while True:
    ret, frame = a.read()

    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangles around detected faces and label them
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Add text label above the rectangle to indicate that a face has been detected
        cv2.putText(
            frame,
            "Face Detected",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            2
        )

    # Display the resulting frame with detected faces in a window titled "frame"
    cv2.imshow("frame", frame)

    # press q to exit the loop and close the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows to free up resources
a.release()
cv2.destroyAllWindows()
