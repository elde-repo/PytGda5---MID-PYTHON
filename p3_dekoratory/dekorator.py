import time
from functools import wraps

def how_long(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        s = func(*args, **kwargs)
        t2 = time.time()
        print(f"funkcja dzialala: {t2 - t1}")
        return s
    return wrapper

@how_long
def owinieta_funkcja_hw(imie_swiata):
    print("bardzo ciezkie operacje dla swiata")
    # time.sleep(2)
    return "hello world " + imie_swiata

s = owinieta_funkcja_hw("EEEEE MAKARENA")
print(s)
x = owinieta_funkcja_hw
print(x.__name__)
