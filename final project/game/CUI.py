from pico2d import *

import gfw
import CPlayer
import math




class Lager_Energy:
    image = None
    image2 = None
    def __init__(self):
        pass
    def __init__(self, x, y):
        self.x,self.y=x,y
        if Lager_Energy.image is None:
            Lager_Energy.image = load_image('Resource/Energy_bar.png')
        if Lager_Energy.image2 is None:
            Lager_Energy.image2 = load_image('Resource/Energy.png')

    def update(self):
        pass

    def draw(self):
      for player in gfw.world.objects_at(gfw.layer.CPlayer): 
        self.image.draw(self.x,self.y,340,28)
        self.image2.clip_draw(0, 0, 304, 28, self.x-152 +player.Gage*1.52 , self.y,player.Gage* 3.04, 14)
        pass


class Player_Bomb:
    image = None
    def __init__(self):
        if Player_Bomb.image is None:
            Player_Bomb.image = load_image('Resource/Item_Bomb2.png')

    def update(self):
        pass

    def draw(self):
      for player in gfw.world.objects_at(gfw.layer.CPlayer): 
        for n in range(player.BombNumber):
            self.image.draw(690,10+20*n,30,20)
        pass


class Life:
    image= None
    def __init__(self):
        if Life.image is None:
                Life.image = load_image('Resource/Life.png')
    def update(self):
        pass

    def draw(self):
     for player in gfw.world.objects_at(gfw.layer.CPlayer):
        for n in range(player.Life):
            self.image.draw(660, 10 + 20 * n, 30, 40)
        pass
