#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    l=len(arr[0])
    t1=0
    last=l-1
    t2=0
    while (last>=0):
       for i in range(l):
          t2+=arr[i][last]
          for j in range(l):
              if i == j:
                 t1+=arr[i][j]
          last=last-1
    if t1>t2:
        a=t1-t2
    else:
        a=t2-t1
    return a
            
                
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
