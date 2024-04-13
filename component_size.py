import tkinter as tk
from tkinter import messagebox, simpledialog
from config import configure_window, create_label, create_entry, create_button
import weapons

def ask_component_size(ship_name, total_cost_so_far):
    window = tk.Tk()
    configure_window(window)

    component_prices = {
        1: 6.04,
        2: 8.35,
        3: 18.98,
        4: 76.35,
        5: 200.91
    }
    selected_sizes = {size: tk.BooleanVar() for size in component_prices.keys()}

    label = create_label(window, "Select component sizes and enter quantities:")
    label.pack(pady=10)

    entries = {}
    for size in component_prices:
        frame = tk.Frame(window, bg="#2f5b87")
        frame.pack(pady=2, fill='x', padx=10)
        check = tk.Checkbutton(frame, text=f"Size {size}", variable=selected_sizes[size],
                               bg="#2f5b87", fg="#a9c1d9", selectcolor="#1d3a57")
        check.pack(side='left')
        entry = create_entry(frame)
        entry.pack(side='left')
        entries[size] = entry

    def calculate_costs():
        total_cost = total_cost_so_far
        try:
            for size, entry in entries.items():
                if selected_sizes[size].get():
                    quantity = int(entry.get())
                    total_cost += component_prices[size] * quantity
        except ValueError:
            messagebox.showerror("Error", "Please enter valid quantities.")
            return
        window.destroy()
        weapons.ask_weapons(ship_name, total_cost)

    submit_button = create_button(window, "Next", calculate_costs)
    submit_button.pack(pady=20)

    window.mainloop()
