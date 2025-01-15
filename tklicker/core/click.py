from math import prod
from .consts import PRICE_VALUE, PRICE_OFFSET, _VALS_N, NotEnoughException


class Clicker:
    def __init__(self):
        self._clicks = 0.0
        self._values = [0.0] * _VALS_N
        
    @property
    def prices(self): return [PRICE_VALUE(self.values[i] + 1) * (PRICE_OFFSET * i) for i in range(len(self.values))]
    
    @property
    def values(self): return self._values
    
    def onclick(self, index: int): 
        if index == -1 and index == len(self.values) - 1: return 1
        return prod(i + 1 for i in self.values[index + 1:])
    
    @property
    def clicks(self): return self._clicks
    
    def click(self, amnt: float = 1): self._clicks += amnt
    def pay(self, amnt: float = 1): 
        if self.clicks >= amnt: self._clicks -= amnt
        else: raise NotEnoughException(self.clicks, amnt)
        
    def inc(self, index: int, amnt: float = 1): 
        self._values[index] += amnt
    def dec(self, index: int, amnt: float = 1):
        if self._values[index] >= amnt: self._values[index] -= amnt
        else: raise NotEnoughException(self.values[index], amnt)
        
    def up_value(self, index: int):
        index %= len(self.values)
        prices = self.prices
        vals = self.values
        
        if index == 0 and self.clicks >= prices[index]: self.pay(prices[index])
        elif vals[index - 1] >= prices[index]: self.dec(index - 1, prices[index])
        
        self.inc(index, self.onclick(index))