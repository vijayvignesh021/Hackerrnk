import math
import os
import random
import re
import sys


def timeInWords(h, m):
    mm={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13 :"thirteen", 14: "fourteen", 15 : "quarter", 16 : "sixteen", 17 :"Seventeen", 18 :"eighteen", 19 : "nineteen", 20 :"twenty",30:"half"}
    timer = "past"
    minu = "minutes"
    if m > 30:
        m = 60-m
        h = h+1
        timer = "to"
        if h == 13:
            h=1
    if m==1:
        minu ="minute"
    if m == 0:
        return("{} o' clock".format(mm[h]))
    elif m==30:
        return("{} {} {}".format(mm[m],timer,mm[h]))
    else:
        if m== 15:
            return("{} {} {}".format(mm[m],timer,mm[h]))
        else:
            if m > 20:
                return("{} {} {} {} {}".format(mm[20],mm[m%20],minu,timer,mm[h]))
            return("{} {} {} {}".format(mm[m],minu,timer,mm[h]))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
