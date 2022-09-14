import math
import os
import random
import re
import sys


def jimOrders(n,orders):
    order_seq = 1
    out = []
    for i in range(n):
        orders[i][0] = orders[i][0] + orders[i][1]
        orders[i][1] = order_seq
        order_seq += 1
    orders.sort()
    for i in orders:
        out.append(i[1])
    return out

        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(n,orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
