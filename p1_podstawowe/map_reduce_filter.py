from functools import reduce

lt = [(1, 2), (3, 4), (5, 1), (4, 8)]

ml = list(map(lambda x: x[0], lt))
mlc = [x[0] for x in lt]

fl = list(filter(lambda x: x[0] > 3, lt))
flc = [x for x in lt if x[0] > 3]

rl = reduce(lambda x, y: x * y[0] * y[1], lt, 1)

print(ml)
print(mlc)
print(fl)
print(flc)
print(rl)
