import math as ma
import sympy as sp

x = sp.Symbol('x')

def p00(theta):
    return 1
         
def assoc_legendre(m,l):
    
    if m==0 and l==0:
        return p00
    else:
        poly=sp.diff((x**2-1)**l,x, l +abs(m))
        b=poly*(1-x**2)**(abs(m)/2.)/(2**l*ma.factorial(l))
        return b 

print  assoc_legendre(1,3)
print  assoc_legendre(-51,3)
