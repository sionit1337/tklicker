from .consts import *
from .system import *
from .gui    import *


# entrypoint
def main():
    # labels init
    labels = (
        money_label,
        level_label,
        mult_label,
        rebirth_label,
    )
    
    for i in range(len(labels)):
        labels[i].grid(
            row=i,
            column=0,
            padx=8,
            pady=8
        )
    # buttons init
    buttons = (
        money_btn,
        level_btn,
        mult_btn,
        rebirth_btn,
    )
    
    for i in range(len(buttons)):
        buttons[i].grid(
            row=i,
            column=1,
            padx=8,
            pady=8
        )
        
    save_btn.grid(
        row=0,
        column=0,
        padx=8,
        pady=8
    )
    
    load_btn.grid(
        row=1,
        column=0,
        padx=8,
        pady=8
    )
    
    version_label.grid(
        row=0,
        column=1,
        padx=8,
        pady=8
    )
    
    choice.grid(
        row=0,
        column=2,
        padx=8,
        pady=8,
    )
        
    # tabs init
    notebook.pack(
        expand=True, 
        fill="both"
    )
    
    game.grid(
        column=0, 
        row=0
    )
    
    settings.grid(
        column=1, 
        row=0
    )
    
    notebook.add(
        game, 
        text="game", 
        image=images["click"], 
        compound="left"
    )
        
    notebook.add(
        settings, 
        text="settings", 
        image=images["settings"], 
        compound="left"
    )
    
    # row center (game)
    for i in range(2): game.columnconfigure(i, weight=1)
    for i in range(4): game.rowconfigure(i, weight=1)
    
    root.mainloop()