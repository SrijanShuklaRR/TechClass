from collections import Counter

s=input()
c=Counter(s)
for i in c:
    if c[i]==1:
        print(i,end=" ")
