#INPUT : Linear Search
print("Linear Search")

def Linear_Search(array,n,k):
    for j in range(0, n):
        if array[j] == k:
            return j
    return -1
array = [1,3,5,7,9]
k = int(input("Enter an element to search in the array : "))
n = len(array)
result = Linear_Search(array,n,k)
if (result == -1):
    print("Element no found !")
else:
    print(f"Element {k} found at index : ",result)

# INPUT : Binary search
 
print("Binary Search")

def Binary_Search(arr,k, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1,3,5,7,9]
k = int(input("Enter a number to search in the array : "))
result = Binary_Search(arr,k,0, len(arr) - 1)

if result != 1:
    print(f"Element {k} found at index : {result}")
else:
    print("Element not Found!")
