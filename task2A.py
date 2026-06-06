mat = []

print("Enter matrix rows (press Enter on empty line to stop):")

while True:
    row = input()

    if row == "":
        break

    mat.append(list(map(int, row.split())))

rows = len(mat)
cols = len(mat[0])

print("Transpose Matrix:")

for j in range(cols):
    for i in range(rows):
        print(mat[i][j], end=" ")
    print()