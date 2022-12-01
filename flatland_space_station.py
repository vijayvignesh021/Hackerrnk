#!/bin/python3

import math
import os
import random
import re
import sys

def flatlandSpaceStations(n, c):
    c = sorted(c)
    max_d = max (c[0], n - c[-1] - 1)
    last_cty = c[0]
    for i in range(1, len(c)):
        dis = (c[i] - last_cty) // 2
        max_d = max(max_d, dis)
        last_city = c[i]
    return max_d

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))
