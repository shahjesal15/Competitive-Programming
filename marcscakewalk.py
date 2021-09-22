# hackerrank.com/challenges/marcs-cakewalk/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    size, miles = len(calorie), 0
    calorie.sort(reverse=True)
    for idx in range(size):
        miles += (calorie[idx] * fastExpo(2, idx))
    return miles        

def fastExpo(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:          
        return fastExpo(a * a, n // 2)
    return a * fastExpo(a, n - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
