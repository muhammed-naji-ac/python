# Accept number of steps from the user
N = int(input("Enter number of steps: "))

# Outer loop for each row
for i in range(1, N + 1):
    # Inner loop to print multiples of current row number
    for j in range(1, i + 1):
        print(i * j, end=" ")
    # Move to next line after printing each row
    print()
