# config.py
import tkinter as tk

font = ('Helvetica', 18)
window_width = 800
window_height = 650
background_color = "#2f5b87"
text_color = "#a9c1d9"
button_color = "#1d3a57"
button_text_color = "#a9c1d9"

def configure_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f'{window_width}x{window_height}+{x}+{y}')
    window.configure(bg=background_color)
    window.title("Space Ship Configuration")

def create_label(window, text):
    return tk.Label(window, text=text, bg=background_color, fg=text_color, font=font)

def create_entry(window):
    return tk.Entry(window, bg="white", fg="black", font=font)

def create_button(window, text, command):
    return tk.Button(window, text=text, command=command, bg=button_color, fg=button_text_color, font=font)
