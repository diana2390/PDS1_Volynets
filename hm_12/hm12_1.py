import concurrent.futures
import time

# ThreadPoolExecutor
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

if __name__=="__main__":
    start1 = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = [executor.submit(factorial, 5) for _ in range(1,10)]
    for i in results:
        print(i.result())
    finish1 = time.perf_counter()

    time_res1 = finish1 - start1
    print(f"ThreadPoolExecutor finished in {time_res1}second(s)")

# ProcessPoolExecutor
    start2 = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = [executor.submit(factorial, 5) for _ in range(1,10)]
    for i in results:
        print(i.result())
    finish2 = time.perf_counter()

    time_res2 = finish2 - start2
    print(f"ProcessPoolExecutor finished in {time_res2}second(s)")

# Compare the time
    if time_res1 < time_res2:
        print(f"ThreadPoolExecutor is faster. Difference is {time_res2 - time_res1}")
    if time_res2 < time_res1:
        print(f"ProcessPoolExecutor is faster. Difference is {time_res1 - time_res2}" )