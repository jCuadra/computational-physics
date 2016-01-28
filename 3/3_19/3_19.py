# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:00:09 2016

@author: nightwing
"""

from tqdm import tqdm
from math import sin,pi
import matplotlib.pyplot as plt

g = 9.8               #gravity acceleration (m/s2)
length = 9.8          #length of the rod (m)
k = g / length        #g/length 
dt = 0.001            #time step (s)
t_end = 6000          #end time (s)
situations = []       #this list store [time, angle]

#caculate the physical pendulum
def PHYSICAL_PENDULUM(q,fd,freq,theta,snap_freq):
    t = 0                 #initial time (s)
    angular_vel = 0       #initial angular velocity (rad/s) 
    angular_velocity = [] #this list store value of angular velocity
    angle = []            #this list store value of angle
    time = []             #this list store value of time
    while t <= t_end:
        if abs(round(t/(2*pi/snap_freq)) - (t/(2*pi/snap_freq))) < 0.001: 
            angular_velocity.append(angular_vel)
            angle.append(theta)
            time.append(t)
        angular_vel += (-k*sin(theta)-q*angular_vel+fd*sin(freq*t)) * dt
        theta += angular_vel * dt
        if theta > pi:
            theta -= 2*pi
        elif theta < -pi:
            theta += 2*pi
        t += dt
    return [angle,angular_velocity]
    
#-------------caculate (Euler-Cromer method)------------
for F in tqdm([0.5, 1.2]):
    situations.append(PHYSICAL_PENDULUM(0.5, F, 2/3.0, 0.2, 3/4.0))
    
#----------------graph--------------
plt.subplot(121)
plt.title("$\omega$ versus $\\theta$  Fd=0.5")
plt.xlabel("$\\theta$ (radians)")
plt.ylabel("$\omega$ (rad/s)")
plt.scatter(situations[0][0],situations[0][1],s=1)
plt.ylim(-1,1)
plt.subplot(122)
plt.title("$\omega$ versus $\\theta$  Fd=1.2")
plt.xlabel("$\\theta$ (radians)")
plt.ylabel("$\omega$ (rad/s)")
plt.scatter(situations[1][0],situations[1][1],s=1)
plt.show()