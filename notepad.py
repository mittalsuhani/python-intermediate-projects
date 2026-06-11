import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = tk.Tk()
root.title("Notepad")
root.geometry("900x600")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=0, minsize=120)
root.columnconfigure(1, weight=1)

def saving_file():
    file_location=asksaveasfilename(
        defaultextension=".txt"
        ,filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not file_location:
        return
    with open(file_location,"w") as file:
        text=text_edit.get(1.0,tk.END)
        file.write(text)
        root.title(f"Notepad - {file_location}")


def opening_file():
    file_location=askopenfilename(
        filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not file_location:
        return
    text_edit.delete(1.0,tk.END)
    with open(file_location,"r") as file:
        text=file.read()
        text_edit.insert(tk.END,text)
        root.title(f"Notepad - {file_location}")


text_edit = tk.Text(root)

frame_button = tk.Frame(root, relief=tk.RAISED, bd=2)
frame_button.grid(row=0, column=0, sticky="ns")

button_open = tk.Button(frame_button, text="Open", command=opening_file)
button_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

button_save = tk.Button(frame_button, text="Save", command=saving_file)
button_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

text_edit.grid(row=0, column=1, sticky="nsew")
root.mainloop()



