# Accept number of rows for the top part
n = int(input("Enter number of rows: "))

# First half - Increasing triangle
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Second half - Decreasing triangle
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
