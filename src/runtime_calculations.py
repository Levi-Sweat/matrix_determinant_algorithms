import user_matrix
import random
import time
import pandas as pd


# Define the data for the DataFrame
data = {
    "size": [5, 10, 15, 20, 25],
    "cofactor_expansion": [None] * 5,
    "lu_factorization": [None] * 5,
    "bareiss_algo": [None] * 5
}

# Create the DataFrame
df = pd.DataFrame(data)

def initialize_random_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(str(random.randint(1, int(10))))
        matrix.append(row)
    return matrix


def calculate(size,stringy, loc, loops=4):
    total = 0

    for i in range(1, loops):
        matrix = initialize_random_matrix(size)
        if stringy == "bareiss_algo":
            matrix = [[int(x) for x in row] for row in matrix]
            start = time.time_ns()
            user_matrix.bareiss_algo(matrix)
            end = time.time_ns()
        elif stringy == "cofactor_expansion":
            matrix = [[float(x) for x in row] for row in matrix]
            start = time.time_ns()
            user_matrix.laplace_expansion(matrix)
            end = time.time_ns()
        else:
            matrix = [[float(x) for x in row] for row in matrix]
            start = time.time_ns()
            user_matrix.plu_decomp(matrix)
            end = time.time_ns()

        total += (end - start) / 1000000000

        print("size:", size, "stringy:", stringy, "time:", (end - start) / 1000000000)

    average = total / 5

    df.at[loc, stringy] = average

#calculate(300, "bareiss_algo", 2)
calculate(300, "plu_decomp", 2)



print(df)

df.to_csv("runtime_output.csv", index=False)


