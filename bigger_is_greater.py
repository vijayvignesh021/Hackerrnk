#!/bin/python3

import math
import os
import random
import re
import sys


def biggerIsGreater(w):
    for i in range(len(w)-2,-1,-1):
        if w[i] < w[i+1]:
            stor = w[i]
            sorts = sorted(w[i:len(w)])
            for j in range(len(sorts)):
                if stor < sorts[j]:
                    ondru =sorts.pop(j)
                    return (w[0:i]+ondru+"".join(sorts))
                    
                    
    return "no answer"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
