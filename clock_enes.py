import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time)

# Creating the main window
root = tk.Tk()
root.title("Clock")

# Set the background color of the window to black
root.configure(bg='black')

# Setting up the label widget to display the time
label = tk.Label(root, font=('calibri', 130, 'bold'), background='black', foreground='#00FF00')

# Placing the clock widget in the center of the window
label.pack(anchor='center')

# Set a fixed window size
root.geometry("700x220")  # Adjust the size as needed

# Make the window non-resizable
root.resizable(False, False)

# Make the window always stay on top
root.attributes("-topmost", True)

time()  # Call the time function initially to display the current time

# Run the Tkinter event loop
root.mainloop()
