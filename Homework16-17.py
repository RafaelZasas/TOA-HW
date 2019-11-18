import math
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
    print(f'Ordered pairs of Px from index 2 to index 8: \n{Px[2:8]}\n')


tuples()

# OUTPUT FOR PROGRAM 1 - GOING TO BE DIFF EACH TIME
# Original Tuple list:
# [(0.113, 0.881), (0.341, -0.898), (0.482, -0.884), (-0.975, -0.924),
# (-0.852, -0.303), (0.3, -0.364), (-0.846, -0.611), (-0.321, -0.795), (-0.396, 0.979)]
#
# First Tuple: (0.113, 0.881)
# Last Tuple: (-0.396, 0.979)
#
# Tuples sorted by x co ordinate:
# [(-0.975, -0.924), (-0.852, -0.303), (-0.846, -0.611), (-0.396, 0.979),
# (-0.321, -0.795), (0.113, 0.881), (0.3, -0.364), (0.341, -0.898), (0.482, -0.884)]
#
# Ordered pairs of Px from index 2 to index 8:
# [(-0.846, -0.611), (-0.396, 0.979), (-0.321, -0.795),
# (0.113, 0.881), (0.3, -0.364), (0.341, -0.898)]


# PROGRAM 2  - CIRCLES

# DONE ON COCALC AND WORKS CORRECTLY.

def generate_tuples():
    x = []
    y = []
    for i in range(1000):
        r1 = round(random.uniform(-1, 1), 3)
        r2 = round(random.uniform(-1, 1), 3)
        distance_from_origin = math.sqrt((0 - r1) ** 2 + (0 - r2) ** 2)  # compute distance from origin
        if distance_from_origin < 1.0:  # only add the points to the list & tuple if its less than 1 from center
            x.append(r1)
            y.append(r2)
    a = list(zip(x, y))
    return a


def circles():
    my_tuple = generate_tuples()  # get the zipped lists as a tuple
    plt.scatter(*zip(*my_tuple))  # unzip the tuples into x and y values

    plt.title("Tuple plot")
    plt.xlabel('x label')
    plt.ylabel('y label')

    plt.show()


circles()


# PROGRAM 3  - BRUTE FORCE TUPLE COMPARISON


def distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def brute(my_tuple):
    x_diff = 1
    y_diff = 1
    k = 1
    d = []
    tuple1 = []
    tuple2 = []
    for i in range(len(my_tuple)):
        x, y = my_tuple[i]
        for j in range(k, len(my_tuple)):
            x2, y2 = my_tuple[j]
            d.append(distance(x, x2, y, y2))  # add each distance btwn tuples to a new distance list
            tuple1.append(i)
            tuple2.append(j)
        k += 1

    a = list(zip(d, tuple1, tuple2))  # create a new tuple containing (distance, tuple1,tuple2)
    a.sort()  # sort the tuple list by distance so that the closest pair is the first tuple
    # print(f'{a}')  # to see all the tuples and their corresponding distances
    closest = a[0]  # isolate the tuple with the smallest distance
    print(f'The closest pair is between tuple number {closest[1]} and {closest[2]}\n'
          f'The distance between them is {closest[0]}\n')


A = [(0, 2.1), (5.7, 9), (-1.3, 4.3), (-5, 4), (2.4, 6)]
brute(A)

# OUTPUT FOR PROGRAM 3:
# The closest pair is between tuple number 0 and 2
# The distance between them is 2.5553864678361276
