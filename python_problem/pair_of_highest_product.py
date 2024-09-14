"""
    Write a program for finding pair of highest product
    input array: [5,3,1,4,3,7,6,9,2]
    Maximum product pair is: (7,9)

    input array: [0,-2,-1,-4,-5,-8,7,-8,8]
    Maximum product pair is: (-8,-8)

"""


# 1st approach
def find_pair_of_highest_product(arr):
    a = arr[0]
    b = arr[1]

    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] * arr[j] > a * b:
                a = arr[i]
                b = arr[j]
    return a, b


print(find_pair_of_highest_product([5, 3, 1, 4, 3, 7, 6, 9, 2]))
print(find_pair_of_highest_product([0, -2, -1, -4, -5, -8, 7, -8, 8]))


# 2nd approach
def max_product_pair(arr):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')

    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    product_max = max1 * max2
    product_min = min1 * min2

    if product_max > product_min:
        return max1, max2
    else:
        return min1, min2


print(max_product_pair([5, 3, 1, 4, 3, 7, 6, 9, 2]))
print(max_product_pair([0, -2, -1, -4, -5, -8, 7, -8, 8]))
