

import math
import os
import random
import re
import sys


def designerPdfViewer(h, word):
    m = 0
    for i in word:
       m = max(m,h[ord(i)-97]) 
    return len(word)*m
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
