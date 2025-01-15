import tkinter as tk
from .system   import Clicker, SaveSystem
from .consts   import VERSION, HERE      , RES, MAX_SLOTS
from tkinter   import ttk


# window
root = tk.Tk()
root.title("tklicker")
root.geometry(f"{RES[0]}x{RES[1]}")
root.resizable(False, False)

# systems
clicker = Clicker((50, 25, 10))
saves   = SaveSystem(clicker)

# tabs
notebook = ttk.Notebook()
settings = ttk.Frame(notebook)
game     = ttk.Frame(notebook)
    
# images lookup
images = {
    # labels
    "coin":        tk.PhotoImage(file=f"{HERE}\\sprites\\labels\\coin.png"),
    "level":       tk.PhotoImage(file=f"{HERE}\\sprites\\labels\\level.png"),
    "mult":        tk.PhotoImage(file=f"{HERE}\\sprites\\labels\\mult.png"),
    "rebirth":     tk.PhotoImage(file=f"{HERE}\\sprites\\labels\\rebirth.png"),
    # buttons
    "click":       tk.PhotoImage(file=f"{HERE}\\sprites\\buttons\\click.png"),
    "level_up":    tk.PhotoImage(file=f"{HERE}\\sprites\\buttons\\lvlup.png"),
    "mult_up":     tk.PhotoImage(file=f"{HERE}\\sprites\\buttons\\multup.png"),
    "rebirth_btn": tk.PhotoImage(file=f"{HERE}\\sprites\\buttons\\rebirth.png"),
    # settings
    "save":        tk.PhotoImage(file=f"{HERE}\\sprites\\buttons\\save.png"),
    "load":        tk.PhotoImage(file=f"{HERE}\\sprites\\buttons\\load.png"),
    "settings":    tk.PhotoImage(file=f"{HERE}\\sprites\\buttons\\settings.png"),
    "info":        tk.PhotoImage(file=f"{HERE}\\sprites\\labels\\info.png"),
}
    
# labels
money_label = tk.Label(
    game, 
    textvariable=clicker.tk_vars[0], 
    image=images["coin"], 
    compound="left"
)

level_label = tk.Label(
    game, 
    textvariable=clicker.tk_vars[1], 
    image=images["level"], 
    compound="left"
)

mult_label = tk.Label(
    game, 
    textvariable=clicker.tk_vars[2], 
    image=images["mult"], 
    compound="left"
)

rebirth_label = tk.Label(
    game, 
    textvariable=clicker.tk_vars[3], 
    image=images["rebirth"], 
    compound="left"
)

version_label = tk.Label(
    settings,
    text=f"v{VERSION}",
    image=images["info"],
    compound="left"
)

# buttons
money_btn = ttk.Button(
    game, 
    text="click me!", 
    command=lambda: clicker.upgrade(0), 
    image=images["click"], 
    compound="left"
)

level_btn = ttk.Button(
    game, 
    text="level up!", 
    command=lambda: clicker.upgrade(1), 
    image=images["level_up"], 
    compound="left"
)

mult_btn = ttk.Button(
    game, 
    text="upgrade multiplier!", 
    command=lambda: clicker.upgrade(2), 
    image=images["mult_up"], 
    compound="left"
)
rebirth_btn = ttk.Button(
    game, 
    text="REBIRTH!", 
    command=lambda: clicker.upgrade(3), 
    image=images["rebirth_btn"], 
    compound="left"
)

# saves
choice = ttk.Spinbox(settings, from_=0, to=MAX_SLOTS)

def slot(): 
    try: return int(choice.get())
    except: return MAX_SLOTS

save_btn = ttk.Button(
    settings, 
    text="save game", 
    command=lambda: saves.manage("save", slot()), 
    image=images["save"], 
    compound="left"
)

load_btn = ttk.Button(
    settings, 
    text="load game", 
    command=lambda: saves.manage("load", slot()), 
    image=images["load"], 
    compound="left"
)
