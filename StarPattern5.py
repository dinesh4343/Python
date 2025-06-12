# This code prints a right-aligned triangle pattern of numbers.
#  # It starts with the largest number at the top and decreases the number of printed digits in each subsequent row.
# Right-aligned triangle pattern of numbers

n=int(input())

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()