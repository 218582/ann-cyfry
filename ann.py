# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

#Na podstawie: Michael A. Nielsen, "Neural Networks and Deep Learning", Determination Press, 2015

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

    def __init__ (self, sizes):
        #Hyper-parameters
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    ##funkcja sigmoid
    def sigmoid(z):
        return 1.0/(1.0+np.exp(-z))

    ##pochodna funkcji sigmoid
    def sigmoid_prime(z):
        return sigmoid(z)*(1-sigmoid(z))


    ## Funkcja aktywacji neuronu sigmoidalnego:
    # y = 1 / (1+exp(- iloczyny wszystkich wag i wejść))
    #
    # dot(x, y) - mnozenie macierzy
    def forwardPropagation (self,inpt):
        for wght in self.weights:
            a = self.sigmoid(np.dot(wght, inpt))
        return a

    ## Funkcja wykonująca Stochastic Gradient Descent
    def SGD(self, data_In_Training, epochs, batch_size, eta):
        l = len(data_In_Training)
        for j in xrange(epochs):
            random.shuffle(data_In_Training)
            batches = [
                data_In_Training[k:k+batch_size]
                for k in xrange(0, l, batch_size)]
            for batch in batches:
                self.update_batch(batch, eta)
                print "Epoch" + str(batch) + "complete"

    ##Funkcja aktualizująca wagi przy użyciu Stochastic Gradient Descent.
    #
    #\param [in] batch lista dane - wynik
    #\param [in] eta prędkość uczenia się sieci
    def update_batch(self, batch, eta):
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in batch:
            delta_nabla_w = self.backPropagation(x, y)
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]

    def backPropagation(self, x, y):
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x] # wszystkie aktywatory
        zs = [] # wszystkie z
        for w in self.weights:
            z = np.dot(w, activation)
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        for l in xrange(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_w)

    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        return (output_activations-y)


#NN = NeuralNet([3,5,2])
#print NN.weights[0]
#
