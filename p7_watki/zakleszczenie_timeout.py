import threading
import logging
from p7_watki.hard_operations import hard_operation


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


def take_A_and_then_B(a, b):
    logging.info(f"W1: potrzebuje A")

    for i in range(5):
        logging.info(f"W1: PROBA {i}")
        success = a.acquire(blocking=True, timeout=10)
        if not success:         # jesli nie udalo mi sie zajac zasobu A
            logging.info("W1: Nie mam zasobu A :(")
            continue            # przeskocz do kolejnej iteracji petli I i sprobuj jeszcze raz

        logging.info("W1: Mam zasob A :)")

        # do some very complicated operations on the resource A
        hard_operation(how_hard=1)

        # oh... I need B too!
        logging.info("W1: o... potrzebuje tez B")
        success = b.acquire(blocking=True, timeout=10)    # poczekajmy chwile na B
        if not success:                        # ale jesli z B sie nie powiedzie
            logging.info("W1: nie mam zasobu B :(")
            a.release()                         # zwolnimy tez A - moze ktos na to czeka?
            continue                            # wowczas moze istniec potrzeba wykonania
                                                # wiekszosci kodu na nowo, przechodzimy zatem
                                                # do nastepnej iteracji petli I

        logging.info("W1: Mam zasob B :)")
        # do some very complicated operations on the resource B
        logging.info("W1: Wykonuje moje mega ciezkie operacje...")
        hard_operation(how_hard=1)

        logging.info("W1: zwalniam A i B")
        a.release()
        b.release()
        break     # jezeli wszystko sie wykonalo, nie przechodz do kolejnego obiegu petli I

    logging.info("W1: KONIEC" + "!"*10)


def take_B_and_then_A(a, b):
    logging.info("W2: potrzebuje B")
    b.acquire(blocking=True)
    logging.info("W2: Mam zasob B :)")
    # do some very complicated operations on the resource B
    hard_operation(how_hard=2)

    # oh... I need A too!
    logging.info("W2: o... potrzebuje tez A")
    a.acquire(blocking=True)
    logging.info("W2: Mam tez zasob A :)")
    # do some very complicated operations on the resource A
    logging.info("W2: Wykonuje moje mega ciezkie operacje...")
    hard_operation(how_hard=1)

    logging.info("W2: zwalniam A i B")
    a.release()
    b.release()
    logging.info("W2: KONIEC" + "!"*10)


def deadlock():
    a = threading.Lock()
    b = threading.Lock()

    th1 = threading.Thread(target=take_A_and_then_B, args=(a, b))
    th2 = threading.Thread(target=take_B_and_then_A, args=(a, b))
    logging.info("M : przed wystartowaniem watkow")
    th1.start()
    th2.start()
    logging.info("M : watki juz ruszyly")
    th1.join()
    th2.join()
    logging.info("M : skonczone")


if __name__ == "__main__":
    deadlock()
