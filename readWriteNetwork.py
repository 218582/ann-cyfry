# -*- coding: utf-8 -*-

from ann import *
import pickle
## Funkcja zapisuje sieć neuronową do pliku
# Zapis w formacie:
# n - liczba warstw
# [] - liczba neuronów w poszczególnych wartswach
# [[]] - wagi
def saveWeights(network, name = "neuralNetwork.txt"):
    # plik = open (name, "w")
    # plik.write(str(NN.layers) + "\n")
    # plik.write(str(NN.sizes) + "\n")
    # plik.write(str(NN.weights)+ "\n")
    # plik.close
    with open(name, 'wb') as f:
        pickle.dump(network.sizes, f)

def initFromFile(name = "neuralNetwork.txt"):
    # plik = open(name, "r")
    # layers = int(plik.readline())
    # lst = int (plik. readline())
    # print layers, lst
    # plik.close
    with open(name, 'rb') as f:
         my_list = pickle.load(f)
    return my_list

#
NN = NeuralNet([784,30,10])
saveWeights(NN)
# saveWeights(NN, name = "nazwa_pliku")

# Użycie initFromFile()
print initFromFile()
print initFromFile() == NN.sizes
