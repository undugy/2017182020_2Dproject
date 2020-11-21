import gfw
from pico2d import *
import main_state
Frame=0
def enter():
    global image
    image = load_image('Resource/character.png')

def update():
    global Frame
    if(Frame<0):
        Frame=5
    elif(Frame>5):
        Frame=0

def draw():
    clear_canvas()
    image.clip_draw(Frame*800,0,800,900,360,480,720,960)
    update_canvas()  
def handle_event(e):
        global Frame
        if e.type==SDL_QUIT:
            gfw.quit()
        else:
            if(e.type, e.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                gfw.quit()
            elif(e.type,e.key)==(SDL_KEYDOWN,SDLK_SPACE):
                gfw.push(main_state)
            elif(e.type, e.key)==(SDL_KEYDOWN,SDLK_RIGHT):
                Frame+=1
            elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_LEFT):
                Frame -=1

def exit():
    global image
    del image

def pause():
    pass
def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()

