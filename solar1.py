# -*- coding: utf-8 -*-
"""
Created on Sun May 16 16:20:09 2021

@author: srpdo
"""
from math import sin, cos, radians, acos, degrees, pi,tan


def declanation_angle(n):
    return 23.45*sin(radians(360*(284+n)/365))
def G_on(n):                                #extraterrestial irradiation
    
    return G_sc*(1+0.033*coss(360*n/365))
def coss(x):
    return cos(radians(x))
def sinn(x):
    return sin(radians(x))
def zenith(n,lat,hourangle):
    return degrees(acos(sinn(declanation_angle(n))*sinn(lat)+coss(declanation_angle(n))*coss(lat)*coss(hourangle)))
def N(n,lat):                               #day length (max sunshine duration)
    return 2*w_s(n, lat)/15
def angle_of_incidence(n,tilt,lat,hourangle,surface_azimuth):

    d=declanation_angle(n)
    b=tilt
    o=lat
    w=hourangle
    y=surface_azimuth
    return degrees(acos(sinn(d)*sinn(o)*coss(b) 
                        -sinn(d)*coss(o)*sinn(b)*coss(y)
                        +coss(d)*coss(o)*coss(b)*coss(w)
                        +coss(d)*sinn(o)*sinn(b)*coss(y)*coss(w)
                        +coss(d)*sinn(b)*sinn(y)*sinn(w)))

def w_s(n,lat):                             #sunset hour angle
    o=lat
    d=declanation_angle(n)
    
    return degrees(acos(-tan(radians(o))*tan(radians(d))))

def I_o(n,lat,w1,w2):                       #extraterrestial irradiation (Hourly)
    
    d=declanation_angle(n)
    o=lat
    return (12*3600/pi)*G_on(n)*(coss(o)*coss(d)*(sinn(w2)-sinn(w1))
                                 +pi*(w2-w1)*sinn(o)*sinn(d)/180)


def H_o(n,lat):                             #extraterrestial irradiation (Daily)
    d=declanation_angle(n)
    o=lat
    ws=w_s(n, lat)
    return (24*3600/pi)*G_on(n)*(coss(o)*coss(d)*sinn(ws)+(pi*ws/180)*sinn(o)*sinn(d))

def HfromH_o(n,lat,nn,N):                   #monthly average of daily total solar irradiation
    Ho=H_o(n,lat)
    return Ho*(0.145+0.845*(nn/N)-(0.280*(nn/N)**2))

def HperH_o(n,lat,nn,N):                    #K_T0 -- kt= I/I0
    return 0.145+0.845*(nn/N)-(0.280*(nn/N)**2)

def IdperI(Kt):
    return 0.9511-0.1604*Kt + 4.388*Kt**2-16.638*Kt**3+12.336*Kt**4



def H_d(n,lat,nn,N):
    Kt=HperH_o(n,lat,nn,N)
    ws=w_s(n,lat)
    H=HfromH_o(n,lat,nn,N)
    if ws>81.4 and 0.3<=Kt<=0.8:
        return (1.311-3.022*Kt+3.427*Kt**2-1.821*Kt**3)*H
    if ws<=81.4 and 0.3<=Kt<=0.8:
        return (1.391-3.560*Kt+4.189*Kt**2-2.137*Kt**3)*H
def H_b(n,lat,nn,N):
    return HfromH_o(n,lat,nn,N)-H_d(n,lat,nn,N)
def R_b(n,lat,tilt):            #average
    o=lat
    b=tilt
    d=declanation_angle(n)
    ws= w_s(n, lat)
    ws1= degrees(acos(-tan(radians(o-b))*tan(radians(d))))
    print(ws,"ws")
    print(ws1,"ws1")
    print(ws,ws1)
    ws1 = min([ws,ws1])
    print(ws1)
    uf=coss(o-b)*coss(d)*sinn(ws1)
    us=(pi/180)*ws1*sinn(o-b)*sinn(d)
    df=coss(o)*coss(d)*sinn(ws)
    ds=(pi/180)*ws*sinn(o)*sinn(d)
    return (uf+us)/(df+ds)
    
def Rb(n,tilt,lat,hourangle,surface_azimuth):
    return coss(angle_of_incidence(n, tilt, lat, hourangle, surface_azimuth))/coss(zenith(n, lat, hourangle))    
    

def eH_t(tilt, rho, Hb, Rb, Hd, H):
    return Hb*Rb+Hd*((1+coss(tilt))/2)+H*rho*((1-coss(tilt))/2)


G_sc = 1367



#print(declanation_angle(109))
#print(w_s(105,39.93))
#print(N(105,39.93))
#print(G_on(302),"W/m^2")
#print(zenith(105,40.8,0))
#
print(angle_of_incidence(110, 25, 40, -7.5, 0))
#print(R_b(110,40,25))
#print(Rb(135, 32, 39.42, -7.5, 0))
#print(eH_t(40,0.4 , 3.23, 0.97, 2.04, 19.83))
#print(I_o(135, 39.42, -15, 0)/1000000, "MJ/(h*m^2)")
#print(H_o(105,39.93)/1000000, "MJ/(h*m^2)")
#print(HfromH_o(105,39.93,10.2,13.06)/1000000, "MJ/(h*m^2)")
#print(HperH_o(105,39.93,10.2,13.06))
#print(H_d(105,39.93,10.2,13.06)/1000000, "MJ/(h*m^2)")
#print(H_b(105,39.93,10.2,13.06)/1000000, "MJ/(h*m^2)")
#print(IdperI(0.38))