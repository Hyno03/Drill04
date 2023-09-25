from pico2d import*

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character_idle = load_image('character_animation.jpg')
#character_idle = load_image('character_animation_idle.jpg')

def handle_events():
    global running, dir_x, dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

running = True
x, y = TUK_WIDTH//2, TUK_HEIGHT//2
frame = 0
dir_x = 0
dir_y = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    character_idle.clip_draw(frame * 95, 2180, 85, 160, x, y)
    #character_idle.clip_draw(frame * 95, 0, 85, 160, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 6
    x += dir_x * 5
    y += dir_y * 5
    delay(0.1)

close_canvas()
