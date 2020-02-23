from pickle import Pickler
from p6_serializacja_przyklady.class_and_function import *

slownik = {
    'a': 903812,
    'b': (2, 3, 4),
    'c': "1234567890",
    'd': [1, 2, 3, 4, 5],
    'e': {"123": "456"},
    'f': fun,
    'gc': Cla,
    'go': Cla()
}

for key, value in slownik.items():
    with open(f'zapiklowane/p{key}.p', 'wb') as f:
        Pickler(f).dump(value)
