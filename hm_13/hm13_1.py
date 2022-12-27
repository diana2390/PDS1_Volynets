import random
from random_words import RandomWords

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(1, 1000))
    float_list.append(random.uniform(0.1, 100))
    str_list.append(w.random_word())

print(f"Int list:{int_list}")
print(f"Float list:{float_list}")
print(f"String list:{str_list}")