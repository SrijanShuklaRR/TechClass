arr=[]
size=int(input())
for i in range(size):
    n=int(input())
    arr.append(n)
neg=[i for i in arr if i<0]
pos=[i for i in arr if i>=0]
print(pos+neg)