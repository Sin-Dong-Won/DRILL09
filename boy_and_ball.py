from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 140), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0 , 100, 100, self.x, self.y)

class Ball:
    global boy
    global boys

    def __init__(self):
        self.x, self.y = boy.x + 30, 70
        self.image = load_image('ball41x41.png')

    def update(self):
        self.x += 5

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

boy = Boy()
grass = Grass()
ball = Ball()

team = [Boy() for i in range(11)]

running = True

# game main loop code
while running:
    handle_events()

    # for boys in team:
    #     boys.update()


    ball.update()
    boy.update()

    clear_canvas()

    boy.draw()
    ball.draw()
    grass.draw()

    # for boys in team:
    #     boys.draw()

    update_canvas()

    delay(0.05)

# finalization code
close_canvas