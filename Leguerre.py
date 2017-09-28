import math as ma
import sympy as sp

p = sp.Symbol('p')
qmp=sp.Symbol('qmp')
x = sp.Symbol('x')

def l00(x):
    return 1
         
def assoc_laguerre(p,qmp):
    if p==0 and qmp==0:
        return l00
    nomial=sp.exp(x)*sp.diff(sp.exp(-x)*x**(qmp+p),x, p+qmp)
    col=sp.diff(nomial,x,p)*(-1)**p
    return col
    
print assoc_laguerre(7,0)
