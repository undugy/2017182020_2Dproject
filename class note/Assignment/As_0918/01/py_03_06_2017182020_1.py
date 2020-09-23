from pico2d import *
import helper
import random
class Boy:
    def __init__(self):
        self.count=0
        self.target_list=[]
        self.target=(400,300)
        self.pos=(400,300) 
        self.speed=0 
        self.img = load_image('../image resources/run_animation.png')
        self.fidx = 4
        self.done=False
        self.delta=(0,0)
        

    def draw(self):
        self.img.clip_draw(self.fidx * 100, 0, 100, 100, self.pos[0], self.pos[1])
    def update(self):
        self.fidx = (self.fidx + 1) % 8
       
        self.delta=helper.delta(self.pos,self.target,self.speed)
        self.pos,self.done=helper.move_toward(self.pos,self.delta,self.target)
        
        if self.done:
          self.speed=1
          self.count+=1
          if(len(self.target_list)-1<self.count):
            self.count-=1
            
          self.target=self.target_list[self.count]
          
        
        
        
           
        
        
class Grass:
    def __init__(self):
        self.img = load_image('../image resources/grass.png')
        self.x, self.y = 400, 30
    def draw(self):
        self.img.draw(self.x, self.y)

     
def handle_events():
    global running, boy,count
    evts = get_events();
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEBUTTONDOWN:
            if (e.button==SDL_BUTTON_LEFT):
              boy.target_list.append((e.x,get_canvas_height() - e.y -1))
              boy.target=boy.target_list[boy.count]
              
            elif(e.button==SDL_BUTTON_RIGHT):
              boy.speed+=1;
                
             
open_canvas()

grass = Grass()
boy=Boy()          

count=0
running = True

while running:
    clear_canvas()
    grass.draw()
    boy.draw()
    handle_events() 
    boy.update()
    
    

    
    update_canvas()
  
    
    

    delay(0.04)


close_canvas()

    
