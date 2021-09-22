# https://www.hackerrank.com/challenges/candies/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    size = len(arr)
    candy = [1] * size
    for idx in range(1, size):
        if arr[idx - 1] < arr[idx]:
            candy[idx] = candy[idx - 1] + 1
    for idx in range(size - 1, 0, -1):
        if (arr[idx - 1] > arr[idx]) and (candy[idx - 1] <= candy[idx]):
            candy[idx - 1] = candy[idx] + 1
    return sum(candy)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
