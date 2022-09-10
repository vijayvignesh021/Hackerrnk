import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    ar.sort()
    count = 0
    i =0
    while(i<n-1):
        if ar[i] == ar[i+1]:
            count += 1
            i += 2
        else :
            i+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
