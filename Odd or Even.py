def Odd_Or_Even(n):
    if n&1==0:
        return "Even"
    else:
        return "Odd"
    
n=int(input())
print(Odd_Or_Even(n))