from itertools import cycle

c = cycle("Ab3")
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print('-' * 50)

i = iter([1, 6, 8, 9])
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(r))
print('-' * 50)

