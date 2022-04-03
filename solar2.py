# -*- coding: utf-8 -*-
"""
Created on Wed May 19 10:34:48 2021

@author: srpdo
"""
t=57.17
adap = 1-1.5879*(10**-3)*t+2.7314*(10**-4)*(t**2)-2.3026*(10**-5)*(t**3)+9.0244*(10**-7)*(t**4)-1.8*(10**-8)*(t**5)+1.7734*(10**-10)*(t**6)-9.9937*(10**-13)*(t**7)

print(adap)

b=25
dr=59.7-0.1388*b+0.001497*b**2      #beam reflection
print(dr)

gr=90-0.5788*b+0.002693*b**2        #ground reflection
print(gr)