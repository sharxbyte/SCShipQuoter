import tkinter as tk
from tkinter import messagebox
from config import configure_window, create_label, create_button
import operator_seats

def ask_ship_category(ship_name):
    window = tk.Tk()
    configure_window(window)

    categories = {
        "Normal": 1.0,
        "Entry Level": 0.95,
        "Starter Ships": 0.9,
        "Drake Ships": 0.7,
        "Premium Ships": 1.25,
        "Limited/Rare Ships": 1.5
    }
    selected_categories = {category: tk.BooleanVar() for category in categories}

    label = create_label(window, "Select Ship Category:")
    label.pack(pady=10)

    for category in categories:
        tk.Checkbutton(window, text=category, variable=selected_categories[category],
                       bg="#2f5b87", fg="#a9c1d9", selectcolor="#1d3a57").pack(anchor='w')

    def submit_category():
        multiplier = 1.0
        any_selected = False  # Track if any category is selected
        for category, var in selected_categories.items():
            if var.get():
                multiplier *= categories[category]
                any_selected = True  # Mark as selected if any checkbox is checked
        
        if not any_selected:  # If no categories are selected, show an error
            messagebox.showerror("Error", "Please select at least one category.")
            return
        window.destroy()
        operator_seats.ask_operator_seats(ship_name, multiplier)

    submit_button = create_button(window, "Submit", submit_category)
    submit_button.pack(pady=20)

    window.mainloop()
