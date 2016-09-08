from graphics import *
from Jogo import *
from Lutador import *
import time
import Tkinter

j = Jogo()
j.start()

FPS = 30
update_time = 1.0/FPS

time1 = time.clock()

while j.getState():
	j.update()
	j.redraw()
	time.sleep(update_time)
j.stop()
