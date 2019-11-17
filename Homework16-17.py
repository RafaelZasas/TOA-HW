# PROGRAM 1  - TUPLES
import math, random
from typing import Match


def tuples():
    x = []
    y = []
    for i in range(9):
        x.append(round(random.uniform(-1, 1), 3))
        y.append(round(random.uniform(-1, 1), 3))
    a = list(zip(x, y))
    print(f'Original Tuple list:\n{a}\n')
    print(f'First Tuple: {a[0]} \nLast Tuple: {a[len(a) - 1]}\n')
    a.sort()
    Px = a
    print(f'Tuples sorted by x co ordinate: \n{Px}\n')
    print(f'Ordered pairs of Px from index 2 to index 8: \n{Px[2:8]}')


tuples()
