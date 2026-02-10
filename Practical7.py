import re

def Program1():
    txt = "The rain in Spain"
    x = re.search("^The.*Spain$", txt)

    if x:
        print("Yes! We have match!!")
    else:
        print("No match!!")

def Program2():
    txt = "The rain in Spain"
    x = re.findall("ai", txt)
    print(x)

def Program3():
    try:
        txt = "The rain in Spain"
        x = re.search("\\s", txt)
        print("The first white-space character is located at index : ",x.start())
    except Exception as error:
        print("<<<<<>>>>>>")

def Program4():
    try: 
        txt = "The rain in Spain"
        x = re.split("\s", txt)
        print(x)
    except Exception as error:
        print("<<<<<>>>>>>")

def Program5():
    try:
        txt = "The rain in Spain"
        x = re.sub("\s","9",txt)
        print(x)
    except Exception as error:
        print("<<<<<>>>>>>")

def match(string, sub_string):
    l = len(string)
    ls = len(sub_string)
    start = sub_string[0]

    for k in range(l - ls + 1):
        if start == string[k]:
            i, j = 1, k+1
            while i < ls:
                if sub_string[i] == string[i]:
                    i += 1
                    j += 1
                else:
                    break
            else:
                print(f"Found the {sub_string} substring in the string at index : ", k)

def main():
    while True:
        print("1. Program 1")
        print("2. Program 2")
        print("3. Program 3")
        print("4. Program 4")
        print("5. Program 5")
        print("6. Brute-Force Algorithm")
        print("7. Exit")

        choice = input("Enter your choice : ")

        if choice == "1":
            Program1()
        elif choice == "2":
            Program2()
        elif choice == "3":
            Program3()
        elif choice == "4":
            Program4()
        elif choice == "5":
            Program5()
        elif choice == "6":
            match("AABAACAADAABAABA","AABA")  
        elif choice == "7":
            break  
        else:
            print("Invalid Choice!!")

if __name__ == "__main__":
    main()