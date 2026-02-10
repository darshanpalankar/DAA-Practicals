#Find the kth smallest / largest element in sorted order

print("Performed By 42 & 47")

a = []
n = int(input("Enter the number of elements of the list : "))
counter = 1

for i in range(n):
    values = int(input(f"Enter element {counter} : "))
    a.append(values)

k = int(input("\nEnter the value of k : " ))
l = int(input("\nEnter '0' for the kth smallest element OR Enter '1' for the kth largest element : "))

for i in range(0, n):
    for j in range(0, n-i-1):
        if (a[j] > a[j+1]):
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t
    
print("The sorted elements : ",end = " ")
for i in range(0, n):
    print(a[i], end = " ")
    
if l == 1:
    for i in range(n-1, n-k-1, -1):
        m = 0
    print("\nThe ",k,"the Largest element is : ", a[i])

else:
    for i in range(0, k):
        m = 0
        print("\nThe ",k,"the Smallest element is : ", a[i])       