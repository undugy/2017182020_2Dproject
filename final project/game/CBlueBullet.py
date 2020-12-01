from pico2d import *

import SoundManagement
import gfw

import CEffect
import random
import math


class Blue_Bullet2:
    image = None
    def __init__(self):
        pass
    def __init__(self, x, y,Number,DeltaX,DeltaY):
        self.Number=Number
        self.x, self.y = x, y
        self.DeltaX,self.DeltaY=DeltaX,DeltaY
        self.Radius = 10
        self.isDead = False
        self.Frame = 0
        self.Sound=SoundManagement
        self.LifeTime = random.randint(100,300) /100
        self.DeathTime = 0
        self.index= 0
        if Blue_Bullet2.image is None:
            Blue_Bullet2.image = load_image('Resource/Blue_Bullet2.png')

    def Bullet_LifeTime(self):
        if self.isDead is True or self.y <= 0 or self.x < 0 or self.x > 720:
            self.remove()

    def update(self):
        self.Bullet_LifeTime()

        self.x +=gfw.delta_time * self.DeltaX * 2
        self.y += gfw.delta_time * self.DeltaY * 2


        self.Frame += gfw.delta_time * 10
        if self.Frame >= 16:
            self.Frame =0
        if self.isDead is True or self.y <= 0 or self.x < -10 or self.x > 740:
            if self.Number > 0:
                self.Sound.PlaySound(12,40)
                bEf=CEffect.Effect(self.x, self.y,80, 80, 100, 100, 10, 7, 0.5)
                gfw.world.add(gfw.layer.CEffect,bEf)
                BB = Blue_Bullet2(self.x, self.y, self.Number-1, 0, 100)
                gfw.world.add(gfw.layer.CMonsterBullet,BB)
                BB1 = Blue_Bullet2(self.x, self.y,  self.Number-1, 50 * math.sqrt(2), 50 * math.sqrt(2))
                gfw.world.add(gfw.layer.CMonsterBullet,BB1)
                BB2 = Blue_Bullet2(self.x, self.y,  self.Number-1, 100, 0)
                gfw.world.add(gfw.layer.CMonsterBullet,BB2)
                BB3 = Blue_Bullet2(self.x, self.y,  self.Number-1, 50 * math.sqrt(2), -50 * math.sqrt(2))
                gfw.world.add(gfw.layer.CMonsterBullet,BB3)
                BB4 = Blue_Bullet2(self.x, self.y, self.Number-1, 0, -100)
                gfw.world.add(gfw.layer.CMonsterBullet,BB4)
                BB5 = Blue_Bullet2(self.x, self.y,  self.Number-1, -50 * math.sqrt(2), -50 * math.sqrt(2))
                gfw.world.add(gfw.layer.CMonsterBullet,BB5)
                BB6 = Blue_Bullet2(self.x, self.y,  self.Number-1, -100, 0)
                gfw.world.add(gfw.layer.CMonsterBullet,BB6)
                BB7 = Blue_Bullet2(self.x, self.y,  self.Number-1, -50 * math.sqrt(2), 50 * math.sqrt(2))
                gfw.world.add(gfw.layer.CMonsterBullet,BB7)
            self.remove()
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(450 * int(self.Frame), 0, 450, 450, self.x, self.y, 20, 20)
