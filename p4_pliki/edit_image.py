PICTURE = 'obraz.bmp'


def czytaj_i_zmieniaj(file):
    with open(file, 'rb+') as f:
        f.read(34)
        # print(f.read(50))

        for j in range(5000):
            # f.write(b'\x00\x00\x00')
            # f.write(b'\xff\xff\xff')
            f.write(b'\xff\xff\xff')
            # f.write(b'\x00\xff\xe2')
            pass


def draw_square(file, img_width: int, img_height: int, square_size: int):
    with open(file, 'rb+') as f:  # draw all image with one color for safety
        f.read(54)
        for j in range(10000):
            f.write(b'\255\255\255')
    with open(file, 'rb+') as f:
        f.read(54)
        counter = 0
        for j in range(10000):
            if counter < square_size:
                if 0 + (img_width * counter) <= j < square_size + (img_width * counter):
                    f.write(b'\0\0\0')
                elif square_size + (img_width * counter) <= j < (img_width * counter) + img_width - 1:
                    f.write(b'\255\255\255')
                else:
                    f.write(b'\255\255\255')
                    counter += 1

if __name__ == "__main__":
    czytaj_i_zmieniaj(PICTURE)
    draw_square(PICTURE, 100, 100, 50)
