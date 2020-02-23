F3 = 'plik3.txt'


def czytaj_i_zmieniaj(file):
    with open(file, 'r+') as f:
        print(f.tell())
        f.read()
        f.write(" -- NA KONCU -- ")
        f.seek(0)
        f.write(" -- NA POCZATKU -- ")
        f.seek(0)
        print()
        print(f.read())


if __name__ == "__main__":
    czytaj_i_zmieniaj(F3)
