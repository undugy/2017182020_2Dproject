from pico2d import *


import math

import gfw
import random
import CEffect
import CMonsterBullet
import CBullet
import CHyperionBullet


class Hyperion():
    image = None
    def __init__(self):
        pass
    def __init__(self,x,y):
        self.x,self.y=x,y
        self.Frame=0
        self.Dist=0
        self.t=0
        self.Dir=random.randint(0,1)
        self.DeltaY=0
        self.BulletTerm=0
        if Hyperion.image == None:
            Hyperion.image = load_image('Resource/Monster_4.png')

    def update(self):

        self.BulletTerm=(self.BulletTerm+gfw.delta_time*1)
        if self.BulletTerm>=0.15:
            self.BulletTerm =0
            Hbullet=CHyperionBullet.Hyperion_Bullet(self.x, self.y + 20, 0)
            gfw.world.add(gfw.layer.CBullet,Hbullet)
            Hbullet2=CHyperionBullet.Hyperion_Bullet(self.x + 100, self.y, 1)
            gfw.world.add(gfw.layer.CBullet,Hbullet2)
            Hbullet3=CHyperionBullet.Hyperion_Bullet(self.x - 100, self.y, 2)
            gfw.world.add(gfw.layer.CBullet,Hbullet3)
        for Mb in gfw.world.objects_at(gfw.layer.CMonsterBullet):
            if (self.x - 120 < Mb.x < self.x + 120) and  (self.y - 60 < Mb.y < self.y + 60):
                Mb.isDead=True
                
                if Mb.index == 2:
                    He=CEffect.Effect(Mb.x,Mb.y,128,128,60,60,8,4)
                    gfw.world.add(gfw.layer.CEffect,He)
                    
                 



        if self.DeltaY<300:
            self.y+= gfw.delta_time * 100
            self.DeltaY +=gfw.delta_time * 100

        elif self.DeltaY >= 300 and self.DeltaY < 500:
            self.DeltaY+=gfw.delta_time * 50
            if self.Dir==0:
                self.y +=gfw.delta_time * 50
                self.x -= gfw.delta_time * 50
            elif self.Dir==1:
                self.y +=gfw.delta_time * 50
                self.x +=gfw.delta_time * 50
        elif self.DeltaY>=500:
            if self.Dir==0:
                self.y +=gfw.delta_time * 300
                self.x -= gfw.delta_time * 150
            elif self.Dir==1:
                self.y += gfw.delta_time * 300
                self.x += gfw.delta_time * 150






        if self.x<-60 or self.x>780:
            self.remove()
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(self.Frame*240, 0, 240, 120, self.x, self.y,240,120)


