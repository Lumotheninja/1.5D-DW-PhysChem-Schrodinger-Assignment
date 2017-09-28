import numpy as np 

def cartesian_to_spherical(x, y, z):
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
    elif x==0:
        phi=np.pi/2
    else:
        phi = np.arctan(y/x)
    return round(r,5),round(theta,5), round(phi,5)
    
print cartesian_to_spherical(2**.5,2**.5,-2)