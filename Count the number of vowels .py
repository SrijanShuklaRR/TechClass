s=input()
v=['a','e','i','o','u']
s.lower()
c=0
for i in s:
    if i in v:
        c+=1
print(c)