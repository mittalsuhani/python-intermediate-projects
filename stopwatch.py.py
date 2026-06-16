import tkinter as tk # used to create gui applications
import time  # used to track time for the stopwatch


class Stopwatch(tk.Frame):    #Creates a custom widget that inherits from Tkinter's Frame.
    def __init__(self, window=None):
        super().__init__(window)
        self.window = window

        # Stopwatch variables
        self.running = False    # checks whether stopwatch is running
        self.start_time = 0     #  stores the time when the stopwatch was started
        self.elapsed_time = 0   #stores elspsed time

        self.create_widgets()     # Creates labels and buttons.

    def create_widgets(self):
        # Time display label
        self.time_label = tk.Label(
            self,
            text="00:00:00",
            font=("Helvetica", 48)
        )
        self.time_label.pack(pady=20)

        # Buttons
        self.start_button = tk.Button(
            self,
            text="Start",
            command=self.start
        )
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(
            self,
            text="Stop",
            command=self.stop
        )
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(
            self,
            text="Reset",
            command=self.reset
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.exit_button = tk.Button(
            self,
            text="Exit",
            command=self.window.destroy
        )
        self.exit_button.pack(side=tk.LEFT, padx=10)

    def start(self):
        """Start the stopwatch"""
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_time()

    def stop(self):
        """Pause the stopwatch"""
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time

    def reset(self):
        """Reset the stopwatch"""
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")

    def update_time(self):
        """Update stopwatch display"""
        if self.running:
            self.elapsed_time = time.time() - self.start_time

            total_seconds = int(self.elapsed_time)

            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60

            self.time_label.config(
                text=f"{hours:02d}:{minutes:02d}:{seconds:02d}"           # changes displayed text 
            )

            self.after(1000, self.update_time)      # Schedules update_time() to run again after 1000 milliseconds (1 second).
                                                        # This creates the stopwatch effect.


# Main window
root = tk.Tk()
root.title("Stopwatch")
root.geometry("500x200")

obj = Stopwatch(root)        # Creates stopwatch instance.
obj.pack(pady=20)

root.mainloop()        # Starts the Tkinter event loop and keeps the window running