# https://www.hackerrank.com/challenges/3d-surface-area/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    H, W = len(A), len(A[0])
    area = 2 * H * W
    for idx in range(H):
        for jdx in range(W):
            left = jdx - 1
            right = jdx + 1
            front = idx - 1
            back = idx + 1
            # left
            if left >= 0:
                if A[idx][left] <= A[idx][jdx]:
                    area += (A[idx][jdx] - A[idx][left])
            else:
                area += A[idx][jdx]
            # right
            if right < W:
                if A[idx][right] <= A[idx][jdx]:
                    area += (A[idx][jdx] - A[idx][right])
            else:
                area += A[idx][jdx]
            # front
            if front >= 0:
                if A[front][jdx] <= A[idx][jdx]:
                    area += (A[idx][jdx] - A[front][jdx])
            else:
                area += A[idx][jdx]
            # back
            if back < H:
                if A[back][jdx] <= A[idx][jdx]:
                    area += (A[idx][jdx] - A[back][jdx])
            else:
                area += A[idx][jdx]
    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
