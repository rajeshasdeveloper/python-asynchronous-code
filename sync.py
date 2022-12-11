from time import sleep
from time import perf_counter


def get_data():
    sleep(1)
    return {"name": "python", "version": 3}


def print_numbers():
    for num in range(10):
        print(num)
        sleep(0.15)


def main():
    # start the timer
    start = perf_counter()
    task_1 = get_data()
    print(task_1)

    # measure the timer after task 1
    print("get_data \u0394t:", round(perf_counter() - start, 3))

    # start the timer for function 2
    start_2 = perf_counter()
    task_2 = print_numbers()
    # measure the timer after task 2

    print("print_numbers \u0394t:", round(perf_counter() - start_2, 3))

    # measure the total time after the successful run

    print(
        "Total execution time of synchronous code \u0394t is: ",
        round(perf_counter() - start, 3),
    )


main()
