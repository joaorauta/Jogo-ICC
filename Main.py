import time

from Jogo import *

j = Jogo()
j.start()

FPS = 30
update_time = 1.0 / FPS

while j.getState():

    start_time = time.time()

    j.update()
    j.redraw()

    loop_time = time.time() - start_time

    if (loop_time < update_time):
        time.sleep(update_time - loop_time)

j.stop()
