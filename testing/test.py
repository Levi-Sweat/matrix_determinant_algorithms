import random

def initialize_random_matrix(size):
    print("gets here")
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(random.randint(0, 1000))
        matrix.append(row)
    return matrix

#only correctly indenting spacing some of the time
def print_matrix(matrix):
    for i, row in enumerate(matrix):
        print("[", end="")
        for j, val in enumerate(row):
            if j > 0:
                print(", ", end="")
            
            max_digits = 0
            #for each row
            for k in range(0, len(matrix)):
                #count the number of digits for each element at that jth element in the kth row
                if len(str(matrix[k][j])) > max_digits:
                    max_digits = len(str(matrix[k][j]))
            
            #print the element with the correct number of spaces
            max_digits = max_digits - len(str(val))
            for l in range(0, max_digits):
                print(" ", end="")
            print(val, end="")

        print("]")



#matrix = initialize_random_matrix(3)

matrix =[[-1.124, 2.0, 3.0], [4.0, 5432.53, 5], [7.0, 8.0, 9.0]]

print_matrix(matrix)
#print(len(str(matrix[0][2])))