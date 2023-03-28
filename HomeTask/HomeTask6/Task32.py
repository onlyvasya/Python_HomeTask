from random import*
arr = [randint(-10,10) for _ in range(randint(1,15))]
print(arr)
result_arr=[]
for i in range(len(arr)):
    if 5<=arr[i]<=9:
        result_arr.append(i)
print(result_arr)        
