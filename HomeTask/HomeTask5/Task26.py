
def grade(a,b):
    if b==1:
        return a
    if b!=1:
        return a*grade(a,b-1)
a= int(input("Ведите число а: "))
b= int(input("Ведите число b: "))    
print(grade(a,b))    


