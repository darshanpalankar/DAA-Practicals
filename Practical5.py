#Practical 5

#Bubble Sort Algorithm
def BubbleSort(collection):
    for value in range(len(collection) -1, 0, -1):
        for i in range(value):
            if collection[i] > collection[i+1]:
                print("Rearranging Collection : ", collection)
                temp = collection[i]
                collection[i] = collection[i+1]
                collection[i+1] = temp

#Selection Sort Algorithm
def SelectionSort(collection):
    for i in range(len(collection)):
        min = i
        for j in range(i+1, len(collection)):
            if collection[min] > collection[j]:
                min = j
                temp = collection[i]
                collection[i] = collection[min]
                collection[min] = temp
                return collection

#Insertion Sort Algorithm
def InsertionSort(collection):
    for i in range(1, len(collection)):
        current_val = collection[i]
        while i > 0 and collection[i-1] > current_val:
            collection[i] = collection[i-1]
            i -= 1
            collection[i] = current_val
            return collection

#Main code
def main():
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")

    choice = input("Enter a choice : ")

    if choice == "1":
        collection = [123, 456, 789, 654, 321, 159, 357, 753, 753, 951]
        print("Collection Before Sort : ", collection)
        BubbleSort(collection)
        print("Sorted Collection      : ", collection)
    elif choice == "2":
        collection = []

        counter = 1
        num = int(input("Enter the size of collection : "))

        for i in range(num):
            value = int(input(f"Enter element {counter} : "))
            collection.append(value)
            counter += 1
            
        print("The Unsorted Collection you created is : ", collection)

        for i in range(10):
            SelectionSort(collection)
            print("The Collection after sorting : ", collection)

        print("The Final Sorted Collection : ", collection)

    elif choice == "3":
        collection = [2, 1, 5, 9, 3, 4, 7]
        print("The Unsorted Collcetion is : ", collection)

        for i in range(len(collection)):
            InsertionSort(collection)
            print("The Sorted Collection is : ",collection)

        print("The Final Sorted Collection is : ", collection)

if __name__ == "__main__":
    main()