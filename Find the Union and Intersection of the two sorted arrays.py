s1=[1,2,3,4,5,6]
s2=[5,6,7,8,9,10]
u,it=[],[]
for i in s1:
    if i in s2:
        it.append(i)
        u.append(i)
    else:
        u.append(i)
for i in s2:
    if i not in u:
        u.append(i) 
print(u)
print(it)