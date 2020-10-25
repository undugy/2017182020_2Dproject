from pico2d import *
import CMonsterBullet
import math
import random

import gfw
import main_state
import gobj

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
      
        self.BulletTerm = ( self.BulletTerm + gfw.delta_time * 3 ) %3
        if self.BulletTerm > 2.5:
            self.BulletTerm = 0
            b=CMonsterBullet.PlaneBullet(self.x, self.y, 0)
            gfw.world.add(gfw.layer.CMonsterBullet,b)

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
        
        self.BulletTerm = (self.BulletTerm + gfw.delta_time * 3) % 3
        if self.BulletTerm > 2.5:
            self.BulletTerm = 0
            bc=CMonsterBullet.PlaneBullet(self.x, self.y, 0)
            gfw.world.add(gfw.layer.CMonsterBullet,bc)

        if (self.y < 750):
            self.x += 100*gfw.delta_time
            self.Frame = 1
            if (self.x < -30):
                return -1
        self.y -= 100*gfw.delta_time
    def remove(self):
            gfw.world.remove(self)

    def draw(self):
        self.image.clip_draw(self.Frame * 42, 0, 42, 34, self.x, self.y, 80, 80)

