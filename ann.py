# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

import numpy as np
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
    #
    # zip(a, b) - tworzy iterator pozwalajacy na przejscie po kolejnych elementach a i b
    #             i wykonac operacje i-tego a z i-tym b. Zatrzymuje sie, gdy jedna ze struktur
    #             (a lub b) sie skonczy
    # dot(x, y) - mnozenie macierzy
    def NeuronActivation (self,inpt):
        for bs, wght in zip(self.biases, self.weights):
            a = sigmoid(np.dot(wght, inpt)+bs)
        return a
    



import mnistHandwriting as mh
    
## Funkcja zwracająca tablicę cyfr z bazy danych, przypisaną do odpowiednich obrazków z bazy
def readTrueValFromMNIST(mnistExampleReturn):
    trueValTable = []
    for i in range(len(mnistExampleReturn)):
        trueVal = mnistExampleReturn[i][1]
        number = 0
        while (trueVal[number] == 0):
            number = number + 1
        trueValTable.append(number)
    return trueValTable

# Test readTrueValFromMNIST
#print(readTrueValFromMNIST(mh.MNISTexample(0,3,bTrain=True,only01=False)))
#mh.writeMNISTimage(mh.MNISTexample(0,3,only01=False))
## Porównaj stworzone pliki z wartościami wyświetlonymi na standardowym wyjściu


## Funkcja zwraca tablicę tablic 0-1, przypisanych do odpowiednich obrazków z bazy
def readValueTableFromMNIST(mnistExampleReturn):
    trueValTable = []
    for i in range(len(mnistExampleReturn)):
        trueVal = mnistExampleReturn[i][1]
        trueValTable.append(trueVal)
    return trueValTable
    
   

## Test readValueTableFromMNIST   
#print(readValueTableFromMNIST(mh.MNISTexample(0,3,bTrain=True,only01=False)))

##Funkcja tworzy tablicę 28x28 reprezentującą obrazek
def TableCreate(mnistExampleReturn):
    i = 0
    pixels = []
    for x in range(0,28):
        line = []
        for y in range(0,28):
            line.insert(0,int(mnistExampleReturn[i][0][x+y*28]*255))
        pixels.append(line)
    rotated_ccw = zip(*pixels)[::-1]
    return rotated_ccw
    

    
