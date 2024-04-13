import tkinter as tk
from tkinter import messagebox
from config import configure_window, create_label, create_entry, create_button
import missile_slots

def ask_weapons(ship_name, total_cost_so_far):
    window = tk.Tk()
    configure_window(window)

    weapon_prices = {
        1: 4.28,
        2: 9.15,
        3: 14.09,
        4: 23.12,
        5: 34.50,
        6: 88.15,
        7: 128.10,
        8: 172.36,
        9: 214.71,
        10: 247.64
    }
    selected_weapon_sizes = {tier: tk.BooleanVar() for tier in weapon_prices.keys()}

    label = create_label(window, "Select weapon tiers and enter quantities of each:")
    label.pack(pady=10)

    entries = {}
    for tier in weapon_prices:
        frame = tk.Frame(window, bg="#2f5b87")
        frame.pack(pady=2, fill='x', padx=10)
        check = tk.Checkbutton(frame, text=f"Weapon Tier {tier}", variable=selected_weapon_sizes[tier],
                               bg="#2f5b87", fg="#a9c1d9", selectcolor="#1d3a57")
        check.pack(side='left')
        entry = create_entry(frame)
        entry.pack(side='left')
        entries[tier] = entry

    def calculate_costs():
        total_cost = total_cost_so_far
        try:
            for tier, entry in entries.items():
                if selected_weapon_sizes[tier].get():
                    quantity = int(entry.get())
                    total_cost += weapon_prices[tier] * quantity
        except ValueError:
            messagebox.showerror("Error", "Please enter valid quantities.")
            return
        window.destroy()
        missile_slots.ask_missile_slots(ship_name, total_cost)

    submit_button = create_button(window, "Next", calculate_costs)
    submit_button.pack(pady=20)

    window.mainloop()
