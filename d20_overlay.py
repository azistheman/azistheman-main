import tkinter as tk
import random

def roll_d20():
    # Roll a 20-sided die and update the label with the result
    result = random.randint(1, 20)
    result_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("D20 Roller")

# Create a button that rolls the d20
roll_button = tk.Button(root, text="Roll D20", command=roll_d20)
roll_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
