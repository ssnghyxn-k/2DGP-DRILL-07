from pico2d import *
import random

# Game object class here
class Grass:
    # Create Func: 객체의 초기 상태를 설정
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass  # 잔디는 변하는 것이 없음

    def draw(self):
        self.image.draw(400,30)

    pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class s_Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = random.randint(0, 7)
        self.image = load_image('ball21x21.png')


class b_Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = random.randint(0, 7)
        self.image = load_image('ball41x41.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global small_balls
    global big_balls
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(10)]
    world += team

    small_balls = [s_Ball() for i in range(20)]
    world += small_balls

    big_balls = [b_Ball() for i in range(20)]
    world += big_balls

running = True

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    # game logic
    handle_events()
    update_world() # simulation
    render_world() # show result
    delay(0.05)

# finalization code
close_canvas()