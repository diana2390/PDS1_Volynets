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

# Bubble Gum
def bubble_sort(data):
    length = len(data)
    for i in range(length):
        swapped = False
        for i in range(0, length - i - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        if not swapped:
            break
    print(f"Bubble Sort: {data}")

cur_time = time.time()
bubble_sort(int_list)
print(f"Duration Bubble time: {time.time() - cur_time}")

# Sorting
def selection_sort(data):
    for s in range (0, len(data)):
        min = s
        for fl in range (s +1,len(data)):
            if data[fl] < data[min]:
                min = fl
            if min != s:
                data[s], data[min] = data[min], data[s]
    print(f"Selection Sort: {data}")

cur_time = time.time()
selection_sort(int_list)
print(f"Duration Sorting time: {time.time() - cur_time}")

# Qwuack
def partition(nums, low, high):
    p = nums[(low + high) // 2]
    i - low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < p:
            i += 1
        j -= 1
        while nums[j] > p:
            j -= 1
    def _quick_sort(items, low, high):
        if low < high:
            spl = partition(items, low, high)
            _quick_sort(items, low, spl)
            _quick_sort(items, spl + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)

cur_time = time.time()
quick_sort(int_list)
print(f"Quick Sort: {int_list}")
print(f"Durations time: {time.time() - cur_time}")