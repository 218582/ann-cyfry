# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

import numpy as np
import maths

class NeuralNet(object):
    
    ## Konstruktor sieci neuronowej
    # Użycie: 
    # \code {.py} net = NeuralNet([1,2,3]) \endcode
    # \param[in] sizes tablica ilości neuronów w klejnych warstwach
    #
    # Konstruktor zawiera rowniez sposob reprezentacji sieci neuronowej
    # layers   - liczba warstw
    # sizes    - ilosc neuronow w poszczegolnych warstwach (lista)
    # biases   - biasy neuronow: lista arrayow, kazdy array odpowiada kolejnej 
    #            warstwie, kazdy element arraya zawiera biasy kolejnych neuronow
    # weights  - wagi polaczen miedzy neuronami: lista arrayow, kazdy array
    #            odpowiada kolejnym "warstwom" polaczen, kazdy element arraya
    #            to lista wag polaczen z kolejnym neuronem
    # [1:]     - od indeksu 1 do konca
    # [:-1]    - od konca: od ostatniego do indeksu 1
    def __init__ (self, sizes):
        self.layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]  #losowe biasy
        self.weights = [np.random.rand(y, x) for x, y in zip(sizes[:-1], sizes[1:])] #losowe wagi polaczen
        
    ## Funkcja aktywacji neuronu sigmoidalnego:
    # y = 1 / (1+exp(- suma iloczynów wszystkich wag i wejść - bias neuronu))
    # zip(a, b) - tworzy iterator pozwalajacy na przejscie po kolejnych elementach a i b
    #             i wykonac operacje i-tego a z i-tym b. Zatrzymuje sie, gdy jedna ze struktur
    #             (a lub b) sie skonczy
    # dot(x, y) - mnozenie macierzy
    def NeuronActivation (self,inpt):
        for bs, wght in zip(self.biases, self.weights):
            a = sigmoid(np.dot(wght, inpt)+bs)
        return a
    
    
    

