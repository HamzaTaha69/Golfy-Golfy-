import random

import pygame
from pygame.locals import *

from pygame import mixer

pygame.init()

game_name = "Golfy Golfy"

WIDTH = 1000
HEIGHT = 1000

BLACK = 0, 0, 0
WHITE = 250, 250, 250

score = "___"

sx = 130
sy = 50
x = WIDTH / 2 - sx / 2
y = HEIGHT / 2 - sy / 2

spawn_x = WIDTH / 2 - sx / 2
spawn_y = HEIGHT / 2 - sy / 2

rx = random.randint((sx / 2.5), (WIDTH - (sx / 2.5)))
ry = random.randint(sy, (WIDTH - sy))

shots = 0

hidden_shots = 0

coin_shots = 0

coins = 0

start = False

LEVEL = 0

forceX = 0
forceY = 0

FPS = 60

font = pygame.font.SysFont(None, 40)

home_screen_font = pygame.font.SysFont(None, 100)

max_distance = 100

shoot = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(game_name)

vel_x = 0
vel_y = 0

floor = pygame.image.load("images/ground/area1.svg")
floor = pygame.transform.scale(floor, (WIDTH * 1.2, HEIGHT * 1.2))

ball_img = pygame.image.load("images/sprites/ball1.svg")
ball_img = pygame.transform.scale(ball_img, (sx, sy))

ball = pygame.Rect(x, y, (sx / 2.5), sy)

hole = pygame.Rect(rx, ry, sx / 2.5, sy)

flag = pygame.image.load("images/sprites/flag1.svg")
flag = pygame.transform.scale(flag, ((sx / 2.5) * 2, sy * 2))

title = pygame.image.load("images/title screen/title.svg")
title = pygame.transform.scale(title, ((WIDTH * 1.2), (HEIGHT * 1.2)))

crs = pygame.Rect(10, 10, 5, 5)

map2_img = pygame.image.load("images/title screen/map2 button.svg")
map2_button = map2_img.get_rect(center=(WIDTH / 2 - 350, 300))

map1_img = pygame.image.load("images/title screen/map1 button.svg")
map1_button = map2_img.get_rect(center=(WIDTH / 2 - 350, 200))

def draw_game():
    screen.blit(floor, (-40, -40))
    screen.blit(ball_img, (x - (sx / 1.65), y - (sy / 25)))
    screen.blit(flag, (rx - 40, ry - 50))
    game_UI(BLACK)
    pygame.display.update()
    
def home_screen():
    screen.blit(title, (-75, -40))
    screen.blit(map2_img, (map2_button.x, map2_button.y))
    screen.blit(map1_img, (map1_button.x, map1_button.y))
    home_screen_UI(WHITE)
    pygame.display.update()
    
def home_screen_UI(color):
    home_screen_text = home_screen_font.render(game_name, True, color)
    screen.blit(home_screen_text, (WIDTH / 2 - 180, HEIGHT / 2 + 200))
    home_screen_text = home_screen_font.render("Click Anywhere to Start", True, BLACK)
    screen.blit(home_screen_text, (WIDTH / 2 - 400, HEIGHT / 2 + 350))
    home_screen_text = home_screen_font.render("You scored", True, BLACK)
    screen.blit(home_screen_text, (WIDTH / 2 - 280, HEIGHT / 2 - 450))
    home_screen_text = home_screen_font.render(str(hidden_shots), True, BLACK)
    screen.blit(home_screen_text, (WIDTH / 2 + 100, HEIGHT / 2 - 450))
    home_screen_text = home_screen_font.render("times", True, BLACK)
    screen.blit(home_screen_text, (WIDTH / 2 + 180, HEIGHT / 2 - 450))
    home_screen_text = font.render("MAP2", True, "BLUE")
    screen.blit(home_screen_text, (map2_button.x + 40, map2_button.y + 30))
    home_screen_text = font.render("MAP1", True, "BLUE")
    screen.blit(home_screen_text, (map1_button.x + 40, map1_button.y + 30))
    home_screen_text = home_screen_font.render(str(round(coins)), True, BLACK)
    screen.blit(home_screen_text, (WIDTH / 2 - 100, HEIGHT / 2 + 150))
    home_screen_text = home_screen_font.render("coins", True, BLACK)
    screen.blit(home_screen_text, (WIDTH / 2 - 50, HEIGHT / 2 + 150))
    pygame.display.update()
    
def restart():
    global rx
    global ry
    global x
    global y
    global shots
    global forceX
    global forceY
    global LEVEL
    global hidden_shots
    global score
    rx = 0
    ry = 0
    x = 0
    y = 0
    shots = 0
    forceX = 0
    forceY = 0
    LEVEL = 0
    score = 0
    
def hole_system():
    global shoot_in
    global rx
    global ry
    global x
    global y
    global shots
    global forceX
    global forceY
    global LEVEL
    if ball.colliderect(hole):
        LEVEL += 1
        rx = random.randint((sx / 2.5), (WIDTH - (sx / 2.5)))
        ry = random.randint(sy, (WIDTH - sy))
        x = spawn_x
        y = spawn_y
        forceX = 0
        forceY = 0
        shots = 0
    if ball.colliderect(hole):
        shoot_in = mixer.Sound("music/sound effect/win.wav")
        shoot_in.set_volume(1000)
        shoot_in.play()
        
    hole.x = rx
    hole.y = ry

def ball_physics():
    global ball_hit
    global x
    global y
    global forceX
    global forceY
    global vel_x
    global vel_y
    mx, my = pygame.mouse.get_pos()
    
    if mx > (x):
        vel_x = ((mx - x) / 80)
        
    if mx < (x):
        vel_x = (((mx - x) * -1) / 80)
        
    if my > (y):
        vel_y = ((my - y) / 80)
        
    if my < (y):
        vel_y = (((my - y) * -1) / 80)
    
    if shoot == False:
        if forceX < max_distance:
            forceX += vel_x
            
        if forceY < max_distance:
            forceY += vel_y
    else:
        if shoot == True:
            if mx < x - 40:                
                x += forceX
            else:
                x -= forceX
                
            if my < y - 40:
                y += forceY
            else:
                y -= forceY
            
            if forceX > 0:
                forceX -= 10
            else:
                forceX = 0
                
            if forceY > 0:
                forceY -= 10
            else:
                forceY = 0
                
    if x > WIDTH or x < 0 or y > HEIGHT or y < 0:
        x = spawn_x
        y = spawn_y
        forceX = 0
        forceY = 0
        
    if shoot == True:
        if forceX > 0 or forceY > 0:
            ball_hit = mixer.Sound("music/sound effect/hitting ball.wav")
            ball_hit.set_volume(5)
            ball_hit.play()
    
    ball.x = x
    ball.y = y

def game_UI(color):
    screen_text = font.render("level:", True, color)
    screen.blit(screen_text, (100, 100))
    screen_text = font.render(str(LEVEL), True, color)
    screen.blit(screen_text, (175, 100))
    screen_text = font.render("shots:", True, color)
    screen.blit(screen_text, (450, 100))
    screen_text = font.render(str(shots), True, color)
    screen.blit(screen_text, (535, 100))
    screen_text = font.render("score:", True, color)
    screen.blit(screen_text, (700, 100))
    screen_text = font.render(str(score), True, color)
    screen.blit(screen_text, (785, 100))
    pygame.display.update()
    
def coin_system():
    global coins
    global coin_shots
    if coin_shots < 10:
        coins += coin_shots * 3
        coin_shots = 0
    else:
        if coin_shots > 10:
            coins += coin_shots / 3
            coin_shots = 0
        else:
            if coins == 10:
                coins += 4
                coin_shots = 0
    
def score_system():
    global shots
    global hidden_shots
    global score
    if ball.colliderect(hole):
        if shots < 3:
            score = "par"
        if shots > 3:
            score = "bride"
        if shots > 6:
            score = "bogey"
        if shots > 9:
            score = "double bogey"
        if shots > 12:
            score = "triple bogey"
        if shots > 15:
            score = "dros"
        if shots > 18:
            score = "double dros"
        if shots > 22:
            score = "triple dros"
        if shots > 25:
            score = "hamboge"
        if shots > 30:
            score = "double hamboge"
        if shots > 36:
            score = "triple hamboge"
        if shots > 40:
            score = "vague"
        if shots > 45:
            score = "double vague"
        if shots > 52:
            score = "triple vague"
        if shots > 56:
            score = "fee"
        if shots > 62:
            score = "double fee"
        if shots > 68:
            score = "triple fee"
        if shots > 71:
            score = "gaffe"
        if shots > 75:
            score = "double gaffe"
        if shots > 80:
            score = "triple gaffe"
        if shots > 85:
            score = "trustee"
        if shots > 93:
            score = "double trustee"
        if shots > 99:
            score = "triple trustee"
        if shots > 108:
            score = "jesti"
        if shots > 114:
            score = "double jesti"
        if shots > 124:
            score = "triple jesti"
        if shots > 130:
            score = "hingk"
        if shots > 137:
            score = "double hingk"
        if shots > 144:
            score = "triple hingk"
        if shots > 150:
            score = "zeroc"
        if shots > 157:
            score = "double zeroc"
        if shots > 164:
            score = "triple zeroc"
        if shots > 170:
            score = "jobc"
        if shots > 177:
            score = "double jobc"
        if shots > 185:
            score = "triple jobc"
        if shots > 193:
            score = "korane"
        if shots > 202:
            score = "double korane"
        if shots > 211:
            score = "triple korane"
            
def level_system():
    global LEVEL
    
def shopUI():
    screen_text = font.render("You need 50 coins", True, BLACK)
    screen.blit(screen_text, (400, 400))
    pygame.display.update()
    
def game_loop():
    global floor
    global coins
    global shots
    global shoot
    global hidden_shots
    global start
    global coin_shots
    gameClock = pygame.time.Clock()
    gameRun = True
    while gameRun == True:
        MX, MY = pygame.mouse.get_pos()
        gameClock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRun = False
                
            if start == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shoot = False
                    shots += 1
                    hidden_shots += 1
                else:
                    if event.type == pygame.MOUSEBUTTONUP:
                        shoot = True
                    
        if start == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if crs.colliderect(map2_button):
                    if coins > 50:
                        coins -= 50
                        floor = pygame.image.load("images/ground/area2.svg")
                        floor = pygame.transform.scale(floor, (WIDTH * 1.2, HEIGHT * 1.2))
                        hidden_shots = 0
                        start = True
                    else:
                        noEffect = mixer.Sound("music/sound effect/no.wav")
                        noEffect.play()
                        shopUI()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if crs.colliderect(map1_button):
                    floor = pygame.image.load("images/ground/area1.svg")
                    floor = pygame.transform.scale(floor, (WIDTH * 1.2, HEIGHT * 1.2))
                    hidden_shots = 0
                    start = True
                
        if LEVEL > 4:
            start = False
    
        if start == True:
            game_UI(BLACK)
            score_system()
            hole_system()
            ball_physics()
            draw_game()
            level_system()
            coin_shots = hidden_shots
            
        else:
            if start == False:
                home_screen()
                restart()
                home_screen_UI(WHITE)
                coin_system()
                crs.x = MX
                crs.y = MY
     
    pygame.quit()
    
if __name__ == "__main__":
    game_loop()