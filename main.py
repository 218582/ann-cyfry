# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

## Funkcja zwraca indeks najwyższej wartości w podanej strukturze (np. liście)
# \param [in] table struktura, w której poszukiwana jest najwyższa liczba
# \retval indeks najwyższej wartości
def result(table):
    return np.argmax(table)

from ann import *
import stopwatch
import mnist_loader

### Testowanie sieci neuronowej
training_data, validation_data, data_test =  mnist_loader.load_data_wrapper()
NN = NeuralNet([784, 30, 10])
time = stopwatch.Stopwatch()
NN.SGD(training_data, 1, 1, 3.0, data_test=data_test)
time.stop()
time.printTime()
# time.saveToFile("filename", "comment")
#bardzo dobre rezultaty uzyskuje sieć z ukryta warstwa 30 neuronów, dla batcha 10 i ilości 10, eta=3.0

# Sprawdzenie, do feedforward przekazujemy tylko sam obrazek w formie dlugiego
# wektora kolumny, wyswietlane wyjscie
print result(NN.forwardPropagation(data_test[1][0]))
#  Tutaj sa wyswietlane prawidlowe wyniki
print data_test[1][1]
