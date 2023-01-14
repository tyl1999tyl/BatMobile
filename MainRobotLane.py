from MotorModule import Motor
from LaneDetectionModule import getLaneCurve
import WebcamModule
import RPi.GPIO as gpio
import time
from floyd_warshall_demo import *

def init():
    gpio.setmode(gpio.BOARD)

    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    print("init")

def reverse(duration):
    # originally forward
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    print('reverse-')
    time.sleep(duration)

def forward(duration):
    # originally reverse
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    print("forward")
    time.sleep(duration)
    
def turn_right():
    # ori left
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    print("turn_right")
    #time.sleep(duration)

def turn_left():
    # ori right
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    print("turn_left")
    #time.sleep(duration)
    
def pivot_right(duration = 1.58):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    print("pivot right")
    time.sleep(duration)
    
def pivot_left(duration = 1.58):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    print("pivot left")
    time.sleep(duration)

def cleanup():
    gpio.cleanup()
    #gpio.output(7, gpio.LOW)
    #gpio.output(11, gpio.LOW)
    #gpio.output(13, gpio.LOW)
    #gpio.output(15, gpio.LOW)

def wait(duration = 1):
    cleanup()
    time.sleep(duration)
    init()

 
def main():
 

    # get image from webcam
    img = WebcamModule.getImg()

    """
    # get curve value of lane 
    curveVal= getLaneCurve(img,2)
 
    
    #sen = 1.3  # SENSITIVITY
    maxVAl= 0.3 # MAX SPEED

    # limit the maximum speed
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    #print(curveVal)
    # don't let the motor move if the curve value is less than a certain angle
    # so that the car won't keep moving left and right and will just move straight
    if curveVal>0:
        sen =1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
    #motor.move(0.20,-curveVal*sen,0.05) # move the car according to the curve
        
    print(curveVal)
    if curveVal < 0:
        turn_left()
    if curveVal > 0:
        pivot_right()
    if curveVal==0:
        forward()
    #time.sleep(2)
    cleanup()
    
    
    cv2.waitKey(1)
    """
     

class Batmobile:
    
    ### Forward
    # 1 -> 2 (1.18) powerbank(1.4)
    # 2 -> 3 (0.95)
    # 3 -> 4 (1)
    # 4 -> 6 (1.31)
    # 6 -> 7 (1.55)
    # 7 -> 8 (1.1)
    # 8 -> 9 (0.65)
    # 9 -> 2 (1.3)
    # pivot (1.58)
    farm = {
        1 : {2: (0, 1.18)},
        2 : {1: (-2, 1.18), 3: (0, 0.93), 9: (-1, 1.3)},
        3 : {2: (-2, 0.93), 4: (-1, 1)},
        4 : {6: (-1, 1.31), 3: (1, 1)},
        6 : {7: (-2, 1.55), 4: (1, 1.31)},
        7 : {8: (1, 1.1), 6: (0, 1.55)},
        8 : {9: (0, 0.65), 7: (-1, 1.1)},
        9 : {2: (1, 1.3), 8: (-2, 0.65)}
    }
    
    """
    Start should always face forward.
    """
    
    def __init__(self):#, curr = 1):
        #self.curr = curr
        #self.pivot_time = 2
        init()
        
    def travel(self, path):
        cur = path[0]
        for i in range(1, len(path)):
            move = self.farm[cur][path[i]][0]
            duration = self.farm[cur][path[i]][1]
            if move == 0:
                forward(duration)
                wait()
            elif move == 1:
                pivot_right()
                wait()
                forward(duration)
                wait()
                pivot_left()
                wait()
            elif move == -1:
                pivot_left()
                wait()
                forward(duration)
                wait()
                pivot_right()
                wait()
            elif move == -2:
                reverse(duration)
                wait()
            
            
            #print(self.farm[cur][path[i]])
            cur = path[i]
        cleanup()
        pass
        
    

 
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    # Add an argument
    parser.add_argument('-s','--start', type=int, required=True)
    parser.add_argument('-e','--end', type=int, required=True)

    # Parse the argument
    args = parser.parse_args()
    
    # define infinity
    I = float('inf')

    # given adjacency representation of the matrix
    adjMatrix = [
        [0, 5, I, I, I, I, I, I, I, I],
        [5, 0, 5, I, I, I, I, I, 7, I],
        [I, 5, 0, 5, I, I, I, I, I, I],
        [I, I, 5, 0, 3, 5, I, I, I, I],
        [I, I, I, 3, 0, I, I, I, I, I],
        [I, I, I, 5, I, 0, 6, I, I, I],
        [I, I, I, I, I, 6, 0, 3, I, I],
        [I, I, I, I, I, I, 3, 0, 1, I],
        [I, 7, I, I, I, I, I, 1, 0, 1],
        [I, I, I, I, I, I, I, I, 1, 0],

    ]

    # Run Floyd–Warshall algorithm
    optimized_path = floydWarshall(adjMatrix,args.start,args.end)
    print(optimized_path)
    
    bm = Batmobile()
    bm.travel(optimized_path)
    
    ### Forward
    # 1 -> 2 (1.18) powerbank(1.4)
    # 2 -> 3 (0.95)
    # 3 -> 4 (1)
    # 4 -> 6 (1.31)
    # 6 -> 7 (1.55)
    # 7 -> 8 (1.1)
    # 8 -> 9 (0.65)
    # 9 -> 2 (1.3)
    # pivot (1.58)
    
    # powerbank multiplier 1.18644
    
    #init()
    #pivot_right(1.58)
    #forward(1.55 * 1.18644)
    #pivot_left(1.58)
    #cleanup()
    
    #while True:
    #    init()
     #   main()
