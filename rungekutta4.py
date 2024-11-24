import numpy as np
import matplotlib.pyplot as plt

def K1(funcion,t,r):
    return funcion(t,r)

def K2(funcion,t,r,K1,h):
    k1=np.array(K1(funcion,t,r))
    Ajuste1=r+ k1*(h/2)
    return funcion(t+h/2,Ajuste1)

def K3(funcion,t,r,K2,h):
    k2=np.array(K2(funcion,t,r,K1,h))
    Ajuste2=r+k2*(h/2)
    return funcion(t+h/2,Ajuste2)

def K4(funcion,t,r,K3,h):
    k3=np.array(K3(funcion,t,r,K2,h))
    Ajuste3=r+k3*h
    return funcion(t+h,Ajuste3)

def RungeKutta(funcion,t,r,K1,K2,K3,K4,h):
    k1=np.array(K1(funcion,t,r))
    k2=np.array(K2(funcion,t,r,K1,h))
    k3=np.array(K3(funcion,t,r,K2,h))
    k4=np.array(K4(funcion,t,r,K3,h))
    ri=r+(k1+2*(k2+k3)+k4)*(h/6)
    return ri
        

def Yx(funcion,t,r,K1,K2,K3,K4,h):
    T=np.arange(0,t,h)
    R=[r]
    for x in T:
        r=RungeKutta(funcion,x,r,K1,K2,K3,K4,h)
        R.append(r)
    R=np.array(R)
    return R




#print(type(Yx(F,2,[0,0],K1,K2,K3,K4,0.1)))
#print(Yx(F,2,[0,0],K1,K2,K3,K4,0.1)[1][0])