import threading
import logging
from p7_watki.hard_operations import hard_operation


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


def take_A_and_then_B(a, b):
    logging.info(f"W1: potrzebuje A")
    a.acquire(blocking=True)
    # do some very complicated operations on the resource A
    hard_operation(how_hard=1)

    # oh... I need B too!
    logging.info(f"W1: o... potrzebuje tez B")
    b.acquire(blocking=True)
    # do some very complicated operations on the resource B
    hard_operation(how_hard=1)

    logging.info(f"W1: zwalniam A i B")
    a.release()
    b.release()


def take_B_and_then_A(a, b):
    logging.info(f"W2: potrzebuje B")
    b.acquire(blocking=True)
    # do some very complicated operations on the resource B
    hard_operation(how_hard=2)

    # oh... I need A too!
    logging.info(f"W2: o... potrzebuje tez A")
    b.acquire(blocking=True)
    # do some very complicated operations on the resource A
    hard_operation(how_hard=1)

    logging.info(f"W2: zwalniam A i B")
    a.release()
    b.release()


def deadlock():
    a = threading.Lock()
    b = threading.Lock()

    th1 = threading.Thread(target=take_A_and_then_B, args=(a, b))
    th2 = threading.Thread(target=take_B_and_then_A, args=(a, b))
    logging.info("Main   : przed wystartowaniem watkow")
    th1.start()
    th2.start()
    logging.info("Main   : watki juz ruszyly")
    th1.join()
    th2.join()
    logging.info(f"Main   : skonczone")


if __name__ == "__main__":
    deadlock()
