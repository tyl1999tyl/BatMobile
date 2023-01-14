import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)

    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    print("init")

def reverse():
    # originally forward
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    print('test---')

def forward():
    # originally reverse
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    
def turn_right():
    # ori left
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)

def turn_left():
    # ori right
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    
def pivot_right():
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    print("pivot right")
    
def pivot_left():
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    print("pivot left")

def cleanup():
    gpio.cleanup()
    #gpio.output(7, gpio.LOW)
    #gpio.output(11, gpio.LOW)
    #gpio.output(13, gpio.LOW)
    #gpio.output(15, gpio.LOW)
    print("cleanup")
 
if __name__=="__main__":
    init()
    #reverse()
    #print("rev********************")
    #time.sleep(5)
    #pivot_right()
    #print("turn_right****************")
    #time.sleep(5)
    #turn_right()
    #print("right****************")
    #time.sleep(2)
    forward()
    time.sleep(10)
    cleanup()
    print("End")
