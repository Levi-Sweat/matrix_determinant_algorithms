import random
from colorama import Back, Style, Fore


def user_input():
    print("This program calculates the determinant of a square matrix using different algorithms.")
    size = input("What size would you like your square matrix to be?\n")
    while size.isdigit() == False:
        size = input("Please enter a valid number.\n")
    rando = input("Would you like to generate a random matrix? (y/n)\n")
    while rando != "y" and rando != "n":
        rando = input("Please enter a valid response.\n")
    return int(size), rando

def initialize_matrix(size):
    print("Below is the empty matrix, with the background")
    
    x = Back.RED + " " + Style.RESET_ALL
    matrix = [[x for _ in range(5)] for _ in range(5)]
    matrix[0][0] = "_"

    return matrix

def initialize_random_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(random.randint(0, 1000))
        matrix.append(row)
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
            max_digits = max_digits - len(str(val))
            for l in range(0, max_digits):
                print(" ", end="")
            print(val, end="")

        print("]") #ending each row




def main():
    '''
    Entry point into the program.
    '''

    size, rando = user_input()

    if rando == "y":
        matrix = initialize_random_matrix(size)
    else:
        matrix = initialize_matrix(size)
    
    print_matrix(matrix)

if __name__ == "__main__":
    main()