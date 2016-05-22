# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

import numpy as np
#import matplotlib.pyplot as plt # do wyświetlania wykresów

## funkcja sigmoidalna
# \retval sigmoid wynik
def sigmoid(exponent):
    return 1.0/(1.0+np.exp(-exponent))
    
#testinput = np.arange(-6,6,0.01)
#plt.plot(testinput, sigmoid(testinput), linewidth=2)
#plt.grid(1)
#plt.show()

##Pochodna funkcji sigmoidalnej
# \retval derivative_sigmoid wynik
def derivative_sigmoid(exponent):
    return np.exp(-exponent)/((1+np.exp(-exponent))**2)
