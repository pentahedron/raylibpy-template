from raylibpy import *
import random

# ---------------------------
# Window settings
# ---------------------------
screen_width = 800
screen_height = 600
init_window(screen_width, screen_height, b"Catch the Falling Objects")
set_target_fps(60)

# ---------------------------
# Player (basket)
# ---------------------------
player_width = 100
player_height = 20
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - 40
player_speed = 7

# ---------------------------
# Falling object
# ---------------------------
object_width = 30
object_height = 30
object_x = random.randint(0, screen_width - object_width)
object_y = 0
object_speed = 5

# ---------------------------
# Score
# ---------------------------
score = 0

# ---------------------------
# Game loop
# ---------------------------
while not window_should_close():

    # ----- Player movement -----
    if is_key_down(KEY_LEFT) and player_x > 0:
        player_x -= player_speed
    if is_key_down(KEY_RIGHT) and player_x < screen_width - player_width:
        player_x += player_speed

    # ----- Falling object movement -----
    object_y += object_speed

    # ----- Collision detection -----
    if (object_y + object_height >= player_y and
        object_x + object_width >= player_x and
        object_x <= player_x + player_width):
        score += 1
        object_y = 0
        object_x = random.randint(0, screen_width - object_width)

    # ----- Reset object if missed -----
    if object_y > screen_height:
        object_y = 0
        object_x = random.randint(0, screen_width - object_width)

    # ----- Draw everything -----
    begin_drawing()
    clear_background(RAYWHITE)
    draw_rectangle(player_x, player_y, player_width, player_height, BLUE)
    draw_rectangle(object_x, object_y, object_width, object_height, RED)
    draw_text(f"Score: {score}", 10, 10, 20, BLACK)
    end_drawing()

# ---------------------------
# Close window
# ---------------------------
close_window()
