print("Performed By 42")
class Practical2:
    # Write a python program to implement 2D array like Row-sum & Col-sum
    def __init__(self):
        pass

    def program1(self):
        Row = int(input("Enter the Number of ROWS : "))
        Column = int(input("Enter the Number of COLUMN : "))
        matrix = []
        print("Enter values in matrix : ")
                    
        for i in range(Row):
            data = []
            for i in range(Column):
                data.append(int(input()))
            matrix.append(data)
                    
        print("\nThe Matrix is \n")

        for i in range(Row):
            for j in range(Column):
                print(matrix[i][j],end = " ")
            print(" ")

        def row_sum():
            sum = 0
            print("\nSUM of ROW\n")
            for i in range(Row):
                for j in range(Column):
                    sum += matrix[i][j]
                print("Sum of row",i+1,"=",sum)
                sum = 0

        def column_sum():
            sum = 0
            print("\nSUM of COLUMN\n")
            for j in range(Column):
                for i in range(Row):
                    sum += matrix[i][j]
                print("Sum of column",i+1,"=",sum)
                sum = 0

        row_sum()
        column_sum()

    #Write a python program to implement 2D array for finding sum of diagonal elements
    def program2(self):

        def printDiagonalSums(mat,n):
            primary = 0
            secondary = 0

            for i in range(n):
                for j in range(n):

                    # Condition for primary diagonal
                    if (i == j):
                        primary += mat[i][j]

                    # Condition for secondary diagonal
                    if ((i + j) == (n-1)):
                        secondary += mat[i][j]
            
            print("Sum of Primary Diagonal is",primary)
            print("Sum of Secondary Diagonal is", secondary)

        # Creating a i*j matix

        a = [[1,2,3,4],
            [5,6,7,8],
            [1,2,3,4],
            [5,6,7,8]]

        printDiagonalSums(a, 4)

    # Write a python program to implement 2D array for Addition of two matrices.

    def program3(self):
        # Matrix X
        x = [[1,2,3],
            [4,5,6],
            [7,8,9]]
            
        # Matrix Y
        y = [[9,8,7],
            [6,5,4],
            [3,2,1]]

        # Result matrix (empty initially)
        result = [[0,0,0],
                [0,0,0],
                [0,0,0]]

        # Matrix Addition
        for i in range(len(x)):               # rows
            for j in range(len(x[0])):        # columns
                result[i][j] = x[i][j] + y[i][j]

        # Print Result in matrix form
        print("\nResultant Matrix (X + Y):")
        for row in result:
            print(row)

    #Write a python program to implement 2D array for Multiplication of two matrics 

    def program4(self):

        A = [[12,7,3],
             [4,5,6],
             [7,8,9]]

        B = [[5,8,1,2],
            [6,7,3,0],
            [4,5,9,1]]

        result = [[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]
        # Iterate by row of A
        for i in range(len(A)):
            # Iterate by column of B
            for j in range(len(B[0])):
                # Iterating by rows of B
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]

        for r in result:
            print(r)



print("1. 2D array like Row-sum & Col-sum")
print("2. finding sum of diagonal elements")
print("3. Addition of two matrices")
print("4. 2D array for Multiplication of two matrics")

x = Practical2()
user_choice = int(input("Enter your Choice : "))

if user_choice == 1:
    x.program1()
elif user_choice == 2:
    x.program2()
elif user_choice == 3:
    x.program3()
elif user_choice == 4:
    x.program4()
else:
    print("Invalid Choice.")
