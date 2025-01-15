from .consts import VERSION  , HERE
from tkinter import StringVar
from random  import randint
from typing  import Literal
from json    import dumps    , load
from math    import prod
from os      import mkdir    , path


# class for clicker logic
class Clicker:
    def __init__(self, prices: tuple[int, int, int]):
        self.values = [0, 0, 0, 0]
        
        self.prices = prices
        
        self.tk_vars = [
            # for updating labels
            StringVar(value=f"money: ${self.values[0]}"),
            StringVar(value=f"level: {self.values[1]}"),
            StringVar(value=f"multiplier: x{self.values[2]}"),
            StringVar(value=f"rebirth: #{self.values[3]}"),
        ]
        
    def _update_vars(self):
        self.tk_vars[0].set(f"money: ${self.values[0]}")
        self.tk_vars[1].set(f"level: {self.values[1]}")
        self.tk_vars[2].set(f"multiplier: x{self.values[2]}")
        self.tk_vars[3].set(f"rebirth: #{self.values[3]}")
        
    def upgrade(self, index: Literal[0, 1, 2, 3]):        
        onclick = prod(i + 1 for i in self.values[index + 1:])
            
        if index == 0: # click on the first button
            self.values[index] += randint(1, 3) * onclick
            self._update_vars()
            return
            
        price = self.prices[index - 1] * (self.values[index] + 1)
            
        if not self.values[index - 1] >= price: return
            
        self.values[index - 1] -= price
        if index == 3: self.values[:2] = [0, 0, 0]
        self.values[index] += onclick # yes
        
        self._update_vars()


class SaveSystem:
    def __init__(self, clicker: Clicker):
        self.clicker = clicker
        
    @property
    def save_data(self):
        data = {
            "values": { # easier iteration             
                "money":   self.clicker.values[0],
                "level":   self.clicker.values[1],
                "mult":    self.clicker.values[2],
                "rebirth": self.clicker.values[3],
            },
            "version": VERSION,
        } 
        
        return data

    def _save(self, filename: str, data: dict | None = None):
        if data is None: data = self.save_data
        for_save = dumps(data, indent=4)
        
        if not path.exists(f"{HERE}\\saves"): mkdir(f"{HERE}\\saves")
            
        with open(f"{HERE}\\saves\\{filename}.json", "w") as file: file.write(for_save)
            
    def _load_data(self, data: dict):    
        if data["version"] != VERSION: raise IncompatibleSaveException(VERSION, data["version"])
                
        self.clicker.values = list(data["values"].values())
        self.clicker._update_vars()
        
    def _load_file(self, filename: str):
        if not path.exists(f"{HERE}\\saves\\{filename}.json"):
            self._save(filename)
            return
        
        with open(f"{HERE}\\saves\\{filename}.json", "r") as file: data = load(file)
        self._load_data(data)
        
    def _reset(self): self.clicker.values = [0, 0, 0, 0]
            
    def manage(self, mode: Literal["save", "load", "reset"], slot: int):
        if slot == 0: mode == "reset"
        if mode != "reset": filename = f"save_{slot}"
        
        match mode:
            case "reset": self._reset
            case "save": self._save(filename)
            case "load": self._load_file(filename)
        
        
class IncompatibleSaveException(Exception):
    def __init__(self, game_version: str, save_version: str):
        super().__init__(f"incompatible versions: '{game_version}' (game), '{save_version}' (save)")