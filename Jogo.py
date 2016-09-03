from graphics import *
from Lutador import *
import time
import Tkinter

class Jogo():
		
	def __init__(self):
		self.state = False

	
	def getState(self):
		return self.state

	
	def start(self):
		self.state = True
		self.lutador = Lutador(100, 0, 90, 310)
		self.win = GraphWin("Fighting Game", 512, 464, autoflush=False)
		self.time_inicial = time.time()
		self.tecla = ""
		self.fundo = Image(Point(256,232), "images/FeiLongStagemaior.png")
		self.fundo.draw(self.win)			
		self.imgLutador = Image(Point(self.lutador.getX(), self.lutador.getY()), self.lutador.getImage())
		self.imgLutador.draw(self.win)
		

	def update(self):
		self.tecla = self.win.checkKey()
		if(self.tecla != "Escape"):
			if(self.tecla == "Right"):
				self.lutador.walk_right()
				print self.lutador.getX()
			if(self.tecla == "Left"):
				self.lutador.walk_left()
				print self.lutador.getX()
		else:
			self.stop()

		self.lutador.move()
		

	def redraw(self):
		update()


	def stop(self):
		self.state = False
