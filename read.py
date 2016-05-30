# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

## Plik zawiera funkcje odczytu obrazków z bazy danych

import mnistHandwriting as mh

## Funkcja zwracająca tablicę cyfr z bazy danych, przypisaną do odpowiednich obrazków z bazy
def readTrueValFromMNIST(mnistExampleReturn):
    trueValTable = []
    for i in range(len(mnistExampleReturn)):
        trueVal = mnistExampleReturn[i][1]
        number = 0
        while (trueVal[number] == 0):
            number = number + 1
        trueValTable.append(number)
    return trueValTable

# Test readTrueValFromMNIST
#print (readTrueValFromMNIST(mh.MNISTexample(0,3,bTrain=True,only01=False)))
#mh.writeMNISTimage(mh.MNISTexample(0,3,only01=False))
## Porównaj stworzone pliki z wartościami wyświetlonymi na standardowym wyjściu


## Funkcja zwraca tablicę tablic 0-1, przypisanych do odpowiednich obrazków z bazy
def readValueTableFromMNIST(mnistExampleReturn):
    trueValTable = []
    for i in range(len(mnistExampleReturn)):
        trueVal = mnistExampleReturn[i][1]
        trueValTable.append(trueVal)
    return trueValTable

## Test readValueTableFromMNIST
#print(readValueTableFromMNIST(mh.MNISTexample(0,3,bTrain=True,only01=False)))

## Funkcja tworzy listę tablic 28x28 reprezentujących obrazki
def TableCreate(mnistExampleReturn):
    alltabs = []
    for i in range(len(mnistExampleReturn)):
        pixels = []
        for x in range(0,28):
            line = []
            for y in range(0,28):
                line.insert(0,int(mnistExampleReturn[i][0][x+y*28]*255))
            pixels.append(line)
        rotated_ccw = zip(*pixels)[::-1]
        alltabs.append(rotated_ccw)
    return alltabs

## Funkcja tworzy listę list - listę wektorów długości 784, do łatwego podawania
# dla neuronów wejściowych
def VectorImage(mnistExampleReturn):
    allVectors = []
    for i in range(0,len(mnistExampleReturn)):
        print i
        vectorI = []
        for x in range(0,28):
            for y in range(0,28):
                vectorI.append(int(mnistExampleReturn[i][0][x+y*28]*255))
        allVectors.append(vectorI)
    return allVectors

## przykład - podobnie dla funkcji VectorImage
#print(TableCreate(mh.MNISTexample(0,2,bTrain=True,only01=False)))
