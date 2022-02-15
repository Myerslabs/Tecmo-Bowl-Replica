import pygame
import math
from pygame import mixer
from pygame.locals import *
from sys import exit

#Basic Needs
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("A Very Good Football Game")


#Starting image location and movement
#Player 1
player_1_x = 400
player_1_y = 300


#Player 2
player_2_x = 500
player_2_y = 300

#Movement Speed and Direction
velocity = 5

#Game States
game_active = False

#Clock
clock = pygame.time.Clock()


#Images
background = pygame.image.load(r"C:\Users\Jeremy\Documents\GitHub\Python\Techmo\Pixel Art\backgroundfield.png").convert()
icon = pygame.image.load(r"C:\Users\Jeremy\Documents\GitHub\Python\Techmo\Pixel Art\football.png").convert()
pygame.display.set_icon(icon)
#Intro Screen
start_screen = pygame.image.load(r"C:\Users\Jeremy\Documents\GitHub\Python\Techmo\Pixel Art\start_screen.png").convert()

player_1_image = pygame.image.load(r"C:\Users\Jeremy\Documents\GitHub\Python\Techmo\Pixel Art\player_1.png").convert()
player_1_rectangle = player_1_image.get_rect(topleft = (200, 200))



player_2_image = pygame.image.load(r"C:\Users\Jeremy\Documents\GitHub\Python\Techmo\Pixel Art\player_2.png").convert()
player_2_rectangle = player_2_image.get_rect(topleft = (player_2_x, player_2_y))

#Music
#mixer.music.load(r"C:\Users\Jeremy\Documents\GitHub\Python\Techmo\Music\music.wav")
#mixer.music.play(-1)


#Text
menu_s = pygame.font.SysFont('arial', 20)
menu = menu_s.render(' Press Spacebar to begin! ', False, (255,255,255))

#Game Loop
running = True
while running:
    #RGB Color for field
    screen.fill((1, 168, 0))
    #background image
    screen.blit(background, (0,47))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # Keyboard Controls
    keys = pygame.key.get_pressed()

    #player1
    if keys[pygame.K_a]: player_1_rectangle.x -= velocity
    if keys[pygame.K_d]: player_1_rectangle.x += velocity
    if keys[pygame.K_w]: player_1_rectangle.y -= velocity
    if keys[pygame.K_s]: player_1_rectangle.y += velocity
    if keys[pygame.K_SPACE]: game_active = True
        
    #player2
    if keys[pygame.K_LEFT]: player_2_rectangle.x -= velocity
    if keys[pygame.K_RIGHT]: player_2_rectangle.x += velocity
    if keys[pygame.K_UP]: player_2_rectangle.y -= velocity
    if keys[pygame.K_DOWN]: player_2_rectangle.y += velocity

    #Quit game
    if keys[pygame.K_q]:
        pygame.quit()
        main = False
    if game_active == True:
        #player_1 X Boundary
        if player_1_x <= 0: player_1_x = 0
        elif player_1_x >= 800: player_1_x = 800

        #player_1 Y Boundary
        if player_1_y <= 0: player_1_y = 0
        elif player_1_y >=600: player_1_y = 600

        #player_2 X Boundary
        if player_2_x <= 0: player_2_x = 0
        elif player_2_x >= 800: player_2_x = 800
            
        #player_2 Y Boundary
        if player_2_y <= 0: player_2_y = 0
        elif player_2_y >= 600: player_2_y = 600
        
        #Collision
        if player_1_rectangle.colliderect(player_2_rectangle): game_active =  False

        
        #Player 1 Image
        screen.blit(player_1_image, player_1_rectangle)

        #Player 2 Image
        screen.blit(player_2_image, player_2_rectangle)
    else:
        game_active = False
        screen.blit(start_screen, (0,0))
        screen.blit(menu, (200, 200))
        player_1_rectangle.left = 200
        player_2_rectangle.left = 400
    #player2(player_2_x, player_2_y)
    #player1(player_1_x, player_1_y)
    pygame.display.update()
    clock.tick(60)



    #     #Tackler Movement
    #     if tackler_state is "fire":
    #         space_tackle(player1_x, tackler_x)
    #         tackler_x == tackler_x_movement

    #     #Tackler leaving screen and resetting
    #     if tackler_y <= 0:
    #         tackler_y = player1_y
        
    #     #Collision
    #     collision = isCollision(player_2_x, player_2_y, player_1_x, player_1_y)
    #     if collision:
    #         tackler_y = player1_y
    #         tackler_state = "ready"
    #         score += 1
    #         print(score)
    # show_score(textX,textY)

    # #def player_1_animation():
#     global player_1_image, player_1_run_right_index

#     if keys[pygame.K_d]:
#         player_1_run_right_index += 0.1
#         #Resets list if longer than variable
#         if player_1_run_right_index >= len(player_1_run_right_index): player_1_run_right_index = 0
#         player_1_image = player_1_image_run[int(player_1_run_right_index)]
            

# def space_tackle(x,y):
#     global tackler_state
#     tackler_state = "fire"
#     screen.blit(tacklerImg, (x + 16, y + 10))

# def isCollision(tackler_x, tackler_y, cpuplayer_x_movement, cpuplayer_y_movement):
#     distance = math.sqrt((math.pow(tackler_x - cpuplayer_x_movement, 2)) + (math.pow(tackler_y-cpuplayer_y_movement, 2)))
#     if distance < 27:
#         return True
#     else:
#         return False

# def show_score(x,y):
#     score = font.render("Score :" + str(score_value), True, (255,255,255))
#     screen.blit(score, (x, y))

# score_value = 0
# font = pygame.font.Font('freesansbold.ttf', 32)
# textX = 100
# textY = 100

# Game loop
#player_1_image_run_right_1 = pygame.image.load(r"C:\Users\Jeremy\Documents\GitHub\Python\Techmo\Pixel Art\Right\Running_1-1.png.png").convert()
#player_1_image_run_right_2 = pygame.image.load(r"C:\Users\Jeremy\Documents\GitHub\Python\Techmo\Pixel Art\Right\Running_1-2.png.png").convert()
#player_1_image_run_right_3 = pygame.image.load(r"C:\Users\Jeremy\Documents\GitHub\Python\Techmo\Pixel Art\Right\Running_1-3.png.png").convert()
#player_1_image_run_right_4 = pygame.image.load(r"C:\Users\Jeremy\Documents\GitHub\Python\Techmo\Pixel Art\Right\Running_1-4.png.png").convert()
#player_1_image_run_right_5 = pygame.image.load(r"C:\Users\Jeremy\Documents\GitHub\Python\Techmo\Pixel Art\Right\Running_1-5.png.png").convert()

#player_1_run_right = [player_1_image_run_right_1,player_1_image_run_right_2,player_1_image_run_right_3,player_1_image_run_right_4,player_1_image_run_right_5]
#player_1_run_right_index_rotation = 0
#player_1_image_run = player_1_run_right_index[0]