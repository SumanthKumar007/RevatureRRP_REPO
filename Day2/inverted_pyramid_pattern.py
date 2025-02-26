size = int(input("Enter the size of the pyramid: "))

for i in range(size, 0, -1):
    # Print spaces
    for j in range(size - i):
        print(" ", end=" ")
    # Print stars
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
