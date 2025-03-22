n=int(input())
print("Leap" if n%4==0 and n%100!=0 else("leap" if n%400 ==0 else " Not Leap"))