from itertools import groupby

for i,j in groupby(input()):
    print((len(list(j)),int(i)),end=" ")
