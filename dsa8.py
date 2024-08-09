# Minimum moves to get number on card and the number in array is same

def minimum_moves(arr):
    arr1 = []
    for i in range(len(arr)):
        arr1.append(arr.count(arr[i]))
    return len(arr)-max(arr1)

n = int(input("enter the length of array"))
lst = []
for i in range(n):
    lst.append(int(input(f"Enter the value of {i} element in array:")))
res = minimum_moves(lst)
print(res)