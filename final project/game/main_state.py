import gfw
from pico2d import *
from CPlayer import Player
import win32api
import gobj
def enter():
    gfw.world.init(['CPlayer','CBullet'])
    global player
    player=Player()
    gfw.world.add(gfw.layer.CPlayer,player)


def update():
    gfw.world.update()


def draw():
    gfw.world.draw()
    
def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
        
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
