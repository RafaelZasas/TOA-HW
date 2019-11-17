# Theory of Algorithms Homework 2 & 3 Rafael Zasas

import time


def linear(l1, target):
    i = 0
    notfound = True
    while notfound:
        notfound = (target != l1[i])
        i += 1
    return i - 1


def binary(l1, target):
    top = len(l1) - 1
    bottom = 0
    while bottom < top:
        mid = (top + bottom) // 2
        if target == l1[mid]:
            return mid
        elif target < l1[mid]:
            top = mid - 1
        else:
            bottom = mid + 1
    return mid


# Test both on a simple list

big_list = []  # Create an empty list
top = 2 ** 26  # Test your 2 programs for a large value 2**26 is better
for i in range(top):
    big_list.append(i)  # We tack on the next int to our big_list
start_linear = time.time()
linear(big_list, top-1)
print(f'it took {time.time()-start_linear} seconds to complete linear search')
start_binary = time.time()
binary(big_list, top-1)
print(f'it took {time.time()-start_binary} seconds to complete binary search')


def dumb_way():
    A = [34, -50, 42, 14, -5, 86]
    best = []

    num = 0
    for i in range(len(A)):  # i starts @ 1 goes till end
        for l in range(len(A) - 1, -1, -1):  # l starts @ end goes till beg
            for x in range(i, l + 1):  # x goes from i till l for middle
                num += A[x]
            best.append(num)
            num = 0
    print(f'array of sums is {best}')

    return max(best)


print(f'The dumb way says that {dumb_way()} is the biggest partial sum')


# the order is 3 n because you have to have 3 loops


def smart_way():
    a = [34, -50, 42, 14, -5, 86]
    back_arr = []
    front_arr = []
    for x in range(len(a)):
        front_arr.append(sum(a[x:len(a)]))
    print(f'front array: {front_arr}')

    for x in range(len(a) - 1, -1, -1):
        back_arr.append(sum(a[x:len(a)]))
    print(f'back array: {back_arr}')

    index_fmax = front_arr.index(max(front_arr))
    index_bmax = back_arr.index(max(back_arr))
    print(f'index of front max is {index_fmax}')
    print(f'index of back max is {index_bmax}')
    num = 0
    for x in range(index_fmax, index_bmax + 3):
        num += a[x]
    print(f'The smart way says that {num} is the biggest partial sum')


smart_way()

# I had to ask john for some help with the smart way but I still
# couldn't get it to work for anything other than this example
