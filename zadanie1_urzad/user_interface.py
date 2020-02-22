import os
import time


def clr():
    # os.system('clear')    # for linux and mac
    os.system('cls')        # for windows


def choose():
    return input("Wybierz kolejke (wpisz odpowiednia litere): ").lower()


def welcome():
    clr()
    print("Witaj!")
    print("Wybierz kolejke odpowiadajaca Twojej sprawie:")
    print("A - rejestracja pojazdow")
    print("B - prawa jazdy")
    print("C - dowody osobiste")
    print()


def official_welcome():
    clr()
    print("Urzedniku wybierz kolejke, ktora obslugujesz:")
    print("A - rejestracja pojazdow")
    print("B - prawa jazdy")
    print("C - dowody osobiste")
    print()

def queue_not_found():
    print("Nieprawidlowa nazwa kolejki!")


def you_are_handling(letter, number):
    clr()
    if number is None:
        print(f"Nie ma ludzi. Mozesz isc na przerwe.")
    else:
        print(f"Obsluz teraz numer {letter.upper()}{number}")
    time.sleep(2)
    clr()


def number_info(letter, number):
    clr()
    print(f"Twoj numerek to {letter.upper()}{number}")
    time.sleep(2)
    clr()
