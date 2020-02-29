import threading
import time
import logging


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

ACCURACY = 1000


def function(x):
    return x


def area_for_value(f, a, b, width, i, results):
    logging.debug(f"watek{i}: {a} - {b}, {width}")
    t1 = time.time()
    oper = 0
    s = 0
    while a < b:
        s += f(a) * width
        a += width
        time.sleep(0.001)
        oper += 1
    results[i] = s
    logging.debug(f"watek{i}: skonczone w czasie {time.time() - t1} ({oper} operacji)")


def integral(f, a, b, threads=4):
    logging.info(f"Master: bede liczyl na {threads} watkach")
    t1 = time.time()

    thr = []

    results = []
    global_width = (b - a) / ACCURACY
    thread_width = (b - a) / threads
    p_thread = a

    for i in range(threads):
        results.append(0)
        thr.append(
            threading.Thread(
                target=area_for_value,
                args=(f, p_thread, p_thread + thread_width, global_width, i, results)
            )
        )
        p_thread += thread_width

    logging.debug("Master: startuje watki")
    for t in thr:
        t.start()

    logging.debug("Master: czekam na watki")
    for t in thr:
        t.join()

    logging.debug("Master: licze sume")
    result = sum(results)

    logging.info(f"Master: skonczone w czasie {time.time() - t1}")
    logging.info(f"Master: calka w zakresie {a} do {b} = {result}")


if __name__ == "__main__":
    for i in range(1, 129):
        integral(function, 0, 1, threads=i)
        logging.info('-' * 100)
