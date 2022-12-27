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

# Sorting
# def selection_sort(data):
#     for s in range (0, len(data)):
#         min = s
#         for fl in range (s +1,len(data)):
#             if data[fl] < data[min]:
#                 min = fl
#             if min != s:
#                 data[s], data[min] = data[min], data[s]
#     print(f"Selection Sort: {data}")
#
# cur_time = time.time()
# selection_sort(int_list)
# print(f"Duration Sorting time: {time.time() - cur_time}")
#
# # Quick Sort
# def partition(nums, low, high):
#     p = nums[(low + high) // 2]
#     i - low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while nums[i] < p:
#             i += 1
#         j -= 1
#         while nums[j] > p:
#             j -= 1
#     def _quick_sort(items, low, high):
#         if low < high:
#             spl = partition(items, low, high)
#             _quick_sort(items, low, spl)
#             _quick_sort(items, spl + 1, high)
#     _quick_sort(nums, 0, len(nums) - 1)
#
# cur_time = time.time()
# _quick_sort(int_list)
# print(f"Quick Sort: {int_list}")
# print(f"Durations time: {time.time() - cur_time}")