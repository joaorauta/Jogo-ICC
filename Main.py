from graphics import *
from Jogo import *
from Lutador import *
import time
import Tkinter

FPS = 60
sleep_time = 1/FPS


j = Jogo()
j.start()

while j.getState():
	j.update()
	j.redraw()
	time.sleep(sleep_time)

j.stop()
