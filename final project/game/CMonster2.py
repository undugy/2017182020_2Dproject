from pico2d import *

import math
import main_state
import gfw
import CItem
import random
import CEffect
import CMonsterBullet
import CBullet
import CUI

class BlueAirPlane:
    image = None

    def __init__(self):
        pass

    def __init__(self, x, y):
        self.Hp = 1
        self.x, self.y = x, y
        self.RadianX, self.PivotY = 40, 10
        self.FirstX, self.FirstY = x, y
        self.SecondX, self.SecondY = x + 200, y - 1000
        self.ThirdX, self.ThirdY = x + 400, y + 200
        self.Frame = 0
        self.t = 0
        self.isDead = False
        self.Initialize = False

        if BlueAirPlane.image is None:
            BlueAirPlane.image = load_image('Resource/Monster_1.png')

    def update(self):
        if self.isDead or self.Hp <= 0:
            CUI.Score().Add_Score(random.randint(70,100))
            Ef3=CEffect.Effect(self.x + random.randint(-20, 20),
            	self.y + random.randint(-20, 20),128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.CEffect,Ef3)
            self.remove()
        if self.Initialize is False and self.t > 0.5:
            self.Initialize = True
            Bb=CMonsterBullet.Monster1_Bullet(self.x, self.y, 0)
            gfw.world.add(gfw.layer.CMonsterBullet,Bb)

        if self.t > 1:
            self.remove()
    
        self.Frame = (self.Frame + gfw.delta_time * 11) % 11
        self.t += gfw.delta_time * 0.3
        self.x = (1 - self.t) ** 2 * self.FirstX + 2 * self.t * (1 - self.t) * self.SecondX + self.t ** 2 * self.ThirdX
        self.y = (1 - self.t) ** 2 * self.FirstY + 2 * self.t * (1 - self.t) * self.SecondY + self.t ** 2 * self.ThirdY
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(int(self.Frame) * 32, 0, 32, 36, self.x, self.y, 80, 80)


class RedAirPlane:
    image = None

    def __init__(self):
        pass

    def __init__(self, x, y):
        self.Hp = 1
        self.x, self.y = x, y
        self.RadianX, self.PivotY = 40, 10
        self.isDead = False
        self.FirstX, self.FirstY = x, y
        self.SecondX, self.SecondY = x + 200, y - 1000
        self.ThirdX, self.ThirdY = x + 400, y + 200
        self.Frame = 0
        self.t = 0
        self.Initialize = False
        if RedAirPlane.image is None:
            RedAirPlane.image = load_image('Resource/Monster_2.png')

    def update(self):
        if self.isDead or self.Hp <= 0:
            CUI.Score().Add_Score(random.randint(200, 300))
            Ef4=CEffect.Effect(self.x + random.randint(-20, 20),
            	self.y + random.randint(-20, 20),128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.CEffect,Ef4)
            RItem=CItem.Power_item(self.x, self.y)
            gfw.world.add(gfw.layer.CItem,RItem)
            self.remove()
        if self.Initialize is False and self.t > 0.5:
            self.Initialize = True
            Rb=CMonsterBullet.Monster1_Bullet(self.x, self.y, 0)
            gfw.world.add(gfw.layer.CMonsterBullet,Rb)
        if self.t > 1:
            self.remove()
        self.Frame = (self.Frame + gfw.delta_time * 11) % 11
        self.t += gfw.delta_time * 0.3
        self.x = (1 - self.t) ** 2 * self.FirstX + 2 * self.t * (1 - self.t) * self.SecondX + self.t ** 2 * self.ThirdX
        self.y = (1 - self.t) ** 2 * self.FirstY + 2 * self.t * (1 - self.t) * self.SecondY + self.t ** 2 * self.ThirdY
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(int(self.Frame) * 32, 0, 32, 36, self.x, self.y, 80, 80)


class WhiteAirPlane:
    image = None
    DeltaX=0
    DeltaY=0
    def __init__(self):
        pass

    def __init__(self, x, y):
        self.Hp = 1
        self.x, self.y = x, y
        self.RadianX, self.PivotY = 40, 10
        self.isDead = False
        #self.DeltaX, self.DeltaY = main_state.ListManager.Get_Player().x - x, main_state.ListManager.Get_Player().y - y
        self.Frame = 0
        self.t = 0
        for player in gfw.world.objects_at(gfw.layer.CPlayer):
         self.DeltaX=player.x-x
         self.DeltaY=player.y-y
        if WhiteAirPlane.image is None:
            WhiteAirPlane.image = load_image('Resource/Monster_3.png')
        
    def update(self):
        if self.isDead or self.Hp <= 0:
            CUI.Score().Add_Score(random.randint(200, 300))
            Ef5=CEffect.Effect(self.x + random.randint(-20, 20),
            	self.y + random.randint(-20, 20),128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.CEffect,Ef5)
            
            self.remove()
        if self.t > 1:
            self.remove()
        self.Frame = (self.Frame + gfw.delta_time * 11) % 11
        
        self.x += self.DeltaX * gfw.delta_time * 0.7
        self.y += self.DeltaY * gfw.delta_time * 0.7
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(int(self.Frame) * 40, 0, 40, 40, self.x, self.y, 80, 80)

class BigAirPlane:
    image = None

    def __init__(self):
        pass

    def __init__(self, x, y):
        self.Hp = 5000
        self.x, self.y = x, y
        self.RadianX, self.PivotY = 250, 20
        self.Dist = 0
        self.BulletTerm = 0
        self.BigBulletTerm = 0
        self.BulletPossibleTime = 0
        self.BigBulletPossibleTime = 0
        self.isDead = False
        if BigAirPlane.image is None:
            BigAirPlane.image = load_image('Resource/BigAirPlan.png')

    def update(self):
        if self.isDead or self.Hp <= 0:
            CUI.Score().Add_Score(random.randint(5000, 6000))
            Bf1=CEffect.Effect(self.x + random.randint(-20, 20),self.y + random.randint(-20, 20),
             252, 200, 600, 500, 14, 6,0.5)
            gfw.world.add(gfw.layer.CEffect,Bf1)
            bItem=CItem.Bomb_item(self.x, self.y)
            gfw.world.add(gfw.layer.CItem,bItem)
            main_state.bisMiddleBossDead = True
            self.remove()

        if self.y > 900:
            self.y -= 30*gfw.delta_time
        self.BigBulletPossibleTime += gfw.delta_time * 1
        self.BulletPossibleTime += gfw.delta_time * 1

        if self.BigBulletPossibleTime > 3:
            self.BigBulletPossibleTime = 0
        if self.BigBulletPossibleTime > 1.5:
            self.BigBulletTerm += gfw.delta_time * 1
            if self.BigBulletTerm > 0.03:
                self.BigBulletTerm = 0
                SMB=CMonsterBullet.PlaneBullet2(self.x, self.y - 150,2, random.randint(-360, 360),
                                              random.randint(500, 700))
                gfw.world.add(gfw.layer.CMonsterBullet,SMB)  
        if self.BulletPossibleTime > 1.5:
            self.BulletPossibleTime = 0
        if self.BulletPossibleTime > 1:
            self.BulletTerm += gfw.delta_time * 1
            if self.BulletTerm > 0.1:
                self.BulletTerm = 0
                CMB=CMonsterBullet.Monster1_Bullet(self.x - 120, self.y - 50, 0)
                gfw.world.add(gfw.layer.CMonsterBullet,CMB)
                CMB2=CMonsterBullet.Monster1_Bullet(self.x + 120, self.y - 50, 0)
                gfw.world.add(gfw.layer.CMonsterBullet,CMB2)
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image.draw(self.x, self.y, 500, 400)


class MidAirPlane:
    image = None

    def __init__(self):
        pass

    def __init__(self, x, y,Dir):
        self.Hp = 250
        self.x, self.y = x, y
        self.Dir = Dir

        self.Frame = 0
        self.RadianX, self.PivotY = 100, 20
        self.Dist = 0
        self.BulletTerm = 0
        self.BulletPossibleTime = 0
        self.isDead = False
        if MidAirPlane.image is None:
            MidAirPlane.image = load_image('Resource/MidAirPlan.png')


    def InitMove(self):
        if self.Dir == -1 and self.x > 540:
            self.x -= gfw.delta_time *100
            pass
        elif self.Dir == 1 and self.x < 180:
            self.x += gfw.delta_time *100
    def update(self):
        self.InitMove()
        if self.isDead or self.Hp <= 0:
            CUI.Score().Add_Score(random.randint(1000, 1500))
            Maf=CEffect.Effect(self.x + random.randint(-20, 20),
                self.y + random.randint(-20, 20),128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.CEffect,Maf)
            self.remove()

        if self.y > 800:
            self.y -= 70 * gfw.delta_time

        self.BulletPossibleTime += gfw.delta_time

        self.Frame += gfw.delta_time * 5
        self.Frame = self.Frame % 2

        if self.BulletPossibleTime > 4:
            self.BulletPossibleTime = 0
        if self.BulletPossibleTime > 3:
            self.BulletTerm += gfw.delta_time * 1
            if self.BulletTerm > 0.1:
                self.BulletTerm = 0
                Mab=CMonsterBullet.PlaneBullet3(self.x - 100, self.y - 50, -100, 0, 300)
                gfw.world.add(gfw.layer.CMonsterBullet,Mab)

                Mab2=CMonsterBullet.PlaneBullet3(self.x, self.y - 50, 0, 0, 400)
                gfw.world.add(gfw.layer.CMonsterBullet,Mab2)

                Mab3=CMonsterBullet.PlaneBullet3(self.x + 100, self.y - 50, 100, 0, 300)
                gfw.world.add(gfw.layer.CMonsterBullet,Mab3)

    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(int(self.Frame) * 310, 0, 310, 335, self.x, self.y, 200, 200)
