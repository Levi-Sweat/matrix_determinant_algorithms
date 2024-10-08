from colorama import Back, Style, Fore
import numpy as np


u2 = [[1, 1, 0], [2, 1, -1], [3, -1, -1]]
L = []
for i in range(len(u2[0])):
    L.append([0] * len(u2))
    L[i][i] = 1


def try1(u2, L):
    for i in range(len(u2[0])):

        #        factor = U[i+1:, i] / U[i, i]

        u2_slice = u2[i+1:]
        factor1 = []
        for row in u2_slice:
            factor1.append(row[i] / u2[i][i])
        
        #    L[i+1:, i] = factor
            
        for j in range(len(factor1)):
            L[i+j+1][i] = factor1[j]


        #       U[i+1:] -= factor[:, np.newaxis] * U[i]

        for j in range(len(factor1)):
            u2[i+j+1][i] -= factor1[j] * u2[i][i]

    print(factor1)
    print(u2)
    print(L)
    print("\n\n")

def try2(U, L):
    for i in range(len(U[0])):
        for j in range(i + 1, len(U[0])): 
            # Set  lji=uji/uii
            L[j][i] = U[j][i] / U[i][i]
            #  Perform  Uj=(Uj−ljiUi)


            row = []
            for element in U[i]:
                row.append(element * L[j][i])
            
            for l in range(len(U[j])):
                U[j][l] = U[j][l] - row[l]
    print("L : ", L)
    print("U : ", U)
    print(multiply(L, U))


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

try2(u2, L)