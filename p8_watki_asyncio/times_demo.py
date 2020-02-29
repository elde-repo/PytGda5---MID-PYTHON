import asyncio
import time


async def do_sth(how_many):
    a = 0
    for i in range(how_many):
        # doing important stuff
        a += 1
        await asyncio.sleep(0.001)
    return a


async def do_real_stuff(how_many):
    a = 0
    for i in range(how_many * 100000):
        a += 1
    return a


async def main(threads):
    t1 = time.time()

    tasks = []

    print(f"Master: bede liczyl na {threads} watkach")
    for i in range(0, threads):
        # tasks.append(asyncio.create_task(do_sth(1000//threads)))
        tasks.append(asyncio.create_task(do_real_stuff(1000//threads)))

    print('Master: czekam na watki')
    for i in range(0, threads):
        await tasks[i]

    print(f"Master: Skonczone w: {time.time() - t1}")


if __name__ == "__main__":
    for i in range(1, 129):
        asyncio.run(main(i))
        print('-' * 100)
