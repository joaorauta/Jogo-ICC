from graphics import *
from Jogo import *
from Lutador import *
import time
import Tkinter

j = Jogo()
j.start()

while j.getState():
	j.update()
	j.redraw()
	

j.stop()
