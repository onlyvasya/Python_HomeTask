from random import randint
n = int(input("Введите размер массива  "))
x = int(input("Введите число Х  "))
list=[]
counter=0
for i in range(n):
    number = randint(1,10)
    list.append(number)
print(list)    
for i in range(n):
    if list[i]==x:
        counter=+1
print("X встречается ", counter, " раз")        


     
    
    
    
#     if number==x:
#         counter=+
# print("X встречается ", counter, " раз")





