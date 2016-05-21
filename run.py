# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

## Funkcja odpowiadajaca implementacji interfejsu IRunnable z poprzednich programow
class Runnable:
    
    ## Konstruktor - przygotowuje i uczy sieć neuronową
    # \param [in] net_sizes lista wielkości warstw
    # \param [in] source_learningData dane do nauki sieci
    # \param [in] era ilość epok testu
    # \param [in] batch_size wielkość "mini_batch" do metody Stochastic Gradient Descent
    # \param [in] eta_speed prędkość uczenia
    def __init__ (self, net_sizes, source_learningData, era, batch_size, eta_speed):
        
    ##Uruchomienie testów trafności klasyfikacji
    # \param [in] source_testData dane do testów sieci
    # \param [out] precision trafność klasyfikacji [0:1]
    def run(self, source_testData):
        return 0
