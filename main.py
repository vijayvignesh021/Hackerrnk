str= "haveaniceday"
print(len(str))
x = [ str[i] for i in range(len(str)) if(str[i] != " ")]
r = int(len(x)**0.5) 
c = r+1
if r*r == len(x):
  c=r
if r*c < len(x):
  r = r+1
i = 0
lis=[]
inx=[]
while(i < len(x)):
  inx.append(x[i])
  if (len(inx)==c or i+1 ==len(x)):
    lis.append(inx)
    inx=[]
  i+=1
str=""
lm =len(lis[0])-len(lis[-1])
print(lm,r,c)
for i in range(c-lm):
  for j in range(len(lis)):
    str += lis[j][i]
  str +=" "
if len(lis[0]) != len(lis[-1]):
  for i in range(len(lis[-1]),len(lis[0])):
    for j in range(r-1):
      str += lis[j][i]
    str += " "
print(str)