# Rock Paper Scissor Game using Tkinter

#importing necessary libraries
from tkinter import *
import random
from PIL import Image, ImageTk

# Create Window
root = Tk()
root.title("Rock Paper Scissor Game")
root.geometry("600x500")

# Load Images
rock_img = ImageTk.PhotoImage(
    Image.open("rock.png").resize((120, 120))
)

paper_img = ImageTk.PhotoImage(
    Image.open("paper.png").resize((120, 120))
)

scissor_img = ImageTk.PhotoImage(
    Image.open("scissor.png").resize((120, 120))
)

# Image Dictionary
image_dict = {
    "Rock": rock_img,
    "Paper": paper_img,
    "Scissor": scissor_img
}

# Computer Choices
computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}


# Disable Buttons After Selection
def button_disable():
    b1["state"] = DISABLED
    b2["state"] = DISABLED
    b3["state"] = DISABLED


# Update Images
def update_images(player_choice, computer_choice):
    player_img_label.config(image=image_dict[player_choice])
    player_img_label.image = image_dict[player_choice]

    computer_img_label.config(image=image_dict[computer_choice])
    computer_img_label.image = image_dict[computer_choice]


# Reset Game
def reset_game():
    b1["state"] = NORMAL
    b2["state"] = NORMAL
    b3["state"] = NORMAL

    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")

    player_img_label.config(image=None)
    computer_img_label.config(image=None)

    player_img_label.image = None
    computer_img_label.image = None


# Rock Selected
def isrock():
    c_v = computer_value[str(random.randint(0, 2))]

    if c_v == "Rock":
        result = "Match Draw"
    elif c_v == "Scissor":
        result = "Player Wins"
    else:
        result = "Computer Wins"

    l1.config(text="Rock")
    l3.config(text=c_v)
    l4.config(text=result)

    update_images("Rock", c_v)
    button_disable()


# Paper Selected
def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]

    if c_v == "Paper":
        result = "Match Draw"
    elif c_v == "Rock":
        result = "Player Wins"
    else:
        result = "Computer Wins"

    l1.config(text="Paper")
    l3.config(text=c_v)
    l4.config(text=result)

    update_images("Paper", c_v)
    button_disable()


# Scissor Selected
def isscissor():
    c_v = computer_value[str(random.randint(0, 2))]

    if c_v == "Scissor":
        result = "Match Draw"
    elif c_v == "Paper":
        result = "Player Wins"
    else:
        result = "Computer Wins"

    l1.config(text="Scissor")
    l3.config(text=c_v)
    l4.config(text=result)

    update_images("Scissor", c_v)
    button_disable()


# Title
Label(
    root,
    text="Rock Paper Scissor",
    font=("Arial", 20, "bold"),
    fg="blue"
).pack(pady=10)

# Player vs Computer Text
frame = Frame(root)
frame.pack()

l1 = Label(frame, text="Player", font=("Arial", 12))
l1.pack(side=LEFT, padx=20)

l2 = Label(frame, text="VS", font=("Arial", 12, "bold"))
l2.pack(side=LEFT, padx=20)

l3 = Label(frame, text="Computer", font=("Arial", 12))
l3.pack(side=LEFT, padx=20)

# Image Section
img_frame = Frame(root)
img_frame.pack(pady=20)

Label(img_frame, text="Player", font=("Arial", 12, "bold")).grid(
    row=0, column=0, padx=50
)

Label(img_frame, text="Computer", font=("Arial", 12, "bold")).grid(
    row=0, column=1, padx=50
)

player_img_label = Label(img_frame)
player_img_label.grid(row=1, column=0, padx=50)

computer_img_label = Label(img_frame)
computer_img_label.grid(row=1, column=1, padx=50)

# Result Label
l4 = Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="white",
    width=20,
    relief="solid",
    borderwidth=2
)
l4.pack(pady=20)

# Buttons
button_frame = Frame(root)
button_frame.pack()

b1 = Button(
    button_frame,
    text="Rock",
    width=10,
    command=isrock
)

b2 = Button(
    button_frame,
    text="Paper",
    width=10,
    command=ispaper
)

b3 = Button(
    button_frame,
    text="Scissor",
    width=10,
    command=isscissor
)
# Pack Buttons
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(side=LEFT, padx=10)

# Reset Button
Button(
    root,
    text="Reset Game",
    bg="white",
    fg="red",
    command=reset_game
).pack(pady=20)

root.mainloop()