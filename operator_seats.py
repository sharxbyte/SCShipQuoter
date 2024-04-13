import tkinter as tk
from tkinter import messagebox
from config import configure_window, create_label, create_entry, create_button
import component_size

def ask_operator_seats(ship_name, multiplier):
    window = tk.Tk()
    configure_window(window)

    label = create_label(window, "Enter number of Pilot + Operator seats:")
    label.pack(pady=10)

    entry = create_entry(window)
    entry.pack(pady=5)

    def submit_seats():
        try:
            number_of_seats = int(entry.get())
            seat_price = 12  # Fixed price per seat
            seats_cost = number_of_seats * seat_price
            total_cost = seats_cost * multiplier
        except ValueError:
            messagebox.showerror("Error", "Invalid number of seats.")
            return
        window.destroy()
        component_size.ask_component_size(ship_name, total_cost)

    submit_button = create_button(window, "Next", submit_seats)
    submit_button.pack(pady=20)

    window.mainloop()
