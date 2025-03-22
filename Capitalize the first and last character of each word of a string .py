s=input()
s_list=s.split()
result=[]
for word in s_list:
    if len(word)==1:
        result.append(word.upper())
    else:
        result.append(word[0].upper()+word[1:-1]+word[-1].upper())
print(" ".join(result)) 
