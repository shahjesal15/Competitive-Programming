# https://www.hackerrank.com/challenges/grid-challenge/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    rows, cols = len(grid), len(grid[0])
    grid[0] = sorted(grid[0])
    for row in range(1, rows):
        grid[row] = sorted(grid[row])
        for col in range(cols):
            if grid[row - 1][col] > grid[row][col]:
                return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
