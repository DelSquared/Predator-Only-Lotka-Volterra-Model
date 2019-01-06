import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

cx,cy,cz = 1,0.5,0.5
dx,dy,dz = 0,0,0

def ddt(x,y,z,c,k,d):
  return (c*x*y - k*x*z - d*x)

def RPSpredatorprey(X,t):
  x,y,z=X
  return [ddt(x,y,z,cx,cz,dx),ddt(y,z,x,cy,cx,dy),ddt(z,x,y,cz,cy,dz)]

Xo=[0.5,0.25,0.25]

t = np.linspace(0, 30, 30001)

X = odeint(RPSpredatorprey, Xo, t)

fig = plt.figure()
plt.plot(t, X[:, 0], 'r', label='x')
plt.plot(t, X[:, 1], 'g', label='y')
plt.plot(t, X[:, 2], 'b', label='z')
plt.plot(t, X[:, 2]+X[:, 1]+X[:, 0], 'y', label='T')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.savefig("soln.png")
