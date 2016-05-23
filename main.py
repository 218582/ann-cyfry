# -*- coding: utf-8 -*-
#Powyższa linia pozwala na wpisywanie polskich znaków

#przyklad dolaczania modulu
#wywolanie: python main.py

#import module #jak include w c++

#print "Hello World!"
#module.functionFromModule() #musi byc tak wywolane przy powyzszym typie zalaczenia

##inny sposob zalaczenia:
#from module import functionFromModule
##wowczas mozna wywolac:
#functionFromModule()

##zeby w taki sposob zaimportowac wszystkie:
#from module import *


"""Przyklad wywolywania modulu mnistHandwriting.py"""
#from mnistHandwriting import *

#writeMNISTimage(MNISTexample(0,2,only01=False))


################################################################################

from ann import *
import run
import stopwatch
import read
import mnistHandwriting as mh

data_part = mh.MNISTexample(0,100,bTrain=True,only01=False)
##pierwsze indeksowanie  - po rekordach z baz
print data_part[0][1]
##drugie indeksowanie    - (znormalizowane piksele w wektorze), (lista 0-1 pozycji dla wyniku*)
## * [0,1,0,...,0] - wynikiem jest 1
print len(data_part[0][0])
#print data_part[0][1]

