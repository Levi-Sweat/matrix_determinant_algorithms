from colorama import Back, Style, Fore

size = 5
matrix = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(Back.RED + "500" + Style.RESET_ALL)
    matrix.append(row)

print("matrix 0: " + matrix[0][0][0])

print("matrix 1: " + matrix[0][0][1])

print("matrix 2: " + matrix[0][0][2])

print("matrix 3: " + matrix[0][0][3])

print("matrix 4: " + matrix[0][0][4])

if matrix[0][0][1] == '[':
    print("TRUE")

new_string = matrix[0][0][matrix[0][0].find('m')+1:matrix[0][0].rfind('\x1b')]

print("result: " + new_string)
print(len(new_string))