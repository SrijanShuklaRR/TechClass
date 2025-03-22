arr=[1,0,0,1,1,2,2,1,0,1,1]
z,o,t=0,0,0
arr2=[]
for i in arr:
    if i ==0:
        z+=1
    elif i==1:
        o+=1
    else:
        t+=1
for i in range(z):
    arr2.append(0)
for i in range(o):
    arr2.append(1)
for i in range(t):
    arr2.append(2)
print(arr2)

