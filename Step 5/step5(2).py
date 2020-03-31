#Step 5
#Grace and Maddie 

#import statemets
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
    theta = [np.pi/4]
    vel = [0]
    acc = [0]
    time = np.linspace(0,20,4000)
    i = 0
    while i < len(time)-1:
        thetaNext, velNext, accNext = update_system(acc[i-1],theta[i-1],vel[i-1],length)
        theta.append(thetaNext)
        vel.append(velNext)
        acc.append(accNext)
        i += 1
    return theta, vel, acc

def find_period(theta): 
    time = np.linspace(0,20,4000)
    theta_filt = sig.medfilt(theta) 
    x_pks, _ = sig.find_peaks(theta_filt)
    
    new_time = time[x_pks]
    period = []
    
    for x in range(len(new_time)-1):
        y = new_time[x+1] - new_time[x]
        period += [y]
    period = np.average(period)
    
    return period

def graph_periods():
    theta_24, vel, acc = sim(24)
    theta_22, vel, acc = sim(22)
    theta_20, vel, acc = sim(20)
    theta_18, vel, acc = sim(18)
    theta_16, vel, acc = sim(16)
    
    period_24 = find_period(theta_24[:])
    period_22 = find_period(theta_22[:])
    period_20 = find_period(theta_20[:])
    period_18 = find_period(theta_18[:])
    period_16 = find_period(theta_16[:])
    
    periods = np.array([period_24, period_22, period_20, period_18, period_16])
    lengths = np.array([24, 22, 20, 18, 16])
    plt.plot(lengths, periods)
    plt.title('periods vs. lengths')
    plt.ylabel('periods')
    plt.xlabel('lengths (in)')
    return plt.show()
    

def plots(length):
    time = np.linspace(0,20,4000)
    theta, vel, acc = sim(length)
    
    figs, axs = plt.subplots(3,1)
    axs[0].plot(time, theta[:])
    axs[0].set_title('_ in pendulum')
    axs[0].set_ylabel('theta (degrees)')
    
    axs[1].plot(time, acc[:]) 
    axs[1].set_ylabel('acc(in/s^2)')
    
    axs[2].plot(time, vel[:]) 
    axs[2].set_ylabel('vel (in/s)')
    axs[2].set_xlabel('time(s)')
    
    return plt.show()

# initial conditions

#main script

plots(22)
plots(24)
plots(20)
plots(18)
plots(16)

graph_periods()