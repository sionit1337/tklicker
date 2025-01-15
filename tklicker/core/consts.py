from os.path import abspath


_VALS_N = 3
_ROOT2 = 2 ** .5
VERSION = "v2.0"
PRICE_VALUE = lambda I: I ** _ROOT2 * _ROOT2
PRICE_OFFSET = 5
PATH = abspath(__file__)


class NotEnoughException(Exception):
    def __init__(self, val: float, price: float):
        super().__init__(f"not enough value ('{price}' expected, '{val}' got)")
        
        
class IncompatibleSaveException(Exception):
    def __init__(self, save_ver: float):
        super().__init__(f"wrong save version ('{VERSION}' expected, '{save_ver}' got)")