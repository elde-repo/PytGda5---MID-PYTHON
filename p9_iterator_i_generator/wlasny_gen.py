def cubic_2(start=0, stop=None):
    number = start
    while True:
        yield f'{number} ** 3 =' # yield packs everything in one block that runs for one iteration
        yield number ** 3
        yield '|||'
        number += 1
        if stop is not None and number >= stop:
            return
        print('^^^^^^^^^^')
for i in cubic_2(0, 4):
    print(i, end=' $$$ ')