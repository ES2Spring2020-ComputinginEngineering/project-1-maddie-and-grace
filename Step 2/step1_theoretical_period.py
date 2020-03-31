#Project 1 Step 2
#Maddie and Grace
#Step 2 uses knwon physics equations for a pendulum to predict the period based on various pendulum lengths

#import statements
import numpy as np
import matplotlib.pyplot as plt

#universal variables
lengths = np.array([24, 22, 20 , 18, 16]) #inches 
 
#functions

#this function takes the lengths and calculates the period of the swings of the pendulum 
#takes an array of the lengths
#returns an array that is the estimated period of swing 
def period(lengths):
    periods = (2*np.pi)*(np.sqrt(lengths/386.1))
    return periods #seconds

#this function graphs the lengths vs. the periods
#it takes no parameters
#it returns the plot of the lengths vs. periods 
def len_vs_per():
    x = lengths
    y = period(lengths)
    plt.plot(x, y)
    plt.xlabel('length (in)')
    plt.ylabel('period')
    plt.title('period vs. length of pendulum')
    return plt.show()

#main 
len_vs_per()

#limits of this model - 
#we must assume that there is constant acceleration from gravity free of air resistance
#we must also assume that there is no friction in the pendulum
#because of these assumptions the model in the real world would never behave exactly to the equaitons usesd
