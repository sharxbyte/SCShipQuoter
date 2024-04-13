import tkinter as tk
from tkinter import messagebox
from config import configure_window, create_label, create_entry, create_button
import storage

def ask_missile_slots(ship_name, total_cost_so_far):
    window = tk.Tk()
    configure_window(window)

    label = create_label(window, "Enter number of missile slots (converted to size 1):")
    label.pack(pady=10)

    entry = create_entry(window)
    entry.pack(pady=5)

    def submit_slots():
        try:
            missile_count = int(entry.get())
            cost_per_slot = 1  # Cost per missile slot
            missile_cost = missile_count * cost_per_slot
            total_cost = total_cost_so_far + missile_cost
        except ValueError:
            messagebox.showerror("Error", "Invalid number of slots.")
            return
        window.destroy()
        storage.ask_storage(ship_name, total_cost)

    submit_button = create_button(window, "Next", submit_slots)
    submit_button.pack(pady=20)

    window.mainloop()
