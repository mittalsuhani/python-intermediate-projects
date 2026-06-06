import tkinter as tk
import time
from tkinter import Label

root= tk.Tk()
root.title("Digital Clock")
# function to display time
def present_time():
    display_time=time.strftime("%H:%M:%S %p") # display time in 12 hour format with AM/PM
    digi_clock.config(text=display_time) # update the clock label with the current time
    digi_clock.after(1000, present_time) # update the time every 1000 milliseconds (1 second)


# create a label to display the clock with a specific font, background color, and foreground color
digi_clock=Label(root, font = ("ds-digital", 80), background = "black", foreground = "cyan")
digi_clock.pack(anchor='center')

present_time() #calls the function to start the clock

# start the main event loop to keep the application running
root.mainloop()

