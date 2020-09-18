from pico2d import *
from random import randint as ri
import os
open_canvas()


a=ri(1,6)
print(a)

os.getcwd()#현재 디렉토리
os.listdir()#디렉토리에 있는 파일 목록

#image=load_image('')#역슬레쉬는 두번 넣어야하고,슬레쉬는 한번만 넣어도 된다.
#image.draw_now(400,300)
#os.chdir('')
print(os.listdir())

close_canvas()

open_canvas()
#os.chdir('C:/Users/양원석/Desktop/2DGP/2DGP class note/Training/image resources')

image=load_image('../image resources/character.png')
image.draw_now(200,300)

'''
hide_lattice()#모눈 숨기기
show_lattice()#모눈 보이기
'''
delay(2)

close_canvas()

