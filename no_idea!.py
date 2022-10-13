n,m = map(int,input().split())
n_int = list(map(int,input().split()))
A= set(map(int,input().split()))
B= set(map(int,input().split()))
out = 0
for i in n_int:
    if i in A:
        out += 1
    elif i in B:
        out -= 1
print(out)
