# -*- coding: utf-8 -*-

from ann import *
import pickle
import mnistHandwriting as mh
## Funkcja zapisuje sieć neuronową do pliku
# Zapis poprzez biblioteki pickle, czyli algorytmu kodującego struktury pythona
# w pojedyńczą serie danych.
# Funkcja zapisuje strukture sieci neuronowej oraz wagi neuronów. Dane te precyzyjnie
# określają format sieci neuronowej
#
# \param[in] network sieć neuronowa która zostanie zapisana do pliku
# \param[in] name nazwa pliku w którym zostaje zapisana sieć neuronowa

def saveWeights(network, name = "neuralNetwork.txt"):
    network_list = [network.sizes, network.weights]
    with open(name, 'wb') as f:
        pickle.dump(network_list, f)

## Funkcja która inicjalizuje siec neuronową z pliku zapisanego poprzez pickle
#\code {.py} net = initFromFile(name = "nazwa_pliku") \endcode
#
# \param[in] name nazwa pliku gdzie jest zapisana sieć neuronowa
#
# \return zwraca zainicjalizowaną sieć neuronową zgodną z plikiem
def initFromFile(name = "neuralNetwork.txt"):
    with open(name, 'rb') as f:
         my_list = pickle.load(f)
    ANN = NeuralNet(my_list[0])
    ANN.weights = my_list[1]
    return ANN



# Użycie saveWeights()
NN = NeuralNet([784,30,10])
saveWeights(NN)
# saveWeights(NN, name = "nazwa_pliku")

# Użycie initFromFile()
NNprime = initFromFile()


# Sprawdzanie czy sieci sa takie same, jeżeli linia saveWeights jest zakomentowana
# test nie powiedzie się
inp1 = mh.MNISTexample(0,2,only01=False)
val = NN.forwardPropagation(inp1[0][0])
# print val
val_prime = NNprime.forwardPropagation(inp1[0][0])
# print val_prime


for it in range(0, len(val)):
    if val[it] != val_prime[it]:
        print "Odczyt i zapis sieci nieuronowej się nie powiódł"
        break
else:
    print "Odczyt i zapis sieci neuronowej przebiegł poprawnie"
