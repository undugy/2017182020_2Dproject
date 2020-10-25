import gfw
from pico2d import *
from CPlayer import Player
import win32api
import gobj
import random
import CMonster

def enter():
    gfw.world.init(['CPlayer','CBullet','CMonster','CMonsterBullet'])
    global player
    player=Player()
    gfw.world.add(gfw.layer.CPlayer,player)

bisAirPlaneMake = True
MakeTerm=0
RedAirPlaneTerm =0
def update():
    gfw.world.update()
    global MakeTerm, RedAirPlaneTerm,bisAirPlaneMake
    global Time

    MakeTerm+=gfw.delta_time * 1
    if MakeTerm >=1 and bisAirPlaneMake is True:
        MakeTerm=0
        gfw.world.add(gfw.layer.CMonster,CMonster.LeftPlane1(random.randint(0, 720), 960))
        gfw.world.add(gfw.layer.CMonster,CMonster.RightPlane1(random.randint(0, 720), 960))
         


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
