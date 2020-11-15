from pico2d import *

import main_state
import gfw
import CPlayer




class Effect():
    image = [None, None, None, None,None,None,None,None,None]

    def __init__(self):
        pass

    def __init__(self, x, y, ImageX, ImageY, SizeX, SizeY, MaxFrame, Index,Speed=1):
        self.x, self.y = x, y
        self.Speed=Speed
        self.Radius=7.5
        self.ImageX, self.ImageY, self.SizeX, self.SizeY, self.MaxFrame = ImageX, ImageY, SizeX, SizeY, MaxFrame
        self.ImageIndex = Index
        self.CurFrame = 0
        self.isDead = False
        if Effect.image[0] is None:
            Effect.image[0] = load_image('Resource/Effect_1.png')
        if Effect.image[1] is None:
            Effect.image[1] = load_image('Resource/ExploS.png')
        if Effect.image[2] is None:
            Effect.image[2] = load_image('Resource/PowerUp.png')
        if Effect.image[3] is None:
            Effect.image[3] = load_image('Resource/BombUp.png')
        if Effect.image[4] is None:
            Effect.image[4] = load_image('Resource/ExploS2.png')
        if Effect.image[5] is None:
            Effect.image[5] = load_image('Resource/Player_Expol.png')
        if Effect.image[6] is None:
            Effect.image[6] = load_image('Resource/ExploL.png')
        if Effect.image[7] is None:
            Effect.image[7] = load_image('Resource/Scarab_Expol.png')
        if Effect.image[8] is None:
            Effect.image[8] = load_image('Resource/Boss_Expol.png')
    def update(self):
        self.CurFrame = (self.CurFrame + gfw.delta_time * self.MaxFrame *self.Speed)
        if self.CurFrame >= self.MaxFrame:
            self.CurFrame = 0
            self.remove()
    def remove(self):
        gfw.world.remove(self)
    def draw(self):
        self.image[self.ImageIndex].clip_draw(int(self.CurFrame) * self.ImageX, 0, self.ImageX, self.ImageY, self.x,
                                              self.y, self.SizeX, self.SizeY)

