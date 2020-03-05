#Step 4 Project 1
#Maddie and Grace

#impmort statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig 


#global variables
file_1 = '20in.csv'
test = pd.read_csv(file_1)
result = test.values
time = result[:, 0]
x_acc =  result[:, 1]
y_acc =  result[:,2]
z_acc =  result[:, 3]

#fucntions

#this function finds the angle of the pendulum
#it takes three numbers the x, y, z acceleration values as parameters
#it returns the theta of the pendulum 
def find_tilt_x(acc_x, acc_y, acc_z):
    y2 =(acc_y**2)
    z2 =(acc_z**2)
    result = np.sqrt(y2+z2)
    TiltX=(np.arctan2(acc_x, result))*(180/np.pi)
    return TiltX

#this function plots time vs accel, theta and period using the raw data from teh microbit
#it takes no arguments
#it returns the subplots
def plots():
    figs, axs = plt.subplots(4,1)
    axs[0].plot(time, x_acc) 
    
    axs[0].set_title('20 inch pendulum')
    axs[0].set_ylabel('x acceleration')
    
    axs[1].plot(time, z_acc) 
    axs[1].set_ylabel('z acceleration')
    
    axs[2].plot(time, theta) 
    axs[2].set_ylabel('theta')
    axs[2].set_xlabel('time')
    
    axs[3].plot(time, period) 
    axs[3].set_ylabel('period')
    axs[3].set_xlabel('time')
    
    return plt.show()


#script 
theta = find_tilt_x(x_acc, y_acc, z_acc)

x_acc_peaks = sig.find_peaks(x_acc) 

plots()