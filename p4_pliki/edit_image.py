PICTURE = 'obraz.bmp'


def czytaj_i_zmieniaj(file):
    with open(file, 'rb+') as f:
        f.read(34)
        # print(f.read(50))

        for j in range(10007):
            # f.write(b'\x00\x00\x00')
            # f.write(b'\xff\xff\xff')
            f.write(b'\xff\xff\xff')
            # f.write(b'\x00\xff\xe2')
            pass


if __name__ == "__main__":
    czytaj_i_zmieniaj(PICTURE)
