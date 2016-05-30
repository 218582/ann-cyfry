# -*- coding: utf-8 -*-

from ann import *

# ## Funkcja zapisuje sieć neuronową do pliku
# def saveWeights(network, name = "neuralNetwork.txt"):
#     plik = open (name, "w")
#
#     #zapis warstw
#     for size in xrange(len(network.sizes)):
#         plik.write(str(network.sizes[size]) + " ")
#     plik.write("\n")
#
#     #zapis wag
#     for each in xrange(len(network.weights)):
#         for it in xrange(len(network.weights[each])):
#             for it2 in xrange(len(network.weights[each][it])):
#                 plik.write(str(network.weights[each][it][it2]) + "\n")
#             plik.write("i\n")
#         plik.write("j\n")
#     plik.write("k\n")
#     plik.close
#
#
# def initFromFile(network, name = "neuralNetwork.txt"):
#     plik = open(name, "r")
#
#     #Odczyt wielkości i ilości warstw
#     string_layers = plik.readline()
#     lay = []
#     lay = string_layers.split()
#     print "lay"
#     print lay
#     for each in xrange(len(lay)):
#         lay[each] = int(lay[each])
#     network.__init__(lay)
#
#     each = 0
#     it = 0
#     it2 = 0
#     # odczyt wag
#     while True:
#         l = plik.readline()
#         if not l: break
#         if l in ['k\n']:
#             each=each+1
#             it = 0
#             it2 = 0
#         elif l in ['j\n']:
#             it=it+1
#             it = 0
#         elif l in ['i\n']:
#             it2=0
#         else:
#             print l
#             if l not in ['k\n', 'j\n', 'i\n']:
#                 l = float(l)
#                 network.weights[each][it][it2] = l
#                 it2 = it2+1
#     else:
#         plik.close()

import pickle
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
# \retval true jeśli rozmiary sieci sa takie same
# \retval false jesli rozmiary sieci sa inne
def initFromFile(network, name = "neuralNetwork.txt"):
    with open(name, 'rb') as f:
         my_list = pickle.load(f)
    if my_list[0] == network.sizes:
        network.weights = my_list[1]
        return True
    else:
        return False

# #
# NN = NeuralNet([3,2,1])
# print NN.weights
# # saveWeights(NN)
# saveWeights(NN, name = "nazwa_pliku")
# NN2 = NeuralNet([2,2,1])
# initFromFile(NN2, "nazwa_pliku")
# print NN2.sizes
# print NN2.layers
# print NN2.weights
