import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time)

root = tk.Tk()
root.title("Clock")

# background color
root.configure(bg='black')

label = tk.Label(root, font=('calibri', 130, 'bold'), background='black', foreground='#00FF00')

label.pack(anchor='center')

root.geometry("700x220")  # Adjust the size as needed

root.resizable(False, False)

# Make the window always stay on top
root.attributes("-topmost", True)

time()  

root.mainloop()
