# created by David Skerritt
# example of a linear function

import matplotlib
import matplotlib.pyplot as plt



def Linear(x): # model / function

    y = 3*x-2        # r = rate of growth, x = population size
    return y



i = 1


for i in range(1, 6):

    
    plt.scatter(i, Linear(i))
    plt.pause(.01)

    print(Linear(i))

    i+=1


plt.grid()
plt.show()
