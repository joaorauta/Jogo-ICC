from graphics import *
import time
import Tkinter
from Lutador import *

class Jogo():
	
	def __init__(self):
		self.state = False		
	
	def getState(self):
		return self.state
	
	def start(self):
		self.state = True
		
		self.win = GraphWin("Fighting Game", 512, 464)
		self.time_inicial = time.time()
		self.lutador = Lutador(100, 0, 90, 310)
				
		self.fundo = Image(Point(256,232), "FeiLongStagemaior.png")
		self.LutadorIdle = Image(Point(lutador.getX(), lutador.getY()), "editado.png")	
		self.LutadorRight = Image(Point(lutador.getX(), lutador.getY()), "editado.png")
		self.LutadorUp = Image(Point(lutador.getX(), lutador.getY()), "balrog pulando.png")
		self.LutadorDown = Image(Point(lutador.getX(), lutador.getY()), "balrog agachado.png")			
		
	def update(self):
		
	
	def redraw(self):
		self.fundo.draw(win)
		
		
		
	def stop(self):
		self.state = False	
	
	
