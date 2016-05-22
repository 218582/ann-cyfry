# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

import numpy as np
import random

import maths

class NeuralNet(object):
    
    ## Konstruktor sieci neuronowej
    # Użycie: 
    # \code {.py} net = NeuralNet([1,2,3]) \endcode
    # \param[in] sizes tablica ilości neuronów w kolejnych warstwach
    #
    # Konstruktor zawiera rowniez sposob reprezentacji sieci neuronowej
    # layers   - liczba warstw
    # sizes    - ilosc neuronow w poszczegolnych warstwach (lista)
    # weights  - wagi polaczen miedzy neuronami: lista arrayow, kazdy array
    #            odpowiada kolejnym "warstwom" polaczen, kazdy element arraya
    #            to lista wag polaczen z kolejnym neuronem
    # weights[0] =  [[w11, w12, w13, ...],
    #               [ w21, w22, w23, ...],
    #               [ w31, w32, w33, ...],
    #               [ ..., ..., ..., ...]]
    # w13        - połączenie neuronu 1 warstwy 1 z neuronem 3 warstwy 2
    # weights[n] - macierz wag połączeń między warstwą n+1 a warstwą n+2 (liczymy n od zera)
    #              więc weights[1] łączy warstwę drugą z trzecią (pierwsza warstwa - 
    #              wejściowa to warstwa "pierwsza") 
    
    def __init__ (self, sizes):
        #Hyper-parameters
        self.layers = len(sizes)
        self.sizes = sizes
        self.weights = [np.random.randn(self.sizes[i], self.sizes[i+1]) for i in range(self.layers-1)]
        
        
    ## Funkcja aktywacji neuronu sigmoidalnego:
    # y = 1 / (1+exp(- suma iloczynów wszystkich wag i wejść - bias neuronu))
    #
    # zip(a, b) - tworzy iterator pozwalajacy na przejscie po kolejnych elementach a i b
    #             i wykonac operacje i-tego a z i-tym b. Zatrzymuje sie, gdy jedna ze struktur
    #             (a lub b) sie skonczy
    # dot(x, y) - mnozenie macierzy
    def NeuronActivation (self,inpt):
        for wght in self.weights:
            a = maths.sigmoid(np.dot(wght, inpt))
        return a
    
    
    
    
#NN = NeuralNet([3,5,2])
#print NN.weights[0]
#    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
