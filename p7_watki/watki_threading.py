import threading
import time
import logging
from p7_watki.hard_operations import hard_operation


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

HOW_MANY = 4


def simple_thread_function(name):
    logging.info(f"Watek {name}: poczatek")
    hard_operation()
    logging.info(f"Watek {name}: koniec")


def simple_example():
    logging.info("Main   : przed stworzeniem watku")
    thr = threading.Thread(target=simple_thread_function, args=(0,))
    logging.info("Main   : przed wystartowaniem watku")
    thr.start()
    logging.info("Main   : watek juz ruszyl")
    # thr.join()
    logging.info(f"Main   : skonczone")


def many_threads():
    thr = []
    logging.info(f"Main   : przed stworzeniem {HOW_MANY} watkow")
    for i in range(HOW_MANY):
        thr.append(threading.Thread(target=simple_thread_function, args=(i,)))
    logging.info("Main   : przed wystartowaniem watkow")
    for t in thr:
        t.start()
    logging.info("Main   : watki juz ruszyly")
    for t in thr:
        t.join()
    logging.info(f"Main   : skonczone")


def many_threads_time():
    t1 = time.time()
    many_threads()
    logging.info(f"Main   : skonczone w czasie {time.time() - t1}")


def single_thread_time():
    logging.info(f"Jeden  : rozpoczynam")
    t1 = time.time()
    for i in range(HOW_MANY):
        hard_operation()
    logging.info(f"Jeden  : skonczone w czasie {time.time() - t1}")


if __name__ == "__main__":
    # simple_example()

    # many_threads()

    single_thread_time()
    logging.info('-' * 100)
    many_threads_time()
    pass
