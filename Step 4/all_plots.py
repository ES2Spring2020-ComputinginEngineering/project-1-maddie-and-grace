#Step 4 Projecy 1
#Maddie and Grace
#Step 4 uses the real world data gathered in step 3 and runs analysis on that data

#import statemets
import numpy as np
import matplotlib.pyplot as plt
import step4_24 
import step4_22
import step4_20 
import step4_18 
import step4_16 

#global variables

#functions

#the purpose of this function is to plot the lengths of pendulums against their periods
#it takes no arguments
#it returns the plot that is period vs. length of pendulum 
def period_vs_length(): 
    periods = np.array([ 0.7571428571428572 ,0.7428571428571429 , 0.6749999999999999, 0.6285714285714287 , 0.6100000000000001])
    lengths = np.array([24, 22, 20 , 18, 16])
    plt.plot(lengths, periods) 
    plt.ylabel('periods')
    plt.xlabel('lengths (in)')
    plt.title('period vs. length of pendulum')
    return plt.show()

#script
step4_24.plots()
step4_22.plots()
step4_20.plots()
step4_18.plots()
step4_16.plots()

period_vs_length()
