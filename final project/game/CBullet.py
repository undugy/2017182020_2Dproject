from pico2d import *
import gfw
from gobj import *
import CPlayer
import CEffect
name='Bullet'
class Bullet():
    image = [None,None,None,None]

    def __init__(self):
        pass
    def __init__(self, x, y,speed=720):
        self.x, self.y = x, y
        self.dy = speed
        self.isDead = False
        if self.image[0] == None:
            self.image[0] = load_image('Resource/Bullet_Eg_a.png')
        if self.image[1] == None:
            self.image[1] = load_image('Resource/Bullet_Eg_b.png')
        if self.image[2] == None:
            self.image[2] = load_image('Resource/Bullet_Eg_c.png')
        if self.image[3] == None:
            self.image[3] = load_image('Resource/Bullet_Eg_d.png')
    def update(self):
        self.y+= self.dy*gfw.delta_time
        if self.isDead==True or self.y>get_canvas_height()+20:
          self.remove()
        
    def draw(self):
     for player in gfw.world.objects_at(gfw.layer.CPlayer):
        self.image[player.Power].draw(self.x-7,self.y+10,120,120)
    def remove(self):
        gfw.world.remove(self)

class Player_Lager():
    image = None

    def __init__(self):
        pass
    def __init__(self,x):
        self.DeltaX=x
        
        self.isDead = False
        self.Frame=0
        self.LifeTime=0
        for player in gfw.world.objects_at(gfw.layer.CPlayer): 
         self.x, self.y=player.x+self.DeltaX,player.y
        if Player_Lager.image== None:
            Player_Lager.image = load_image('Resource/fire_lazer.png')

    def update(self):
      self.LifeTime+=1
      for player in gfw.world.objects_at(gfw.layer.CPlayer):
         self.x =player.x+self.DeltaX
         self.y =player.y
      for Monster in gfw.world.objects_at(gfw.layer.CMonster):
         if Monster.x - Monster.RadianX < self.x < Monster.x+Monster.RadianX and self.y<Monster.y:
                Pp=CEffect.Effect(Monster.x + random.randint(-15, 15),
                      Monster.y + random.randint(-15, 15), 30, 27, 30, 27, 12,0)
                gfw.world.add(gfw.layer.CEffect,Pp)
                Monster.Hp -=gfw.delta_time*30
      self.LifeTime+=0.1
      self.Frame=(self.Frame+1)%80
      for player in gfw.world.objects_at(gfw.layer.CPlayer):
         player.Gage -= 5*gfw.delta_time*2

      if self.isDead is True or player.Gage <=0:
        for player in gfw.world.objects_at(gfw.layer.CPlayer):
            player.Gage = 0
            self.remove()
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw((self.Frame//10) * 60, -20, 80, 100, self.x, self.y+480, 10, 960)
