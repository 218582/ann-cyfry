# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

import time

## Obsluga mierzenia czasu operacji
#
# Przyklad wykorzystania:
## \code{.py}
##czas = Stopwatch()
##operacja()
##czas.stop()
##czas.printTime()
##czas.saveToFile("result.txt")
## \endcode
class Stopwatch:

    ## Konstruktor
    #
    # Stworzenie obiektu uruchamia zegar
    def __init__ (self):
        self.zero = time.time()

    ## Zatrzymanie zegara
    #
    # \retval Czas od uruchomienia do zatrzymania zegara
    def stop(self):
        self.t = time.time() - self.zero
        return self.t

    ## Wyświetla na standardowym wyjściu czas działania
    #
    # \warning Użycie przed zatrzymaniem zegara spowoduje błąd
    def printTime(self):
        print str(self.t) + " s"

    ## Zapisuje do pliku filename czas działania
    #
    # \warning Użycie przed zatrzymaniem zegara spowoduje błąd
    #
    # \param [in] filename nazwa pliku
    # \param [in] comment komentarz do pliku (nie może zawierać '\n')
    def saveToFile(self, filename, comment=None):
        self.file = open(filename, "a")
        if not self.file.closed:
            if comment:
                self.file.write('#' + comment + "\n")
            self.file.write(str(self.t) + "\n")
        self.file.close()
