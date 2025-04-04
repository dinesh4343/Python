# Split String - Equal Unique Count

# The program must accept a string S as the input.

# The program must print the number of ways to split the string S into two parts so that the number of unique characters in both parts are equal.
# Boundary Condition(s): 2 <= Length of S <= 1000
# Input Format: The first line contains S.
# Output Format: The first line contains an integer value.

# Example Input/Output 1:
# Input: acaddabac
# Output: 2
# Explanation: All possible ways to split the string acaddabac are given below.


# a caddabac
# ac addabac
# aca ddabac
# acad dabac
# acadd abac -> Same number of unique characters
# acadda bac -> Same number of unique characters
# acaddab ac
# acaddaba c


# Hence the output is 2.
# Example Input/Output 2:
# Input: SSSSSS
# Output: 5

def unique(x):
    s = ""
    for i in x:
        if i not in s:
            s += i
    return len(s)

x = input().strip()

c = 0

for i in range(len(x)):
    y = "".join(x[:i])
    z = "".join(x[i:])
    if unique(y) == unique(z):
        c += 1

print(c)
        