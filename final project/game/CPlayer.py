from pico2d import *
import gfw
import win32api
from gobj import *
import CBullet 
class Player():
    def __init__(self):
        self.x, self.y = 0, 90
        self.image = load_image('Resource/Player_T.png')
        self.Frame=3##speed
        self.Time=0
        self.Interval=0
        self.PlayerState=0
       
    
 
        
    def fire(self):
        
        if win32api.GetAsyncKeyState(0x20) & 0x8000 and self.Interval>=1:  # space
            self.Interval=0
            bullet=CBullet.Bullet(self.x,self.y+20)
            gfw.world.add(gfw.layer.CBullet,bullet)
        pass       
    def update(self):
        self.fire()
        self.Interval += (20 * gfw.delta_time)
        self.x = clamp(40, self.x, 700)
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
