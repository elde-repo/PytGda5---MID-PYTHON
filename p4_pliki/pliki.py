from collections import Counter

F1 = 'plik1.txt'
F2 = 'plik2.txt'


def print_file(file_name):
    with open(file_name, "r") as f:
        print(f.read())


def print_n_lines(file_name, lines_number):
    with open(file_name, "r") as f:
        for line in f:
            print(line, end="")
            if lines_number <= 1:
                return
            lines_number -= 1


def print_n_lines_2(file_name, lines_number):
    with open(file_name, "r") as f:
        for _ in range(lines_number):
            print(f.readline())


def find_the_longest_word_2(file_name):
    with open(file_name, "r") as f:
        return max(str(f.read()).split(), key=lambda x: len(x))


def find_the_longest_word(file_name):
    w = ""
    with open(file_name, "r") as f:
        for line in f:
            potential = max(line.split(), key=lambda x: len(x))
            w = potential if len(potential) > len(w) else w
    return w


def find_freq(file_name):
    with open(file_name, "r") as f:
        return Counter(f.read().split())


def write_to_file(file_name, lines):
    with open(file_name, "w") as f:
        f.write("\n".join(lines))


def copy_content(file_from, file_to):
    with open(file_from, "r") as f1:
        with open(file_to, "w") as f2:
            for lines in f1:
                f2.write(lines)


def remove_new_lines(file):
    content = ""
    with open(file, "r") as f:
        content = f.read().replace("\n", "")
    with open(file, "w") as f:
        f.write(content)


if __name__ == "__main__":
    write_to_file(F1, [
        'dsa sdaiw erw dsai dasuidasn',
        'jdsad werjiorwejio ewiroj erw',
        'djioasndsa da da jdsa jdsad',
        'sadodaso adioasndiasdasds',
        'dasdnas sadodaso dkoaskodasd',
        'da erw da jdsad dsa sadas erw'
    ])

    print_file(F1)

    print_n_lines(F1, 3)
    print("LONGEST WORD: ", find_the_longest_word(F1))
    print("LONGEST WORD in 3 lines: ", find_the_longest_word_2(F1))
    print(find_freq(F1))
    write_to_file(F2, ['dsadas', 'linia2', 'iweom'])
    copy_content(F1, F2)
    remove_new_lines(F2)
