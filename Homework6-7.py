# THEORY OF ALGORITHMS   FALL 2019     RAFAEL ZASAS

# HOMEWORK 6 & 7


# Programming problem 1- Euclidean GCD
import math

print("Program 1 -- Euclidean GCD" + "\n")


def gcd(y, x):  # Greatest Common Denominator program
    while x > 0:
        y, x = x, y % x
    return y


a = 320
b = 128
print(f'The greatest common denominator of {a} and {b} is  {gcd(a, b)} \n')

a = 6546846
b = 21534
print(f'The greatest common denominator of {a} and {b} is  {gcd(a, b)} \n')

#  output for program 1:
# Program 1 -- Euclidean GCD
#
# The greatest common denominator of 320 and 128 is  64
#
# The greatest common denominator of 6546846 and 21534 is  6


# Programming problem 2- Adding binary numbers

print("Program 2 -- Binary Sum" + "\n")


def sum_binary(a, b):
    carry = 0
    bin_sum = []
    for i in range(len(a) - 1, -1, -1):
        r = carry
        r += 1 if a[i] == 1 else 0
        r += 1 if b[i] == 1 else 0
        bin_sum.insert(0, 1) if r % 2 == 1 else bin_sum.insert(0, 0)
        carry = 0 if r < 2 else 1
    bin_sum.insert(0, 1) if carry > 0 else bin_sum.insert(0, 0)
    return bin_sum


def convert_binary(a):
    n = 0
    power = len(a)
    for i in range(0, len(a)):
        power -= 1
        if a[i] == 1:
            n += 2 ** power
    return n


num1 = [0, 0, 1, 0, 0, 1, 1, 1]
print(f"Binary 1: {num1} = {convert_binary(num1)}")
num2 = [0, 0, 0, 1, 0, 1, 1, 1]
print(f"Binary 2: {num2} = {convert_binary(num2)}")
print(f"The sum of the Binary is {sum_binary(num1, num2)} ={convert_binary(sum_binary(num1, num2))} \n")

num1 = [1, 0, 1, 1, 0, 1, 0, 1]
print(f"Binary 1: {num1} = {convert_binary(num1)}")
num2 = [1, 1, 1, 1, 0, 0, 1, 0]
print(f"Binary 1: {num2} = {convert_binary(num2)}")
print(f"The sum of the Binary is {sum_binary(num1, num2)} ={convert_binary(sum_binary(num1, num2))}\n ")

#  output for program 2:

# Binary 1: [0, 0, 1, 0, 0, 1, 1, 1] = 39
# Binary 2: [0, 0, 0, 1, 0, 1, 1, 1] = 23
# The sum of the Binary is [0, 0, 0, 1, 1, 1, 1, 1, 0] =62
#
# Binary 1: [1, 0, 1, 1, 0, 1, 0, 1] = 181
# Binary 1: [1, 1, 1, 1, 0, 0, 1, 0] = 242
# The sum of the Binary is [1, 1, 0, 1, 0, 0, 1, 1, 1] =423


# Programming problem 3- Rosen pg 136 problem 39

print("Program 3 -- Binary Comparison " + "\n")


def binary_comparison(a, b):
    if a == b:
        return 'The numbers are equal'
    else:
        for i in range(0, len(a)):
            if a[i] > b[i]:
                return f"num 1 is the bigger number"
            elif b[i] > a[i]:
                return f"num 2 is the bigger number"


print("Test Case 1:\n")
num1 = [0, 1, 1, 0, 0, 1, 1, 1]
print(f"num 1: {num1} = {convert_binary(num1)}")
num2 = [0, 0, 0, 1, 1, 1, 1, 0]
print(f"num 2: {num2} = {convert_binary(num2)}")
print(binary_comparison(num1, num2) + "\n")

print("Test Case 2:\n")
num1 = [0, 1, 1, 1, 0, 1, 1, 1]
print(f"num 1: {num1} = {convert_binary(num1)}")
num2 = [0, 1, 1, 1, 0, 1, 1, 1]
print(f"num 2: {num2} = {convert_binary(num2)}")
print(binary_comparison(num1, num2) + "\n")

print("Test Case 3:\n")
num1 = [1, 1, 1, 1, 1, 1, 1, 0]
print(f"num 1: {num1} = {convert_binary(num1)}")
num2 = [1, 1, 1, 1, 1, 1, 1, 1]
print(f"num 2: {num2} = {convert_binary(num2)}")
print(binary_comparison(num1, num2) + "\n")

# Output for Program 3:
#     Test Case 1:
# #
# #     num 1: [0, 1, 1, 0, 0, 1, 1, 1] = 103
# #     num 2: [0, 0, 0, 1, 1, 1, 1, 0] = 30
# #     num 1 is the bigger number
# #
# #     Test Case 2:
# #
# #     num 1: [0, 1, 1, 1, 0, 1, 1, 1] = 119
# #     num 2: [0, 1, 1, 1, 0, 1, 1, 1] = 119
# #     The numbers are equal
# #
# #     Test Case 3:
# #
# #     num 1: [1, 1, 1, 1, 1, 1, 1, 0] = 254
# #     num 2: [1, 1, 1, 1, 1, 1, 1, 1] = 255
# #     num 2 is the bigger number

# Programming problem 4- Karatsuba algorithm

print("Program 4 -- Karatsuba algorithm" + "\n")


def multiply(x, y):
    n = int(math.log10(x)) + 1  # how many digits are in the number
    # print(f'n is {n}')
    if n == 1:
        return x * y
    else:
        power = n // 2  # double slash rounds the number when you divide
        # print(f'power is {power}')
        a, b = x // 10 ** power, x % 10 ** power
        # print(f'a is {a}')
        # print(f'b is {b}')
        c, d = y // 10 ** power, y % 10 ** power
        # print(f'ac is {c}')
        # print(f'd is {d}')

        ac = multiply(a, c)
        ad = multiply(a, d)
        bc = multiply(b, c)
        bd = multiply(b, d)
    return 10 ** n * ac + 10 ** (n // 2) * (ad + bc) + bd


x = 4321
y = 5678
print(f'Test Case 1: \n {x} X {y} \n = \n {multiply(x, y)}\n')
x = 1234567891011121314151617181920212223242526272829303132333435363
y = 1357911131517192123252729313335373941434547495153555759616365676
print(f'Test Case 2: \n {x} X {y} \n = \n {multiply(x, y)}\n')

#  output for program 4:

# Test Case 1:
#  1234 X 5678
#  =
#  7006652
#
# Test Case 2:
#  1234567891011121314151617181920212223242526272829303132333435363 X 1357911131517192123252729313335373941434547495153555759616365676
#  =
#  1676433481817705266129514737418074430686007117601914669622664784839603755332117192533414749453310762762797651012520861917800388
