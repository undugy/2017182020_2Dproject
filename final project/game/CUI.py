from pico2d import *
import main_state
import gfw
import CPlayer
import math




class Lager_Energy:
    image = None
    image2 = None
    def __init__(self):
        pass
    def __init__(self, x, y):
        self.x,self.y=x,y
        if Lager_Energy.image is None:
            Lager_Energy.image = load_image('Resource/Energy_bar.png')
        if Lager_Energy.image2 is None:
            Lager_Energy.image2 = load_image('Resource/Energy.png')

    def update(self):
        pass

    def draw(self):
      for player in gfw.world.objects_at(gfw.layer.CPlayer): 
        self.image.draw(self.x,self.y,340,28)
        self.image2.clip_draw(0, 0, 304, 28, self.x-152 +player.Gage*1.52 , self.y,player.Gage* 3.04, 14)
        pass


class Player_Bomb:
    image = None
    def __init__(self):
        if Player_Bomb.image is None:
            Player_Bomb.image = load_image('Resource/Item_Bomb2.png')

    def update(self):
        pass

    def draw(self):
      for player in gfw.world.objects_at(gfw.layer.CPlayer): 
        for n in range(player.BombNumber):
            self.image.draw(690,10+20*n,30,20)
        pass


class Life:
    image= None
    def __init__(self):
        if Life.image is None:
                Life.image = load_image('Resource/Life.png')
    def update(self):
        pass

    def draw(self):
     for player in gfw.world.objects_at(gfw.layer.CPlayer):
        for n in range(player.Life):
            self.image.draw(660, 10 + 20 * n, 30, 40)
        pass

class Score:
    image= [None,None,None,None,None]
    def __init__(self):
        if Score.image[0] is None:
            for i in range(5):
                Score.image[i]= load_image('Resource/Count.png')
        self.Score = 0
        self.PreScore =0
        self.Index =[0,0,0,0,0]

    def Add_Score(self,x):
        self.Score += x
    def Notify(self):
        self.Index[0] = self.Score / 10000
        self.Index[1] = (self.Score % 10000) / 1000
        self.Index[2] = (self.Score % 1000) / 100
        self.Index[3] = (self.Score % 100) / 10
        self.Index[4] = self.Score % 10
        print(self.Index[2])
    def update(self):

        if self.PreScore != self.Score:
            self.Notify()

        self.PreScore = self.Score
        pass

    def draw(self):

        for i in range(5):
            self.image[i].clip_draw(int(self.Index[i])*60,0, 60,78, 100+i*10, 940,13,30)
        pass



class FinalScore:
    image = None
    image2 = [None, None, None, None, None]

    def __init__(self):
        self.Index = [0, 0, 0, 0, 0]
         
        if FinalScore.image2[0] is None:
            for i in range(5):
                FinalScore.image2[i] = load_image('Resource/Count.png')
        self.x,self.y=720/2,650
        if FinalScore.image is None:
                FinalScore.image = load_image('Resource/Score.png')
        for score in gfw.world.objects_at(gfw.layer.CUI):
         self.Index[0] = score / 10000
         self.Index[1] = (score % 10000) / 1000
         self.Index[2] = (score% 1000) / 100
         self.Index[3] = (score% 100) / 10
         self.Index[4] =score % 10
    def update(self):
        pass
    def draw(self):

        self.image.draw(self.x,self.y,720,350)
        for i in range(5):
            self.image2[i].clip_draw(int(self.Index[i]) * 60, 0, 60, 78, 500 + i * 30, 570, 20, 40)

