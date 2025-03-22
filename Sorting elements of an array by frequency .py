from collections import Counter
arr=[]
size=int(input())
for i in range(size):
    n=int(input())
    arr.append(n)
c=Counter(arr)
# print(c)
s=sorted(c,key=c.get,reverse=True)
print(s)