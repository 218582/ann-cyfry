# -*- coding: utf-8 -*-

from ann import *

## Funkcja zapisuje sieć neuronową do pliku
def saveWeights(network, name = "neuralNetwork.txt"):
    plik = open (name, "w")
    plik.write(str(NN.layers) + "\n")
    plik.write(str(NN.sizes) + "\n")
    plik.write(str(NN.weights)+ "\n")
    plik.close

#
NN = NeuralNet([784,30,10])
# saveWeights(NN)
saveWeights(NN, name = "nazwa_pliku")

def initFromFile(name = "neuralNetwork.txt"):
    pass
