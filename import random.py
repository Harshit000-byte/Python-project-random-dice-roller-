import tkinter as tk
import random

class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")
        
        # Label to display the dice roll result
        self.result_label = tk.Label(root, text="Click 'Roll' to roll the dice!", font=("Helvetica", 16))
        self.result_label.pack(pady=20)
        
        # Dice image placeholder
        self.dice_label = tk.Label(root, text="🎲", font=("Helvetica", 100))
        self.dice_label.pack(pady=20)

        # Button to roll the dice
        self.roll_button = tk.Button(root, text="Roll", font=("Helvetica", 14), command=self.roll_dice)
        self.roll_button.pack(pady=20)
    
    def roll_dice(self):
        # Animation of the dice rolling
        for _ in range(10):
            # Display random numbers to simulate dice rolling animation
            random_roll = random.randint(1, 6)
            self.dice_label.config(text=f"{random_roll}")
            self.root.update()
            self.root.after(100)  # Delay in milliseconds
        
        # Final dice roll result
        result = random.randint(1, 6)
        self.dice_label.config(text=f"{result}")
        self.result_label.config(text=f"You rolled a {result}!")

# Create the main window
root = tk.Tk()
# Create the dice roller app
app = DiceRollerApp(root)
# Start the GUI event loop
root.mainloop()
