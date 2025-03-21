
"""
Swap Values - Two Matrices
Problem Statement:
The program must accept two matrices M1 and M2 of the same size R × C as input.

M1 represents an integer matrix.
M2 represents a character matrix.
For each occurrence of a vowel in M2, the program must swap the values between the two matrices at the same position.
Finally, the program must print the modified matrices M1 and M2 as output.

Boundary Condition(s):
2 ≤ 𝑅 , 𝐶 ≤ 50
2 ≤ R, C ≤ 50
1 ≤ 1 ≤ 
Each integer value  ≤ 1000 ≤1000
Input Format:
The first line contains two integers R and C separated by a space.
The next R lines contain the integer matrix M1.
The next R lines (starting from the (R+2)th line) contain the character matrix M2.
Output Format:
The first R lines contain the modified matrix M1.
The next R lines contain the modified matrix M2.


"""



r,c=map(int,input().split())

l1=[list(map(str,input().split())) for i in range(r)]

l2=[list(map(str,input().split())) for i in range(r)]


for i in range(r):
    for j in range(c):
        
        if l2[i][j] in "aeiouAEIOU":
            l2[i][j],l1[i][j]=l1[i][j],l2[i][j]
            
for i in l1+l2:
    print(*i)
    
