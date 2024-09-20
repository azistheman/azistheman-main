import tkinter as tk
from tkinter import ttk
import random

def roll_dice(sides, count):
    return [random.randint(1, sides) for _ in range(count)]

def show_result(dice_type, count):
    results = roll_dice(dice_type, count)
    total = sum(results)
    result_str = (f"Rolling {count}d{dice_type}:\n" 
                  + ', '.join(map(str, results))
                  + f"\nTotal: {total}")
    result_label.config(text=result_str)

def roll_custom_dice():
    try:
        sides = int(sides_entry.get())
        count = int(count_entry.get())
        if sides <= 0 or count <= 0:
            result_label.config(text="Please enter positive integers.")
            return
        show_result(sides, count)
    except ValueError:
        result_label.config(text="Please enter valid integers.")

# Create the main window
root = tk.Tk()
root.title("Dice Roller")

# Create and pack the result label
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Create a frame for dice type dropdowns
dropdown_frame = tk.Frame(root)
dropdown_frame.pack(pady=10)

# Define dice options with their counts
dice_options = {
    4: [1, 2, 3, 4],
    6: [1, 2, 3, 4, 6],
    8: [1, 2, 3, 4],
    10: [1, 2, 3, 4, 6],
    12: [1, 2, 3, 4],
    20: [1, 2, 3, 4]
}

# Create dropdowns for each dice type
def create_dropdown(dice_type, options):
    selected_count = tk.IntVar(value=options[0])
    
    def on_select(value):
        show_result(dice_type, value)
    
    label = tk.Label(dropdown_frame, text=f"d{dice_type}:")
    label.pack(anchor=tk.W)
    
    option_menu = tk.OptionMenu(dropdown_frame, selected_count, *options, command=on_select)
    option_menu.pack(pady=5, fill=tk.X)

for dice_type, counts in dice_options.items():
    create_dropdown(dice_type, counts)

# Create a frame for custom dice inputs
custom_frame = tk.Frame(root)
custom_frame.pack(pady=10)

# Add widgets for custom dice input
tk.Label(custom_frame, text="Number of sides:").pack(side=tk.TOP, padx=5)
sides_entry = tk.Entry(custom_frame, width=5)
sides_entry.pack(side=tk.TOP, padx=5)

tk.Label(custom_frame, text="Number of dice:").pack(side=tk.TOP, padx=5)
count_entry = tk.Entry(custom_frame, width=5)
count_entry.pack(side=tk.TOP, padx=5)

roll_custom_button = tk.Button(custom_frame, text="Roll Custom Dice", command=roll_custom_dice)
roll_custom_button.pack(side=tk.TOP, pady=5)

# Start the Tkinter event loop
root.mainloop()
