from pico2d import *
import gfw
import win32api
from gobj import *
import CBullet
import CHyperion 
class Player():
    def __init__(self):
        self.x, self.y = 0, 90
        self.image = load_image('Resource/Player_T.png')
        self.Frame=3##speed
        self.Time=0
        self.Interval=0
        self.PlayerState=0
        self.Life = 5
        self.PreLife=self.Life
        self.Gage=0
        self.LagerTime=0
        self.Power=0#플레이어 파워
        self.BombNumber=2 #필살기개수
        self.SoundDelta=0
        self.IsShield=False
        self.ShieldTime=0

        self.SuperMode =False
    def Player_LifeSystem(self):
        #0x44 D
          if win32api.GetAsyncKeyState(0x44) & 0x1001:
             if self.SuperMode is True:
                self.SuperMode=False
             elif self.SuperMode is False:
                self.SuperMode=True

          if self.PreLife !=self.Life:
             self.IsShield=True
          self.PreLife=self.Life

          if self.IsShield is True:
            #self.Life-=1
            self.ShieldTime +=gfw.delta_time
            if self.ShieldTime > 3:
                self.ShieldTime=0
                self.IsShield=False
    def fire(self):
        
        if win32api.GetAsyncKeyState(0x20) & 0x8000 and self.Interval>=1:  # space
            self.Interval=0
            bullet=CBullet.Bullet(self.x,self.y+20)
            gfw.world.add(gfw.layer.CBullet,bullet)
    def Make_Hyperion(self):
        if  win32api.GetAsyncKeyState(0x53) & 0x1001 and self.BombNumber >= 1 :  # s:
            self.BombNumber -= 1
            Ch=CHyperion.Hyperion(360, 0)
            gfw.world.add(gfw.layer.CHyperion,Ch)
            Lh=CHyperion.Hyperion(200, -100)
            gfw.world.add(gfw.layer.CHyperion,Lh)
            Rh=CHyperion.Hyperion(520, -100)
            gfw.world.add(gfw.layer.CHyperion,Rh)
            
    def Make_Lager(self):
        if gfw.world.count_at(gfw.layer.CLazer) >0:
            self.LagerTime+=gfw.delta_time
        if win32api.GetAsyncKeyState(0x41) & 0x1001:
            if gfw.world.count_at(gfw.layer.CLazer) == 0 and self.Gage>20:# a
                LayL=CBullet.Player_Lager(25)
                gfw.world.add(gfw.layer.CLazer,LayL)
                LayR=CBullet.Player_Lager(-25)
                gfw.world.add(gfw.layer.CLazer,LayR)
                
            elif self.LagerTime> 3 and gfw.world.count_at(gfw.layer.CLazer) >0:
                self.LagerTime=0
                for Lager in gfw.world.objects_at(gfw.layer.CLazer):
                    Lager.isDead=True
        pass       
    def update(self):
        self.Player_LifeSystem()
        self.Make_Lager()
        self.Make_Hyperion()
        self.fire()
        self.Interval += (20 * gfw.delta_time)
        self.x = clamp(40, self.x, 700)
        self.Gage=clamp(0, self.Gage,100)
        self.y=clamp(40,self.y,900)
        if(win32api.GetAsyncKeyState(0x25) & 0x8000 or win32api.GetAsyncKeyState(0x26) & 0x8000
        or win32api.GetAsyncKeyState(0x27) & 0x8000 or win32api.GetAsyncKeyState(0x28) & 0x8000):
            if win32api.GetAsyncKeyState(0x25) & 0x8000:
                self.x-= 400 * gfw.delta_time
            if win32api.GetAsyncKeyState(0x27) & 0x8000:
                self.x += 400 * gfw.delta_time
            if win32api.GetAsyncKeyState(0x26) & 0x8000: # UP
                self.y +=400 * gfw.delta_time
            if win32api.GetAsyncKeyState(0x28) & 0x8000: #DOWN
                self.y -= 400 * gfw.delta_time
        else:
            PlayerState=0
        self.Time=(self.Time+1)%50
        if win32api.GetAsyncKeyState(0x25) & 0x8000 and self.Time>=48:
            self.Frame -= 1
        if win32api.GetAsyncKeyState(0x27) & 0x8000 and self.Time>=48:
            self.Frame += 1
            
        if self.Frame<=0:
            self.Frame=0
        if self.Frame>=6:
            self.Frame=6
    def draw(self):
        self.image.clip_draw(3*33, 0, 33, 33, self.x, self.y,80,80)
