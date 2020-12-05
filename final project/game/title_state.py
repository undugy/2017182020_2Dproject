import gfw
from pico2d import *
import main_state
Frame=0
Music=1
def enter():
  
    global image
    image = load_image('Resource/character.png')
    global bgm
    bgm=load_music('Sound/select.mp3')
    bgm.set_volume(40)
    bgm.repeat_play()
def update():
    global Frame,Music,bgm
    if(Frame<0):
        Frame=4
    elif(Frame>4):
        Frame=0
    if Music>0:
       bgm.repeat_play()
       Music-=1

def draw():
    clear_canvas()
    image.clip_draw(Frame*800,0,800,900,360,480,720,960)
    update_canvas()  
def handle_event(e):
        global Frame,ch,Music
        if e.type==SDL_QUIT:
            gfw.quit()
        else:
            if(e.type, e.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                gfw.quit()
            elif(e.type,e.key)==(SDL_KEYDOWN,SDLK_SPACE):
                main_state.Ch_num=Frame+1
                gfw.push(main_state)
                Music+=1
                
            elif(e.type, e.key)==(SDL_KEYDOWN,SDLK_RIGHT):
                Frame+=1
            elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_LEFT):
                Frame -=1

def exit():
    global image,bgm
    del image
    del bgm

def pause():
    pass
def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()

