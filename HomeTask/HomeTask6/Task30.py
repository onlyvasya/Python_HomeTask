a1,d,n = int(input("Введите первый элемент : ")),int(input("Введите разность : ")),int(input("Введите количество элементов: "))
arr=[]
for j in range(1,n+1):
    arr.append(a1+((j-1)*d))
print(arr)  


