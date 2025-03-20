"""P
rimary Colors Addition 

The program must accept a character matrix of size R*C representing the primary colors (R, G, B) as the input. The value of C is always even. The program must fold the given color matrix vertically and print the resulting colours based on the following conditions

1) Red + Red = Red
2) Green + Green = Green
3) Blue + Blue = Blue
4) Green + Blue = Cyan (repres  ented as C)
5) Red + Blue = Magenta (represented as M)
6) Red + Green = Yellow (represented as Y)

Boundary Condition(s):
2 <= R, C <= 50

Input Format:
- The first line contains R and C separated by a space.
- The next R lines, each contains C characters separated by a space.

Output Format:
- The first R lines, each contains C characters separated by a space.

Example Input/Output 1:
Input:
5 6
R G B B G B
B R B G R G
R G R R B R
R R G R G R
G R G R B R

Output:
M G B 
C R C
R C R 
R Y Y
G R M

"""

def Colors(x,y):
    if x=="R" and y=="R":
        return "R"
    elif x=="G" and y=="G":
        return "G"
    elif x=="B" and y=="B":
        return "B"
    elif (x=="R" or x=="B") and (y=="B" or y=="R"):
        return "M"
    elif (x=="G" or x=="B") and (y=="B" or y=="G"):
        return "C"
    elif (x=="R" or x=="G") and (y=="G" or y=="R"):
        return "Y"

r,c=map(int,input().split())

l=[list(map(str,input().split())) for i in range(r)]


for i in range(r):
    for j in range(c//2):
        x="".join(l[i][j])
        y="".join(l[i][-j-1])
        print(Colors(x,y),end=" ")
    print()
    
