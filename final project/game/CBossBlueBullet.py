from pico2d import *

import gfw
import CPlayer
import CBlueBullet
import CEffect
import random
import math
import SoundManagement

class Blue_Bullet:
    image = None

    def __init__(self):
        pass
    def __init__(self, x, y):

        self.x, self.y = x, y
        self.Radius = 25
        self.isDead = False
        self.Frame = 0
        self.LifeTime=random.randint(100,300) /100
        self.DeathTime=0
        self.index = 0
        self.Sound=SoundManagement
        self.Number=0
        self.RandomSpeed_Delta= random.randint(30,50) /100
        if Blue_Bullet.image is None:
            Blue_Bullet.image = load_image('Resource/Blue_Bullet2.png')
        for player in gfw.world.objects_at(gfw.layer.CPlayer):
         self.DeltaX = self.x-player.x
         self.DeltaY = self.y-player.y

    def Bullet_LifeTime(self):
        self.DeathTime +=gfw.delta_time
        if self.DeathTime > self.LifeTime:
            self.isDead= True
    def update(self):
        self.Bullet_LifeTime()

        self.x -= self.DeltaX * gfw.delta_time *self.RandomSpeed_Delta
        self.y -= self.DeltaY * gfw.delta_time *self.RandomSpeed_Delta
        self.Frame += gfw.delta_time *15

        if self.Frame >= 15:
            self.Frame = 0
        if self.isDead is True:
            Bf1=CEffect.Effect(self.x, self.y,80, 80, 100, 100, 10, 7, 0.5)
            gfw.world.add(gfw.layer.CEffect,Bf1)
            self.Sound.PlaySound(12,40)
            BBB = CBlueBullet.Blue_Bullet2(self.x, self.y, self.Number-1, 0, 100)
            gfw.world.add(gfw.layer.CMonsterBullet,BBB)
            BBB1 = CBlueBullet.Blue_Bullet2(self.x, self.y,  self.Number-1, 50 * math.sqrt(2), 50 * math.sqrt(2))
            gfw.world.add(gfw.layer.CMonsterBullet,BBB1)
            BBB2 = CBlueBullet.Blue_Bullet2(self.x, self.y,  self.Number-1, 100, 0)
            gfw.world.add(gfw.layer.CMonsterBullet,BBB2)
            BBB3 = CBlueBullet.Blue_Bullet2(self.x, self.y,  self.Number-1, 50 * math.sqrt(2), -50 * math.sqrt(2))
            gfw.world.add(gfw.layer.CMonsterBullet,BBB3)
            BBB4 = CBlueBullet.Blue_Bullet2(self.x, self.y, self.Number-1, 0, -100)
            gfw.world.add(gfw.layer.CMonsterBullet,BBB4)
            BBB5 = CBlueBullet.Blue_Bullet2(self.x, self.y,  self.Number-1, -50 * math.sqrt(2), -50 * math.sqrt(2))
            gfw.world.add(gfw.layer.CMonsterBullet,BBB5)
            BBB6 = CBlueBullet.Blue_Bullet2(self.x, self.y,  self.Number-1, -100, 0)
            gfw.world.add(gfw.layer.CMonsterBullet,BBB6)
            BBB7 = CBlueBullet.Blue_Bullet2(self.x, self.y,  self.Number-1, -50 * math.sqrt(2), 50 * math.sqrt(2))
            gfw.world.add(gfw.layer.CMonsterBullet,BBB7)
            self.remove()

    def remove(self):
        gfw.world.remove(self)      

    def draw(self):
        self.image.clip_draw(450 * int(self.Frame), 0, 450, 450, self.x, self.y, 50, 50)


