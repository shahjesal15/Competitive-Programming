# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(array: list) -> int:
    _min, size = float("inf"), len(array)
    array.sort()
    for idx in range(size - 1):
        _min = min(abs(array[idx] - array[idx + 1]), _min)
    return _min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
