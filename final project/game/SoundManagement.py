from pico2d import *

def init():
        global SoundLst,bgm,bgm2
        bgm = load_music('Sound/Stage0.mp3')
        bgm.set_volume(40)
        
        bgm2 = load_music('Sound/GameOver.mp3')
        bgm2.set_volume(40)

        Expol_Sound1 = load_wav('Sound/Explode_Bomb.wav')
        Expol_Sound2 = load_wav('Sound/Explode_Guide.wav')
        Expol_Sound3 = load_wav('Sound/Explode_StaticAI.wav')
        BossExpol_1=load_wav('Sound/BossExpol_1.wav')
        BossExpol_2 = load_wav('Sound/BossExpol_2.wav')
        BossExpol_3 = load_wav('Sound/BossExpol_3.wav')
        BossExpol_4 = load_wav('Sound/BossExpol_4.wav')
        BossExpol_5 = load_wav('Sound/BossExpol_5.wav')


        PowerUp = load_wav('Sound/PowerUp.wav')#8
        PowerDown = load_wav('Sound/PowerDown.wav')#9
        ScoreUp = load_wav('Sound/ScoreUp.wav')#10
        Bullet = load_wav('Sound/Bullet.wav')#11
        BlueBulletExpol = load_wav('Sound/BlueBullet_Expol.wav')#12
        Bullet_Scout = load_wav('Sound/Bullet_Scout.wav')  # 13


        LifeExpol = load_wav('Sound/LifeExpol.wav') #14


        SoundLst = [Expol_Sound1,Expol_Sound2, Expol_Sound3, BossExpol_1,BossExpol_2,
                        BossExpol_3,BossExpol_4,BossExpol_5,PowerUp,PowerDown,
                        ScoreUp,Bullet,BlueBulletExpol,Bullet_Scout,LifeExpol]

        for i in range(3,10):
            SoundLst[i].set_volume(50)
        SoundLst[11].set_volume(40)
        SoundLst[12].set_volume(64)
        SoundLst[13].set_volume(64)
        SoundLst[14].set_volume(80)
        Expol_Sound1.set_volume(64)
        Expol_Sound2.set_volume(32)
        Expol_Sound3.set_volume(32)
    
def GameOverSound():
    global bgm,bgm2
    bgm.stop()
    bgm2.repeat_play()
def PlaySound(number,volume):
    global SoundLst
    SoundLst[number].set_volume(volume)
    SoundLst[number].play(1)
def PlaySound2(number,volume):
    global SoundLst
    SoundLst[number].set_volume(volume)
    SoundLst[number].play()
