import math
import random


# Programming problem 1

def binomial(n, k):
    bin = math.factorial(n) / (math.factorial(k) * (math.factorial(n - k)))
    if bin % 2 == 0:
        return bin, "X"
    else:
        return bin, " "


for i in range(2, 50, 1):
    for j in range(i, 50, 1):
        C, polarity = binomial(j, i)
        # print(f'C({j},{i}) \t {C} \t {polarity}')
        print(polarity + " ", end='')
    print("")


# Output for program 1:

# a serpinski triangle


# Programming problem 2

def gcd(y, x):  # Greatest Common Denominator program
    while x > 0:
        y, x = x, y % x
    return y


def stats(n):
    count = 0
    for i in range(10000):
        x = random.randint(0, n)
        y = random.randint(0, n)
        if gcd(x, y) == 1:
            count += 1
    return count / 10000 * 100


print(f'There is a {stats(100)}% chance that two random numbers between 0-100 will be relatively prime.')
print(f'There is a {stats(1000)}% chance that two random numbers between 0-1000 will be relatively prime.')
print(f'There is a {stats(10000)}% chance that two random numbers between 0-10000 will be relatively prime.\n')


# Output for problem 2:
# There is a 58.85% chance that two random numbers between 0-100 will be relatively prime.
# There is a 60.56% chance that two random numbers between 0-1000 will be relatively prime.
# There is a 60.39% chance that two random numbers between 0-10000 will be relatively prime.


# Programming problem 3 - Permutations

def perm(A):
    largest = A[-1]
    x = len(a) - 1
    while x > 0:
        if A[x] > A[x - 1]:
            A[x], A[x - 1] = A[x - 1], A[x]
            print(A)
            x -= 1


a = [1, 2, 3, 4]
perm(a)
print('\n')


# Programming Problem 4 - r combinations

def next_comb(Arr, n, r):
    pass


# I couldn't get number 3 or number 4

# Programming problem 5: add 1 to binary
def add_1(a):
    hasZero = False
    for x in range(len(a)):
        if a[x] == 0:
            hasZero = True

    x = len(a) - 1
    if hasZero:
        while a[x] != 0:
            a[x] = a[x] % 1
            x -= 1
        a[x] = 1
    else:
        a = [0] * (x + 1)
        a.insert(0, 1)

    return a


a = [0, 1, 0, 1, 1, 0, 0, 1, 1, 1]
b = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
c = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(add_1(a))
print(add_1(b))
print(add_1(c))


# Output for program 5:
# a = [0, 1, 0, 1, 1, 0, 0, 1, 1, 1] -> [0, 1, 0, 1, 1, 0, 1, 0, 0, 0]
# b = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] -> [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# c = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] -> [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Programming Problem 6: Bit Strings
def bit_strings():
    count1 = 0
    count2 = 1
    count3 = 2
    A = [0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(56):
        for i in range(8):
            A[i]
# ... I did not manage to get this to work...
