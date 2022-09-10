import math
import os
import random
import re
import sys

def larrysArray(A):#A=[3,1,2]
    count = 0
    for i in range(1,len(A)):
        for j in range(i):
            if A[j] > A[i]:
                count += 1
    if count%2 == 0:
        return "YES"
    return "NO"
                
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
