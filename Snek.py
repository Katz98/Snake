import pygame
import time
import random

pygame.init()
 
 
my_width = 800
my_height  = 600
dis = pygame.display.set_mode((my_width, my_height))
pygame.display.set_caption('Game Snake')
 
game_over = False
 
# Current position
my_x = 0
my_y = 0

food_x = random.randint(0,80)*10
food_y = random.randint(0,60)*10

snake_size= 20
food_size = 20
# Amount of change
x_move = 0
y_move = 0
 
t = pygame.time.Clock()
speed=25

score = 0 # score for the game

font_style = pygame.font.SysFont(None, 52)
 
def message(msg):
    m = font_style.render(msg, True, (255, 0, 0))
    dis.blit(m, [my_width/3, my_height/2])
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_move = -10
                y_move = 0
            elif event.key == pygame.K_RIGHT:
                x_move = 10
                y_move = 0
            elif event.key == pygame.K_UP:
                x_move = 0
                y_move = -10
            elif event.key == pygame.K_DOWN:
                x_move = 0
                y_move = 10
               

    if my_x >= my_width or my_x < 0 or my_y >= my_height or my_y < 0:
        game_over = True

    my_x = my_x + x_move
    my_y = my_y + y_move
    

    dis.fill((255, 255, 255))
    pygame.draw.rect(dis, (0,0,0), [my_x, my_y, snake_size, snake_size])
    pygame.draw.rect(dis, (255,0,0), [food_x , food_y, food_size, food_size]) # making the food 

    if my_x == food_x and my_y == food_y:
        food_x = random.randint(0,80)*10
        food_y = random.randint(0,60)*10       # moving the food each time its eaten
        score = score + 1
        print("your score is", score)          # score increases everytime the snake eats it
        
    pygame.display.update()
 
    t.tick(speed)
 
message("Game Over")
pygame.display.update()
time.sleep(3)
 
pygame.quit()
quit()
