s=(input("enter 3 nummbers:"))
x,y,z=s.split(",") 
a=int(x)
b=int(y)
c=int(z)      
if a>b:
    if a>c:
        print(a)
elif b>c:
    print(b)
else:
    print(c)
       