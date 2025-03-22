arr=[]
size=int(input())
for i in range(size):
    n=int(input())
    arr.append(n)
n=min(arr)
new_arr=[i for i in arr if i != n]
print(min(arr))
