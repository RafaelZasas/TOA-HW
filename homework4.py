import math
# PROGRAM 1 - REVERSED ARRAY


def program1(arr):
    for x in range(len(arr)):
        arr.insert((x - 1), arr[-1])
        arr.pop(-1)
    return arr


print("Program 1 -- Reverse Array" + "\n")
program1Arr1 = [1, 2, 3, 4]
program1Arr2 = [15, 23, 53, 66]
print(f'test case 1 :  [1, 2, 3, 4] becomes -> {program1(program1Arr1)}')
print(f'test case 2 :  [15, 23, 53, 66] becomes -> {program1(program1Arr2)}')


#  output for program 1:
# Program 1 -- Reverse Array
# test case 1 :  [1, 2, 3, 4] becomes -> [4, 3, 2, 1]
# test case 2 :  [15, 23, 53, 66] becomes -> [66, 53, 23, 15]

# PROGRAM 2 - WRAP BY K

def program2(lst, k):
    i = 0
    y = k
    for x in range(k, 0, -1):
        # print(y, i, lst)
        lst.insert(i, lst[-y])
        lst.pop(-y)
        i += 1
        y -= 1
    return lst


print("\n" + "Program 2 -- wrap by k" + "\n")
program2Arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
k1 = 3
program2Arr2 = [1, 23, 46, 64, 22, 67, 88, 8, 10, 13, 5, 33]
k2 = 5

print(f'test case 1 :  [1, 2, 3, 4, 5, 6, 7, 8] wrap by {k1}  becomes -> {program2(program2Arr1, k1)}')
print(f'test case 1 :  [1, 23, 46, 64, 22, 67, 88, 8, 10, 13, 5, 33] wrap by {k2}'
      f' becomes -> {program2(program2Arr2, k2)}')

#  output for program 2:
# Program 2 -- wrap by k
# test case 1 :  [1, 2, 3, 4, 5, 6, 7, 8] wrap by 3  becomes -> [6, 7, 8, 1, 2, 3, 4, 5]
# test case 1 :  [1, 23, 46, 64, 22, 67, 88, 8, 10, 13, 5, 33] wrap by 5 becomes
# -> [8, 10, 13, 5, 33, 1, 23, 46, 64, 22, 67, 88]

# questions:
# How many swaps are required for an array of size n with  a wrap of k places?
#     - I didn't use any swaps but k "swaps will be required"
# This method is O(?)
#     - it is 1n because there is only 1 loop


# PROGRAM 3 - ZEROS


def program3(n):
    count = 0
    for x in range(n, 1, -1):
        var = x
        while var % 5 == 0:
            var /= 5
            count += 1

    return count


print("\n" + "Program 3 -- Zeros of n!" + "\n")
n1 = 10
print(f'test case 1 :  {n1}! has {program3(n1)} zero(s)')
print(f'{n1}! is {math.factorial(n1)}')
n2 = 23
print(f'test case 2 :  {n2}! has {program3(n2)} zero(s)')
print(f'{n2}! is {math.factorial(n2)}')
n3 = 20
print(f'test case 3 :  {n3}! has {program3(n3)} zero(s)')
print(f'{n3}! is {math.factorial(n3)}')

# #  output for program 2:
# test case 1 :  10! has 2 zero(s)
# 10! is 3628800
# test case 2 :  23! has 4 zero(s)
# 23! is 25852016738884976640000
# test case 3 :  20! has 4 zero(s)
# 20! is 2432902008176640000

# questions:
# Your method is what order?
#     - my method is order n because you have to loop through n times
