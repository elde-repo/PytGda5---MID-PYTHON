import asyncio


async def nested():
    return 42


async def main():
    print(await nested())

    task = asyncio.create_task(nested())
    print(await task)

if __name__ == "__main__":
    asyncio.run(main())