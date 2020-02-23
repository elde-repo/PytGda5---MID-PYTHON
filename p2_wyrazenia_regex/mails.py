import re


if __name__ == "__main__":
    while True:
        i = input("temat wiadomosci: ")

        if i == i.upper():
            print('UPPER!')
        else:
            print('not upper')
        print(re.fullmatch(".*!{3,}$", i))
        print(re.search("H+\W*E+\W*L+\W*P+", i, re.I))
        print(re.search("A+\W*S+\W*A+\W*P+", i, re.I))
        print(re.search("U+\W*R+\W*G+\W*E+\W*N+\W*T+", i, re.I))
