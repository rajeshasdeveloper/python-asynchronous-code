import asyncio
from time import perf_counter


async def get_data():
    start = perf_counter()
    await asyncio.sleep(1)
    print("get_data \u0394t:", round(perf_counter() - start, 3))
    return {"name": "python", "version": 3}


async def print_numbers():
    start = perf_counter()
    for num in range(10):
        print(num)
        await asyncio.sleep(0.14)
    print("print_numbers \u0394t:", round(perf_counter() - start, 3))


async def main():
    # start the timer
    start = perf_counter()
    task_1 = asyncio.create_task(get_data())
    task_2 = asyncio.create_task(print_numbers())

    task1_value = await task_1
    print(task1_value)
    await task_2

    # measure the total time after the successful run

    print(
        "Total execution time of asynchronous code \u0394t is: ",
        round(perf_counter() - start, 3),
    )


asyncio.run(main())
