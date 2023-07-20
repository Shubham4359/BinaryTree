# importing the sys module
import sys
 
# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
 
sys.setrecursionlimit(10**6)
def fib(n):
    if n<=1:
        return n 
    else:
        return fib(n-1)+fib(n-2)

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def power(a,n):
    if n==0:
        return 1
    else:
        x = power(a,int(n/2))
        x=x*x;
        if n%2==1 :
            x=x*a 
        return x

def towerofhanoi(n,st,im,ed):
    if n==0:
        return 0
    x = towerofhanoi(n-1,st,ed,im)
    print(n," moves from ",st," using ",im," to ",ed)
    y = towerofhanoi(n-1,im,st,ed)
    return x+y+1
 

print(factorial(1000))
