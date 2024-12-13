import random
from colorama import Back, Style, Fore
import time
import copy
#important srcs:
# https://johnfoster.pge.utexas.edu/numerical-methods-book/LinearAlgebra_LU.html
# https://github.com/adolfos94/Bareiss-Algorithm

def user_input():
    print("This program calculates the determinant of a square matrix using different algorithms.")
    size = input("What size would you like your square matrix to be?\n")
    while size.isdigit() == False or int(size) <= 0:
        size = input("Please enter a valid number.\n")
    rando = input("Would you like to generate a random matrix? (y/n)\n")
    while rando != "y" and rando != "n":
        rando = input("Please enter a valid response.\n")
    return int(size), rando

def initialize_matrix(size):

    x = Back.RED + " " + Style.RESET_ALL
    matrix = [[x for _ in range(size)] for _ in range(size)]
    matrix[0][0] = "_"

    print("Below is the empty matrix, with the red elements being uninitialized.")
    print_matrix(matrix)
    for i in range(size ** 2):

        #checks if the user-input element is a number
        keep_going = True
        while keep_going:
            try:
                element = input("Enter the element you would like at the underlined location.\n")
                float(element)
                keep_going = False
            except:
                print("Please enter a valid number.")

        
        matrix[i // size][i % size] = element 

        #move the underline
        if i < size ** 2 - 1: #if not the last element
            if i % size == size - 1: #if at the end of the row
                matrix[i // size + 1][0] = "_"
            else:
                matrix[i // size][i % size + 1] = "_" #move the underline to the right
        
        print_matrix(matrix)



    return matrix

def initialize_random_matrix(size):

    random_num = input("What would you like the largest possible value to be?" + 
                 " (the random values will range from 0 to said value)\n")
    while random_num.isdigit() == False or int(random_num) <= 0:
        random_num = input("Please enter a valid number.\n")

    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(str(random.randint(0, int(random_num))))
        matrix.append(row)
    print_matrix(matrix)
    return matrix

def print_matrix(matrix):
    ''''
    Prints the matrix in a visually appealing way (with correct spacing)
    Args:
        matrix: (2d array) the matrix to be printed
    '''
    #iterate through the rows
    for i, row in enumerate(matrix):
        print("[", end="") #print the opening bracket, starting each row
        
        #iterate through the elements in the row
        for j, val in enumerate(row):
            if j > 0:
                print(", ", end="") #print a comma & space after first element
            
            max_digits = 0
            #for each row
            for k in range(0, len(matrix)):
                #count the number of digits for each element at that jth element in the kth row
                
                # case where background color is in string, only need to consider characters
                # after color and before reset
                #check if len > 1 to avoid index out of bounds
                if len(matrix[k][j]) > 1 and matrix[k][j][1] == "[": 
                    #get all characters after color and before reset
                    new_string = matrix[k][j][matrix[k][j].find('m')+1:matrix[k][j].rfind('\x1b')]
                    if len(new_string) > max_digits:
                        max_digits = len(new_string)
                
                elif len(str(matrix[k][j])) > max_digits:
                    max_digits = len(str(matrix[k][j]))
            
            #print the element with the correct number of spaces
            if val.count('[') > 0:
                max_digits = max_digits - len(val[val.find('m')+1:val.rfind('\x1b')])
            else:
                max_digits = max_digits - len(str(val))
            for l in range(0, max_digits):
                print(" ", end="")
            print(val, end="")

        print("]") #ending each row

def determinant_choice():
    num = input("How many algorithms would you like to use to calculate the determinant? (1/2/3)\n")
    while num != "1" and num != "2" and num != "3":
        num = input("Please enter a valid choice.\n")

    choices = []
    for i in range(1, int(num) + 1):
        choice = input("Which algorithm would you like to use to calculate the determinant? (1/2/3)\n1. Laplace Expansion\n2. LU Decomposition\n3. Bareiss Algorithm\n")
        while choice != "1" and choice != "2" and choice != "3":
            choice = input("Please enter a valid choice.\n")
        while choice in choices:
            choice = input("Please enter an algorithm that hasn't already been selected.\n")
        choices.append(choice)
    
    return choices 

def laplace_expansion(matrix):
    '''
    O(n!) time complexity-recursively computes determinant using Laplace Expansion
    Args:
        matrix: (2d array) the matrix to compute the determinant of
    Returns:
        det: (float) the determinant of the matrix
    '''
        # Base case of recursive function: 1x1 matrix
    if len(matrix) == 1: 
        return matrix[0][0]

    det = 0
    #column = number (0, 1, 2, ...)
    #element = actual values of that column

    for column, element in enumerate(matrix[0]):
        # Exclude first row and current column.
        K = [x[:column] + x[column + 1 :] for x in matrix[1:]]
        #multiply by 1 or -1
        s = 1 if column % 2 == 0 else -1 
        #recursive call
        det += s * element * laplace_expansion(K)
    return det


#might need for bareiss algo
def swap_0pivot_rows(matrix):


    return matrix

def bareiss_algo(matrix):
    pivot = 1
    for k in range(len(matrix) - 1):
        for i in range(k + 1, len(matrix)):
            for j in range(k + 1, len(matrix)):
                matrix[i][j] = matrix[k][k] * matrix[i][j] - matrix[i][k] * matrix[k][j]
                print("matrix[i][j]:", matrix[i][j])
                print("pivot:", pivot)
                matrix[i][j] = matrix[i][j] // pivot
        
        pivot = matrix[k][k]

    det = matrix[len(matrix) - 1][len(matrix) - 1]
    return det

def plu_decomp(matrix):    
    '''
    PLU decomposition of a matrix. Determinant is simply the diagonal elements of U
    multiplied together, with a negative sign if there were an odd number of permutations.
    Args:
        matrix: (2d list) the matrix to be decomposed
    Returns:
        det: (float) the determinant of the matrix (Note: because the determinant is a float, 
        sometimes it is not exactly the whole number we expect, but instead a fraction that is very close to it)
    '''
    #let U just be a copy of the original matrix
    U = matrix.copy()

    #initialize L and P to be identity matrices of the correct size
    L = []
    for i in range(len(U[0])):
        L.append([0] * len(U))
        L[i][i] = 1

    P = L.copy()

    permutations = 0

    for i in range(len(U[0])):

        #Swap rows if necessary
        for k in range(i, len(matrix[0])): 
            if (U[i][i] != 0):
                break
            U[[k][k+1]] = U[[k+1][k]]
            permutations += 1

        #optimized gaussian elimination to find L & U
        for j in range(i + 1, len(U[0])): #lii never gets changed from 1 because j is always i + 1
            # Set  lji=uji/uii
            L[j][i] = U[j][i] / U[i][i] #this line should be changed to just being called the ratio
                                        #and not changing the elements of L, as doing so  makes it upper triangular
            
            print("L[j][i]:", L[j][i])

            row = []
            for element in U[i]:
                row.append(element * L[j][i])
            
            for l in range(len(U[j])):
                U[j][l] = U[j][l] - row[l]
                print("U[j][l]:", U[j][l])

            

    det = 1
    #for PLU decomp, the determinant is the product of the diagonal elements of U
    for m in range(len(U)):
        det *= U[m][m]

    #if there were an odd number of permutations, the determinant is negated
    if permutations % 2 == 1:
        det *= -1
    
    return det


def multiply(matrix1, matrix2):
    '''
    Multiplies two matrices together
    Args:
        matrix1: (2d list) the first matrix to be multiplied
        matrix2: (2d list) the second matrix to be multiplied
    Returns:
        result: (2d list) the result of the matrix multiplication
    '''
    # Get the size of the matrix (assuming both are square and same size)
    n = len(matrix1)
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    # Perform matrix multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def small_edge_cases(matrix):
    if len(matrix) == 1:
        print("The determinant of a 1x1 matrix is itself")
    else:
        print("The determinant of a 2x2 matrix is easy to calculate and doesn't require a complex algorihtm.")
        print("[a, b]\n[c, d]\n det = ad - bc")
        print("The determinant of the matrix above is " + str(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]))
    exit()

def main():
    '''
    Entry point into the program.
    '''

    size, rando = user_input()

    if rando == "y":
        matrix = initialize_random_matrix(size)
    else:
        matrix = initialize_matrix(size)
    
    #convert str values in matrix to float values
    matrix = [[float(x) for x in row] for row in matrix]


    if size < 3:
        small_edge_cases(matrix)

    choices = determinant_choice()

    for choice in choices:
        #determinant
        match choice:
            case "1":
                start = time.time_ns()
                print("determinant using laplace expansion: ", laplace_expansion(matrix))
                end = time.time_ns()
                total = (end - start) / 1000000000
                print("Time taken: ", total, " seconds\n\n")
            case "2":
                cp_matrix = copy.deepcopy(matrix)
                start = time.time_ns()
                print("determinant using plu decomposition: ", plu_decomp(cp_matrix))
                end = time.time_ns()
                total = (end - start) / 1000000000
                print("Time taken: ", total, " seconds\n\n")
                print("Time taken 2 : ", (end - start), "\n\n")
                print("start:", start)
                print("end:", end, "\n\n")


            case "3":
                for i, row in enumerate(matrix):
                    for j, value in enumerate(row):
                        if not value.is_integer():
                            print(Fore.RED + "Bareiss Algorithm only works with integer matrices." + Style.RESET_ALL)
                            exit()


                matrix = [[int(x) for x in row] for row in matrix]
                start = time.time_ns()
                print("determinant using bareiss algo: ", bareiss_algo(matrix))
                end = time.time_ns()
                total = (end - start) / 1000000000
                print("Time taken: ", total, " seconds\n\n")
                print("Time taken 2 : ", (end - start), " seconds\n\n")
                print("start:", start)
                print("end:", end, "\n\n")


    

if __name__ == "__main__":
    main()