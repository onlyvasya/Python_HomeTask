from random import randint
n = int(input("Введите размер массива  "))
x = int(input("Введите число Х  "))
list=[]
counter=0
for i in range(n):
    number = randint(1,10)
    list.append(number)
print(list)  
diff=10
list_min = 0
for i in range(n):
    diff_temp = list[i] - x
    if diff_temp<0:
        diff_temp = (diff_temp)*-1 
    if diff_temp<diff:
        diff=diff_temp
        list_min=list[i]
print("Максимально приближенное число из массива равно  ",list_min)        
