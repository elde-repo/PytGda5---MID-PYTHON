from itertools import *


print("COUNT:")
licz = 20
for i in count(10, 2):
    print(i, end=" ")
    if licz > 0:
        licz -= 1
    else:
        break

############################################
print('\n', '-' * 100)
############################################

print("CYCLE:")
licz = 10
for i in cycle("1Ad6"):
    print(i, end=" ")
    if licz > 0:
        licz -= 1
    else:
        break

############################################
print('\n', '-' * 100)
############################################

print("REPEAT:")
licz = 10
for i in repeat("element"):
    print(i, end=" ")
    if licz > 0:
        licz -= 1
    else:
        break

print("\nREPEAT(element, 3):")
for i in repeat("element", 3):
    print(i, end=" ")

############################################
print('\n', '-' * 100)
############################################

print("ACCUMULATE:")
for i in accumulate([1, 2, 3, 4, 5]):
    print(i, end=" ")

print("\nACCUMULATE:")
for i in accumulate("element"):
    print(i, end=" ")

############################################
print('\n', '-' * 100)
############################################

print("CHAIN:")
for i in chain("ABC", {"key": "value", "key2": "v2"}, [2, 4, 7]):
    print(i, end=" ")

############################################
print('\n', '-' * 100)
############################################

print("TAKEWHILE:")
for i in takewhile(lambda x: x<5, [1, 4, 6, 4, 1]):
    print(i, end=" ")
