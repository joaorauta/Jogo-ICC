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
		self.win = GraphWin("Fighting Game", 512, 464)
		self.time_inicial = time.time()
		self.tecla = ""
		self.fundo = Image(Point(256,232), "images/FeiLongStagemaior.png")
		self.LutadorIdle = Image(Point(self.lutador.getX(), self.lutador.getY()), "images/editado.png")	
		self.LutadorRight = Image(Point(self.lutador.getX(), self.lutador.getY()), "images/editado.png")
		self.LutadorUp = Image(Point(self.lutador.getX(), self.lutador.getY()), "images/balrog pulando.png")
		self.LutadorDown = Image(Point(self.lutador.getX(), self.lutador.getY()), "images/balrog agachado.png")			
		self.fundo.draw(self.win)
		
	def update(self):
		self.lutador.move()
		self.tecla = self.win.checkKey()
		
	def redraw(self):
		self.lutador.getImage().undraw()
		self.lutador.getImage().draw(self.win)
		
	def stop(self):
		self.state = False
