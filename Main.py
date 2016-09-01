from Jogo import *

j = Jogo()
j.start()

while j.getState():
	j.update()
	j.redraw()

j.stop()
