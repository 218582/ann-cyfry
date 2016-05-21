# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

import numpy as np

# funkcja sigmoidalna
def sigmoid(exponent):
    return 1.0/(1.0+np.exp(exponent))
