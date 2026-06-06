def unique_elements(arr):
    unique = []

    for i in range(len(arr)):
        found = False

        for j in range(len(unique)):
            if arr[i] == unique[j]:
                found = True
                break

        if found == False:
            unique.append(arr[i])

    return unique


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input()))

print(unique_elements(arr))
# we can also use the inbuilt function to determine the unique elements..
