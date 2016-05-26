# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

#Na podstawie: Michael A. Nielsen, "Neural Networks and Deep Learning", Determination Press, 2015

import random
import numpy as np

class NeuralNet(object):

    ## Konstruktor
    # \param [in] sizes lista ilości neuronów w kolejnych warstwach
    # \param [in] self wskaźnik na obiekt
    # Tworzy sieć neuronową o zadanej głębokości i ilości neuronów w każdej warstwie
    # Użycie:
    # \code {.py} net = NeuralNet([1,2,3]) \endcode
    def __init__(self, sizes):
        #"Hyper-parameters"
        self.layers = len(sizes) #ilość warstw
        self.sizes = sizes #lista rozmiarów warstw
        self.weights = [np.random.randn(b, a) for a, b in zip(sizes[:-1], sizes[1:])]
        #losowe wagi połączeń między neuronami

    ## Metoda mechanizmu propagacji do przodu
    # Oblicza kolejno iloczyny wag i wejść dla kolejnych połączeń oraz
    # wstawia do funkcji aktywacji danego neuronu, przechodząc tym samym po całej sieci
    #
    # \param [in] wejście danych do sieci
    # \param [in] self wskaźnik na obiekt
    # \retval wyjście danych z sieci
    def forwardPropagation(self, inpt):
        for weight in self.weights:
            inpt = self.sigmoid(np.dot(weight, inpt))
        return inpt

    ## Metoda przeprowadzająca Stochastic Gradient Descent
    # \param [in] self wskaźnik na obiekt
    # \param [in] data_training dane do nauki sieci (z mnist_loader)
    # \param [in] epochs liczba epok
    # \param [in] batch_size liczba testów w danej epoce
    # \param [in] eta prędkość uczenia się sieci
    # \param [in] data_test dane do testu trafności przewidywań sieci (None - brak testu poprawności - domyśnie)
    def SGD(self, data_training, epochs, batch_size, eta, data_test=None):
        if data_test: n_test = len(data_test)
        n = len(data_training)
        for j in xrange(epochs): #xrange() zwraca iterator (dla pythona 3.0 odpowiednikiem jest range())
            random.shuffle(data_training) #losowe przemieszanie danych treningowych
            #Podział danych na mniejsze kawałki aby przyspieszyć uczenie sieci
            #Mimo zmniejszenia ilości danych wykorzystanych do nauki, możemy uzyskać całkiem dobre przybliżenie
            #gradientu funkcji kosztów
            batches = [data_training[k:k+batch_size] for k in xrange(0, n, batch_size)]
            for batch in batches:
                self.update_batch(batch, eta)
            if data_test:
                print "Epoka {0}: {1} / {2}".format(
                    j, self.evaluation(data_test), n_test)
            else:
                print "Epoka {0} ukończona".format(j)

    ##Metoda aktualizująca wagi w sieci
    # \param [in] self wskaźnik na obiekt
    # \param [in] batch lista tupli typu (wejście, wyjście), część danych z danych treningowych
    # \param [in] eta prędkość uczenia sieci
    def update_batch(self, batch, eta):
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in batch:
            delta_nabla_w = self.backPropagation(x, y)
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(batch))*nw for w, nw in zip(self.weights, nabla_w)]

    ## Metoda uruchamiająca wsteczną propagację
    # Za Michael A. Nielsen, "Neural Networks and Deep Learning", Determination Press, 2015
    # Wsteczna propagacja odnosi się do błędu na wyjściu sieci między watrością uzyskaną a oczekiwaną.
    # Ta czynność pozwala na propagację błędu po całej sieci w taki sposób, by umożliwić nastawienie
    # wag w całej sieci.
    #
    # \param [in] self wskaźnik na obiekt
    # \param [in] x wejście
    # \param [in] y wyjście
    # \retval (nabla_w)
    def backPropagation(self, x, y):
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        activation = x
        activations = [x] # lista wszystkich wyników aktywacji neuronów, warstwa po warstwie
        zs = [] # lista wszystkich wektorów z warstwa po warstwie
        for w in self.weights:
            z = np.dot(w, activation)
            zs.append(z)
            activation = self.sigmoid(z)
            activations.append(activation)
        delta = self.cost_derivative(activations[-1], y) * \
            self.derivative_sigmoid(zs[-1])
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        for l in xrange(2, self.layers):
            z = zs[-l]
            sp = self.derivative_sigmoid(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_w)

    ##Metoda wykonuje test trafności wyników
    # \param [in] self wskażnik na obiekt
    # \param [in] data_test dane testujące nauczoną sieć, odrębne od danych wykorzystanych do nauki
    # \retval suma poprawnych wyników
    def evaluation(self, data_test):
        test_results = [(np.argmax(self.forwardPropagation(x)), y) for (x, y) in data_test]
        return sum(int(x == y) for (x, y) in test_results)

    ##Metoda oblicza pochodną funkcji kosztów
    # \param [in] aktywacje wszytskich neuronów - wyjście sieci
    # \param [in] oczekiwane wyjście
    # \retval pochodna funkcji kosztów
    def cost_derivative(self, output_activations, y):
        return (output_activations-y)

    ##Metoda obliczająca funkcję aktywacji neuronu - funkcja sigmoidalna
    # \param [in] self wskaźnik na obiekt
    # \param [in] z obiekt poddawany działaniu funkcji
    # \retval wynik działania funkcji sigmoidalnej
    def sigmoid(self,z):
        return 1.0/(1.0+np.exp(-z))

    ##Metoda wyliczająca pochodną funkcji sigmoidalnej
    # \param [in] self wskaźnik na obiekt
    # \param [in] z obiekt poddawany działaniu funkcji
    # \retval wynik działania funkcji
    def derivative_sigmoid(self,z):
        return self.sigmoid(z)*(1-self.sigmoid(z))
