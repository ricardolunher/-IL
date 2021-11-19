# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 09:41:13 2021
Integración con Lagrange
@author:Jesús Ricardo luna Hernández
"""

import math as mt
import numpy as np

h=0.001
res=int(5/h)

def lagrangeb2(x,idx,x_at):
    res=np.prod([(x_at-j)/(x[idx]-j) if idx!=i else 1 for i,j in enumerate(x)])
    return res

def lagrange2(x,y,x_at):
    px=sum([j*lagrangeb2(x,i,x_at) for i,j in enumerate(y)])
    return px

def nd(x):
    return (1/mt.sqrt(2*mt.pi))*mt.exp(-0.5*mt.pow(x,2))

grid=[-4+h*i for i in range(res+1)]
f_x=[nd(i) for i in grid]
punto_m=[i+h/2 for i in grid]


area=0
for i in range(len(grid)-1):
    XS=[grid[i],punto_m[i],grid[i+1]]
    YS=[nd(grid[i]),nd(punto_m[i]),nd(grid[i+1])]
    grid_temp=[grid[i]+j*(h/10) for j in range(10)]
    y_eval=[lagrange2(XS,YS,k) for k in grid_temp]
    area+=sum(y_eval)*(h/10)
print(area)





