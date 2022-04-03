# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:59:07 2021

@author: srpdo
"""
from math import pi, e
ul=3.5
w=120*10**-3
d=5*10**-3
di=4*10**-3
F=0.96
hf=300
a=1/ul
b1=a/(d+F*(w-d))
b2=1/(pi*di*hf)
fp=a/(w*(b1+b2))
print( fp)


mp=0.03
cp=4190
ac=1.5
coef=mp*cp/(ac*ul)
exp=-fp/coef
fr=coef*(1-e**exp)
print(fr)