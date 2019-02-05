a=int(input())
if(a%400==0):
    print("leapyear")
elif(a%4==0):
    print("leapyear")
elif(a%100!=0):
    print("leapyear")
else:
    print("not leapyear")
