arr=[]
size=int(input())
for i in range(size):
    n=int(input())
    arr.append(n)
s=set(arr)
print(len(s))