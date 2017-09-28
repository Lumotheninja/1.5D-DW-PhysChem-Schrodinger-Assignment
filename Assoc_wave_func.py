import math as ma
import sympy as sp
import scipy as c
import cmath as cma
import numpy as np

x = sp.Symbol('x')

def p00(theta):
    return 1
         
def assoc_legendre(m,l):
    
    if m==0 and l==0:
        return p00
    def col(z):
        poly=sp.diff((x**2-1)**l,x, l +abs(m))
        b=poly*(1-x**2)**(abs(m)/2.)/(2**l*ma.factorial(l))
        return b.subs(x,ma.cos(z)).evalf()
    return col
    

def angular_wave_func(m,l,theta,phi):
    f= assoc_legendre(m,l)
    y= f(theta)
    if m<= 0:
        soln=complex(ma.sqrt((2*l+1)*ma.factorial(l-abs(m))/(4*c.pi*ma.factorial(l+abs(m))))*y*cma.exp(m*phi*1j))
    else:
        soln=complex((-1)**m*ma.sqrt((2*l+1)*ma.factorial(l-abs(m))/(4*c.pi*ma.factorial(l+abs(m))))*y*cma.exp(1j * phi*m))
    return np.round(soln,5)

    
print angular_wave_func(0,0,0,0)