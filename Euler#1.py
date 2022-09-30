def prj(n):
    threes = n//3
    fives = n//5
    fifteens = n//15
    threes = (threes*threes+threes)//2
    fives = (fives*fives+fives)//2
    fifteens =(fifteens*fifteens+fifteens)//2
    print((threes*3)+(fives*5)-(fifteens*15))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    prj(n-1)
