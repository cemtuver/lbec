from numpy import *
from scipy.optimize import *
from BinaryModularArithmetic import BinaryModularArithmetic

x = 1
m = 127
polynomail = [127, 63, 0]
bma = BinaryModularArithmetic(m, polynomail)

def myFunc(y):
    return pow(y[0], 2) + x * y[0] - pow(x, 3) - pow(x, 2) - 1

for i in range(1, bma.getPrimitive()):
    x = i
    y = fsolve(myFunc, 0)
    print(x, y[0])
    if (y[0] == int(y[0]) and int(y[0]) != 25550):
        print("found")
        break