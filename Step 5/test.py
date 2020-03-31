import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig 

#custom functions
def update_system(acc,theta,vel,length):
    dt = .005
    thetaNext = theta+vel*dt
    velNext = vel+acc*dt
    accNext = -386.1*np.sin(theta)/length
    return thetaNext,velNext, accNext

def sim(length):
    i = 0
    while i < len(time)-1:
        thetaNext, velNext, accNext = update_system(acc[i-1],theta[i-1],vel[i-1],length)
        theta.append(thetaNext)
        vel.append(velNext)
        acc.append(accNext)
        i += 1
    return theta, vel, acc

thetanext, velnext, accnext = sim(24)
thetanext1, velnext1, accnext1 = sim( 22)
thetanext2, velnext2, accnext2 = sim(20)