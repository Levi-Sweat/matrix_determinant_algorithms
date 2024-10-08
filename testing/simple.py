from colorama import Back, Style, Fore
from numpy import isclose, eye, array

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

L = eye(3)

U = array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])

print(U[0, 2])

print(matrix[0][2])