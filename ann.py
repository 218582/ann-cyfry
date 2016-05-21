# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

import numpy as np
import maths

class NeuralNet(object):
    
    # konstruktor - użycie: net = NeuralNet([1,2,3])
    # kolejne liczby wpisane w sizes decyduja o ilosci neuronow w danej warstwie
    # ilosc liczb - ilosc warstw
    # zawiera rowniez sposob reprezentacji sieci neuronowej
    ## layers   - liczba warstw
    ## sizes    - ilosc neuronow w poszczegolnych warstwach
    ## biases   - biasy neuronow: lista arrayow, kazdy array odpowiada kolejnej 
    ##            warstwie, kazdy element arraya zawiera biasy kolejnych neuronow
    ## weights  - wagi polaczen miedzy neuronami: lista arrayow, kazdy array
    ##            odpowiada kolejnym "warstwom" polaczen, kazdy element arraya
    ##            to kolejna waga polaczenia
    def __init__ (self, sizes):
        self.layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]  #losowe biasy
        self.weights = [np.random.rand(y, x) for x, y in zip(sizes[:-1], sizes[1:])] #losowe wagi polaczen
        
    # funkcja aktywacji neuronu sigmoidalnego:
    # y = 1 / (1+exp(- suma iloczynów wszystkich wag i wejść - bias neuronu))
    def NeuronActivation (self,inpt):
        for bs, wght in zip(self.biases, self.weights):
            a = sigmoid(np.dot(wght, inpt)+bs)
        return a
    
    

