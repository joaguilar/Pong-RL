import pygame
import sys
from pygame.constants import QUIT, K_w
import torch
import random

def ball_restart(ball,
                ball_speed_x,
                ball_speed_y,
                screen_width,
                screen_height):
    ball.center = (
        screen_width/2-ball_size/2,
        screen_height/2-ball_size/2)
    ball_speed_x *= random.choice((1,-1)) 
    ball_speed_y *= random.choice((1,-1)) 
    return ball,ball_speed_x,ball_speed_y


def ball_animation(
    screen_width, 
    screen_height, 
    ball, 
    player1, 
    player2, 
    ball_speed_x, 
    ball_speed_y):
    # Move the ball:
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Collisions with the sides of the screen:
        if ball.top <= 0 or ball.bottom >= screen_height:
            ball_speed_y *= -1
        if ball.left <= 0  or ball.right >= screen_width:
            ball,ball_speed_x,ball_speed_y = ball_restart(
                                                            ball,
                                                            ball_speed_x,
                                                            ball_speed_y,
                                                            screen_width,
                                                            screen_height
                                                        )
        
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_speed_x *= -1
        return ball,ball_speed_x,ball_speed_y



def player_animation(screen_height, p, ps):
    if p.bottom >= screen_height:
        p.bottom = screen_height
    if p.top <= 0:
        p.top = 0

    p.y += ps

# Initialization
pygame.init()
clock = pygame.time.Clock()

#Main Window:
screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong-RL')

# Pong Ball:
ball_size = 30
ball = pygame.Rect(
    screen_width/2-ball_size/2,
    screen_height/2-ball_size/2,
    ball_size,ball_size
)

player_size_width = 10
player_size_heigth = 140
player1 = pygame.Rect(
    5,
    screen_height/2-player_size_heigth/2,
    player_size_width,
    player_size_heigth
)

player2 = pygame.Rect(
    screen_width-15,
    screen_height/2-player_size_heigth/2,
    player_size_width,
    player_size_heigth
)

bg_color = pygame.Color('grey12')

color = (255,255,255)

# Speed variables:
ball_speed_x = 7
ball_speed_y = 7

player_speed_1 = 0
player_speed_2 = 0
player_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed_2 += 7
            if event.key == pygame.K_UP:
                player_speed_2 -= 7
            if event.key == pygame.K_s:
                player_speed_1 += 7
            if event.key == pygame.K_w:
                player_speed_1 -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed_2 -= 7
            if event.key == pygame.K_UP:
                player_speed_2 += 7
            if event.key == pygame.K_s:
                player_speed_1 -= 7
            if event.key == pygame.K_w:
                player_speed_1 += 7

    player_animation(screen_height, player1, player_speed_1)
    player_animation(screen_height, player2, player_speed_2)

    ball,ball_speed_x,ball_speed_y = ball_animation(screen_width, screen_height, ball, player1, player2, ball_speed_x, ball_speed_y)
    

    #Visuals:
    screen.fill(bg_color) # Clears the screen
    pygame.draw.rect(screen,color,player1) 
    pygame.draw.rect(screen,color,player2) 
    pygame.draw.ellipse(screen,color,ball) # Draws an ellipse inside the rectangle, so it is a ball in this case
    # Draw a line to separate the fields:
    pygame.draw.aaline(screen,color,(screen_width/2,0),(screen_width/2,screen_height))

    
    pygame.display.flip() # Draw everything in the loop
    clock.tick(60) 

