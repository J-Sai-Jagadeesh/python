def unique(string):
    leght=0
    for i in string:
        leght+=1
    for i in range(leght):
        for j in range(i+1,leght):
            if string[i]==string[j]:
                return False
    return True    
a=input("enter a word:")            
if unique(a):
    print("no duplicate elements")
else:
    print("duplicate elements found!")    