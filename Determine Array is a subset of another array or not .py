arr1=[]
size=int(input())
for i in range(size):
    n=int(input())
    arr1.append(n)
arr2=[]
size=int(input())
for i in range(size):
    n=int(input())
    arr2.append(n)
if all(n in arr2 for n in arr1):
    print(True)
else:
    print(False)
