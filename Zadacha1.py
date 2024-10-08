from math import *
x=float(input('введите x: '))
y=float(input('введите y: '))
z=float(input('введите z: '))
s=(fabs(cos(x)-cos(y))**(2*sin(y)**2))*(1+z+((z**2)/2));
print(s)