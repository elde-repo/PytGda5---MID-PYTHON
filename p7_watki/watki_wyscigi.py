import threading
import logging


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

HOW_MANY = 8


def add_to_resource(r):
    for i in range(1000000):    # 1M
        r['resource'] += 1


def add_to_resource_blocking(r, l):
    for i in range(1000000):    # 1M
        l.acquire(blocking=True)
        try:
            r['resource'] += 1
        finally:
            l.release()


def races():
    thr = []
    # l = threading.Lock()

    r = {'resource': 0}

    logging.info(f"Main   : przed stworzeniem {HOW_MANY} watkow")
    for i in range(HOW_MANY):
        thr.append(threading.Thread(target=add_to_resource, args=(r,)))
        # thr.append(threading.Thread(target=add_to_resource_blocking, args=(r, l)))
    logging.info("Main   : przed wystartowaniem watkow")
    for t in thr:
        t.start()
    logging.info("Main   : watki juz ruszyly")
    for t in thr:
        t.join()
    logging.info(f"Main   : skonczone")
    logging.info(f"Main   : rezultat {r['resource']}")


if __name__ == "__main__":
    races()
    pass
