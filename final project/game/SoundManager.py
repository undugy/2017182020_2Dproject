from pico2d import *

class SoundManager:
    def __init__(self):
        self.bgm = load_music('Sound/Stage0.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.bgm2 = load_music('Sound/GameOver.mp3')
        self.bgm2.set_volume(64)

        self.Expol_Sound1 = load_wav('Sound/Explode_Bomb.wav')
        self.Expol_Sound2 = load_wav('Sound/Explode_Guide.wav')
        self.Expol_Sound3 = load_wav('Sound/Explode_StaticAI.wav')
        self.BossExpol_1=load_wav('Sound/BossExpol_1.wav')
        self.BossExpol_2 = load_wav('Sound/BossExpol_2.wav')
        self.BossExpol_3 = load_wav('Sound/BossExpol_3.wav')
        self.BossExpol_4 = load_wav('Sound/BossExpol_4.wav')
        self.BossExpol_5 = load_wav('Sound/BossExpol_5.wav')


        self.PowerUp = load_wav('Sound/PowerUp.wav')#8
        self.PowerDown = load_wav('Sound/PowerDown.wav')#9
        self.ScoreUp = load_wav('Sound/ScoreUp.wav')#10
        self.Bullet = load_wav('Sound/Bullet.wav')#11
        self.BlueBulletExpol = load_wav('Sound/BlueBullet_Expol.wav')#12
        self.Bullet_Scout = load_wav('Sound/Bullet_Scout.wav')  # 13


        self.LifeExpol = load_wav('Sound/LifeExpol.wav') #14


        self.SoundLst = [self.Expol_Sound1, self.Expol_Sound2, self.Expol_Sound3, self.BossExpol_1,self.BossExpol_2,
                         self.BossExpol_3,self.BossExpol_4,self.BossExpol_5,self.PowerUp,self.PowerDown,
                         self.ScoreUp,self.Bullet, self.BlueBulletExpol, self.Bullet_Scout,self.LifeExpol]

        for i in range(3,10):
            self.SoundLst[i].set_volume(80)
        self.SoundLst[11].set_volume(40)
        self.SoundLst[12].set_volume(64)
        self.SoundLst[13].set_volume(64)
        self.SoundLst[14].set_volume(80)
        self.Expol_Sound1.set_volume(64)
        self.Expol_Sound2.set_volume(32)
        self.Expol_Sound3.set_volume(32)


    def GameOverSound(self):
        self.bgm.stop()
        self.bgm2.repeat_play()
    def PlaySound(self,number):
        self.SoundLst[number].play(1)
