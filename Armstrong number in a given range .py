low,high=int(input()),int(input())
for n in range(low,high+1):

    # n=int(input())
    k=len(str(n))
    m=sum(list(map(lambda x:int(x)**k ,str(n))))
    print(n==m )