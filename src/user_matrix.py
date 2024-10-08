import random
from colorama import Back, Style, Fore


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
    choice = input("Which algorithm would you like to use to calculate the determinant? (1/2/3)\n1. Laplace Expansion\n2. LU Decomposition\n3. Bareiss Algorithm\n")
    while choice != "1" and choice != "2" and choice != "3":
        choice = input("Please enter a valid choice.\n")
    return choice

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
    for column, element in enumerate(matrix[0]):
        # Exclude first row and current column.
        K = [x[:column] + x[column + 1 :] for x in matrix[1:]]
        #multiply by 1 or -1
        s = 1 if column % 2 == 0 else -1 
        #recursive call
        det += s * element * laplace_expansion(K)
    return det

def plu_decomp(matrix):    
    '''
    LU decomposition of a matrix, using deloittles algorithm (maybe?)
    '''
    #let U just be a copy of the original matrix
    U = matrix.copy()

    #initialize L and P to be identity matrices
    L = []
    for i in range(len(U[0])):
        L.append([0] * len(U))
        L[i][i] = 1

    P = L.copy()

    



def bareiss_algorithm(matrix):
    return

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
    
    if size < 3:
        small_edge_cases(matrix)

    #convert str values in matrix to float values
    matrix = [[float(x) for x in row] for row in matrix]


    choice = determinant_choice()

    match choice:
        case "1":
            print("determinant: ", laplace_expansion(matrix))
        case "2":
            plu_decomp(matrix)
        case "3":
            bareiss_algorithm(matrix)

    

if __name__ == "__main__":
    main()