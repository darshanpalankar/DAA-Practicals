import array as arr
print("Performed By 42 & 47")

# Sum of elements of an array (using built-in sum)
def sum_built_in():
    NumArray = []
    Number = int(input("\nPlease Enter the total Number of array Elements : "))
    for i in range(1, Number + 1):
        value = int(input(f"Please Enter the value of {i} Element : "))
        NumArray.append(value)

    total = sum(NumArray)
    print(f"\nThe Sum of all elements in the Array {NumArray} is : {total}")

# Sum of elements of an array (using loop)
def sum_loop():
    NumArray = []
    Number = int(input("\nPlease Enter the size of An Array : "))

    for i in range(1, Number + 1):
        value = int(input(f"Please Enter the value of {i} Element : "))
        NumArray.append(value)

    total = 0
    for i in NumArray:
        total += i
    print(f"\nThe Sum of all elements in the Array {NumArray} is : {total}")

#Searching an element in an array
def search_element():
    a = int(input("\nEnter size of the array : "))
    array = []

    for i in range(a):
        b = int(input("\nEnter Element : "))
        array.append(b)

    print("\nThe Array you created is ", array)
    c = int(input("\nEnter the element to search : "))

    for i in range(a):
        if array[i] == c :
            print("Element is", array[i])
            print("At Index",i)
            print("At Position", i+1)
            break
        else:
    	    print("The Element is not Found..!!")

def max_min():
    NumArray = []
    Number = int(input("\nPlease Enter the Size of Array : "))

    for i in range(1, Number + 1):
        value = int(input(f"Please enter the value of {i} Element : "))
        NumArray.append(value)

    print("\nThe array you created is:", NumArray)
    print(f"Greatest element in the array is: {max(NumArray)}")
    print(f"Smallest element in the array is: {min(NumArray)}")

def max_min_Loop():
    def MaxofArray(arr):
        max = a[0]
        n = len(arr)
        for i in range(n):
            if max < a[i]:
                max = a[i]
        return max
    def MinofArray(arr):
        min = a[0]
        n = len(arr)
        for i in range(n):
            if min > a[i]:
                min = a[i]
        return min
    
    #input values
    a = []
    Number = int(input("\nPlease Enter the Size of Array : "))

    for i in range(1, Number+1):
        value = int(input("Please enter the value of %d Element : "%i))
        a.append(value)

    #Display
    print("\nThe array you created is ", a)
    print(f"\nGreatest element in the {a} is ", MaxofArray(a),".")
    print(f"Smallest element in the {a} is ", MinofArray(a),".")
    
def even_odd():
    n=int(input("\nEnter Array Size : "))
    arr=[]

    for i in range(1,n+1):
        value=int(input("Please enter the value of %d elements : "%i))
        arr.append(value)
        
    even_count , odd_count= 0 , 0
    for i in arr:
        if i % 2 == 0 :
            even_count +=1
        else:
            odd_count +=1

    print("\nNumber of Even elements : ", even_count)
    print("Number of odd elements : ", odd_count)

def main():
    #Program List
    print("1. Sum of elements of an array (By using sum)")
    print("2. Sum of elements of an array (By using Loop)")
    print("3. Searching an element in an array")
    print("4. Finding Minimum & Maximum element in an array(Using Min() & Max() Functions)")
    print("5. Finding Minimum & Maximum element in an array(By Using Loops & Conditions)")
    print("6. Count the number of even & odd numbers in an array")

    user_choice = input("Enter your Choice : ")

    if user_choice == "1":
        sum_built_in()
    elif user_choice == "2":
        sum_loop()
    elif user_choice == "3":
        search_element()
    elif user_choice == "4":
        max_min()
    elif user_choice == "5":
        max_min_Loop()
    elif user_choice == "6":
        even_odd()
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()