from pico2d import *

import math


import CUI
import gfw
import random
import CEffect
import CMonsterBullet
import CBullet
import CBossBlueBullet


class BigPosin:
    image = None

    def __init__(self):
        pass

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.Frame = 0
        self.Dist = 0
        self.isDead = False
        self.Hp = 1000
        self.RadianX, self.PivotY = 50, 50
        self.bisOpen = False
        self.BulletMakeTerm = 0
        self.RandomDelta=random.randint(40,90)/100
        if BigPosin.image == None:
            BigPosin.image = load_image('Resource/BigPosin.png')

    def Frame_Manegement(self):
        if self.bisOpen is True:
            self.Frame+= 10 *gfw.delta_time
            if self.Frame > 32:
                self.Frame = 24


    def Bullet_Make(self):
        self.BulletMakeTerm+=gfw.delta_time *self.RandomDelta
        if self.BulletMakeTerm > 5 :
            self.RandomDelta = random.randint(60, 90) / 100
            self.BulletMakeTerm = 0
            Bm=CBossBlueBullet.Blue_Bullet(self.x, self.y)
            gfw.world.add(gfw.layer.CMonsterBullet,Bm)
    def update(self):

        self.Frame_Manegement()
        self.Bullet_Make()
        if self.isDead or self.Hp< 0:
            CUI.Score().Add_Score(random.randint(1500, 2000))
            pEf=CEffect.Effect(self.x + random.randint(-20, 20),self.y + random.randint(-20, 20),128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.CEffect,pEf)
            for boss in gfw.world.objects_at(gfw.layer.Boss):
             boss.DeathCnt+=1
            self.remove()
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(int(self.Frame) * 60, 0, 60, 60, self.x, self.y,100,100)



class MiddlePosin:
    image = None

    def __init__(self):
        pass

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.Frame = 0
        self.Dist = 0
        self.isDead = False
        self.Hp = 350
        self.RadianX, self.PivotY = 25, 25

        self.Time =0
        self.BulletTime = 3
        self.BulletPossibleTime = 0
        self.MakeBulletTerm = 0
        self.bisBulletPossible = False
        if MiddlePosin.image is None:
            MiddlePosin.image = load_image('Resource/Boat_Posin.png')
        
    def MakeBullet(self):
        self.Time += gfw.delta_time
        if self.Time > self.BulletTime and self.bisBulletPossible is False:  # 불렛텀보다 커지면
            self.BulletPossibleTime = random.randint(2,4)
            self.bisBulletPossible =True
            self.Time =0
        if  self.bisBulletPossible is True:
            self.MakeBulletTerm += gfw.delta_time
            if self.MakeBulletTerm > 0.5:
                self.MakeBulletTerm=0
                speed= random.randint(40, 70) /100
                Mbb1=CMonsterBullet.Monster1_Bullet(self.x-7, self.y, 0,speed)
                gfw.world.add(gfw.layer.CMonsterBullet,Mbb1)
                Mbb2=CMonsterBullet.Monster1_Bullet(self.x+7, self.y, 0, speed)
                gfw.world.add(gfw.layer.CMonsterBullet,Mbb2)
                if self.BulletPossibleTime< self.Time:
                    self.Time = 0
                    self.bisBulletPossible = False
                    self.BulletTime=random.randint(2, 4)
    def Dir_Calculate(self):
        for player in gfw.world.objects_at(gfw.layer.CPlayer): 
         X = player.x - self.x
         Y = self.y - player.y
        Cter = math.atan2(X, -Y)
        NewCter = Cter * (180/3.14)
        if NewCter < 0 :
            NewCter = 180 + (180+NewCter)

        self.Frame = NewCter / 11.25
        pass

    def update(self):
        self.MakeBullet()
        self.Dir_Calculate()
        if self.isDead or self.Hp< 0:
            CUI.Score().Add_Score(random.randint(1500, 2000))
            pEf2=CEffect.Effect(self.x + random.randint(-20, 20),
             self.y + random.randint(-20, 20),128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.CEffect,pEf2)
            
            for boss in gfw.world.objects_at(gfw.layer.Boss):
             boss.DeathCnt+=1
            self.remove()
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(int(self.Frame) * 30, 0, 30, 30, self.x, self.y,50,50)



class SmallPosin:
    image = None

    def __init__(self):
        pass

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.Frame = 0
        self.Dist = 0
        self.isDead = False
        self.Hp = 250
        self.RadianX, self.PivotY = 30, 20
        self.BulletTime = 0
        self.MakeBulletTerm = random.randint(20,40) / 10
        if SmallPosin.image is None:
            SmallPosin.image = load_image('Resource/Boat_Posin2.png')
    def Dir_Calculate(self):
        for player in gfw.world.objects_at(gfw.layer.CPlayer): 
         X = player.x - self.x
         Y = self.y - player.y
        Cter = math.atan2(X, -Y)
        NewCter = Cter * (180/3.14)
        if NewCter < 0 :
            NewCter = 180 + (180+NewCter)
        self.Frame = NewCter / 11.25
        pass

    def MakeBullet(self):
        self.BulletTime+=gfw.delta_time
        if self.MakeBulletTerm < self.BulletTime:
            self.BulletTime = 0
            self.MakeBulletTerm = random.randint(20,40) / 10
            speed = random.randint(70, 100) / 100
            Spb=CMonsterBullet.Monster1_Bullet(self.x, self.y, 0,speed)
            gfw.world.add(gfw.layer.CMonsterBullet,Spb)
            pass
    def update(self):
        self.MakeBullet()
        self.Dir_Calculate()
        if self.isDead or self.Hp< 0:
            CUI.Score().Add_Score(random.randint(500, 1000))
            Sce=CEffect.Effect(self.x + random.randint(-20, 20),
             self.y + random.randint(-20, 20),128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.CMonsterBullet,Sce)
            for boss in gfw.world.objects_at(gfw.layer.Boss):
             boss.DeathCnt+=1
            self.remove()
    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        self.image.clip_draw(int(self.Frame) * 40, 0, 40, 30, self.x, self.y,60,40)
