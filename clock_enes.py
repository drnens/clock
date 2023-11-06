import tkinter as tk
from time import strftime
import requests

def get_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            data = response.json()
            content = data["content"]
            author = data["author"]
            return f'"{content}"\n- {author}'
        else:
            return "Failed to fetch a quote"
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def update_quote():
    quote = get_random_quote()
    quote_label.config(text=quote)
    quote_label.after(20*60*500, update_quote) # Duration time is about 20 mins.

def update_time():
    current_time = strftime('%H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time) 

# Creating the main window
root = tk.Tk()
root.title("Focus Clock")
root.configure(bg='black')

time_label = tk.Label(root, 
                      font=('calibri', 100, 'bold'), 
                      background='black', 
                      foreground='#00FF00')  # Dark green color
time_label.pack(anchor='center')

quote_label = tk.Label(root, font=('calibri', 14, 'italic'), background='black', foreground='white', wraplength=400)
quote_label.pack(anchor='s', pady=20)  

root.geometry("600x370")  # Adjust
root.resizable(False, False)
root.attributes("-topmost", True)

update_time()  
update_quote()  

if __name__ =='__main__':
    root.mainloop()
