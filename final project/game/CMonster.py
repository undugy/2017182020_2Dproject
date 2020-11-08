from pico2d import *
import CMonsterBullet
import math
import random
import CEffect
import gfw
import main_state
import gobj
import CUI
class LeftPlane1():
    image = None

    def __init__(self):
        pass

    def __init__(self, x, y):
        self.Hp = 5
        self.x, self.y = x, y
        self.RadianX, self.PivotY = 40, 10
        self.Frame = 0
        self.BulletTerm = 0
        self.Dist = 0
        self.isDead = False
        if LeftPlane1.image is None:
            LeftPlane1.image = load_image('Resource/Monster_6_left.png')

    def update(self):
        if self.isDead or self.Hp<=0:
            #for score in gfw.world.objects_at(gfw.layer.CUI):
             CUI.Score().Add_Score(random.randint(100, 150))
             Ef1=CEffect.Effect(self.x + random.randint(-20, 20),self.y + random.randint(-20, 20),128, 128, 200, 200, 9, 1)
             gfw.world.add(gfw.layer.CEffect,Ef1)
             self.remove()
        self.BulletTerm = ( self.BulletTerm + gfw.delta_time * 3 ) %3
        if self.BulletTerm > 2.5:
            self.BulletTerm = 0
            Lb=CMonsterBullet.PlaneBullet(self.x, self.y, 0)
            gfw.world.add(gfw.layer.CMonsterBullet,Lb)

        if self.y < 750:
            self.x -=  100*gfw.delta_time
            self.Frame = 1
            if self.x < -30:
                self.remove()
        self.y -= 100*gfw.delta_time
    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        self.image.clip_draw(self.Frame * 42, 0, 42, 34, self.x, self.y, 80, 80)
class RightPlane1():
    image = None

    def __init__(self):
        pass

    def __init__(self, x, y):
        self.Hp = 5
        self.x, self.y = x, y
        self.RadianX, self.PivotY = 40, 10
        self.Frame = 0
        self.Dist = 0
        self.isDead = False
        self.BulletTerm = 0

        if RightPlane1.image == None:
            RightPlane1.image = load_image('Resource/Monster_6_right.png')

    def update(self):
        if self.isDead or self.Hp<=0:
            #for score in gfw.world.objects_at(gfw.layer.CUI):
             CUI.Score().Add_Score(random.randint(100, 150))
             Ef2=CEffect.Effect(self.x + random.randint(-20, 20),self.y + random.randint(-20, 20),128, 128, 200, 200, 9, 1)
             gfw.world.add(gfw.layer.CEffect,Ef2)
             self.remove()

        self.BulletTerm = (self.BulletTerm + gfw.delta_time * 3) % 3
        if self.BulletTerm > 2.5:
            self.BulletTerm = 0
            Rb=CMonsterBullet.PlaneBullet(self.x, self.y, 0)
            gfw.world.add(gfw.layer.CMonsterBullet,Rb)

        if (self.y < 750):
            self.x += 100*gfw.delta_time
            self.Frame = 1
            if (self.x < -30):
                self.remove()
        self.y -= 100*gfw.delta_time
    def remove(self):
            gfw.world.remove(self)

    def draw(self):
        self.image.clip_draw(self.Frame * 42, 0, 42, 34, self.x, self.y, 80, 80)
        

