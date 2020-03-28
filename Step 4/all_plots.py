#Step 4 Projecy 1
#Maddie and Grace

#import statemets
import step4_24 
import step4_22
import step4_20 
import step4_18 
import step4_16 

#global variables

#functions
def period_vs_length(): 
    periods = np.array([0.7571428571428572 ,0.7428571428571429 , 0.6749999999999999, 0.5900000000000001 , 0.6100000000000001])
    lengths = np.array([24, 22, 20 , 18, 16])
    plt.plot(lengths,periods) 
    plt.ylabel('periods')
    plt.xlabel('lengths')
    return plt.show()

#script
step4_24.plots()
step4_22.plots()
step4_20.plots()
step4_18.plots()
step4_16.plots()

period_vs_length()
