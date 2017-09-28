# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:54:31 2017

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=np.load('xdata3px.dat')
y=np.load('ydata3px.dat')
z=np.load('zdata3px.dat')

mag=np.load('density3px.dat')

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

for a in range(0,len(mag)):
    for b in range(0,len(mag)):
        for c in range(0,len(mag)):
            ax.scatter(x[a][b][c],y[a][b][c],z[a][b][c],marker='o',alpha=(mag[a][b][c]/np.amax(mag)))
plt.show