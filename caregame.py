#importing pygame module
#befor importing ,you have to install it in system
#installing code >>>pip install pygame  in cmd or powershell or terminal

import pygame as pg
from random import randint
pg.font.init()
pg.mixer.init()


def player():
    screen.blit(cars_img[0], (player_x - int(car_x / 2), player_y - int(car_y / 2)))


def enemies():
    screen.blit(cars_img[1], (enemies_x - 115, enemy1_y))
    screen.blit(cars_img[2], (enemies_x - int(car_x / 2), enemy2_y))
    screen.blit(cars_img[3], (enemies_x + 60, enemy3_y))


def text(txt_msg, txt_color, txt_size, txt_x, txt_y):
    font = pg.font.SysFont('arial', txt_size, True)
    txt = font.render(txt_msg, True, txt_color)
    screen.blit(txt, (txt_x, txt_y))


'COLORS (RGB)'
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

'WINDOW'
wid, hei = 400, 500
screen = pg.display.set_mode((wid, hei))
pg.display.set_caption('PyCar')

'SPRITE SIZE'
car_x, car_y = 54, 94

'PLAYER'
player_x, player_y = int(wid / 2), int(hei - 50)
player_spd = 5

'ENEMIES'
enemies_x = int(wid / 2)
enemy1_y = randint(-hei, -car_y)  # Posição do carro vermelho (lado esquerdo).
enemy2_y = randint(-hei, -car_y)  # Posição do carro amarelo (lado direito).
enemy3_y = randint(-hei, -car_y)  # Posição do carro azul (centro).
enemies_spd = 0

'IMAGES'
bg = pg.image.load('road.png').convert()
bg = pg.transform.scale(bg, (wid, hei))
bg_y = 0
cars_img = [pg.image.load('Player_Car.png'),
            pg.image.load('Enemy1_Car.png'),
            pg.image.load('Enemy2_Car.png'),
            pg.image.load('Enemy3_Car.png')]

'MUSIC'
pg.mixer_music.load('Chillwave_Nightdrive.mp3')
pg.mixer_music.play(-1)

#'SOUND EFFECT'
#car_collision = pg.mixer.Sound('assets/sounds/sound_effects/Car_Collision.wav')

clock = pg.time.Clock()
score = 1
score_spd = 0
main = True
while main:
    clock.tick(60)
    # bg_y = 0
    # --- Faz com que a imagem de background se repita, deslizando de cima para baixo --- #
    bg_y1 = bg_y % bg.get_height()
    bg_y += 3
    screen.blit(bg, (0, bg_y1 - bg.get_height()))
    if bg_y1 < hei:
        screen.blit(bg, (0, bg_y1))

    player()
    enemies()

    pg.draw.rect(screen, white, (0, 0, 54, 20))
    text('S: ' + str(score), black, 15, 0, 0)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            main = False

    'CONTROLS'
    arrows = pg.key.get_pressed()
    if arrows[pg.K_RIGHT] and player_x <= 290:
        player_x += player_spd
    if arrows[pg.K_LEFT] and player_x >= 110:
        player_x -= player_spd

    'ENEMIES SPEED'
    enemy1_y += enemies_spd + 5
    enemy2_y += enemies_spd + 2
    enemy3_y += enemies_spd + 4

    # --- Os inimigos aparecem, aleatoriamente, fora do background após sair do mesmo --- #
    if enemy1_y > hei:
        enemy1_y = randint(-2500, - 2000)
    if enemy2_y > hei:
        enemy2_y = randint(-1000, -750)
    if enemy3_y > hei:
        enemy3_y = randint(-1750, -1250)

    'SCORE'
    if score_spd <= 60:
        score_spd += 1
    else:
        score += 1
        score_spd = 0

    'COLLISION'
    if player_x - 40 > enemies_x and player_y - 140 < enemy3_y:  # Lado direito.
        car_collision.play()
        score -= 10
        enemy3_y = randint(-1750, -1250)
    if player_x + 40 < enemies_x and player_y - 140 < enemy1_y:  # Lado esquerdo.
        car_collision.play()
        score -= 10
        enemy1_y = randint(-2500, - 2000)
    if player_x - 40 < enemies_x + 10 and player_y - 140 < enemy2_y:  # Centro.
        if player_x + 40 > enemies_x - 10 and player_y - 140 < enemy2_y:
            car_collision.play()
            score -= 10
            enemy2_y = randint(-1000, -750)

    if score <= 0:
        break

    pg.display.update()

pg.quit()
