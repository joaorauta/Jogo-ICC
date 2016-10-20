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
        self.fundo = Image(Point(375, 225), "images/fundo.png")
        self.fundo.draw(self.win)

        self.lutador = Lutador(300, 0, 90, 310, "ken")
        self.lutador2 = Lutador(300, 0, 500, 310, "sagat2")

        self.imgLutador1 = Image(Point(self.lutador.getX(), self.lutador.getY()), self.lutador.getImage())
        self.imgLutador1.draw(self.win)
        self.imgLutador2 = Image(Point(self.lutador2.getX(), self.lutador2.getY()), self.lutador2.getImage())
        self.imgLutador2.draw(self.win)
        self.distance = Line(self.imgLutador1.getAnchor(), self.imgLutador2.getAnchor())
        self.limit = self.imgLutador1.getWidth() / 2

        self.healthBar1 = Rectangle(Point(20, 20), Point(320, 50))
        self.healthBar1.setOutline("white")
        self.healthBar1.setFill("yellow")
        self.healthBar1.draw(self.win)

        self.healthBar2 = Rectangle(Point(430, 20), Point(730, 50))
        self.healthBar2.setOutline("white")
        self.healthBar2.setFill("yellow")
        self.healthBar2.draw(self.win)

        self.redIncrement1 = 0
        self.redBar1 = Rectangle(Point(20, 20), Point(20 + self.redIncrement1, 50))
        self.redBar1.setOutline("white")
        self.redBar1.setFill("red")

        self.redIncrement2 = 0
        self.redBar2 = Rectangle(Point(430, 20), Point(430 + self.redIncrement2, 50))
        self.redBar2.setOutline("white")
        self.redBar2.setFill("red")

    def update(self):
        if (self.lutador.isDead()):
            print "Jogador 2 venceu!"
            print "console tosco paliativo"
            self.stop()

        if (self.lutador2.isDead()):
            print "Jogador 1 venceu!"
            print "console tosco paliativo"
            self.stop()
        # Alterei a classe graphics, agora o metodo checkKey retorna uma lista com as teclas pressionadas.
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

        if ("Escape" not in self.tecla):

            # ========== LUTADOR 1 ==========#

            if ("d" in self.tecla):
                self.lutador.walk_right()
            if ("a" in self.tecla):
                self.lutador.walk_left()
            if ("s" in self.tecla):
                self.lutador.crouch()
            if ("s" not in self.tecla and self.lutador.isCrouching()):
                self.lutador.idle()

            if ("q" in self.tecla):
                self.lutador.punch()
            if ("e" in self.tecla):
                self.lutador.kick()
            if ("w" in self.tecla):
                self.lutador.block()
            if ("w" not in self.tecla and self.lutador.isBlocking()):
                self.lutador.stopBlocking()

            # ========== LUTADOR 2 ==========#

            if ("Left" in self.tecla):
                self.lutador2.walk_left()
            if ("Right" in self.tecla):
                self.lutador2.walk_right()
            if ("Down" in self.tecla):
                self.lutador2.crouch()
            if ("Down" not in self.tecla and self.lutador2.isCrouching()):
                self.lutador2.idle()

            if ("b" in self.tecla):
                self.lutador2.punch()
            if ("m" in self.tecla):
                self.lutador2.kick()
            if ("n" in self.tecla):
                self.lutador2.block()
            if ("n" not in self.tecla and self.lutador2.isBlocking()):
                self.lutador2.stopBlocking()
        else:
            self.stop()

        self.checkColisions()
        self.lutador.move()
        self.lutador2.move()

    def checkColisions(self):
        # 300hp/damage
        # Se a distancia entre o centro da linha entre os dois jogadores for menor
        # que o centro do comeco da linha + a largura do jogador1/2 houve colisao!
        # enquanto o pulo nao estiver pronto calculamos apenas essas distancias em X

        rect1x = self.lutador.getImageObject().getAnchor().getX()
        rect2x = self.lutador2.getImageObject().getAnchor().getX()
        width1 = self.lutador.getImageObject().getWidth()
        width2 = self.lutador2.getImageObject().getWidth()

        if (rect1x < rect2x + width2 and rect1x + width1 > rect2x):
            # colisao com as paredes
            if (self.lutador.getDx() > 0):
                self.lutador.setDx(0)
            if (self.lutador2.getDx() < 0):
                self.lutador2.setDx(0)

            # ======= SOCO =======#

            if ("punch2" in self.lutador.getImage()):
                if (self.lutador2.isBlocking()):
                    self.lutador2.getHit(15 / 4, True)
                else:
                    self.lutador2.getHit(15, False)

            if ("punch2" in self.lutador2.getImage()):
                if (self.lutador.isBlocking()):
                    self.lutador.getHit(15 / 4, True)
                else:
                    self.lutador.getHit(15, False)

            # ======= CHUTE =======#

            if ("kick2" in self.lutador.getImage()):
                if (self.lutador2.isBlocking()):
                    self.lutador2.getHit(30 / 4, True)
                else:
                    self.lutador2.getHit(30, False)

            if ("kick2" in self.lutador2.getImage()):
                if (self.lutador.isBlocking()):
                    self.lutador.getHit(30 / 4, True)
                else:
                    self.lutador.getHit(30, False)

    def redraw(self):
        self.redIncrement1 = 300 - self.lutador.getHp()
        self.redIncrement2 = 300 - self.lutador2.getHp()

        self.redBar1 = Rectangle(Point(20, 20), Point(20 + self.redIncrement1, 50))
        self.redBar1.setOutline("white")
        self.redBar1.setFill("red")

        self.redBar2 = Rectangle(Point(430, 20), Point(430 + self.redIncrement2, 50))
        self.redBar2.setOutline("white")
        self.redBar2.setFill("red")

        self.redBar1.undraw()
        self.redBar2.undraw()

        self.lutador.animate(self.lutador.getImage())
        self.lutador2.animate(self.lutador2.getImage())

        self.fundo.undraw()
        self.imgLutador1.undraw()
        self.imgLutador2.undraw()

        self.healthBar1.undraw()
        self.healthBar2.undraw()

        self.imgLutador1 = Image(Point(self.lutador.getX(), self.lutador.getY()), self.lutador.getImage())
        self.imgLutador2 = Image(Point(self.lutador2.getX(), self.lutador2.getY()), self.lutador2.getImage())

        self.distance = Line(self.imgLutador1.getAnchor(), self.imgLutador2.getAnchor())
        self.limit = self.imgLutador2.getWidth() / 2

        self.fundo.draw(self.win)

        self.imgLutador1.draw(self.win)
        self.imgLutador2.draw(self.win)

        self.healthBar1.draw(self.win)
        self.healthBar2.draw(self.win)

        self.redBar1.draw(self.win)
        self.redBar2.draw(self.win)

        self.win.update()

    def stop(self):
        self.state = False
