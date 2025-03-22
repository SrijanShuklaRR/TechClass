n=int(input())
k=len(str(n))
m=sum(list(map(lambda x:int(x)**k ,str(n))))
print(n==m )