#Step 5
#Grace and Maddie 

#import statemets
import numpy as np
import matplotlib.pyplot as plt

#global variables 

#custom functions
def update_system(acc,theta,vel,l):
    dt = .01
    thetaNext = theta+vel*dt
    velNext = vel+acc*dt
    accNext = -386.1*np.sin(theta)/l
    return thetaNext,velNext, accNext

# initial conditions
theta = [np.pi/2]
vel = [0]
acc = [0]
time = np.linspace(0,20,2000)

#main script
i = 0
while i < len(time)-1:
    thetaNext, velNext, accNext = update_system(acc[i-1],theta[i-1],vel[i-1],24)
    theta.append(thetaNext)
    vel.append(velNext)
    acc.append(accNext)
    i += 1

plt.plot(time, theta) 
plt.xlabel('time')
plt.ylabel('theta')
plt.show()

plt.plot(time, acc) 
plt.xlabel('time')
plt.ylabel('acc')
plt.show()

plt.plot(time, vel) 
plt.xlabel('time')
plt.ylabel('vel')
plt.show()
