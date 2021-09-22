# https://www.hackerrank.com/challenges/absolute-permutation/problem
#!/bin/python3

import math
import os
import random
import re
import itertools
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k

def absolutePermutation(n, k):
    array = [i for i in range(n + 1)]
    if k == 0:
        return array[1:]
    elif n % k == 1:
        return [-1]
    for idx in range(1, n - k + 1):
        if array[idx] == array[idx + k] - k:
            array[idx], array[idx + k] = array[idx + k], array[idx]
        elif abs(array[idx] - idx) != k:
            return [-1]
    for idx in range(n - k + 1, n + 1):
        if abs(idx - array[idx]) != k:
            return [-1]
    return array[1:]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
