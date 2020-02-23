from zadanie1_urzad.exceptions import NoMoreElementsException
from zadanie1_urzad.my_queue import MyQueue
from zadanie1_urzad.user_interface import *

queues = {
    "a": MyQueue(),
    "b": MyQueue(),
    "c": MyQueue()
}

VERY_PRIVATE_PASS = "admin1"


if __name__ == "__main__":
    while True:
        welcome()
        choice = choose()

        if choice in queues.keys():
            q = queues[choice]
            place = q.add_element()
            number_info(choice, place)
        elif choice == VERY_PRIVATE_PASS:
            official_welcome()
            officials_choice = choose()
            q = queues[officials_choice]
            try:
                place = q.remove_element()
            except NoMoreElementsException:
                place = None
            you_are_handling(officials_choice, place)
        else:
            queue_not_found()
