# -*- coding: utf-8 -*-
# import sys
# from PyQt4 import QtGui, QtCore, uic
#
##Aby działało należy wpisać sudo apt-get install python-qt4
# if __name__ == '__main__':
#     app = QtGui.QApplication(sys.argv)
#     app.setStyle("cleanlooks")
#
#     data = QtCore.QStringList()
#     data << "Jeden" << "Dwa" << "Trzy" << "Cztery"
#
#     listWidget = QtGui.QListWidget()
#     listWidget.show()
#     listWidget.addItems(data)
#
#     count = listWidget.count()
#     for i in range(count):
#         item = listWidget.item(i)
#         item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
#
#     combobox = QtGui.QComboBox()
#     combobox.show()
#     combobox.addItems(data)
#
#     sys.exit (app.exec_())

### PyGame
import sys, pygame
from pygame.locals import *
from PIL import Image, ImageFilter

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (180, 180, 180)

OUTPUT_IMAGE_SIZE = (28, 28)

PAINT_SIZE = (20*OUTPUT_IMAGE_SIZE[0], 20*OUTPUT_IMAGE_SIZE[1] )
RESULT_HEIGHT = 150
WINDOW_SIZE = (PAINT_SIZE[0], PAINT_SIZE[1] + RESULT_HEIGHT)

class Painter(object):

    ## Inicjalizuje wygląd okna
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.paintScreen = self.screen.subsurface( pygame.Rect((0,0), PAINT_SIZE) )
        self.resultScreen = self.screen.subsurface( pygame.Rect((0, PAINT_SIZE[1]),(WINDOW_SIZE[0], RESULT_HEIGHT) ) )

        self.screen.fill(WHITE)
        self.resultScreen.fill(GREY)
        self.drawBorders()
        pygame.display.flip()
        self.fps = 0
        self.running = True
		self.clock = pygame.time.Clock()
		self.size = WINDOW_SIZE

    def drawBorders(self):
        pygame.draw.line(self.screen, BLACK, (0, PAINT_SIZE[1]), (WINDOW_SIZE[0], PAINT_SIZE[1]), 2)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTOMDOWN:
                self.paintCircle(event.pos)

    def isInPaintScreen(self, pos, error=(0, 0)):
        x, y = pos
        dx, dy = error
        if x - dx < PAINT_SIZE[0] and y - dy < PAINT_SIZE[1]:
            return True
        else:
            return False

	def paintCircle(self, pos):
		pygame.draw.circle(self.paintScreen, BLACK, pos, self.lineWidth/2)

	def mainLoop (self, fps=0):
		self.fps = fps
		while self.running:
			self.handleEvents()
			pygame.display.flip()
			self.clock.tick(self.fps)

    #

	# def handleEvents(self):
    #     for event in pygame.event.get():
    #     	if event.type == pygame.QUIT:
    #     		self.running = False
    #     	elif event.type == pygame.KEYDOWN:
    #     		self.keyDown(event.key)
    #     	elif event.type == pygame.KEYUP:
    #     		if event.key == pygame.K_ESCAPE:
    #     			self.running = False
    #     		self.keyUp(event.key)
    #     	elif event.type == pygame.MOUSEBUTTONUP:
    #     		self.mouseUp(event.button, event.pos)
    #     	elif event.type == pygame.MOUSEBUTTONDOWN:
    #     		self.mouseDown(event.button, event.pos)
    #     	elif event.type == pygame.MOUSEMOTION:
    #     		self.mouseMotion(event.buttons, event.pos, event.rel)

if __name__ == "__main__":
    gui = Painter()
    gui.mainLoop(40)
