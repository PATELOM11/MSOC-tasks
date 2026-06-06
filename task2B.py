mat = []

print("Enter the square matrix (press Enter on empty line to stop):")

while True:
    row = input()

    if row == "":
        break

    mat.append(list(map(int, row.split())))

n = len(mat)

primary_sum = 0
secondary_sum = 0

for i in range(n):
    primary_sum += mat[i][i]
    secondary_sum += mat[i][n - 1 - i]

print("Primary Diagonal Sum =", primary_sum)
print("Secondary Diagonal Sum =", secondary_sum)