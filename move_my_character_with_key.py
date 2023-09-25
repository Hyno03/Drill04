from pico2d import*

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character_idle = load_image('character_animation.jpg')

def draw_Background():
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

def handle_events():
    global running, walking, composite, dir_x, dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                walking = True
                composite = True
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                walking = True
                composite = False
            elif event.key == SDLK_UP:
                dir_y += 1
                walking = True
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                walking = True
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
                walking = False
            elif event.key == SDLK_LEFT:
                dir_x += 1
                walking = False
            elif event.key == SDLK_UP:
                dir_y -= 1
                walking = False
            elif event.key == SDLK_DOWN:
                dir_y += 1
                walking = False

# def move_Until_Canvas():
#     global can_move
#     if x < (TUK_WIDTH - 40) or y < (TUK_HEIGHT - 20) or x > 40 or y > 20:
#         can_move = True
#     else:
#         can_move = False

running = True
walking = False
composite = False
can_move = False
x, y = TUK_WIDTH//2, TUK_HEIGHT//2
frame = 0
dir_x = 0
dir_y = 0

while running:
    draw_Background()
    if composite:
        character_idle.clip_composite_draw(frame * 95, 2180, 85, 160, 0, 'h',x, y, 85, 160)
    elif not composite:
        character_idle.clip_draw(frame * 95, 2180, 85, 160, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 6
    delay(0.1)

    while walking:
        draw_Background()
        if composite:
            character_idle.clip_composite_draw(frame * 95, 2008, 85, 160, 0, 'h', x, y, 85, 160)
        elif not composite:
            character_idle.clip_draw(frame * 95, 2008, 85, 160, x, y)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 6
        x += dir_x * 10
        if x > (TUK_WIDTH - 40) or x < 40:
            x -= dir_x * 10
        y += dir_y * 10
        if y > (TUK_HEIGHT - 80) or y < 80:
            y -= dir_y * 10
        delay(0.1)

close_canvas()
