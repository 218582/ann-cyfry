# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

import numpy as np
import random
import mnistHandwriting as mh

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
        self.weights = [np.random.randn(self.sizes[i], self.sizes[i+1]) for i in range(0,(self.layers)-1)]


    ## Metoda aktywacji neuronu sigmoidalnego:
    # y = 1 / (1+exp(- iloczyny wszystkich wag i wejść))
    # zwraca activity i-tej warstwy połączeń
    # i liczone od zera
    #
    #\param[in] inpt macierz wejściowa warstwy neuronów
    #\param[in] i warstwa połączeń (indeks od 0)
    #\retval activity Aktywność warstwy i
    #
    # np.dot(x, y) - mnozenie macierzy
    def NeuronActivation(self,inpt,i):
        return self.sigmoid(np.dot(inpt, self.weights[i]))


    ## Metoda przeprowadzająca propagację do przodu
    #\param[in] lista lista list z danymi wejściowymi
    #
    #\warning każda lista wewnętrzna danych wejściowych musi zawierać tyle elementów,
    #\warning ile neuronów wejściowych posiada sieć
    def forwardPropagation(self,inpt):
        an = inpt
        for i in range((self.layers-1)):
            an = self.NeuronActivation(an,i)
        return an

    ## Metoda wyliczająca funkcję kosztów
    def costFunction(self, inpt, targt):
        self.outp_estim = self.forwardPropagation(inpt)
        J = 0.5*sum((targt-self.outp_estim)**2)
        return J

    ## funkcja sigmoidalna
    # \retval sigmoid wynik
    def sigmoid(self, exponent):
        return 1.0/(1.0+np.exp(-exponent))

    ##Pochodna funkcji sigmoidalnej
    # \retval derivative_sigmoid wynik
    def derivative_sigmoid(self,exponent):
        return np.exp(-exponent)/((1+np.exp(-exponent))**2)


# ##Test sieci
# NN = NeuralNet([784,30,10])
# #print NN.weights
# #print NN.layers
# inp = mh.MNISTexample(0,1,only01=False)
# # input1 = [0.2, 0.4]
# # input2 = [0.3, 0.5]
# # inp = [input1, input2]
# print "Input:"
# print inp
# val = NN.forwardPropagation(inp[0][0])
# print "\n"
# print val

#
#     ## Funkcja zapisująca nauczone wagi
#     def saveWeights(self):
#         return 0
#
#
# ##Funkcja wczytująca sieć
# def NetworkInitFromFile():
#     return 0
