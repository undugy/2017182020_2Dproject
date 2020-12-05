
import gfw
from pico2d import *
import title_state
import highscore

def enter():
    gfw.world.init(['highscore'])
    global game_over_image
    game_over_image = gfw.image.load('Resource/game_over.png')
    global bgm
    bgm=load_music('Sound/awesomeness.mp3')
    bgm.set_volume(40)
    bgm.repeat_play()
    global font
    font = gfw.font.load('Resource/2P.ttf', 40)
    highscore.load()
    gfw.world.add(gfw.layer.highscore, highscore)
def update():
	gfw.world.update()
	pass

def draw():
  game_over_image.draw(360,480,720,960)
  gfw.world.draw()
  
  font.draw(170,750,'BEST SCORE',(0,0,0))

def handle_event(e):
        global bgm
        if e.type==SDL_QUIT:
            gfw.quit()
        else:
            if(e.type, e.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                bgm.stop()
                gfw.quit() 
            elif(e.type,e.key)==(SDL_KEYDOWN,SDLK_r):
                bgm.stop()
                gfw.pop()
            

def exit():
    global bgm, game_over_image
    del bgm
    del game_over_image
    pass

def pause():
    pass
def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()

