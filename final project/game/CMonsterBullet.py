from pico2d import *


import gfw
import CPlayer

import random
import math



class PlaneBullet:
    image = None

    def __init__(self):
        pass

    def __init__(self, x, y, index, speed=500):
        self.index = index
        self.speed = speed
        self.x, self.y = x, y
        self.Radius = 7.5
        self.isDead = False
        self.Frame = 0
        if PlaneBullet.image == None:
            PlaneBullet.image = load_image('Resource/PlaneBullet.png')

    def update(self):
        self.y -= self.speed * gfw.delta_time
        self.Frame = (self.Frame + 1) % 8
        if self.isDead == True or self.y <= 0 or self.x < 0 or self.x > 720:
           self.remove()
    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        self.image.clip_draw(8 * self.Frame, 0, 8, 10, self.x, self.y, 15, 15)


class PlaneBullet2:
    image = None

    def __init__(self):
        pass

    def __init__(self, x, y,index, DeltaX, speed=500):
        self.speed = speed
        self.x, self.y = x, y
        self.DeltaX = DeltaX
        self.Radius = 10
        self.index = index
        self.isDead = False
        self.Frame = 0
        if PlaneBullet2.image == None:
            PlaneBullet2.image = load_image('Resource/Bullet.png')

    def update(self):
        self.x += self.DeltaX * gfw.delta_time
        self.y -= self.speed * gfw.delta_time
        self.Frame = (self.Frame + 1) % 2
        if self.isDead == True or self.y <= 0 or self.x < 0 or self.x > 720:
            self.remove()
    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        self.image.clip_draw(23 * self.Frame, 0, 23, 41, self.x, self.y, 20, 30)


class PlaneBullet3:
    image = None

    def __init__(self):
        pass

    def __init__(self, x, y, DeltaX, index, speed=500):
        self.index = index
        self.speed = speed
        self.x, self.y = x, y
        self.DeltaX = DeltaX
        self.Radius = 7.5
        self.isDead = False
        self.Frame = 0
        if PlaneBullet3.image is None:
            PlaneBullet3.image = load_image('Resource/PlaneBullet.png')

    def update(self):
        self.x += self.DeltaX * gfw.delta_time
        self.y -= self.speed * gfw.delta_time
        self.Frame = (self.Frame + 1) % 8
        if self.isDead is True or self.y <= 0 or self.x < 0 or self.x > 720:
          self.remove()
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(8 * self.Frame, 0, 8, 10, self.x, self.y, 15, 15)


class Monster1_Bullet:
    image = None

    def __init__(self):
        pass

    def __init__(self, x, y, index, speed=500):
        self.index = index
        self.speed = speed
        self.x, self.y = x, y
        self.Radius = 7.5
        self.isDead = False
        self.Frame = 0
        self.random_Delta= random.randint(60,100)/100
        if Monster1_Bullet.image is None:
            Monster1_Bullet.image = load_image('Resource/PlaneBullet.png')
        for player in gfw.world.objects_at(gfw.layer.CPlayer):
         self.DeltaX=x-player.x
         self.DeltaY=y-player.y
    def update(self):
        #for player in gfw.world.objects_at(gfw.layer.CPlayer):
         #self.DeltaX=x-player.x
         #self.DeltaY=y-player.y
        self.x -= self.DeltaX * gfw.delta_time *self.random_Delta
        self.y -= self.DeltaY * gfw.delta_time *self.random_Delta
        self.Frame = (self.Frame + 1) % 8
        if self.isDead == True or self.y <= 0 or self.x < 0 or self.x > 720:
                self.remove()
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(8 * self.Frame, 0, 8, 10, self.x, self.y, 15, 15)

