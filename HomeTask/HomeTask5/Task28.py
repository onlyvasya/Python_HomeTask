def my_summ(a,b):
    if b==0:
        return a
    else:
        return my_summ(a+1,b-1)
a= int(input("Ведите число а: "))
b= int(input("Ведите число b: "))   
print(my_summ(a,b))     
