import tkinter as tk
from tkinter import messagebox
from config import configure_window, create_label, create_entry, create_button
import results

def ask_storage(ship_name, total_cost_so_far):
    window = tk.Tk()
    configure_window(window)

    label = create_label(window, "Enter storage capacity in SCU (Standard Cargo Units):")
    label.pack(pady=10)

    entry = create_entry(window)
    entry.pack(pady=5)

    def submit_storage():
        try:
            scu = float(entry.get())
            price_per_scu = 0.18  # Price per Standard Cargo Unit
            storage_cost = scu * price_per_scu
            total_cost = total_cost_so_far + storage_cost
        except ValueError:
            messagebox.showerror("Error", "Invalid storage capacity.")
            return
        window.destroy()
        results.show_results(ship_name, total_cost)

    submit_button = create_button(window, "Next", submit_storage)
    submit_button.pack(pady=20)

    window.mainloop()
