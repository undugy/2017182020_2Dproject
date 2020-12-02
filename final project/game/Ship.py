from pico2d import *

import math


import gfw
import random
import CEffect
import CMonsterBullet
import CBullet
import Posin
import CUI
import SoundManagement
deadyet=False
checkDead=False
class BossShip:
    image = None
    image2 = None
    image3 = None
    def __init__(self):
        pass

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.Frame = 0
        self.Dist = 0
        self.isDead = False
        self.Sound=SoundManagement

        self.DeathCnt=0
        self.EffectTerm=0
        self.DeathSizeX = 0
        self.DeathSizeY = 0
        self.bisOpen = False
        self.LateInit=False
        
        self.MoveSpeed= 100
        if BossShip.image== None:
            BossShip.image = load_image('Resource/Ship.png')
        if BossShip.image2 == None:
            BossShip.image2 = load_image('Resource/Ship2.png')
        if BossShip.image3 == None:
            BossShip.image3 = load_image('Resource/gameclear.png')
        self.BigPosin1 = Posin.BigPosin(self.x-360,self.y)
        gfw.world.add(gfw.layer.CMonster,self.BigPosin1)
        self.BigPosin2 = Posin.BigPosin(self.x-248, self.y)
        gfw.world.add(gfw.layer.CMonster,self.BigPosin2)
        self.BigPosin3 = Posin.BigPosin(self.x +336, self.y)
        gfw.world.add(gfw.layer.CMonster,self.BigPosin3)
        self.BigPosinLst = [ self.BigPosin1, self.BigPosin2, self.BigPosin3]
    
        self.MiddlePosin1 = Posin.MiddlePosin(self.x - 72.5, self.y-20)
        gfw.world.add(gfw.layer.CMonster,self.MiddlePosin1)
        self.MiddlePosin2 = Posin.MiddlePosin(self.x - 72.5, self.y+54)
        gfw.world.add(gfw.layer.CMonster,self.MiddlePosin2)
        self.MiddlePosin3 = Posin.MiddlePosin(self.x + 167.5, self.y-20)
        gfw.world.add(gfw.layer.CMonster,self.MiddlePosin3)
        self.MiddlePosin4 = Posin.MiddlePosin(self.x + 167.5, self.y+54)
        gfw.world.add(gfw.layer.CMonster,self.MiddlePosin4)
        self.MiddlePosinLst = [self.MiddlePosin1,self.MiddlePosin2,self.MiddlePosin3,self.MiddlePosin4]
        
        self.SmallPosin1 = Posin.SmallPosin(self.x +20, self.y + 84)
        gfw.world.add(gfw.layer.CMonster,self.SmallPosin1)
        self.SmallPosin2 = Posin.SmallPosin(self.x +20, self.y - 62)
        gfw.world.add(gfw.layer.CMonster,self.SmallPosin2)
        self.SmallPosin3 = Posin.SmallPosin(self.x + 75.5, self.y + 84)
        gfw.world.add(gfw.layer.CMonster,self.SmallPosin3)
        self.SmallPosin4 = Posin.SmallPosin(self.x + 75.5,self.y - 62)
        gfw.world.add(gfw.layer.CMonster,self.SmallPosin4)
        self.SmallPosin5 = Posin.SmallPosin(self.x -200, self.y + 74)
        gfw.world.add(gfw.layer.CMonster,self.SmallPosin5)
        self.SmallPosin6 = Posin.SmallPosin(self.x -200, self.y - 52)
        gfw.world.add(gfw.layer.CMonster,self.SmallPosin6)
        self.SmallPosinLst = [self.SmallPosin1, self.SmallPosin2, self.SmallPosin3, self.SmallPosin4, self.SmallPosin5, self.SmallPosin6]
        
    def InitMove(self):
        if self.x > 390:
            for Posin in self.BigPosinLst:
                Posin.x -= gfw.delta_time * self.MoveSpeed
            for Posin in self.MiddlePosinLst:
                Posin.x -= gfw.delta_time * self.MoveSpeed
            for Posin in self.SmallPosinLst:
                Posin.x -= gfw.delta_time * self.MoveSpeed
         
            self.x -= gfw.delta_time * self.MoveSpeed
          
        else:
            if self.bisOpen is False:
                self.bisOpen =True
                for BigPosin in self.BigPosinLst:
                   BigPosin.bisOpen=True
       
        pass

    def BossDead(self):
        global checkDead,deadyet
        
         
        if self.DeathCnt >=13 :
            self.DeathSizeX += gfw.delta_time * (137.5/2)
            self.DeathSizeY += (gfw.delta_time * 10)
            self.EffectTerm +=gfw.delta_time
            if self.EffectTerm > 0.1 and self.DeathSizeX< 600:
                self.Sound.PlaySound(random.randint(3, 7),50)
                self.EffectTerm = 0
                DbEf=CEffect.Effect(self.x + random.randint(int(-700+self.DeathSizeX),int(700-self.DeathSizeX)),
                    self.y + random.randint(int(-100+self.DeathSizeY), int(100-self.DeathSizeY)), 149, 149,
                    250, 250, 32, 8, 0.3)
                gfw.world.add(gfw.layer.CEffect,DbEf)
                deadyet=True
        if self.LateInit is False and self.DeathSizeX>600:
            
            self.LateInit = True
            checkDead=True
            
    def update(self):
        
        self.BossDead()
        self.InitMove()
        if self.isDead:
            Bcef=CEffect.Effect(self.x + random.randint(-20, 20),
                self.y + random.randint(-20, 20),128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.CEffect,Bcef)
            
            self.remove()
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        if self.DeathCnt<13:
            self.image.draw(self.x, self.y, 1375, 200)
        else :
            self.image2.draw(self.x, self.y, 1375-self.DeathSizeX, 200-self.DeathSizeY)
            self.image3.draw(360,480,300,300)

