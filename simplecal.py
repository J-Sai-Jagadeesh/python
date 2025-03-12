num1=float(input("enter 1st valu:"))
num2=float(input("enter 2nd value:"))
opr=input("enetr operation:")
if opr=="+":
    print(f"addition is:{num1+num2}")
elif opr=="-":
    print(f"sub is:{num1-num2}")
elif opr=="*":
    print(f"mul is:{num1*num2}")
elif opr=="/":
    print(f"divison is:{num1/num2}")
elif opr=="//":
    print(f"floar division:{num1//num2}")
elif opr=="**":
    print(f"square is:{num1**num2}")
elif opr=="%":
    print(f"modlues is:{num1%num2}")      
else:
    print("invalid operation!")