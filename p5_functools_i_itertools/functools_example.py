from functools import lru_cache, total_ordering, singledispatch


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print([fib(n) for n in range(16)])
print(fib.cache_info())


############################################
print('-' * 100)
############################################


@total_ordering
class Student:
    def __init__(self, lastname, firstname, age):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age

    def __lt__(self, other):
        if type(other) == Student:
            return self.age < other.age
        if type(other) == int:
            return self.age < other

student1 = Student('Zenke', 'Bartosz', 22)
student2 = Student('Martyniuk', 'Zenek', 52)

print("Bartek <  Zenek  ", student1 < student2)
print("Bartek >  Zenek  ", student1 > student2)
print("Bartek == Zenek  ", student1 == student2)
print("Bartek <= Zenek  ", student1 <= student2)
print("Bartek >= Zenek  ", student1 >= student2)


############################################
print('-' * 100)
############################################


@singledispatch
def adasdas(arg):
    print("Let me just say,", end=" ")
    print(arg)


@adasdas.register
def _(arg: int):
    print("Strength in numbers, eh?", end=" ")
    print(arg)


@adasdas.register
def _(arg: list):
    print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)


adasdas('string')
adasdas(12)
adasdas(['l', 'i', 's', 't'])
