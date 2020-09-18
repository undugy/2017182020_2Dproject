from pico2d import *

open_canvas()
img = load_image('../image resources/character.png')
gra = load_image('../image resources/grass.png')

for x in range(0, 800, 2):
    clear_canvas()
    gra.draw(400, 30)
    img.draw(x, 80)
    update_canvas()
    delay(0.01)

delay(5)
close_canvas()
