

from pico2d import *

import SoundManagement
import gfw
import CPlayer
import math
import CEffect





class Bomb_item():
    image=None
    def __init__(self,x,y):
        self.x,self.y=x,y
        self.Frame=0
        self.state1='L'
        self.state2 ='T'
        
        if Bomb_item.image==None:
            Bomb_item.image = load_image('Resource/Item_Bomb.png')
    def Move_Item(self):

        if self.state1 == 'L':
            self.x -= gfw.delta_time * 200
            if self.x <= 0:
                self.state1 = 'R'
        elif self.state1 == 'R':
            self.x += gfw.delta_time * 200
            if self.x >= 720:
                self.state1 = 'L'

        if self.state2 == 'T':
            self.y += gfw.delta_time * 400
            if self.y >= 960:
                self.state2 = 'B'
        elif self.state2 == 'B':
            self.y -= gfw.delta_time * 400
            if self.y <= 0:
                self.state2 = 'T'

    def update(self):
       for Player in gfw.world.objects_at(gfw.layer.CPlayer): 
        Distance = math.sqrt((Player.x - self.x) ** 2 + (Player.y - self.y) ** 2)
        if Distance < 30:
            Pp=CEffect.Effect(self.x, self.y, 144, 100, 80, 50, 8, 3)
            gfw.world.add(gfw.layer.CEffect,Pp)
            
            if Player.BombNumber < 5:
                Player.BombNumber += 1
            self.remove();
        self.Move_Item()

        self.Frame = (self.Frame+gfw.delta_time*6) % 4

    def draw(self):
        self.image.clip_draw(int(self.Frame)*54, 0, 54, 32, self.x, self.y, 50, 30)
    def remove(self):
        gfw.world.remove(self)
class Power_item():
    image=None
    def __init__(self,x,y):
        self.x , self.y= x , y
        self.Frame = 0
        self.state1 = 'L'
        self.state2 = 'T'
        self.Sound=SoundManagement
        if Power_item.image == None:
            Power_item.image = load_image('Resource/Item_Power.png')
        #for player in gfw.world.objects_at(gfw.layer.CPlayer):
        self.PlayerX=0#player.x
        self.PlayerY=0#player.y
        self.PlayerPower=0#player.Power 
    def Move_Item(self):
        if self.state1 == 'L':
            self.x -= gfw.delta_time * 200
            if self.x <= 0:
                self.state1 = 'R'
        elif self.state1 == 'R':
            self.x +=gfw.delta_time * 200
            if self.x >= 720:
                self.state1 = 'L'

        if self.state2 == 'T':
            self.y += gfw.delta_time * 400
            if self.y >= 960:
                self.state2 = 'B'
        elif self.state2 == 'B':
            self.y -= gfw.delta_time * 400
            if self.y <= 0:
                self.state2 = 'T'

    def update(self):
        for player in gfw.world.objects_at(gfw.layer.CPlayer):
         self.PlayerX=player.x
         self.PlayerY=player.y
         self.PlayerPower=player.Power 
        Distance = math.sqrt((self.PlayerX - self.x) ** 2 + (self.PlayerY - self.y) ** 2)
        if Distance < 30:
            
            self.Sound.PlaySound(10)
            if self.PlayerPower < 3:
             for player in gfw.world.objects_at(gfw.layer.CPlayer):
                player.Power += 1
                Pp=CEffect.Effect(self.x, self.y, 144, 100, 80, 50, 8, 2)
                
                gfw.world.add(gfw.layer.CEffect,Pp)
                

            self.remove()

        self.Move_Item()
        self.Frame=(self.Frame+gfw.delta_time*9) %6
    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        self.image.clip_draw(int(self.Frame)*25, 0, 25, 18, self.x, self.y, 50, 30)
