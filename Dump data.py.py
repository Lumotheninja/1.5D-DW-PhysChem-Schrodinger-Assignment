import math as ma
import sympy as sp
import scipy.constants as c
import numpy as np
import cmath as cma

def energy_n(n):
    energy =-(c.m_e*(c.e*c.e/(4*c.pi*c.epsilon_0))**2)/((2*(c.hbar**2))*(n**2)*c.e)
    return round(energy,5)
    
def degToRad(deg):
    rad=deg*c.pi/180.
    return round (rad,5)

def radToDeg(rad):
    deg=rad*180/c.pi
    return round (deg,5)

def sphericalToCartesian(r,theta,phi):
    x=r*np.sin(theta)*np.cos(phi)
    y=r*np.sin(theta)*np.sin(phi)
    z=r*np.cos(theta)
    return round(x,1),round(y,1),round(z,1)

def cartesianToSpherical(x, y, z):
    r = (x**2+y**2+z**2)**.5
    if x==0 and y==0 and z==0:
        theta =0.
    elif z==0:
        theta=np.pi/2
    else:
        theta = np.arctan (((x**2+y**2)**.5)/z)
        if z<0:
            theta = np.pi + theta
    if x==0 and y==0:
        phi=0.
    elif x==0 and y<0:
        phi=-np.pi/2
    elif x==0 and y>0:
        phi=np.pi/2
    else:
        phi = np.arctan(y/x)
    return round(r,5),round(theta,5), round(phi,5)
    
p = sp.Symbol('p')
qmp=sp.Symbol('qmp')
x = sp.Symbol('x')
a = c.physical_constants['Bohr radius'][0]

def l00(x):
    return 1
         
def assoc_laguerre(p,qmp):
    if p==0 and qmp==0:
        return l00
    def col(z):
        nomial=sp.exp(x)*sp.diff(sp.exp(-x)*x**(qmp+p),x, p+qmp)
        b=sp.diff(nomial,x,p)*(-1)**p
        return b.subs(x,z)
    return col



def radial_wave_func(n,l,r):
    lfunc=assoc_laguerre(2*l+1,n-l-1)
    y = lfunc(2*r/(n*a))
    soln=a**(1.5)*cma.sqrt((2/(n*a))**3*ma.factorial(n-l-1)/(2*n*(ma.factorial(n+l))**3))*ma.exp(-r/(n*a))*(2*r/(n*a))**l*float(y)
    return np.round(soln,5)
    
k = sp.Symbol('k')

def p00(theta):
    return 1
         
def assoc_legendre(m,l):
    if m==0 and l==0:
        return p00
    def col(z):
        poly=sp.diff((k**2-1)**l,k, l +abs(m))
        b=poly*(1-k**2)**(abs(m)/2.)/(2**l*ma.factorial(l))
        return b.subs(k,ma.cos(z)).evalf()
    return col
    
def angular_wave_func(m,l,theta,phi):
    f= assoc_legendre(m,l)
    y= f(theta)
    if m<= 0:
        soln=complex(ma.sqrt((2*l+1)*ma.factorial(l-abs(m))/(4*c.pi*ma.factorial(l+abs(m))))*y*cma.exp(m*phi*1j))
    else:
        soln=complex((-1)**m*ma.sqrt((2*l+1)*ma.factorial(l-abs(m))/(4*c.pi*ma.factorial(l+abs(m))))*y*cma.exp(1j * phi*m))
    return np.round(soln,5)
    
def hydrogen_wave_func(n, m, l, roa, Nx, Ny, Nz):
    x = np.linspace(-roa,roa,Nx)
    y = np.linspace(-roa,roa,Ny)
    z = np.linspace(-roa,roa,Nz)
    xx,yy,zz = np.meshgrid(x,y,z)
    r, theta, phi = np.vectorize(cartesianToSpherical)(xx,yy,zz)
    ang = np.vectorize(angular_wave_func)(m,l,theta,phi)
    rad = np.vectorize(radial_wave_func)(n,l,r*a)
    wave_func = np.round((np.absolute(ang*rad))**2,5)
    return np.round(xx,5),np.round(yy,5),np.round(zz,5),wave_func

x,y,z,mag = hydrogen_wave_func(4,-1,3,10,20,20,20)
x.dump('xdata3px.dat')
y.dump('ydata3px.dat')
z.dump('zdata3px.dat')
mag.dump('density3px.dat')
