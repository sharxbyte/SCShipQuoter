import tkinter as tk
from tkinter import messagebox
from config import configure_window, create_label, create_button

def show_results(ship_name, total_cost):
    window = tk.Tk()
    configure_window(window)

    result_text = f"Total Estimated Cost for '{ship_name}' Under New Model: ${total_cost:.2f}"
    label = create_label(window, result_text)
    label.pack(pady=20)

    close_button = create_button(window, "Close", window.destroy)
    close_button.pack(pady=20)

    window.mainloop()
