import time
import random


def hard_operation(*args, **kwargs):
    t = kwargs['how_hard'] if 'how_hard' in kwargs else 2
    t += random.random() / 10
    time.sleep(t)
