arr=[]
size=int(input())
for i in range(size):
    n=int(input())
    arr.append(n)
count_e=0
count_o=0
for i in arr:
    if i%2==0:
        count_e+=1
    else:
        count_o+=1
print("even ",count_e," odd ",count_o)