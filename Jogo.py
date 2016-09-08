from graphics import *
from Lutador import *
import time
import Tkinter
import threading

class Jogo():
		
	def __init__(self):
		self.state = False

	
	def getState(self):
		return self.state

	
	def start(self):
		self.state = True
		self.win = GraphWin("Fighting Game", 750, 450, autoflush=False)
		self.time_inicial = time.clock()
		self.tecla = ""
		self.fundo = Image(Point(375,225), "images/fundo.png")
		self.fundo.draw(self.win)
		
		self.lutador = Lutador(100, 0, 90, 310, "ken")
		self.lutador2 = Lutador(100, 0, 500, 310, "dummy")

		self.imgLutador1 = Image(Point(self.lutador.getX(), self.lutador.getY()), self.lutador.getImage())
		self.imgLutador1.draw(self.win)
		self.imgLutador2 = Image(Point(self.lutador2.getX(), self.lutador2.getY()), self.lutador2.getImage())
		self.imgLutador2.draw(self.win)
		self.distance = Line(self.imgLutador1.getAnchor(), self.imgLutador2.getAnchor())
		self.limit = self.imgLutador1.getWidth()/2

	def update(self):
		
		#	Alterei a classe graphics, agora o metodo checkKey retorna uma lista com as teclas pressionadas.
		#	A classe graphics agora trata mais dois eventos.
		#	<KeyPress>:
		#		Quando uma tecla eh pressionada adiciona seu codigo na lista de teclas
		#	<KeyRelease>:
		#		Quando uma tecla eh solta remove seu codigo da lista de teclas
		#	Agora o checkKey() eh chamado em cada atualizaco do jogo, se a lista estiver vazia 
		#	(nenhuma tecla pressionada) o jogo nem entra nos ifs que processam essa teclas
		#
		#	Rael me ajudou bastante com isso
		
		self.tecla = self.win.checkKey()
		print self.tecla

		curr_time = time.clock()
		
		if("Escape" not in self.tecla):
			if("Right" in self.tecla):
				self.lutador.walk_right()
			if("Left" in self.tecla):
				self.lutador.walk_left()
			if("Up" in self.tecla):
				if(not self.lutador.isJumping()):
					self.lutador.jump(curr_time)
			if("a" in self.tecla):
				self.lutador.punch()
		else:
			self.stop()
	
		self.checkColisions()	
		self.lutador.move()
		

	def checkColisions(self):

		# Se a distancia entre o centro da linha entre os dois jogadores for menor
		# que o centro do comeco da linha + a largura do jogador1/2 houve colisao!
		# enquanto o pulo nao estiver pronto calculamos apenas essas distancias em X
		
		distance_center = self.distance.getCenter().getX()
		img_center = self.distance.getP1().getX()
		center = distance_center - img_center	

		#verifica qual dos dois esta na frente
		if(self.lutador.getX() <= self.lutador2.getX()):
			if(center <= self.limit):
				if("punch2" in self.lutador.getImage()):
					print "SOCO"
		else:
			if(center > self.limit):
				if("punch2" in self.lutador.getImage()):
					print "SOCO"
			
	def redraw(self):

		self.lutador.animate(self.lutador.getImage())

		self.fundo.undraw()
		self.imgLutador1.undraw()
		self.imgLutador2.undraw()
		#self.distance.undraw()
		
		if("punch2" in self.lutador.getImage()):
			#correcao em X porque a largura do sprite do soco eh diferente
			self.imgLutador1 = Image(Point(self.lutador.getX()+15, self.lutador.getY()), self.lutador.getImage())
		else:
			self.imgLutador1 = Image(Point(self.lutador.getX(), self.lutador.getY()), self.lutador.getImage())
		
		self.imgLutador2= Image(Point(self.lutador2.getX(), self.lutador2.getY()), self.lutador2.getImage())
		self.distance = Line(self.imgLutador1.getAnchor(), self.imgLutador2.getAnchor())
		self.limit = self.imgLutador1.getWidth()/2

		self.fundo.draw(self.win)
		self.imgLutador1.draw(self.win)
		self.imgLutador2.draw(self.win)
		#self.distance.draw(self.win)
		self.win.update()

	def stop(self):
		self.state = False
