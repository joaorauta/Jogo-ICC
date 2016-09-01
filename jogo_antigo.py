from graphics import *
import time
import Tkinter
from Lutador import *

def main():
	#personagem = 49x84
	win = GraphWin("Fighting Game", 512, 464)
	time_inicial = time.time()
	fundo = Image(Point(256,232), "FeiLongStagemaior.png")
	Image.draw(fundo,win)
	IdleImg = Image(Point(90,310), "editado.png")
	IdleImg.draw(win)	
	RightImg = Image(Point(90,310), "editado.png")
	tecla = ""
	
	l = Lutador(100, 0, 90, 310)2
	
	while tecla != "Escape":
		time_final = time.time() - time_inicial
		tecla = win.checkKey()
		#print(tecla)
		PosX = RightImg.getAnchor().getX()
		PosY = RightImg.getAnchor().getY()
		DownImg = Image(Point(PosX,PosY), "balrgo agachado.png")

		Hitbox1Right = RightImg.getAnchor().getX() - 24.5
		Hitbox2Right = RightImg.getAnchor().getY() - 42
		Hitbox3Right = RightImg.getAnchor().getX() + 24.5
		Hitbox4Right = RightImg.getAnchor().getY() + 42
        
		
		HitboxRightFinal = Rectangle(Point(Hitbox1Right, Hitbox2Right), Point(Hitbox3Right, Hitbox4Right))

		if tecla == "Right":
	        #DownImg = Image(Point(PosX,PosY), "balrgo agachado.png")
		    #UpImg = Image(Point(PosX,PosY), "balrog pulando.png")
			#UpImg.undraw()
			IdleImg.undraw()
			#DownImg.undraw()
			RightImg.undraw()
		
			l.walk_right()
			l.move()
			RightImg = Image(Point(l.getX(), l.getY()), "editado.png")
			RightImg.draw(win)
			#HitboxRightFinal.draw(win)
			'''
			for i in range(5):
				RightImg.move(2,0)
				HitboxRightFinal.move(2,0)
			HitboxRightFinal.undraw()
            '''
		if tecla == "Left":
			#DownImg = Image(Point(PosX,PosY), "balrgo agachado.png")
			#UpImg = Image(Point(PosX,PosY), "balrog pulando.png")
			#UpImg.undraw()
			DownImg.undraw()
			RightImg.undraw()
			#HitboxRightFinal.draw(win)
			#for i in range(5):
			#	RightImg.move(-2,0)
			#	HitboxRightFinal.move(-2,0)
			HitboxRightFinal.undraw()
			l.walk_left()
			l.move()
			RightImg = Image(Point(l.getX(), l.getY()), "editado.png")
			RightImg.draw(win)
			#HitboxRightFinal.draw(win)
				
			
		if tecla == "Up":
			DownImg = Image(Point(l.getX(), l.getY()), "balrgo agachado.png")
			UpImg = Image(Point(l.getX(), l.getY()), "balrog pulando.png")
			'''
			Hitbox1Up = UpImg.getAnchor().getX() - 24.5
			Hitbox2Up = UpImg.getAnchor().getY() - 62
			Hitbox3Up = UpImg.getAnchor().getX() + 24.5
			Hitbox4Up = UpImg.getAnchor().getY() + 42	
			HitboxUpFinal = Rectangle(Point(Hitbox1Up, Hitbox2Up), Point(Hitbox3Up, Hitbox4Up))
			HitboxUpFinal.draw(win)
			'''
			IdleImg.undraw()
			RightImg.undraw()
			DownImg.undraw()
			l.jump(time_final)
			l.move()
			#UpImg.draw(win)
			'''
			for i in range(5):
				UpImg.move(0,-20)
				time.sleep(0.07)
				UpImg.move(0,20)
				HitboxUpFinal.move(0,20)
				HitboxUpFinal.move(0,-20)
			'''
			#HitboxUpFinal.undraw()
			UpImg.undraw()
			RightImg.draw(win)
			
				
		if tecla == "Down":
			DownImg = Image(Point(PosX,PosY), "balrgo agachado.png")
			UpImg = Image(Point(PosX,PosY), "balrog pulando.png")

			Hitbox1Down = DownImg.getAnchor().getX() - 24.5
			Hitbox2Down = DownImg.getAnchor().getY() - 22
			Hitbox3Down = DownImg.getAnchor().getX() + 24.5
			Hitbox4Down = DownImg.getAnchor().getY() + 42
			
			HitboxFinalDown = Rectangle(Point(Hitbox1Down, Hitbox2Down), Point(Hitbox3Down, Hitbox4Down))
			HitboxFinalDown.draw(win)

			RightImg.undraw()
			IdleImg.undraw()
			UpImg.undraw()
			DownImg.draw(win)
			for i in range(5):
				DownImg.move(0,0)
				time.sleep(0.07)
			DownImg.undraw()
			HitboxFinalDown.undraw()
			RightImg.draw(win)
		#print time.time()
		#print time_inicial
        

	print(PosX)
	print(PosY)
	print time_final
	win.close()
main()
