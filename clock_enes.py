import tkinter as tk
from time import strftime
import requests
import tkinter as tk
from time import strftime
import requests

def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        content = data["content"]
        author = data["author"]
        return f'"{content}"\n- {author}'
    else:
        return "Failed to fetch a quote"

def update_quote():
    quote = get_random_quote()
    quote_label.config(text=quote)
    quote_label.after(20*60*500, update_quote)

def update_time():
    current_time = strftime('%H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)  # Update time every second

# Creating the main window
root = tk.Tk()
root.title("Focus Clock")

# Set the background color of the window to black
root.configure(bg='black')

# Setting up the label widget to display the time
time_label = tk.Label(root, font=('calibri', 100, 'bold'), background='black', foreground='#00FF00')  # Dark green color
time_label.pack(anchor='center')

# Setting up the label widget to display random quotes
quote_label = tk.Label(root, font=('calibri', 14, 'italic'), background='black', foreground='white', wraplength=400)
quote_label.pack(anchor='s', pady=20)  # Place it below the time_label

# Set a fixed window size
root.geometry("600x370")  # Adjust the size as needed

# Make the window non-resizable
root.resizable(False, False)

# Make the window always stay on top
root.attributes("-topmost", True)

update_time()  # Call the update_time function initially to display the current time
update_quote()  # Call the update_quote function initially to display a quote

if __name__ =='__main__':
    root.mainloop()