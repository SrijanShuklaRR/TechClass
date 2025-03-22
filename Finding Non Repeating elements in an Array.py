from collections import Counter
arr=[]
size=int(input())
for i in range(size):
    n=int(input())
    arr.append(n)
c=Counter(arr)
for i in c:
    if c[i]==1:
        print(i,end=" ")