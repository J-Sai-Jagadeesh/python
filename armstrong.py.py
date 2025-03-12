
def arm_num(number):
    lenght=0
    for i in str(number):
        lenght+=1  
    digt=str(number)
    tsum=sum(int(x)**lenght for x in digt)
    return tsum==number
a=int(input("enter a number:"))    
if arm_num(a):
    print(f"{a} is armstrong number")
else:
    print("%d is not armstrong number",a)   