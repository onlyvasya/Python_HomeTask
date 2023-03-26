from math import*
from random import*
n = int(input("количество кустов: "))
list1 = [randint(1,10) for i in range(n)]
print(list1)
list_count =list()
for i in range(n-1):
    list_count.append(list1[i-1]+list1[i]+list1[i+1])
list_count.append(list1[-2]+list1[-1]+list1[0])
print(max(list_count))
