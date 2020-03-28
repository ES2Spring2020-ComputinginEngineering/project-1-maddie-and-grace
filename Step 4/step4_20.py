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
time = result[80:300, 0]
x_acc =  result[80:300, 1]
y_acc =  result[80:300,2]
z_acc =  result[80:300, 3]

#fucntions

#this function finds the angle of the pendulum
#it takes three numbers the x, y, z acceleration values as parameters
#it returns the theta of the pendulum 
def find_tilt_y(acc_x, acc_y, acc_z):
    z2 =(acc_z**2)
    x2 =(acc_x**2)
    result = np.sqrt(z2+x2)
    Tilty =(np.arctan2(acc_y, result))*(180/np.pi)
    return Tilty

#this function plots time vs accel, theta and period using the raw data from teh microbit
#it takes no arguments
#it returns the subplots
def plots():
    theta = find_tilt_y(x_acc, y_acc, z_acc)
    
    figs, axs = plt.subplots(3,1)
    axs[0].plot(time, y_acc)
    axs[0].set_title('20 inch pendulum')
    axs[0].set_ylabel('y acc')
    
    axs[1].plot(time, x_acc) 
    axs[1].set_ylabel('x acc')
    
    axs[2].plot(time, theta) 
    axs[2].set_ylabel('theta')
    axs[2].set_xlabel('time')
    
    return plt.show()

#script 
x_acc_filt = sig.medfilt(x_acc) 
x_pks, _ = sig.find_peaks(x_acc_filt)

new_time = time[x_pks]
period = []

for x in range(len(new_time)-1):
    y = new_time[x+1] - new_time[x]
    period += [y]
period_20 = np.average(period) 
    
plots()


