#Logger Step 3 Project 1
#Maddie and Grace

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=18, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging


# Read and send accelerometer data repeatedly until button A is pressed again
time0 = mb.running_time()
while not mb.button_a.is_pressed():
    acc_x= mb.accelerometer.get_x()
    acc_y= mb.accelerometer.get_y()
    acc_z= mb.accelerometer.get_z()
    time1 = mb.running_time()
    elapsed_time = round((time1 - time0)/1000,1)
    message = str(elapsed_time) + ', ' + str(acc_x) + ', ' + str(acc_y) + ', ' +  str(acc_z)
    radio.send(message)
    print(message)
    mb.sleep(10)



mb.display.show(mb.Image.SQUARE)  # Display Square when program ends