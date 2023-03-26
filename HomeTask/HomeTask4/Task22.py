from random import*
m = int(input("Введите размер списка 1: "))
list1 = [randint(1,10) for i in range(m)]
print(list1)
n = int(input("Введите размер списка 2: "))
list2 = [randint(1,10) for i in range(n)]
print(list2)
print(*set(list1)&set(list2))    


