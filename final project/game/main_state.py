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

import SoundManagement
import highscore
import game_over_state

Ch_num=0
canvas_width = 720
canvas_height = 960
STATE_IN_GAME, STATE_GAME_OVER = range(2)


def end_game():
    global state,Sound,score
    state = STATE_GAME_OVER
    Sound.bgm.stop()
    
    highscore.add(score)
    gfw.world.clear() 
    gfw.change(game_over_state)


def enter():
    gfw.world.init(['bg','Boss','CLazer','CPlayer','CBullet','CMonster','CMonsterBullet',
        'CUI','CEffect','CItem','CHyperion'])
    global player,score,Sound,state,Ch_num
    state=STATE_IN_GAME
    
    player=CPlayer.Player()
    CPlayer.Player.playertype=Ch_num
    gfw.world.add(gfw.layer.CPlayer,player)
    global font
    font = gfw.font.load('Resource/2P.ttf', 20)

    Sound=SoundManagement
    Sound.init()
    Sound.bgm.repeat_play()
    

    global game_over_image
    game_over_image = gfw.image.load('Resource/GameOver.png')


    score =0 #Score(canvas_width - 20, canvas_height - 50)
    #gfw.world.add(gfw.layer.CUI, score) 
   
    life=CUI.Life()

    #gfw.world.add(gfw.layer.CUI, score)
    gfw.world.add(gfw.layer.CUI, CUI.Lager_Energy(160,30))
    gfw.world.add(gfw.layer.CUI, CUI.Player_Bomb())
    gfw.world.add(gfw.layer.CUI, life)

    bg=VertScrollBackground('Map_2.png')
    bg.speed=50
    gfw.world.add(gfw.layer.bg,bg)

    
    highscore.load()
    
    global  MakeTerm, RedAirPlaneTerm,bisAirPlaneMake,SmallBoss_MakeTerm,SmallBossCnt,MiddleBossCnt,FinalBossCnt,bisMiddleBossDead
    global Time,BossdeadCnt
    bisAirPlaneMake = True
    MakeTerm=0
    RedAirPlaneTerm =0
    SmallBoss_MakeTerm =0
    SmallBossCnt = 2
    MiddleBossCnt = 1
    FinalBossCnt = 1
    BossdeadCnt = 1
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
         player.Gage += 1/(player.Power*10+10)
          
         score+=1
         PlayerBullet.isDead = True
         
         Pp=CEffect.Effect(PlayerBullet.x + random.randint(-15, 15),
                      PlayerBullet.y + random.randint(-15, 15), 30, 27, 30, 27, 12,0)
         gfw.world.add(gfw.layer.CEffect,Pp)
         
def PlayerBullet_Collision():
    global player,Sound,state
    for Monster in gfw.world.objects_at(gfw.layer.CMonster):
     for MonsterBullet in gfw.world.objects_at(gfw.layer.CMonsterBullet):
        Dist = math.sqrt((player.x - MonsterBullet.x) ** 2 + (player.y - MonsterBullet.y) ** 2)
        if Dist <=MonsterBullet.Radius and player.IsShield is False:
            MonsterBullet.isDead = True
            Sound.PlaySound(14,40)   
            if player.SuperMode is False:
                player.IsShield=True
                player.Life-=1
                Cp=CEffect.Effect(player.x + random.randint(-20, 20),
                    player.y + random.randint(-20, 20), 128, 128,
                                      250, 250, 64, 5,0.3)
                gfw.world.add(gfw.layer.CEffect,Cp)
                if player.Life<=0:
                    state=STATE_GAME_OVER
                    return True

               
def makeTime():
    
    global  MakeTerm, RedAirPlaneTerm,bisAirPlaneMake,SmallBoss_MakeTerm,SmallBossCnt,MiddleBossCnt,FinalBossCnt,bisMiddleBossDead
    global Time, boss,score, Sound,BossdeadCnt

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
        Sound.bgm.stop()
        Sound.bgm3.repeat_play()
        score+=5000
        FinalBossCnt-=1
        boss=Ship.BossShip(1400, 860)
        gfw.world.add(gfw.layer.Boss,boss)
        bisAirPlaneMake= False
        #for b in gfw.world.objects_at(gfw.layer.Boss):
    if Ship.deadyet and BossdeadCnt>0:
        Sound.bgm3.stop()
        Sound.bgm4.repeat_play()
        BossdeadCnt-=1
        
    if Ship.checkDead:
        score+=10000
        Ship.checkDead=False
        Ship.deadyet=False
        return True

def update():
    if state != STATE_IN_GAME:
        return
    MonsterBullet_Collision()
    PlayerBullet_Collision()
    gfw.world.update()
    ends=PlayerBullet_Collision()
    clear=makeTime()
    if ends or clear:
        end_game()
    
    
    
    pass   
def draw():
    gfw.world.draw()
    score_pos = 30, get_canvas_height() - 30
    font.draw(*score_pos, 'Score: %d' % score, (255,255,255))
    
def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()    
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

def exit():
    global Sound
    Sound.Delete_AllList()
    pass


if __name__ == '__main__':
    gfw.run_main()
