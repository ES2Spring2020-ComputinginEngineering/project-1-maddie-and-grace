#Step 5
#Grace and Maddie 
#Step 5 creates a numerical model of a pendulum to gather simulated data and then run analysis on that data

#import statemets
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig 

#custom functions

#this function models how theta, velocity and acceleration of a pendulum would change based off the euluer step model
#it takes 4 arguments all integers which are the acceleration, theta, velocity and length of the pendulum 
#it returns three integers which are the next theta, velocity, and acceleration of the pendulum based off the eurler step model 
def update_system(acc,theta,vel,length):
    dt = .005
    thetaNext = theta+vel*dt
    velNext = vel+acc*dt
    accNext = -386.1*np.sin(theta)/length 
    return thetaNext,velNext, accNext

#this function simulates the movement of a pendulum with a start angle less than 90 degrees by updating three lists with calculated values for how acc, vel, and theta changes for a pendulum of a given length 
#it takes one argument an integer which is the length of the pendulum in inches
#it returns three lists the theta, velocity, and acceleration of the pendulum 
def sim_less_than_90(length):
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

#this function simulates the movement of a pendulum with a start angle greater than 90 degrees by updating three lists with calculated values for how acc, vel, and theta changes for a pendulum of a given length 
#it takes one argument an integer which is the length of the pendulum in inches
#it returns three lists the theta, velocity, and acceleration of the pendulum 
def sim_greater_than_90(length):
    theta = [2*np.pi/3]
    vel = [0]
    acc = [0]
    time = np.linspace(0,10,2000)
    i = 0
    while i < len(time)-1:
        thetaNext, velNext, accNext = update_system(acc[i-1],theta[i-1],vel[i-1],length)
        theta.append(thetaNext)
        vel.append(velNext)
        acc.append(accNext)
        i += 1
    return theta, vel, acc

#this function calulates the period of the pendulum with a start angle less than 90 degrees based off the data collected by the simulation
#it takes one argument the list of positions of the pendulum known as theta
#it returns the period of that pendulum based off the positions which occurr at certain times
def find_period_less_than_90(theta): 
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

#this function calulates the period of the pendulum with a start angle greater than 90 degrees based off the data collected by the simulation
#it takes one argument the list of positions of the pendulum known as theta
#it returns the period of that pendulum based off the positions which occurr at certain times
def find_period_greater_than_90(theta): 
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

#this function graphs the periods of pendulums with a start angle greater than 90 degrees against their lengths based on the data gathered in the simulation 
#it takes no arguments 
#it returns the plot that is period vs. length
def graph_periods_greater_than_90():
    theta_24, vel, acc = sim_greater_than_90(24)
    theta_22, vel, acc = sim_greater_than_90(22)
    theta_20, vel, acc = sim_greater_than_90(20)
    theta_18, vel, acc = sim_greater_than_90(18)
    theta_16, vel, acc = sim_greater_than_90(16)
    
    period_24 = find_period_greater_than_90(theta_24)
    period_22 = find_period_greater_than_90(theta_22)
    period_20 = find_period_greater_than_90(theta_20)
    period_18 = find_period_greater_than_90(theta_18)
    period_16 = find_period_greater_than_90(theta_16)
    
    periods = np.array([period_24, period_22, period_20, period_18, period_16])
    lengths = np.array([24, 22, 20, 18, 16])
    plt.plot(lengths, periods)
    plt.title('periods vs. lengths')
    plt.ylabel('periods')
    plt.xlabel('lengths (in)')
    return plt.show()

#this function graphs the periods of pendulums with a start angle less than 90 degrees against their lengths based on the data gathered in the simulation 
#it takes no arguments 
#it returns the plot that is period vs. length
def graph_periods_less_than_90():
    theta_24, vel, acc = sim_less_than_90(24)
    theta_22, vel, acc = sim_less_than_90(22)
    theta_20, vel, acc = sim_less_than_90(20)
    theta_18, vel, acc = sim_less_than_90(18)
    theta_16, vel, acc = sim_less_than_90(16)
    
    period_24 = find_period_less_than_90(theta_24[:])
    period_22 = find_period_less_than_90(theta_22[:])
    period_20 = find_period_less_than_90(theta_20[:])
    period_18 = find_period_less_than_90(theta_18[:])
    period_16 = find_period_less_than_90(theta_16[:])
    
    periods = np.array([period_24, period_22, period_20, period_18, period_16])
    lengths = np.array([24, 22, 20, 18, 16])
    plt.plot(lengths, periods)
    plt.title('periods vs. lengths')
    plt.ylabel('periods')
    plt.xlabel('lengths (in)')
    return plt.show()
    
#this function plots a subplot containing time vs. vel, acc, and theta based on the data gathered in the simulation for a pendulum with a start angle less tha 90 degrees
#it takes one argument an integer that is the length of the pendulum in inches
#it returns the subplot that contains the three plots discussed in the purpose
def plots_less_than_90(length):
    time = np.linspace(0,20,4000)
    theta, vel, acc = sim_less_than_90(length)
    
    figs, axs = plt.subplots(3,1)
    axs[0].plot(time, theta[:])
    axs[0].set_title(str(length) + ' inch pendulum')
    axs[0].set_ylabel('theta (degrees)')
    
    axs[1].plot(time, acc[:]) 
    axs[1].set_ylabel('acc(in/s^2)')
    
    axs[2].plot(time, vel[:]) 
    axs[2].set_ylabel('vel (in/s)')
    axs[2].set_xlabel('time(s)')
    
    return plt.show()

#this function plots a subplot containing time vs. vel, acc, and theta based on the data gathered in the simulation for a pendulum with a start angle greater tha 90 degrees
#it takes one argument an integer that is the length of the pendulum in inches
#it returns the subplot that contains the three plots discussed in the purpose
def plots_greater_than_90(length):
    time = np.linspace(0,10,2000)
    theta, vel, acc = sim_greater_than_90(length)
    
    figs, axs = plt.subplots(3,1)
    axs[0].plot(time, theta[:])
    axs[0].set_title(str(length) + ' inch pendulum')
    axs[0].set_ylabel('theta (degrees)')
    
    axs[1].plot(time, acc[:]) 
    axs[1].set_ylabel('acc(in/s^2)')
    
    axs[2].plot(time, vel[:]) 
    axs[2].set_ylabel('vel (in/s)')
    axs[2].set_xlabel('time(s)')
    
    return plt.show()
#main script

plots_greater_than_90(24)
plots_greater_than_90(22)
plots_greater_than_90(20)
plots_greater_than_90(18)
plots_greater_than_90(16)

graph_periods_greater_than_90()


plots_less_than_90(24)
plots_less_than_90(22)
plots_less_than_90(20)
plots_less_than_90(18)
plots_less_than_90(16)

graph_periods_less_than_90()