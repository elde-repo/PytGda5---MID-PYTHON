def szesciennie_inf(start=0):
    number = start
    while True:
        yield number ** 3
        number += 1


def szesciennie(start=0, stop=None):
    number = start
    while True:
        yield number ** 3
        number += 1
        if stop is not None and number >= stop:
            return


l = 0
for i in szesciennie_inf(0):
    print(i)
    l += 1
    if l > 5:
        break

print('-' * 50)

for i in szesciennie(0, 12):
    print(i+1)

print(type(szesciennie()))
