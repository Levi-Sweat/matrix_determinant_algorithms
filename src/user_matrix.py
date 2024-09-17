import random
from colorama import Back, Style, Fore


def user_input():
    print("This program calculates the determinant of a square matrix using different algorithms.")
    size = input("What size would you like your square matrix to be?\n")
    while size.isdigit() == False:
        size = input("Please enter a valid number.\n")
    random = input("Would you like to generate a random matrix? (y/n)\n")
    while random != "y" and random != "n":
        random = input("Please enter a valid response.\n")
    return int(size), random

def initialize_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):

            row.append(" ")
        matrix.append(row)
    return matrix

def initialize_random_matrix(size):
    print("gets here")
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(random.randint(0, 10))
        matrix.append(row)
    return matrix

#not sure if this formatting works the way I want it to, needs testing
def print_matrix(matrix):
    for i, row in enumerate(matrix):
        print("[", end="")
        for j, val in enumerate(row):
            if j > 0:
                print(", ", end="")
            print(val, end="")
        print("]")



size, rando = user_input()

if rando == "y":
    matrix = initialize_random_matrix(size)
else:
    matrix = initialize_matrix(size)

print_matrix(matrix)
print(matrix)