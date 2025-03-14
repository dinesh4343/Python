# Column Binary Representation 
# The program must accept an integer matrix of size R*C containing only 0s and 1s as the input. 
# Each column of the matrix represents the binary representation of an integer.The program must find the maximum possible decimal equivalent for each column in the matrix 
# (i.e., the maximum value between the decimal equivalent of the column from top to bottom and 
# the decimal equivalent of the column from bottom to top). 
# Finally, the program must print the sum of all the C integers obtained as the output. 

# Boundary Condition(s): 
# 2 <= R, C <= 50 

# Input Format: 
# The first line contains R and C separated by a space. 
# The next R lines, each contains C integer values separated by a space. 

# Output Format: 
# The first line contains an integer representing the sum of all the C integers obtained from the matrix. 

# Example Input/Output 1: 
# Input: 
# 5 6 
# 0 0 1 1 0 1 
# 0 1 1 1 1 1 
# 0 0 1 0 1 1 
# 0 1 1 0 0 0 
# 1 1 1 1 0 0 

# Output: 138 



rows, cols = map(int, input().split())

matrix = [list(map(str, input().split())) for _ in range(rows)]

columns = [[matrix[row][col] for row in range(rows)] for col in range(cols)]

max_values = []

for i in columns:
    binary_str = "".join(i)
    max_values.append(max(int(binary_str, 2), int(binary_str[::-1], 2)))

print(sum(max_values))
