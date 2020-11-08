from pico2d import *
import gfw
import CEffect


class Hyperion_Bullet():
    image = None
    def __init__(self):
        pass
    def __init__(self, x, y,Dir):
        self.x, self.y = x, y
        self.Dir=Dir
        self.isDead = False
        if Hyperion_Bullet.image== None:
            Hyperion_Bullet.image = load_image('Resource/Special_Bullet.png')


    def update(self):
        if self.Dir==0:
            self.y += gfw.delta_time*720
        elif self.Dir==1:
           self.x-= gfw.delta_time*720
           self.y+= gfw.delta_time*720
        elif self.Dir == 2:
           self.x+= gfw.delta_time*720
           self.y+= gfw.delta_time*720

        if self.x<0 or self.x>720 or self.y > 960:
            self.remove()
        if self.isDead == True:
            self.remove()
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(self.Dir * 42, 0, 40, 48, self.x, self.y, 50, 50)