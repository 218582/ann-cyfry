# -*- coding: utf-8 -*-

from ann import *

## Funkcja zapisuje sieć neuronową do pliku
def saveWeights(network, name = "neuralNetwork.txt"):
    plik = open (name, "w")

    #zapis warstw
    for size in xrange(len(network.sizes)):
        plik.write(str(network.sizes[size]) + " ")
    plik.write("\n")

    #zapis wag
    for each in xrange(len(network.weights)):
        for it in xrange(len(network.weights[each])):
            for it2 in xrange(len(network.weights[each][it])):
                plik.write(str(network.weights[each][it][it2]) + " ")
            plik.write("\n")
        plik.write("\n\n")
    plik.write("\n\n\n")
    plik.close


def initFromFile(network, name = "neuralNetwork.txt"):
    plik = open(name, "r")

    #Odczyt wielkości i ilości warstw
    string_layers = plik.readline()
    lay = []
    lay = string_layers.split()
    print "lay"
    print lay
    for each in xrange(len(lay)):
        lay[each] = int(lay[each])
    network.__init__(lay)

    # odczyt wag
    # while line not in ['\n', '\r\n']:
    # float(temp[it2])


    plik.close()

#
NN = NeuralNet([3,2,1])
# saveWeights(NN)
saveWeights(NN, name = "nazwa_pliku")
NN2 = NeuralNet([2,2,1])
initFromFile(NN2, "nazwa_pliku")
print NN2.sizes
print NN2.layers
# print NN2.weights
