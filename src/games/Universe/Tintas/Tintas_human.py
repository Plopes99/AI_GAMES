from random import random
from turtle import color, width
import pygame 
import random
import math

pygame.init()

myfont = pygame.font.SysFont("monospace", 75)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK =(0,0,0)
WHITE = (255,255,255)

SPACES = 49

win_size_y = 740
win_size_x = 1300


win = pygame.display.set_mode((win_size_x, win_size_y))

pygame.display.set_caption("Universe")

bg = pygame.image.load("images/bg.jpg")
hex_sprite = pygame.image.load("images/hex.png")
sprite = pygame.image.load("images/sprite.png")
pawn = pygame.image.load("images/pawn.png")

clock = pygame.time.Clock()

hitboxes = True
isSelected = False

turn = 0

class hexagon(object):
    def __init__(self, coluna, linha, x, y, width, height, color, sprite, isSelected, player, isPlayed):
        self.coluna = coluna
        self.linha = linha
        self.x = x
        self.y = y
        self.width = width
        self.color = color
        self.height = height
        self.sprite = sprite
        self.isSelected = isSelected
        self.player = player
        self.isPlayed = isPlayed
        self.hitbox = (self.x, self.y, width, height)
        

    
    def draw(self, win, color):
            win.blit(self.sprite, (self.x, self.y))
            if hitboxes == True:
                
                pygame.draw.rect(win, self.color, self.hitbox)



def redraw_game_window():
    
    win.blit(bg, (0, 0))
    win.blit(sprite,(0,0))
    hex01.draw(win, color)
    hex02.draw(win, color)
    hex03.draw(win, color)
    hex04.draw(win, color)
    hex05.draw(win, color)
    hex06.draw(win, color)
    hex07.draw(win, color)
    hex08.draw(win, color)
    hex09.draw(win, color)
    hex10.draw(win, color)
    hex11.draw(win, color)
    hex12.draw(win, color)
    hex13.draw(win, color)
    hex14.draw(win, color)
    hex15.draw(win, color)
    hex16.draw(win, color)
    hex17.draw(win, color)
    hex18.draw(win, color)
    hex19.draw(win, color)
    hex20.draw(win, color)
    hex21.draw(win, color)
    hex22.draw(win, color)
    hex23.draw(win, color)
    hex24.draw(win, color)
    hex25.draw(win, color)
    hex26.draw(win, color)
    hex27.draw(win, color)
    hex28.draw(win, color)
    hex29.draw(win, color)
    hex30.draw(win, color)
    hex31.draw(win, color)
    hex32.draw(win, color)
    hex33.draw(win, color)
    hex34.draw(win, color)
    hex35.draw(win, color)
    hex36.draw(win, color)
    hex37.draw(win, color)
    hex38.draw(win, color)
    hex39.draw(win, color)
    hex40.draw(win, color)
    hex41.draw(win, color)
    hex42.draw(win, color)
    hex43.draw(win, color)
    hex44.draw(win, color)
    hex45.draw(win, color)
    hex46.draw(win, color)
    hex47.draw(win, color)
    hex48.draw(win, color)
    hex49.draw(win, color)
    hex50.draw(win, color)
    hex51.draw(win, color)
    hex52.draw(win, color)
    hex53.draw(win, color)
    hex54.draw(win, color)
    hex55.draw(win, color)
    hex56.draw(win, color)
    hex57.draw(win, color)
    hex58.draw(win, color)
    hex59.draw(win, color)
    hex60.draw(win, color)
    hex61.draw(win, color)
    hex62.draw(win, color)
    hex63.draw(win, color)
    hex64.draw(win, color)
    hex65.draw(win, color)
    hex66.draw(win, color)
    hex67.draw(win, color)
    hex68.draw(win, color)
    hex69.draw(win, color)
    hex70.draw(win, color)
    hex71.draw(win, color)
    hex72.draw(win, color)
    hex73.draw(win, color)
    hex74.draw(win, color)
    hex75.draw(win, color)
    hex76.draw(win, color)
    hex77.draw(win, color)
    hex78.draw(win, color)
    hex79.draw(win, color)
    hex80.draw(win, color)
    hex81.draw(win, color)
    hex82.draw(win, color)
    hex83.draw(win, color)
    hex84.draw(win, color)
    hex85.draw(win, color)
    hex86.draw(win, color)
    hex87.draw(win, color)
    hex87.draw(win, color)
    hex88.draw(win, color)
    hex89.draw(win, color)
    hex90.draw(win, color)
    hex91.draw(win, color)
    hex92.draw(win, color)
    hex93.draw(win, color)
    hex94.draw(win, color)
    hex95.draw(win, color)
    hex96.draw(win, color)
    hex97.draw(win, color)
    hex98.draw(win, color)
    hex99.draw(win, color)
    hex100.draw(win, color)
    hex101.draw(win, color)
    hex102.draw(win, color)
    hex103.draw(win, color)
    hex104.draw(win, color)
    hex105.draw(win, color)
    hex106.draw(win, color)
    hex107.draw(win, color)
    hex108.draw(win, color)
    hex109.draw(win, color)
    hex110.draw(win, color)
    hex111.draw(win, color)
    hex112.draw(win, color)
    hex113.draw(win, color)
    hex114.draw(win, color)
    hex115.draw(win, color)
    hex116.draw(win, color)
    hex117.draw(win, color)
    hex118.draw(win, color)
    hex119.draw(win, color)
    hex120.draw(win, color)
    hex121.draw(win, color)
    hex122.draw(win, color)
    hex123.draw(win, color)
    hex124.draw(win, color)
    hex125.draw(win, color)
    hex126.draw(win, color)
    hex127.draw(win, color)
    hex128.draw(win, color)
    hex129.draw(win, color)
    hex130.draw(win, color)
    hex131.draw(win, color)
    hex132.draw(win, color)
    hex133.draw(win, color)
    hex134.draw(win, color)
    hex135.draw(win, color)
    hex136.draw(win, color)
    hex137.draw(win, color)
    hex138.draw(win, color)
    hex139.draw(win, color)
    hex140.draw(win, color)
    hex141.draw(win, color)
    hex142.draw(win, color)
    hex143.draw(win, color)
    hex144.draw(win, color)
    hex145.draw(win, color)
    hex146.draw(win, color)
    hex147.draw(win, color)
    hex148.draw(win, color)
    hex149.draw(win, color)
    hex150.draw(win, color)
    hex151.draw(win, color)
    hex152.draw(win, color)
    hex153.draw(win, color)
    hex154.draw(win, color)
    hex155.draw(win, color)
    hex156.draw(win, color)
    hex157.draw(win, color)
    hex158.draw(win, color)
    hex159.draw(win, color)
    hex160.draw(win, color)
    hex161.draw(win, color)
    hex162.draw(win, color)
    hex163.draw(win, color)
    hex164.draw(win, color)
    hex165.draw(win, color)
    hex166.draw(win, color)
    hex167.draw(win, color)
    hex168.draw(win, color)
    hex169.draw(win, color)
    hex170.draw(win, color)
    hex171.draw(win, color)
    hex172.draw(win, color)
    hex173.draw(win, color)
    hex174.draw(win, color)
    hex175.draw(win, color)
    hex176.draw(win, color)
    hex177.draw(win, color)
    hex178.draw(win, color)
    hex179.draw(win, color)
    hex180.draw(win, color)
    hex181.draw(win, color)
    hex182.draw(win, color)
    hex183.draw(win, color)
    hex184.draw(win, color)
    hex185.draw(win, color)
    hex186.draw(win, color)
    hex187.draw(win, color)
    hex188.draw(win, color)
    hex189.draw(win, color)
    hex190.draw(win, color)
    hex191.draw(win, color)
    hex192.draw(win, color)
    hex193.draw(win, color)
    hex194.draw(win, color)
    hex195.draw(win, color)
    hex196.draw(win, color)
    hex197.draw(win, color)
    hex198.draw(win, color)
    hex199.draw(win, color)
    

    pygame.display.update()





#mainloop
hex01 = hexagon(0, 0, 0, 0 ,10, 10, color, hex_sprite, False, 0, False)
hex02 = hexagon(0, 1, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex03 = hexagon(0, 2, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex04 = hexagon(0, 3, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex05 = hexagon(0, 4, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex06 = hexagon(1, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex07 = hexagon(1, 1, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex08 = hexagon(1, 2, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex09 = hexagon(1, 3, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex10 = hexagon(1, 4, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex11 = hexagon(1, 5, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex12 = hexagon(1, 6, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex13 = hexagon(1, 7, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex14 = hexagon(1, 8, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex15 = hexagon(1, 9, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex16 = hexagon(2, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex17 = hexagon(2, 1, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex18 = hexagon(2, 2, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex19 = hexagon(2, 3, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex20 = hexagon(2, 4, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex21 = hexagon(2, 5, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex22 = hexagon(2, 6, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex23 = hexagon(2, 7, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex24 = hexagon(2, 8, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex25 = hexagon(2, 9, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex26 = hexagon(3, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex27 = hexagon(3, 1, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex28 = hexagon(3, 2, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex29 = hexagon(3, 3, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex30 = hexagon(3, 4, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex31 = hexagon(3, 5, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex32 = hexagon(3, 6, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex33 = hexagon(3, 7, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex34 = hexagon(3, 8, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex35 = hexagon(3, 9, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex36 = hexagon(3, 10, 0, 0,150,150, color, hex_sprite, False, 0, False)
hex37 = hexagon(3, 11, 0, 0,150,150, color, hex_sprite, False, 0, False)
hex38 = hexagon(3, 12, 0, 0,150,150, color, hex_sprite, False, 0, False)
hex39 = hexagon(3, 13, 0, 0,150,150, color, hex_sprite, False, 0, False)
hex40 = hexagon(4, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex41 = hexagon(4, 1, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex42 = hexagon(4, 2, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex43 = hexagon(4, 3, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex44 = hexagon(4, 4, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex45 = hexagon(4, 5, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex46 = hexagon(4, 6, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex47 = hexagon(4, 7, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex48 = hexagon(4, 8, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex49 = hexagon(4, 9, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex50 = hexagon(4, 10, 0, 0,150,150, color, hex_sprite, False, 0, False)
hex51 = hexagon(4, 11, 0, 0,150,150, color, hex_sprite, False, 0, False)
hex52 = hexagon(4, 12, 0, 0,150,150, color, hex_sprite, False, 0, False)
hex53 = hexagon(4, 13, 0, 0,150,150, color, hex_sprite, False, 0, False)
hex54 = hexagon(5, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex55 = hexagon(5, 1, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex56 = hexagon(5, 2, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex57 = hexagon(5, 3, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex58 = hexagon(5, 4, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex59 = hexagon(5, 5, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex60 = hexagon(5, 6, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex61 = hexagon(5, 7, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex62 = hexagon(5, 8, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex63 = hexagon(5, 9, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex64 = hexagon(5, 10, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex65 = hexagon(5, 11, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex66 = hexagon(5, 12, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex67 = hexagon(5, 13, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex68 = hexagon(5, 14, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex69 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex70 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex71 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex72 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex73 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex74 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex75 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex76 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex77 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex78 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex79 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex80 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex81 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex82 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex83 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex84 = hexagon(6, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex85 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex86 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex87 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex87 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex88 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex89 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex90 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex91 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex92 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex93 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex94 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex95 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex96 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex97 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex98 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex99 = hexagon(7, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex100 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex101 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex102 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex103 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex104 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex105 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex106 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex107 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex108 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex109 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex110 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex111 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex112 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex113 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex114 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex115 = hexagon(8, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex116 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex117 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex118 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex119 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex120 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex121 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex122 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex123 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex124 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex125 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex126 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex127 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex128 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex129 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex130 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex131 = hexagon(9, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex132 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex133 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex134 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex135 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex136 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex137 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex138 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex139 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex140 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex141 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex142 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex143 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex144 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex145 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex146 = hexagon(10, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex147 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex148 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex149 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex150 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex151 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex152 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex153 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex154 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex155 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex156 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex157 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex158 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex159 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex160 = hexagon(11, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex161 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex162 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex163 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex164 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex165 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex166 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex167 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex168 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex169 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex170 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex171 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex172 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex173 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex174 = hexagon(12, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex175 = hexagon(13, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex176 = hexagon(13, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex177 = hexagon(13, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex178 = hexagon(13, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex179 = hexagon(13, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex180 = hexagon(13, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex181 = hexagon(13, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex182 = hexagon(13, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex183 = hexagon(13, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex184 = hexagon(13, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex185 = hexagon(14, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex186 = hexagon(14, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex187 = hexagon(14, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex188 = hexagon(14, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex189 = hexagon(14, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex190 = hexagon(14, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex191 = hexagon(14, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex192 = hexagon(14, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex193 = hexagon(14, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex194 = hexagon(14, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex195 = hexagon(15, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex196 = hexagon(15, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex197 = hexagon(15, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex198 = hexagon(15, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)
hex199 = hexagon(15, 0, 0, 0, 10, 10, color, hex_sprite, False, 0, False)





hex_list = [hex01, hex02, hex03, hex04, hex05, hex06, hex07, hex08, hex09,
            hex10, hex11, hex12, hex13, hex14, hex15, hex16, hex17, hex18, hex19,
            hex20, hex21, hex22, hex23, hex24, hex25, hex26, hex27, hex28, hex29, 
            hex30, hex31, hex32, hex33, hex34, hex35, hex36, hex37, hex38, hex39,
            hex40, hex41, hex42, hex43, hex44, hex45, hex46, hex47, hex48, hex49,
            hex50, hex51, hex52, hex53, hex54, hex55, hex56, hex57, hex58, hex59,
            hex60, hex61, hex62, hex63, hex64, hex65, hex66, hex67, hex68, hex69,
            hex70, hex71, hex72, hex73, hex74, hex75, hex76, hex77, hex78, hex79,
            hex80, hex81, hex82, hex83, hex84, hex85, hex86, hex87, hex87, hex88,
            hex89, hex90, hex91, hex92, hex93, hex94, hex95, hex96, hex97, hex98,
            hex99, hex100, hex101, hex102, hex103, hex104, hex105, hex106, hex107,
            hex108, hex109, hex110, hex111, hex112, hex113, hex114, hex115, hex116,
            hex117, hex118, hex119, hex120, hex121, hex122, hex123, hex124, hex125,
            hex126, hex127, hex128, hex129, hex130, hex131, hex132, hex133, hex134,
            hex135, hex136, hex137, hex138, hex139, hex140, hex141, hex142, hex143,
            hex144, hex145, hex146, hex147, hex148, hex149, hex150, hex151, hex152,
            hex153, hex154, hex155, hex156, hex157, hex158, hex159, hex160, hex161,
            hex162, hex163, hex164, hex165, hex166, hex167, hex168, hex169, hex170,
            hex171, hex172, hex173, hex174, hex175, hex176, hex177, hex178, hex179,
            hex180, hex181, hex182, hex183, hex184, hex185, hex186, hex187, hex188,
            hex189, hex190, hex191, hex192, hex193, hex194, hex195, hex196, hex197,
            hex198, hex199 ]

color_list = [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
              WHITE, WHITE ]


hex_column = 0
hex_row = 0
box_size = 66


for i in range(49):
    if not hex_column % 2 or hex_column == 0:
        hex_list[i].x = hex_column * 75
        hex_list[i].y = hex_row * 100
        hex_list[i].color = color_list[i]
        
        
    if hex_column % 2:
        hex_list[i].x = hex_column * 75
        hex_list[i].y = (hex_row * 100) + 50
        hex_list[i].color = color_list[i]
    hex_row += 1

    if hex_row >= 6:
        hex_column += 1
        hex_row = 0 
for i in range(49):
    hex_list[i].hitbox = (hex_list[i].x + 22 , hex_list[i].y + 20, box_size, box_size)
    

def is_play_valid(col,row):
    pass

def play(col, row, posx, posy):

    for i in range(SPACES):
        if hex_list[i].coluna == col and hex_list[i].linha == row:
            hex_list[49].hitbox = (posx, posy, 30, 30)
            hex_list[i].isSelected = True

        pygame.display.update()


def check_win(result):
    pass

def check_pieces(i):
    pass




def move():
    pass


    
        
pygame.display.update() 

def main():
    run = True
    result = False 
    while run:
        clock.tick(27)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                
                
                
                col = int(math.floor((posx ) /(box_size + 13 )))
                #Colunas Pares
                if col % 2 == 0:
                    row = int(math.floor((posy) /100))
                #Colunas Impares
                else:
                    row = int(math.floor((posy - box_size) /(100)))
                

                play(col, row, posx, posy)
                move()
                if check_win(result) == 1:
                    label = myfont.render("Player 1 wins!!", 1 , BLACK)
                    win.blit(label, (40,400))
                    run = False
                elif check_win(result) == 2:
                    label = myfont.render("Player 2 wins!!", 1 , BLACK)
                    win.blit(label, (40,400))
                    run = False
                pygame.display.update()
                
                if not run:
                    pygame.time.wait(3000)


        pygame.display.update()
        redraw_game_window()
    pygame.quit
main()           
