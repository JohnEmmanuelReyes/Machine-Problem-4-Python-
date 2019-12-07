import numpy as np
import matplotlib.pyplot as plt

#Input of Height, Magnitude,Angle,Acceleration in X, Acceleration in Y
h = int(input('Initial height (m) of the projectile: '))
v = int(input('Magnitude of velocity (m/s): '))
theta = int(input('Angle (degrees) at which the projectile is fired: '))
ax = int(input('Acceleration (m/s^2) in the x-component(consider the sign!): '))
ay = float(input('Acceleration (m/s^2) in the y-component(consider the sign!): '))

#Conditions
if h < 0:
    raise NameError("The height should be above the ground!")
if ay >= 0:
    raise NameError("There would be no free fall!")
    
#Velocity in X and Y component
vy=v*np.sin(theta * (np.pi/180)); vx=v*np.cos(theta * (np.pi/180))  

Tf = (-np.sqrt(vy**2-2*ay*h) - vy)/ay 
if Tf <= 0:
     Tf = (-np.sqrt(vy**2-2*ay*h) - vy)/ay
     
#Time interval       
t = np.linspace(0, Tf, 10000)
#Y Displacement
y = np.array([(1/2)*ay, vy, h])
y = np.polyval(y, t)
y  = y[y >= 0]
#X Displacement
x = np.array([(1/2)*ax,vx, 0])
x = np.polyval(x, t)
x = x[0:(len(y))]
#Ideal motion 
x2 = t*vx
x2 = x2[0:(len(y))]
    
plt.plot(x, y,color='b')
plt.plot(x2, y, '-.',color='r')
plt.legend(['non ideal motion', 'ideal motion'],bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
plt.title('Projectile Motion')
plt.xlabel('Horizontal displacement (m)')
plt.ylabel('Vertical displacement (m)')
plt.show
    