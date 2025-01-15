import os
import json
from typing import Optional, Any
from .consts import VERSION, IncompatibleSaveException, PATH
from .click import Clicker
from dataclasses import dataclass


@dataclass
class SaveData:
    clicks: float
    values: list[float]
    version: str = VERSION
    
    @property
    def json(self):
        values = {
            f"val_{i}": self.values[i] for i in range(len(self.values))
        }
        
        data = {
            "version": self.version,
            "clicks": self.clicks,
            "values": values,
        }
        
        return data
    
    @staticmethod
    def from_json(json: dict[str, Any]):
        return SaveData(json["clicks"], list(json["values"].values()), json["version"])


class Saves:
    def __init__(self, clicker: Clicker):
        self.clicker = clicker
        
    @property
    def data(self): return SaveData(self.clicker.clicks, self.clicker.values)
    
    def load_data(self, data: Optional[SaveData]):
        data = data.json if data else self.data.json
        
        clicks = data["clicks"]
        values = data["values"]
        version = data["version"]
        
        if version != VERSION: raise IncompatibleSaveException(version)
        
        self.clicker.clicks = clicks
        self.clicker.values = values
        
        
class SaveFiles(Saves):    
    def save_file(self, filename: str, directory: Optional[str] = None, data: Optional[SaveData] = None):
        data = data or self.data
        directory = directory or f"{PATH}/saves"
        
        if not os.path.exists(directory): os.mkdir(directory)
        with open(f"{directory}/{filename}.json", "w") as file: json.dump(data, file)
        
    def load_file(self, filename: str, directory: Optional[str] = None):
        directory = directory or f"{PATH}/saves"
        
        if not os.path.exists(f"{directory}/{filename}.json"): self.save_file(filename, directory)
        
        with open(f"{directory}/{filename}.json") as file: data = file.read()
        to_load = SaveData.from_json(json.loads(data))
        self.load_data(to_load)