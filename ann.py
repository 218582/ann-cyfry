# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

import numpy as np
import random

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

    def __init__ (self, sizes): #od teraz mogą być max 3 warstwy
        #Hyper-parameters
        self.sizes = sizes #[3"""784""", 2 """wybrać""", 1 """10"""]
        self.layers = len(self.sizes)
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
    # def NeuronActivation(self,inpt,i):
    #     self.ax = np.dot(inpt, self.weights[i])
    #     return self.sigmoid(self.ax)


    ## Metoda przeprowadzająca propagację do przodu
    #\param[in] lista list z danymi wejściowymi
    #
    #\warning każda lista wewnętrzna danych wejściowych musi zawierać tyle elementów,
    #\warning ile neuronów wejściowych posiada sieć
    def forwardPropagation(self,inpt):
        self.Z1 = np.dot(inpt,self.weights[0])
        self.A1 = self.sigmoid(self.Z1)
        self.Z2 = np.dot(self.A1, self.weights[1])
        OUTPUT = self.sigmoid(self.Z2)
        return OUTPUT

    ## Metoda wyliczająca funkcję kosztów
    def costFunction(self, inpt, targt):
        self.OUTPUT = self.forwardPropagation(inpt)
        J = 0.5*sum((targt-self.OUTPUT)**2)
        return J

    ##Pochodna funkcji kosztów
    def derivative_costFunction(self, inpt, targt):
        self.OUTPUT = self.forwardPropagation(inpt)
        d2 = np.multiply(-(targt - self.OUTPUT), self.derivative_sigmoid(self.Z2))
        # dJdW1 = np.dot(self.transpose(self.A1), d2)
        dJdW1 = np.dot(self.A1.T, d2)
        d1 = np.multiply(np.dot(d2, self.transpose(self.weights[1])), self.derivative_sigmoid(self.Z1))
        dJdW0 = np.dot(self.transpose(inpt), d1)
        return dJdW0, dJdW1

    ##Dokonuje transpozycji macierzy
    # \retval macierz po transpozycji
    def transpose(self, matrix):
        return [list(i) for i in zip(*matrix)]

    ## funkcja sigmoidalna
    # \retval sigmoid wynik
    def sigmoid(self, exponent):
        return 1.0/(1.0+np.exp(-exponent))

    ##Pochodna funkcji sigmoidalnej
    # \retval derivative_sigmoid wynik
    def derivative_sigmoid(self,exponent):
        return np.exp(-exponent)/((1+np.exp(-exponent))**2)

    def getParams(self):
        params = np.concatenate((self.weights[0].ravel(), self.weights[1].ravel()))
        return params

    def setParams(self, params):
        #Set W1 and W2 using single paramater vector.
        W0_start = 0
        W0_end = self.sizes[1] * self.sizes[0]
        self.weights[0] = np.reshape(params[W0_start:W0_end], (self.sizes[0] , self.sizes[1]))
        W1_end = W0_end + self.sizes[1]*self.sizes[2]
        self.W1 = np.reshape(params[W0_end:W1_end], (self.sizes[1], self.sizes[2]))




























# ## Test sieci
NN = NeuralNet([2,3,1])
print NN.weights
# print NN.layers
# #inp = np.random.rand(1,2)
# input1 = [0.2, 0.4]
# input2 = [0.3, 0.5]
# input3 = [0.1, 0.5]
# inp = [input1, input2, input3]
# # print "Input:"
# # print inp
# out = [[0.3], [0.4], [0.3]]
# #
# val = NN.forwardPropagation(inp)
# #
# costf1 = NN.costFunction(inp, out)
# # print "CostFunction1:"
# # print costf1
# dJdW0, dJdW1 = NN.derivative_costFunction(inp, out)
# NN.weights[0] = NN.weights[0] - 2*dJdW0
# NN.weights[1] = NN.weights[1] - 2*dJdW1
# costf2 = NN.costFunction(inp, out)
# # print "CostFunction2:"
# print costf2
# while (costf2 < costf1):
#     costf1 = NN.costFunction(inp, out)
#     print "CostFunction1:"
#     print costf1
#     dJdW0, dJdW1 = NN.derivative_costFunction(inp, out)
#     NN.weights[0] = NN.weights[0] - 2*dJdW0
#     NN.weights[1] = NN.weights[1] - 2*dJdW1
#     costf2 = NN.costFunction(inp, out)
#     print "CostFunction2:"
#     print costf2
# print "\n"
# print val
# deriv = NN.derivative_costFunction(inp, tgt)
# # print deriv
print
print
print
print NN.getParams()
