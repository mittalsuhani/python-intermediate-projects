from tkinter import *
import calendar

def show_calendar():
    year = int(year_entry.get())

    cal = calendar.calendar(year)

    output.delete("1.0", END)  # Clear previous content
    output.insert(END, cal)

root = Tk()
root.configure(bg="lightblue")

root.title("Calendar GUI")
root.geometry("700x500")

# Heading
name = Label(root, text="Calendar GUI", font=("Arial", 20), bg="lightblue")
name.grid(row=0, column=0, columnspan=2, pady=10)

# Year input
year_label = Label(root, text="Enter Year:", font=("Arial", 14), bg="lightblue")
year_label.grid(row=1, column=0, padx=10, pady=10)

year_entry = Entry(root, font=("Arial", 14))
year_entry.grid(row=1, column=1, padx=10, pady=10)

# Button
show_button = Button(root, text="Show Calendar", command=show_calendar)
show_button.grid(row=2, column=0, columnspan=2, pady=10)

# Output area
output = Text(root, width=80, height=20)
output.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()