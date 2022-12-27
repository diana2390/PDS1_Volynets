import random
from random_words import RandomWords
import time

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(1, 1000))
    float_list.append(random.uniform(0.1, 100))
    str_list.append(w.random_word())

# Bubble Sort:
def bubble_sort(list, iter):
    total_time = []
    for i in range(iter):
        start = time.perf_counter()
        length = len(list)
        for y in range(length):
            for i in range(0, length - i - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
    # print(f"Bubble Sort: {list}")

        finish = time.perf_counter()
        cur_time = finish - start
        total_time.append(cur_time)
    print(f"Duration Bubble time: {sum(total_time) / len(total_time)} sec.")
bubble_sort(int_list, 10)
bubble_sort(float_list, 10)
bubble_sort(str_list, 10)