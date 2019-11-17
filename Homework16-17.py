import random


# import matplotlib.pyplot as plt
# import numpy as np

# PROGRAM 1  - TUPLES
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


# PROGRAM 2  - CIRCLES

# DONE ON COCALC BUT CURRENTLY NOT WORKING

# def generate_tuples():
#     x = []
#     y = []
#     for i in range(10):
#         x.append(round(random.uniform(-1, 1), 3))
#         y.append(round(random.uniform(-1, 1), 3))
#     a = list(zip(x, y))
#     return a
#
#
# def circles():
#     x = np.linspace(0, 1, 100)
#     y = np.linspace(0, 1, 100)
#     my_tuple = generate_tuples()
#
#     for tup in my_tuple:
#         x, y = tup
#         plt.plot(x, y)
#
#     plt.title("Tuple plot")
#     plt.xlabel('x label')
#     plt.ylabel('y label')
#
#     plt.show()
#
#
# circles()


# PROGRAM 3  - BRUTE FORCE TUPLE COMPARISON

# ALSO CURRENTLY NOT WORKING

def brute(my_tuple):
    x_diff = 1
    y_diff = 1
    for tup in my_tuple:
        x, y = tup
        print(f'{x} {y}')


A = [(0, 2.1), (-1.3, 4.3), (5.7, 9), (-5, 4), (2.4, 6)]
brute(A)
