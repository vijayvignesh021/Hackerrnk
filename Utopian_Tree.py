import math
import os
import random
import re
import sys

def utopianTree(n):
    h,p = 1,0
    while p<n :
        if h%2 != 0:
            h *= 2
        else:
            h+=1
        p += 1
    return h
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
  
