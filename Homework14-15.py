# PROGRAM 1 - BRUTE FORCE INVERSIONS

def brute(arr):
    numInv = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                numInv += 1

    return numInv


A = [3, 2, 1, 5, 10, 6, 4, 8, 7, 9]
print(f'The array has {brute(A)} inversions')


# PROGRAM 2 - MERGES TWO SORTED ARRAYS AND COUNTS THE SPLIT INVERSIONS

def merge_countSplitInv(a, b):
    i = 0
    j = 0
    splitInv = 0
    c = []
    for x in range(2 * len(a)):
        if i >= len(a):  # IF THE FIRST ARRAY IS FULLY TRANSFERRED TO OUTPUT ARRAY
            c.append(b[j])
            j += 1
            splitInv += (len(a) - i)
        elif j >= len(b):  # IF THE SECOND
            # ARRAY IS FULLY TRANSFERRED TO OUTPUT ARRAY
            c.append(a[i])
            i += 1
        elif a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            splitInv += (len(a) - i)
    return c, splitInv


C = [1, 2, 4, 7]
D = [0, 3, 5, 6]
merged, split = merge_countSplitInv(C, D)
print(f'The merged array  is {merged} and split inversions count is {split}')
C = [2, 3, 5, 7]
D = [0, 1, 4, 6]
merged, split = merge_countSplitInv(C, D)
print(f'The merged array  is {merged} and split inversions count is {split}')


# PROGRAM 3 - SORTS AN ARRAY AND RETURNS TOTAL INVERSIONS

def sort_countInt(arr):
    n = len(arr)
    if n == 1:
        return arr, 0
    else:
        front, leftInversions = sort_countInt(arr[:len(arr) // 2])  # : = front tll
        back, rightInversions = sort_countInt(arr[len(arr) // 2:])  # half way till end
        b, splitInv = merge_countSplitInv(front, back)
        return b, (leftInversions + rightInversions + splitInv)


A = [4, 2, 1, 7, 6, 5, 3, 0]
sorted_arr, count = sort_countInt(A)
print(f'sorted: {sorted_arr} \ninversions: {count}')
A = [5, 2, 3, 7, 4, 0, 1, 6]
sorted_arr, count = sort_countInt(A)
print(f'sorted: {sorted_arr} \ninversions: {count}')

#       OUTPUT:

# PROGRAM 1:
# The array has 11 inversions

# PROGRAM2:
# The merged array  is [0, 1, 2, 3, 4, 5, 6, 7] and split inversions count is 8
# The merged array  is [0, 1, 2, 3, 4, 5, 6, 7] and split inversions count is 11

# PROGRAM3:
# sorted: [0, 1, 2, 3, 4, 5, 6, 7]
# inversions: 17
# sorted: [0, 1, 2, 3, 4, 5, 6, 7]
# inversions: 15
