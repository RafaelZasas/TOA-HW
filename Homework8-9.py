# THEORY OF ALGORITHMS   FALL 2019     RAFAEL ZASAS

# HOMEWORK 8 & 9


# Programming problem 1 - Merge Sort
import time


def mergesort(arr):
    n = len(arr)
    # print(n)
    if n == 1:
        return arr
    else:
        # print(arr[:len(arr) // 2])
        # print(arr[len(arr) // 2:])
        front = mergesort(arr[:len(arr) // 2])  # : = front tll
        back = mergesort(arr[len(arr) // 2:])  # half way till end
        return merge(front, back)  # do you return thiss or just call it?


def merge(a, b):
    i = 0
    j = 0
    c = []
    for x in range(2 * len(a)):
        # print(a)
        # print(b)
        # print(x)
        if i >= len(a):
            c.append(b[j])
            j += 1
        elif j >= len(b):
            c.append(a[i])
            i += 1
        elif a[i] < b[j]:  # the index is out of range here
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c


array = [5, 6, 3, 2, 1, 4, 8, 7, 15, 14, 13, 12, 11, 9, 10, 16, 17, 18, 19, 20]

print(mergesort(array))


# This program is O(n log n)

#  output for program 1:
# [1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 17, 18, 19]

# Programming problem 2 - Second Largest

def second_largest(a):
    largest = a[0]
    second = a[0]
    for x in range(0, len(a)):
        if a[x] > largest:
            largest = a[x]
        # print(f'l {largest}')
        if second < a[x] < largest:
            second = a[x]
            # print(second)

    return largest, second


A = [4, 7, 2, 3, 9, 1, 6, 0]
print(f'The Largest and Second Largest are {second_largest(A)} respectively.\n')


# This program is O(n)

#  output for program 2:
#
# The Largest and Second Largest are (9, 7) respectively.

# Programming problem 3 - find peak


def find_peak(a):
    n = len(a)

    if n == 1:
        return a[0]
    else:
        front = a[:len(a) // 2]  # : = front tll
        back = a[len(a) // 2:]  # half way till end
        if front[-1] < back[0]:
            return find_peak(back)
        else:
            return find_peak(front)


A = []
for i in range(2 ** 24):
    A.append(i)
for i in range(10):
    A.append(10 - i)
start_time = time.time()
print(f'peak of the arr is {find_peak(A)} \nProgram took {time.time() - start_time} seconds to complete.\n')


# This program is O(n)

#  output for program 3:
# peak of the arr is 8


#  output for program 4:
# peak of the arr is 16777215
# Program took 3.4337704181671143 seconds to complete. (old way without recursion)
# Program took 0.5535576343536377 seconds to complete. (new way with recursion)


# Programming problem 5 - index = value


def Ai_equals_i(a):
    x = 0
    index = 0
    while x < len(a):
        if a[x] == x:
            index = x
            break
        else:
            index = "non existent"
        x += 1
    return index


A = [-4, -3, 1, 2, 4, 8, 9, 10, 11, 12, 14, 18, 19, 22, 50, 51]
print(f'the matching index is {Ai_equals_i(A)} \n')


# The complexity of this program is O(n)

#  output for program 5:
# the matching index is 4


# Programming problem 6 - longest sequence


def longest_sequence(a):
    x = 0
    count_inc = 1
    count_dec = 1
    longest_inc = []
    longest_dec = []
    while x < len(a):
        if a[x] < a[x - 1]:  # if the one were on is less than the one before (ie decreasing)
            longest_inc.append(count_inc)
            count_inc = 1
        else:
            count_inc += 1

        if a[x] > a[x - 1]:  # if the one were on is greater than the one before (ie increasing)
            longest_dec.append(count_dec)
            count_dec = 1
        else:
            count_dec += 1

        x += 1
    return longest_inc, longest_dec


A = [1, 2, 4, 3, 2, 5, 7, 8, 12, 8, 13, 14, 12, 8, 6, 4, 2, 3, 4]
inc, dec = longest_sequence(A)
print(f'The longest sequence of increasing integers is {max(inc)}')
print(f'The longest sequence of decreasing integers is {max(dec)}')

# The complexity of this program is O(n)

#  output for program 6:
# The longest sequence of increasing integers is 5
# The longest sequence of decreasing integers is 6
