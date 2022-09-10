import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    single = 0
    for i in range(len(bill)):
        if i != k:
            single += bill[i]
    single = b-int(single/2)
    if single==0:
        print("Bon Appetit")
    else:
        print(single)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
