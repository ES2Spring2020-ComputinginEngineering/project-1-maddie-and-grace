#Project 1 Step 2
#Maddie and Grace

#import statements
import numpy as np
import matplotlib.pyplot as plt

#universal variables
lengths = np.array([24, 22, 20 , 18, 16]) #inches 
 
#functions
def period(lengths):
    periods = (2*np.pi)*(np.sqrt(lengths/386.1))
    return periods #seconds

def len_vs_per():
    x = lengths
    y = period(lengths)
    plt.plot(x, y)
    plt.xlabel('length of pendulum')
    plt.ylabel('period')
    plt.title('length vs. period')
    return plt.show()

#main 
print(len_vs_per())