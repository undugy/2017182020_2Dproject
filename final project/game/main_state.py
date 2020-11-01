import gfw
from pico2d import *
from CPlayer import Player
import win32api
import gobj
import random
import CMonster
import CUI
import CEffect

def enter():
    gfw.world.init(['CPlayer','CBullet','CMonster','CMonsterBullet','CUI','CEffect'])
    global player,score,life
    player=Player()
    gfw.world.add(gfw.layer.CPlayer,player)

    score=CUI.Score()
    life=CUI.Life()
    gfw.world.add(gfw.layer.CUI, score)
    gfw.world.add(gfw.layer.CUI, CUI.Lager_Energy(160,30))
    gfw.world.add(gfw.layer.CUI, CUI.Player_Bomb())
    gfw.world.add(gfw.layer.CUI, life)





def MonsterBullet_Collision():
 global player,score
 for Monster in gfw.world.objects_at(gfw.layer.CMonster):    
  for MonsterBullet in gfw.world.objects_at(gfw.layer.CMonsterBullet):   
    for PlayerBullet in gfw.world.objects_at(gfw.layer.CBullet):
        if  Monster.x +Monster.RadianX > PlayerBullet.x > Monster.x-Monster.RadianX and Monster.y + Monster.PivotY >PlayerBullet.y > Monster.y - Monster.PivotY:
         Monster.Hp -= 2 + player.Power * 0.75
         player.Gage += 0.5
         score.Add_Score(random.randint(3, 7))
         PlayerBullet.isDead = True
         Pp=CEffect.Effect(PlayerBullet.x + random.randint(-15, 15),
                      PlayerBullet.y + random.randint(-15, 15), 30, 27, 30, 27, 12,0)
         gfw.world.add(gfw.layer.CEffect,Pp)
         
def PlayerBullet_Collision():
    global player,score
    for Monster in gfw.world.objects_at(gfw.layer.CMonster):
     for MonsterBullet in gfw.world.objects_at(gfw.layer.CMonsterBullet):       
      for PlayerBullet in gfw.world.objects_at(gfw.layer.CBullet):
        Dist = math.sqrt((player.x - MonsterBullet.x) ** 2 + (player.y - MonsterBullet.y) ** 2)
        if Dist <=MonsterBullet.Radius and player.IsShield is False:
            MonsterBullet.isDead = True   
            if player.SuperMode is False:
                player.Life-=1;
                
            Cp=CEffect.Effect(player.x + random.randint(-20, 20),
                                       player.y + random.randint(-20, 20), 128, 128,
                                      250, 250, 64, 5,0.3)
            gfw.world.add(gfw.layer.CEffect,Cp)
           
bisAirPlaneMake = True
MakeTerm=0

RedAirPlaneTerm =0
def update():
    PlayerBullet_Collision()
    MonsterBullet_Collision()
    gfw.world.update()
    
    
    
    
    global MakeTerm, RedAirPlaneTerm,bisAirPlaneMake
    global Time

    MakeTerm+=gfw.delta_time * 0.5
    if MakeTerm >=1 and bisAirPlaneMake is True:
        MakeTerm=0
        Lp=CMonster.LeftPlane1(random.randint(0, 720), 960)
        Rp=CMonster.RightPlane1(random.randint(0, 720), 960)
        gfw.world.add(gfw.layer.CMonster,Lp)
        gfw.world.add(gfw.layer.CMonster,Rp)
        


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
