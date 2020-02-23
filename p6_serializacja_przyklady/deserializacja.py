from pickle import Unpickler
from p6_serializacja_przyklady.class_and_function import *

pliki = ['a', 'b', 'c', 'd', 'e', 'f', 'gc', 'go']

for plik in pliki:
    with open(f'zapiklowane/p{plik}.p', 'rb') as f:
        variable = Unpickler(f).load()
    print(variable)
    print(type(variable))
    print()
