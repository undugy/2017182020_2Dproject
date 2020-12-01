import gfw
from pico2d import *
import CPlayer 
import win32api
import gobj
import random
import CMonster
import CMonster2
import CUI
import CEffect
import CItem
import CHyperion
import Posin
import Ship
from background import VertScrollBackground
import title_state
import SoundManagement

Sound=None
def enter():
    gfw.world.init(['bg','CPlayer','Boss','CBullet','CMonster','CMonsterBullet',
        'CUI','CEffect','CItem','CLazer','CHyperion'])
    global player,score,Sound
    player=CPlayer.Player()
    Sound=SoundManagement
    Sound.init()
    Sound.bgm.repeat_play()
    gfw.world.add(gfw.layer.CPlayer,player)
    #gfw.world.add(gfw.layer.SoundManagement,Sound)
 
    score=CUI.Score() 
    life=CUI.Life()
    gfw.world.add(gfw.layer.CUI, score)
    gfw.world.add(gfw.layer.CUI, CUI.Lager_Energy(160,30))
    gfw.world.add(gfw.layer.CUI, CUI.Player_Bomb())
    gfw.world.add(gfw.layer.CUI, life)

    bg=VertScrollBackground('Map_2.png')
    bg.speed=50
    gfw.world.add(gfw.layer.bg,bg)

    global  MakeTerm, RedAirPlaneTerm,bisAirPlaneMake,SmallBoss_MakeTerm,SmallBossCnt,MiddleBossCnt,FinalBossCnt,bisMiddleBossDead
    global Time
    bisAirPlaneMake = True
    MakeTerm=0
    RedAirPlaneTerm =0
    SmallBoss_MakeTerm =0
    SmallBossCnt = 2
    MiddleBossCnt = 1
    FinalBossCnt = 1
    Time = 0
    bisMiddleBossDead = False



def MonsterBullet_Collision():
 global player,score,Sound
 for Monster in gfw.world.objects_at(gfw.layer.CMonster):    
  for MonsterBullet in gfw.world.objects_at(gfw.layer.CMonsterBullet):   
    for PlayerBullet in gfw.world.objects_at(gfw.layer.CBullet):
        if  Monster.x +Monster.RadianX > PlayerBullet.x > Monster.x-Monster.RadianX and Monster.y + Monster.PivotY >PlayerBullet.y > Monster.y - Monster.PivotY:
         PlayerBullet.isDead=True
         Monster.Hp -= 0.5 + player.Power * 0.75
         player.Gage += 0.5
         score.Add_Score(random.randint(3, 7))
         PlayerBullet.isDead = True
         
         Pp=CEffect.Effect(PlayerBullet.x + random.randint(-15, 15),
                      PlayerBullet.y + random.randint(-15, 15), 30, 27, 30, 27, 12,0)
         gfw.world.add(gfw.layer.CEffect,Pp)
         
def PlayerBullet_Collision():
    global player,Sound
    for Monster in gfw.world.objects_at(gfw.layer.CMonster):
     for MonsterBullet in gfw.world.objects_at(gfw.layer.CMonsterBullet):
        Dist = math.sqrt((player.x - MonsterBullet.x) ** 2 + (player.y - MonsterBullet.y) ** 2)
        if Dist <=MonsterBullet.Radius and player.IsShield is False:
            MonsterBullet.isDead = True
            Sound.PlaySound(14,40)   
            if player.SuperMode is False:
                player.IsShield=True
                player.Life-=1
                print(player.Life)
                
                Cp=CEffect.Effect(player.x + random.randint(-20, 20),
                    player.y + random.randint(-20, 20), 128, 128,
                                      250, 250, 64, 5,0.3)
                gfw.world.add(gfw.layer.CEffect,Cp)
               
def makeTime():
    
    global  MakeTerm, RedAirPlaneTerm,bisAirPlaneMake,SmallBoss_MakeTerm,SmallBossCnt,MiddleBossCnt,FinalBossCnt,bisMiddleBossDead
    global Time

    MakeTerm+=gfw.delta_time * 0.7
    RedAirPlaneTerm += gfw.delta_time * 0.3
    SmallBoss_MakeTerm += gfw.delta_time * 1
    Time +=gfw.delta_time * 1 
    if MakeTerm >=1 and bisAirPlaneMake is True:
        MakeTerm=0
        Lp=CMonster.LeftPlane1(random.randint(0, 720), 960)
        Rp=CMonster.RightPlane1(random.randint(0, 720), 960)
        gfw.world.add(gfw.layer.CMonster,Lp)
        gfw.world.add(gfw.layer.CMonster,Rp)
        Bp=CMonster2.BlueAirPlane(random.randint(0, 300), 960)
        Wp=CMonster2.WhiteAirPlane(1000, random.randint(500,960))
        gfw.world.add(gfw.layer.CMonster,Bp)
        gfw.world.add(gfw.layer.CMonster,Wp)
    if RedAirPlaneTerm >= 4 and FinalBossCnt>0:
        RedAirPlaneTerm=0
        Redp=CMonster2.RedAirPlane(random.randint(0, 300), 960)
        gfw.world.add(gfw.layer.CMonster,Redp)
            
    if SmallBoss_MakeTerm > 10 and SmallBossCnt > 0:
        SmallBoss_MakeTerm= 0
        SmallBossCnt -=1
        Sp1=CMonster2.MidAirPlane(1300, 1300, -1)
        Sp2=CMonster2.MidAirPlane(-580, 1300, 1)
        gfw.world.add(gfw.layer.CMonster,Sp1)
        gfw.world.add(gfw.layer.CMonster,Sp2)
    
    if Time > 40 and MiddleBossCnt > 0:
        MiddleBossCnt -=1
        BAP=CMonster2.BigAirPlane(360, 1160)
        gfw.world.add(gfw.layer.CMonster,BAP)
        


    if Time > 60 and CMonster2.checkDead == True and FinalBossCnt>0:
        FinalBossCnt-=1
        boss=Ship.BossShip(1400, 860)
        gfw.world.add(gfw.layer.Boss,boss)
        bisAirPlaneMake= False

def update():
   
    MonsterBullet_Collision()
    PlayerBullet_Collision()
    gfw.world.update()
    
    makeTime()
    
    
    
    pass   
def draw():
    gfw.world.draw()
    
def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()    
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

def exit():
    pass


if __name__ == '__main__':
    gfw.run_main()
