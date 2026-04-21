
import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def bubble_sort(small):
    a=small
    n=len(small)
    for x in range(n):
        for i in range(0, n-1):
            if a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a

small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
values = random_numbers(10)  # 10 čísel v rozsahu 0–100
print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
print(bubble_sort(small))