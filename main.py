import tkinter as tk
from tkinter import messagebox
from config import configure_window, create_label, create_entry, create_button
import ship_category

def main():
    def start_data_collection():
        ship_name = ship_name_entry.get()
        if not ship_name:
            messagebox.showerror("Error", "Please enter a ship name.")
            return
        root.destroy()
        ship_category.ask_ship_category(ship_name)

    root = tk.Tk()
    configure_window(root)

    label = create_label(root, "Enter Ship Name:")
    label.pack(pady=10)

    ship_name_entry = create_entry(root)
    ship_name_entry.pack(pady=5)

    begin_button = create_button(root, "Begin", start_data_collection)
    begin_button.pack(pady=20)

    exit_button = create_button(root, "Exit", root.quit)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
