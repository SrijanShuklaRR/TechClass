import heapq
arr1=[]
size=int(input())
for i in range(size):
    n=int(input())
    arr1.append(n)
k=int(input())
print(heapq.nlargest(k,arr1)[-1])
print(heapq.nsmallest(k,arr1)[-1])