# https://www.hackerrank.com/challenges/picking-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    _max, subarray, oscillator = 0, 1, 0
    for idx in range(1, len(a)):
        oscillator += abs(a[idx - 1] - a[idx])
        if oscillator <= 1:
            subarray += 1
        else:
            subarray = 1
            oscillator = 0
        _max = max(subarray, _max)
    return _max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
