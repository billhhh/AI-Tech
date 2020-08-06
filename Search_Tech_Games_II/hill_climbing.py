import numpy as np
import matplotlib.pyplot as plt
import math

# step size
DELTA = 0.01
# define the domain
BOUND = [5,8]
# random times
RANDOM_TIMES = 100


def F(x):
    return math.sin(x*x)+2.0*math.cos(2.0*x)

def hillClimbing(x):
    while F(x+DELTA)>F(x) and x+DELTA<=BOUND[1] and x+DELTA>=BOUND[0]:
        x = x+DELTA
    while F(x-DELTA)>F(x) and x-DELTA<=BOUND[1] and x-DELTA>=BOUND[0]:
        x = x-DELTA
    return x,F(x)

def findMax():
    highest = [0,-1000]
    
    for i in range(RANDOM_TIMES):
        x = np.random.rand()*(BOUND[1]-BOUND[0])+BOUND[0]
        currentValue = hillClimbing(x)
        print('current value is :',currentValue)
        
        if currentValue[1] > highest[1]:
            highest[:] = currentValue
    return highest
    
[x,y] = findMax()
print('highest point is x :{},y:{}'.format(x,y))