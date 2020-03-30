#Step 5
#Grace and Maddie 

#import statemets
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig 

#global variables 

#custom functions
def update_system(acc,theta,vel,length):
    dt = .01
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

#def find_period(theta):    
#    theta_filt = sig.medfilt(theta) 
#    x_pks, _ = sig.find_peaks(theta_filt)
#    
#    new_time = time[x_pks]
#    period = []
#    
#    for x in range(len(new_time)-1):
#        y = new_time[x+1] - new_time[x]
#        period += [y]
#    period = np.average(period)
#    
#    return period
#
#def graph_periods():
#    theta_24, vel, acc = sim(24)
#    theta_22, vel, acc = sim(22)
#    theta_20, vel, acc = sim(20)
#    theta_18, vel, acc = sim(18)
#    theta_16, vel, acc = sim(16)
#    
#    period_24 = find_period(theta_24[:1650])
#    period_22 = find_period(theta_22[:1650])
#    period_20 = find_period(theta_20[:1650])
#    period_18 = find_period(theta_18[:1650])
#    period_16 = find_period(theta_16[:1650])
#    
#    periods = np.array([period_24, period_22, period_20, period_18, period_16])
#    lengths = np.array([24, 22, 20, 18, 16])
#    plt.plot(lengths, periods) 
#    plt.ylabel('periods')
#    plt.xlabel('lengths')
#    return plt.show()
#    
#
#def plots(length):
#    theta, vel, acc = sim(length)
#    
#    figs, axs = plt.subplots(3,1)
#    axs[0].plot(time, theta[:1650])
#    axs[0].set_title('22 in pendulum')
#    axs[0].set_ylabel('theta')
#    
#    axs[1].plot(time, acc[:1650]) 
#    axs[1].set_ylabel('acc')
#    
#    axs[2].plot(time, vel[:1650]) 
#    axs[2].set_ylabel('vel')
#    axs[2].set_xlabel('time')
#    
#    return plt.show()

# initial conditions
theta = [np.pi/4]
vel = [0]
acc = [0]
time = np.linspace(0,20,1650)

#main script
theta, vel, acc = sim(24)
theta1, vel1, acc1 = sim(22)

#plots(22)
#plots(24)
#plots(20)
#graph_periods()
