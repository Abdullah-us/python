'''
5! matlb honda va
5!=5x4x3x2x1
4!=4x3x2x1 
7!=7x6x5x4x3x2x1

forexample 5 k a factorial nikal rhy hy 
n!=n*(n-1)*(n-2)X....X3x2x1

genral formula honda va
n!=n*factorial(n-1)
'''

def factorial(n):
    if(n==0) or (n==1): #bascase is really important
        return 1
    return n*factorial(n-1)

n=int(input("enter number: "))
result=factorial(n)
print(result)
