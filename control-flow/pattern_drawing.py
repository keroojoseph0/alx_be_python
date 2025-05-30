size = int(input("Enter the size of the pattern: "))

j = size
while j > 0:
    for i in range(1, size + 1):
        print("*", end="")
        i += 1
    j -= 1
    print()
