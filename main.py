#przyklad dolaczania modulu
#wywolanie: python main.py

import module #jak include w c++

print "Hello World!"
module.functionFromModule() #musi byc tak wywolane przy powyzszym typie zalaczenia

##inny sposob zalaczenia:
#from module import functionFromModule
##wowczas mozna wywolac:
#functionFromModule()

##zeby w taki sposob zaimportowac wszystkie:
#from module import *
