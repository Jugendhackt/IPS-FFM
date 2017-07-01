import math
import numpy
import time

def getlocation(xA,yA,zA,xB,yB,zB,xC,yC,zC):
    A1 = (-(xA)*2)
    B1 = ((xA)**2)
    C1 = (-(yA)*2)
    D1 = ((yA)**2)
    E1 = ((zA)**2)
    print (A1, B1, C1, D1, E1)

    A2 = (-(xB)*2)
    B2 = ((xB)**2)
    C2 = (-(yB)*2)
    D2 = ((yB)**2)
    E2 = ((zB)**2)
    print (A2, B2, C2, D2, E2)

    A3 = (-(xC)*2)
    B3 = ((xC)**2)
    C3 = (-(yC)*2)
    D3 = ((yC)**2)
    E3 = ((zC)**2)
    print (A3, B3, C3, D3, E3)

    print (A1-A2, B1-B2, C1-C2, D1-D2, E1-E2)
    A=A1-A2
    B=B1-B2
    C=C1-C2
    D=D1-D2
    E=E1-E2
    E-=B
    E-=D
    A=-A
    E=E/float(C)
    A=A/float(C)
    print ("y1",A, E )


    A2=A2-A3
    B2=B2-B3
    C2=C2-C3
    D2=D2-D3
    E2=E2-E3
    E2-=B2
    E2-=D2
    A2=-A2
    E2=E2/float(C2)
    A2=A2/float(C2)
    print ("y2",A2, E2)

    A5=E2-E
    B5=abs(A2)+A
    x=A5/B5
    print (B5,A5)
    print ("x=",x)

    y=(A2*x)+E2
    print ("y=",y)
    return [x, y]

def distance(rssi):
   print(rssi)
   diff = -rssi - 40
   num = diff/6
   return math.pow(2, num)
