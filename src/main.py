import tkinter as tk
from tkinter import ttk
import os
import random
import json


# window
root = tk.Tk()
root.title("tklicker")
root.geometry("480x320")



# class for clicker logic
class Clicker:
    def __init__(self, val_1, val_2, val_3, val_4, price_1, price_2, price_3):
        self.values = [val_1, val_2 ,val_3, val_4]
        self.prices = (price_1, price_2, price_3)
        
        
    # increasing values
    def increase_v1(self):
        self.values[0] += round(random.uniform(1, 3)) * ((self.values[1] + 1) * (self.values[2] + 1) * (self.values[3] + 1))
        update()
        
    def increase_v2(self):
        if not self.values[0] >= self.prices[0] * (self.values[1] + 1):
            return
        
        self.values[0] -= self.prices[0] * (self.values[1] + 1)
        self.values[1] += 1
        update()
        
    def increase_v3(self):
        if not self.values[1] >= clicker.prices[1] * (self.values[2] + 1):
            return
        
        self.values[0] = 0
        self.values[1] -= clicker.prices[1] * (self.values[2] + 1)
        self.values[2] += 1
        update()
        
    def increase_v4(self):
        if not self.values[2] >= clicker.prices[2] * (self.values[3] + 1):
            return
        
        self.values[0], self.values[1], self.values[2] = (0, 0, 0)
        self.values[3] += 1
        update()


    # save system
    def make_save_data(self):
        data = {
            "money": clicker.values[0],
            "level": clicker.values[1],
            "mult": clicker.values[2],
            "rebirth": clicker.values[3]
        } # TODO: save encryption 
        
        return data

    def save(self):
        if not os.path.exists(f"{here}\\saves"):
            os.mkdir(f"{here}\\saves")
            
        with open(f"{here}\\saves\\save.json", "w") as file:
            file.write(str(json.dumps(self.make_save_data(), indent=4)))
            
            
    def load(self):
        if not os.path.exists(f"{here}\\saves"):
            os.mkdir(f"{here}\\saves")
            
        if not os.path.exists(f"{here}\\saves\\save.json"):
            with open(f"{here}\\saves\\save.json", "w") as file:
                file.write(str(json.dumps(self.make_save_data(), indent=4)))
                
            return
            
        with open(f"{here}\\saves\\save.json", "r") as file:
            data = json.load(file)
            
        self.values = list(data.values())
        update()


clicker = Clicker(0, 0, 0, 0, 50, 15, 5)

# update labels
def update():
    labels[0]["text"] = f"money: ${clicker.values[0]}"
    labels[1]["text"] = f"level: {clicker.values[1]}"
    labels[2]["text"] = f"multiplier: x{clicker.values[2]}"
    labels[3]["text"] = f"rebirths: {clicker.values[3]}"
    
    buttons[0]["text"] = f"click me! (gives ${(clicker.values[1] + 1) * (clicker.values[2] + 1) * (clicker.values[3] + 1)}-${3 * ((clicker.values[1] + 1) * (clicker.values[2] + 1) * (clicker.values[3] + 1))})"
    buttons[1]["text"] = f"level up! (costs ${clicker.prices[0] * (clicker.values[1] + 1)})"
    buttons[2]["text"] = f"upgrade multiplier! (costs {clicker.prices[1] * (clicker.values[2] + 1)} levels)"
    buttons[3]["text"] = f"REBIRTH! (costs {clicker.prices[2] * (clicker.values[3] + 1)} multipliers)"


# images
here = os.path.dirname(os.path.abspath(__file__))
images = (tk.PhotoImage(file=f"{here}\\sprites\\labels\\coin.png"),
        tk.PhotoImage(file=f"{here}\\sprites\\labels\\level.png"),
        tk.PhotoImage(file=f"{here}\\sprites\\labels\\mult.png"),
        tk.PhotoImage(file=f"{here}\\sprites\\labels\\rebirth.png"),
        tk.PhotoImage(file=f"{here}\\sprites\\buttons\\click.png"),
        tk.PhotoImage(file=f"{here}\\sprites\\buttons\\lvlup.png"),
        tk.PhotoImage(file=f"{here}\\sprites\\buttons\\multup.png"),
        tk.PhotoImage(file=f"{here}\\sprites\\buttons\\rebirth.png"),
        tk.PhotoImage(file=f"{here}\\sprites\\buttons\\save.png"),
        tk.PhotoImage(file=f"{here}\\sprites\\buttons\\load.png"),
        tk.PhotoImage(file=f"{here}\\sprites\\buttons\\settings.png"))

# tabs
notebook = ttk.Notebook()
game = ttk.Frame(notebook)
settings = ttk.Frame(notebook)

# labels
labels = (tk.Label(game, text=f"money: ${clicker.values[0]}", image=images[0], compound="left"),
        tk.Label(game, text=f"level: {clicker.values[1]}", image=images[1], compound="left"),
        tk.Label(game, text=f"multiplier: x{clicker.values[2]}", image=images[2], compound="left"),
        tk.Label(game, text=f"rebirths: {clicker.values[3]}", image=images[3], compound="left"))

# buttons
buttons = (ttk.Button(game, text="click me!", command=clicker.increase_v1, image=images[4], compound="left"),
            ttk.Button(game, text="level up!", command=clicker.increase_v2, image=images[5], compound="left"),
            ttk.Button(game, text="upgrade multiplier!", command=clicker.increase_v3, image=images[6], compound="left"),
            ttk.Button(game, text="REBIRTH!", command=clicker.increase_v4, image=images[7], compound="left"),
            ttk.Button(settings, text="save game", command=clicker.save, image=images[8], compound="left"),
            ttk.Button(settings, text="load game", command=clicker.load, image=images[9], compound="left"))

# labels init
for label in labels:
    label.grid(row=labels.index(label),
                column=0,
                padx=8,
                pady=8)

# buttons init
for button in buttons:
    button.grid(row=buttons.index(button),
                column=1,
                padx=8,
                pady=8)
    
notebook.pack(expand=True, fill="both")
game.grid(column=0, row=0)
settings.grid(column=1, row=0)

# row center
for i in range(2): game.columnconfigure(i, weight=1)
for i in range(4): game.rowconfigure(i, weight=1)

notebook.add(game, text="game", image=images[4], compound="left")
notebook.add(settings, text="settings", image=images[10], compound="left")

root.mainloop()