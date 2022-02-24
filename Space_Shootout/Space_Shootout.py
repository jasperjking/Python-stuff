from cmath import pi
from turtle import width
import pygame
import os
import random
import math
pygame.font.init()
pygame.mixer.init()


"""
The list of all subprograms (as of 23 Feb):
1. draw window
2. yellow movement
3. red movement
4. handle bullets
5. handle asteroid
6. create asteroid
7. draw winner
8. main

things to do:
1. add powerups
    - faster bullets? - probably not
    - sheild? - maybe change heart to sheild
1.5 change frequency of powerups.
2. fix the deletion/collection of different powerups
    - think i finished it
3. get better colour theme? done?
4. add pause button

"""

# declare different gloval variables
# declare recangles that are comonly used
# sounds that are used
# fonts
# events
# images


# declare different gloval variables
WIDTH, HEIGHT = 1080, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shootout!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60
I_TIME = 1

VEL = 5
BULLET_VEL = 7
ASTEROID_VEL = 7
MAX_BULLETS = 3

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

ASTEROID_WIDTH, ASTEROID_HEIGHT = 40, 55

POWERUP_HEIGHT, POWERUP_WIDTH = 40, 40

BULLET_WIDTH, BULLET_HEIGHT = 10, 5

BULLET_PADDING_X, BULLET_PADDING_Y = 4, 10

POWERUP_TIME = 20

POWERUP_BULLET_VEL = 11
POWERUP_BULLET_NUMBER = 5

# declare recangles that are comonly used
BORDER1 = pygame.Rect(WIDTH//2 - 4, 0, 8, HEIGHT - 50)
BORDER2 = pygame.Rect(WIDTH//2 - 3, 1, 6, HEIGHT - 40)

MENU_BAR1 = pygame.Rect(0, HEIGHT - 50, WIDTH, 50)
MENU_BAR2 = pygame.Rect(1, HEIGHT - 49, WIDTH - 2, 48)

MENU_BUTTON1 = pygame.Rect(WIDTH//2 - 20, HEIGHT - 45, 40, 40)
MENU_BUTTON2 = pygame.Rect(WIDTH//2 - 19, HEIGHT - 44, 38, 38)

MENU_BOX1 = pygame.Rect(WIDTH//2 - 201, HEIGHT//2 - 201, 402, 402)
MENU_BOX2 = pygame.Rect(WIDTH//2 - 200, HEIGHT//2 - 200, 400, 400)

MENU_BUTTON_PAUSE1 = pygame.Rect(WIDTH//2 - 13, HEIGHT - 40, 10, 30)
MENU_BUTTON_PAUSE2 = pygame.Rect(WIDTH//2  + 3, HEIGHT - 40, 10, 30)

MENU_BUTTON_PLAY = [(WIDTH//2 - 13, HEIGHT - 40), (WIDTH//2 - 13, HEIGHT - 10), (WIDTH//2 + 13, HEIGHT - 25)]



# sounds that are used
DO_SOUND = False
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Space_Shootout', 'Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Space_Shootout', 'Assets', 'Gun+Silencer.mp3'))



# fonts
HEALTH_FONT = pygame.font.SysFont('comicsans', 20)
WINNER_FONT = pygame.font.SysFont('comicsans', 110)
MENU_FONT = pygame.font.SysFont('comicsans', 40)



# events
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
YELLOW_HIT_ASTEROID = pygame.USEREVENT + 3
RED_HIT_ASTEROID = pygame.USEREVENT + 4
ASTEROID_HIT = pygame.USEREVENT + 5



# images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Space_Shootout', 'Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Space_Shootout', 'Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

ASTEROID_IMAGE = pygame.image.load(os.path.join('Space_Shootout', 'Assets', 'asteroid.png'))
ASTEROID = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(ASTEROID_IMAGE, (ASTEROID_WIDTH, ASTEROID_HEIGHT)), 270), flip_x = True, flip_y = False)

HEART_IMAGE = pygame.image.load(os.path.join('Space_Shootout', 'Assets', 'heart.png'))
HEART = pygame.transform.scale(HEART_IMAGE, (POWERUP_WIDTH, POWERUP_HEIGHT))

BULLET_MORE_IMAGE = pygame.image.load(os.path.join('Space_Shootout', 'Assets', 'bullets_more.png'))
BULLET_MORE = pygame.transform.scale(BULLET_MORE_IMAGE, (POWERUP_WIDTH, POWERUP_HEIGHT))
BULLET_MORE_EMBLEM = pygame.transform.scale(BULLET_MORE, (POWERUP_WIDTH * 5/8, POWERUP_HEIGHT * 5/8))

BULLET_SPEED_IMAGE = pygame.image.load(os.path.join('Space_Shootout', 'Assets', 'bullets_speed.png'))
BULLET_SPEED = pygame.transform.scale(BULLET_SPEED_IMAGE, (POWERUP_WIDTH, POWERUP_HEIGHT))
BULLET_SPEED_EMBLEM = pygame.transform.scale(BULLET_SPEED, (POWERUP_WIDTH * 5/8, POWERUP_HEIGHT * 5/8))


SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Space_Shootout', 'Assets', 'space.png')), (WIDTH, HEIGHT))



def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, asteroid, powerup_list_rect, powerup_list, draw_yellow_max_bullets, draw_red_max_bullets, menu_open, asteroid_present, draw_yellow_speed_bullets, draw_red_speed_bullets): 
    WIN.blit(SPACE, (0,0))

    pygame.draw.rect(WIN, WHITE, MENU_BAR1) # bottom white menu bar
    pygame.draw.rect(WIN, BLACK, MENU_BAR2) # bottom black menu bar

    pygame.draw.rect(WIN, WHITE, BORDER1) # middle white dividing line
    pygame.draw.rect(WIN, BLACK, BORDER2) # middle black dividing line

    pygame.draw.rect(WIN, WHITE, MENU_BUTTON1)
    pygame.draw.rect(WIN, BLACK, MENU_BUTTON2)

    pygame.draw.rect(WIN, WHITE, MENU_BUTTON_PAUSE1)
    pygame.draw.rect(WIN, WHITE, MENU_BUTTON_PAUSE2) 

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    if asteroid_present: WIN.blit(ASTEROID, (asteroid.x, asteroid.y))

    for i in range(0, len(powerup_list_rect)):
        WIN.blit(powerup_list[i], powerup_list_rect[i])


    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, HEIGHT - 40))
    WIN.blit(yellow_health_text, (10, HEIGHT - 40))

    if draw_yellow_max_bullets:
        WIN.blit(BULLET_MORE_EMBLEM, (10 + yellow_health_text.get_width() + 10 + 5, HEIGHT - 36))
    if draw_red_max_bullets:
        WIN.blit(BULLET_MORE_EMBLEM, (WIDTH - 10 - red_health_text.get_width() - 10 - 25, HEIGHT - 36))

    if draw_yellow_speed_bullets:
        WIN.blit(BULLET_SPEED_EMBLEM, (10 + yellow_health_text.get_width() + 15 + BULLET_MORE_EMBLEM.get_width() + 15, HEIGHT - 36))
    if draw_red_speed_bullets:
        WIN.blit(BULLET_SPEED_EMBLEM, (WIDTH - 10 - red_health_text.get_width() - 35 - 15 - BULLET_SPEED_EMBLEM.get_width(), HEIGHT - 36))
    

    pygame.draw.rect(WIN, WHITE, MENU_BOX1)
    pygame.draw.rect(WIN, BLACK, MENU_BOX2)
    menu_text = MENU_FONT.render("MENU", 1, WHITE)
    WIN.blit(menu_text, (WIDTH//2 - menu_text.get_width()//2, HEIGHT//2 - 200))
    pygame.draw.polygon(WIN, WHITE, MENU_BUTTON_PLAY)



    pygame.display.update()




def yellow_movement(keys_pressed, yellow, yellow_vel):
        if keys_pressed[pygame.K_a] and yellow.x - yellow_vel > 0: # LEFT
            yellow.x -= yellow_vel
        if keys_pressed[pygame.K_d] and yellow.x + yellow_vel + yellow.width < BORDER1.x: # RIGHT
            yellow.x += yellow_vel
        if keys_pressed[pygame.K_w] and yellow.y - yellow_vel > 0: # UP
            yellow.y -= yellow_vel
        if keys_pressed[pygame.K_s] and yellow.y + yellow_vel + yellow.height < HEIGHT - 65: # DOWN
            yellow.y += yellow_vel




def red_movement(keys_pressed, red, red_vel):
        if keys_pressed[pygame.K_LEFT] and red.x - red_vel > BORDER1.x + 20: # LEFT
            red.x -= red_vel
        if keys_pressed[pygame.K_RIGHT] and red.x + red_vel + red.width < WIDTH: # RIGHT
            red.x += red_vel
        if keys_pressed[pygame.K_UP] and red.y - red_vel > 0: # UP
            red.y -= red_vel
        if keys_pressed[pygame.K_DOWN] and red.y + red_vel + red.height < HEIGHT - 65: # DOWN
            red.y += red_vel




def handle_bullets(yellow_bullets, red_bullets, yellow, red, yellow_bullet_vel, red_bullet_vel):
    for bullet in yellow_bullets:
        bullet.x += yellow_bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= red_bullet_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

    for red in red_bullets:
        for yellow in yellow_bullets:
            if red.x + BULLET_WIDTH + BULLET_PADDING_X >= yellow.x and red.x - BULLET_WIDTH - BULLET_PADDING_X <= yellow.x:
                if red.y + BULLET_HEIGHT + BULLET_PADDING_Y >= yellow.y and red.y - BULLET_HEIGHT - BULLET_PADDING_Y <= yellow.y:
                    red_bullets.remove(red)
                    yellow_bullets.remove(yellow)
                    





def handle_asteroid(red, yellow, asteroid, yellow_bullets, red_bullets, asteroid_hitpoints):
    if asteroid.colliderect(yellow):
        pygame.event.post(pygame.event.Event(YELLOW_HIT_ASTEROID))
    if asteroid.colliderect(red):
        pygame.event.post(pygame.event.Event(RED_HIT_ASTEROID))

    for bullet in yellow_bullets:
        if asteroid.colliderect(bullet):
            yellow_bullets.remove(bullet)
            asteroid_hitpoints -= 1
    for bullet in red_bullets:
        if asteroid.colliderect(bullet):
            asteroid_hitpoints -=1
            red_bullets.remove(bullet)

    if asteroid_hitpoints == 0:
        asteroid_hitpoints = 3
        pygame.event.post(pygame.event.Event(ASTEROID_HIT))
    return asteroid_hitpoints




    
def create_asteroid():
    asteroid_start_corner = random.randint(0, 3) 
    if asteroid_start_corner == 0: asteroid_start_corner_x, asteroid_start_corner_y = 25, HEIGHT - ASTEROID_HEIGHT - 75
    if asteroid_start_corner == 1: asteroid_start_corner_x, asteroid_start_corner_y = 25, 25
    if asteroid_start_corner == 2: asteroid_start_corner_x, asteroid_start_corner_y = WIDTH - ASTEROID_WIDTH - 25, 25
    if asteroid_start_corner == 3: asteroid_start_corner_x, asteroid_start_corner_y = WIDTH - ASTEROID_WIDTH - 25, HEIGHT - ASTEROID_HEIGHT - 75


    asteroid = pygame.Rect(asteroid_start_corner_x, asteroid_start_corner_y, ASTEROID_WIDTH, ASTEROID_HEIGHT)

    asteroid_orientation = random.uniform(math.radians(20), math.radians(70)) + pi/2 * asteroid_start_corner # * (4 - asteroid_start_corner + 1)
    asteroid_x_vel = math.cos(asteroid_orientation) * ASTEROID_VEL
    asteroid_y_vel = math.sin(asteroid_orientation) * ASTEROID_VEL

    #if asteroid_start_corner == 1: asteorid_y_vel *= -1
    #if asteroid_start_corner == 2: asteroid_x_vel *= -1
    #if asteroid_start_corner == 2: asteroid_y_vel *= -1,
    #if asteroid_start_corner == 3: asteorid_x_vel *= -1

    return asteroid, asteroid_x_vel, asteroid_y_vel




def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)    




def main():

    red = pygame.Rect(WIDTH - WIDTH//6, HEIGHT//2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(WIDTH//6, HEIGHT//2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    asteroid, asteroid_x_vel, asteroid_y_vel = create_asteroid()
    asteroid_present = True
    asteroid_hitpoints = 3

    red_i = 0
    yellow_i = 0

    powerup_list = []
    powerup_list_rect = []

    red_bullets = []
    yellow_bullets = []

    red_vel = VEL
    yellow_vel = VEL

    red_max_bullets = MAX_BULLETS
    yellow_max_bullets = MAX_BULLETS

    red_bullet_vel = BULLET_VEL
    yellow_bullet_vel = BULLET_VEL

    red_max_bullets_ticks = 0
    yellow_max_bullets_ticks = 0

    red_speed_bullets_ticks = 0
    yellow_speed_bullets_ticks = 0

    menu_open = False

    yellow_health = 10
    red_health = 10

    asteroid_tick = 1
    clock_tick = 1

    clock = pygame.time.Clock()
    run = True


    while run:
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
                

            if event.type == pygame.KEYDOWN and not menu_open:

                if event.key == pygame.K_c and len(yellow_bullets) < yellow_max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 + 2, BULLET_WIDTH, BULLET_HEIGHT)
                    yellow_bullets.append(bullet)
                    # BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_BACKSLASH and len(red_bullets) < red_max_bullets:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 + 3, BULLET_WIDTH, BULLET_HEIGHT)
                    red_bullets.append(bullet)
                    # BULLET_FIRE_SOUND.play()
                
                if event.key == pygame.K_EQUALS:
                    asteroid, asteroid_x_vel, asteroid_y_vel = create_asteroid()


                
            if event.type == RED_HIT:
                red_health -= 1
                if DO_SOUND: BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                if DO_SOUND: BULLET_HIT_SOUND.play()

            if event.type == RED_HIT_ASTEROID and red_i == 0:
                red_health -= 1
                red_i = I_TIME
                red_max_bullets_ticks = 0
            if event.type == YELLOW_HIT_ASTEROID and yellow_i == 0:
                yellow_health -= 1
                yellow_i = I_TIME
                yellow_max_bullets_ticks = 0


            if event.type == ASTEROID_HIT:
                powerup_list_rect.append(pygame.Rect(asteroid.x, asteroid.y, 40, 40))
                powerup_chosen = random.randint(1, 3)
                if powerup_chosen == 1:
                    powerup_list.append(HEART)
                elif powerup_chosen == 2:
                    powerup_list.append(BULLET_MORE)
                elif powerup_chosen == 3:
                    powerup_list.append(BULLET_SPEED)

                asteroid_x_vel, asteroid_y_vel, asteroid_present = 0, 0, False
                asteroid.x = -100

                
            
            if  event.type == pygame.MOUSEBUTTONDOWN:
                mousepress = pygame.mouse.get_pressed()
                if mousepress[0]:
                    mousepos = pygame.mouse.get_pos()
                    if mousepos[0] <= WIDTH//2 + 20 and mousepos[0] >= WIDTH//2 - 20 and mousepos[1] >= HEIGHT - 45 and mousepos[1] <= HEIGHT - 5:
                        menu_open = not menu_open
                    # if mousepos[0] <= WIDTH//2 + 20 and mousepos[0] >= WIDTH//2 and mousepos[1] >= HEIGHT//2 and mousepos[1] <= HEIGHT//2 + 20:
                    #     stat_on = not stat_on            
                

        # fix the removal of powerups. sometimes they are changing when one is collected/removed


        for i in range(len(powerup_list_rect) - 1, -1, -1):
            if powerup_list_rect[i].colliderect(red):
                if powerup_list[i] == HEART:
                    if red_health < 10:
                        red_health += 1
                elif powerup_list[i] == BULLET_MORE:
                    red_max_bullets = POWERUP_BULLET_NUMBER
                    red_max_bullets_ticks = POWERUP_TIME
                elif powerup_list[i] == BULLET_SPEED:
                    red_bullet_vel = POWERUP_BULLET_VEL
                    red_speed_bullets_ticks = POWERUP_TIME
                powerup_list_rect.pop(i)
                powerup_list.pop(i)
            elif powerup_list_rect[i].colliderect(yellow):
                if powerup_list[i] == HEART:
                    if yellow_health < 10:
                        yellow_health += 1
                elif powerup_list[i] == BULLET_MORE:
                    yellow_max_bullets = POWERUP_BULLET_NUMBER
                    yellow_max_bullets_ticks = POWERUP_TIME    
                elif powerup_list[i] == BULLET_SPEED:
                    yellow_bullet_vel = POWERUP_BULLET_VEL
                    yellow_speed_bullets_ticks = POWERUP_TIME
                powerup_list_rect.pop(i)
                powerup_list.pop(i)



        
        
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if not menu_open:
            keys_pressed = pygame.key.get_pressed()
            yellow_movement(keys_pressed, yellow, yellow_vel)
            red_movement(keys_pressed, red, red_vel)

            handle_bullets(yellow_bullets, red_bullets, yellow, red, yellow_bullet_vel, red_bullet_vel)

            asteroid_hitpoints = handle_asteroid(red, yellow, asteroid, red_bullets, yellow_bullets, asteroid_hitpoints)

            if asteroid.x <= 0 or asteroid.x >= WIDTH - asteroid.width:
                asteroid_x_vel = asteroid_x_vel * -1
            if asteroid.y <= 0 or asteroid.y >= HEIGHT - asteroid.height - 50:
                asteroid_y_vel = asteroid_y_vel * -1
            asteroid.x += asteroid_x_vel
            asteroid.y += asteroid_y_vel

            clock_tick += 1
            if clock_tick % FPS == 0:
                clock_tick = 0

                if yellow_i != 0: yellow_i -= 1
                if red_i != 0: red_i -= 1

                if yellow_max_bullets_ticks != 0: yellow_max_bullets_ticks -= 1
                if yellow_max_bullets_ticks == 0: yellow_max_bullets = MAX_BULLETS

                if red_max_bullets_ticks != 0: red_max_bullets_ticks -= 1
                if red_max_bullets_ticks == 0: red_max_bullets = MAX_BULLETS    

                if red_speed_bullets_ticks != 0: red_speed_bullets_ticks -= 1
                if red_speed_bullets_ticks == 0: red_bullet_vel = BULLET_VEL   

                if yellow_speed_bullets_ticks != 0: yellow_speed_bullets_ticks -= 1
                if yellow_speed_bullets_ticks == 0: yellow_bullet_vel = BULLET_VEL  

                asteroid_tick += 1
                if asteroid_tick % 10 == 0:
                    asteroid_tick = 0
                    
                    if not asteroid_present:
                        asteroid_tick = 0
                        asteroid, asteroid_x_vel, asteroid_y_vel = create_asteroid()
                        asteroid_present = True
                        


        draw_yellow_max_bullets, draw_red_max_bullets, draw_yellow_speed_bullets, draw_red_speed_bullets = False, False, False, False
        if yellow_max_bullets_ticks != 0: draw_yellow_max_bullets = True 
        if red_max_bullets_ticks != 0: draw_red_max_bullets = True
        if yellow_bullet_vel != BULLET_VEL: draw_yellow_speed_bullets = True
        if red_bullet_vel != BULLET_VEL: draw_red_speed_bullets = True

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, asteroid, powerup_list_rect, powerup_list, draw_yellow_max_bullets, draw_red_max_bullets, menu_open, asteroid_present, draw_yellow_speed_bullets, draw_red_speed_bullets)

        if winner_text != "":
            draw_winner(winner_text)
            break

    main()




if __name__ == "__main__":
    main()
