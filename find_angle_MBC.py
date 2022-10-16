import math
ab = int(input())
bc = int(input())
tn = math.degrees(math.atan2(ab,bc))
print("{}\N{DEGREE SIGN}".format(round(tn)))
