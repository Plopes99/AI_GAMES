from random import random
from turtle import color, width
import pygame 
import random
import math

pygame.init()

myfont = pygame.font.SysFont("monospace", 75)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
ORANGE = (255,140,0)
CYAN = (0,255,255)
BLACK = (0,0,0)
MAROON = (128,0,0)
SPACES = 49

win_size_y = 700
win_size_x = 940


win = pygame.display.set_mode((win_size_x, win_size_y))

pygame.display.set_caption("Tintas")

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
    pawn.draw(win, BLACK)
    

    pygame.display.update()





#mainloop
hex01 = hexagon(0, 0, 0, 0 ,50, 50, color, hex_sprite, False, 0, False)
hex02 = hexagon(0, 1, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex03 = hexagon(0, 2, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex04 = hexagon(0, 3, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex05 = hexagon(0, 4, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex06 = hexagon(0, 5, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex07 = hexagon(1, 0, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex08 = hexagon(1, 1, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex09 = hexagon(1, 2, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex10 = hexagon(1, 3, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex11 = hexagon(1, 4, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex12 = hexagon(1, 5, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex13 = hexagon(2, 0, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex14 = hexagon(2, 1, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex15 = hexagon(2, 2, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex16 = hexagon(2, 3, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex17 = hexagon(2, 4, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex18 = hexagon(2, 5, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex19 = hexagon(3, 0, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex20 = hexagon(3, 1, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex21 = hexagon(3, 2, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex22 = hexagon(3, 3, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex23 = hexagon(3, 4, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex24 = hexagon(3, 5, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex25 = hexagon(4, 0, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex26 = hexagon(4, 1, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex27 = hexagon(4, 2, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex28 = hexagon(4, 3, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex29 = hexagon(4, 4, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex30 = hexagon(4, 5, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex31 = hexagon(5, 0, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex32 = hexagon(5, 1, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex33 = hexagon(5, 2, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex34 = hexagon(5, 3, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex35 = hexagon(5, 4, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex36 = hexagon(5, 5, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex37 = hexagon(6, 0, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex38 = hexagon(6, 1, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex39 = hexagon(6, 2, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex40 = hexagon(6, 3, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex41 = hexagon(6, 4, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex42 = hexagon(6, 5, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex43 = hexagon(7, 0, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex44 = hexagon(7, 1, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex45 = hexagon(7, 2, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex46 = hexagon(7, 3, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex47 = hexagon(7, 4, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex48 = hexagon(7, 5, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
hex49 = hexagon(8, 0, 0, 0, 50, 50, color, hex_sprite, False, 0, False)
pawn =  hexagon(1, 1, 0, 0, 0, 0, BLACK, win , False, 0, False)


hex_list = [hex01, hex02, hex03, hex04, hex05, hex06, hex07, hex08, hex09, 
            hex10, hex11, hex12, hex13, hex14, hex15, hex16, hex17, hex18, hex19,
            hex20, hex21, hex22, hex23, hex24, hex25, hex26, hex27, hex28, hex29, 
            hex30, hex31, hex32, hex33, hex34, hex35, hex36, hex37, hex38, hex39,
            hex40, hex41, hex42, hex43, hex44, hex45, hex46, hex47, hex48, hex49, pawn]

color_list = [RED, RED, RED, RED, RED, RED, RED, 
BLUE, BLUE, BLUE, BLUE, BLUE, BLUE, BLUE,
GREEN, GREEN, GREEN, GREEN, GREEN, GREEN, GREEN,
YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW,
CYAN, CYAN, CYAN, CYAN, CYAN, CYAN, CYAN, 
ORANGE, ORANGE, ORANGE, ORANGE, ORANGE, ORANGE, ORANGE, 
WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE]

random.shuffle(color_list)

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
    for i in range(SPACES):
        if hex_list[i].isPlayed == False:
            continue
        if hex_list[i].isPlayed == True:
            pass

def play(col, row, posx, posy):
    colRand = random.randrange(5)
    rowRand = random.randrange(5)
    for i in range(SPACES):
        if turn == 0:
            if hex_list[i].coluna == col and hex_list[i].linha == row:
                hex_list[49].hitbox = (posx, posy, 30, 30)
                hex_list[i].isSelected = True
        elif turn == 1:
            if hex_list[i].coluna == colRand and hex_list[i].linha == rowRand:
                hex_list[49].hitbox = ((colRand *10), (rowRand * 10), 30 ,30)
                hex_list[i].isSelected = True


        pygame.display.update()


def check_win(result):
    Red_P1 = 0
    BLUE_P1 = 0
    WHITE_P1 = 0
    GREEN_P1 = 0
    YELLOW_P1 = 0
    ORANGE_P1 = 0
    CYAN_P1 = 0

    Red_P2 = 0
    BLUE_P2 = 0
    WHITE_P2 = 0
    GREEN_P2 = 0
    YELLOW_P2 = 0
    ORANGE_P2 = 0
    CYAN_P2 = 0
    p=0

    for i in range(SPACES):
        
        #check p1 wins
        if hex_list[i].player == 1 and hex_list[i].color == RED:
            Red_P1 += 1
        
        if hex_list[i].player == 1 and hex_list[i].color == BLUE:
            BLUE_P1 += 1
        
        if hex_list[i].player == 1 and hex_list[i].color == WHITE:
            WHITE_P1 += 1

        if hex_list[i].player == 1 and hex_list[i].color == GREEN:
            GREEN_P1 += 1
        
        if hex_list[i].player == 1 and hex_list[i].color == CYAN:
            CYAN_P1 += 1
        
        if hex_list[i].player == 1 and hex_list[i].color == ORANGE:
            ORANGE_P1 += 1

        if hex_list[i].player == 1 and hex_list[i].color == YELLOW:
            YELLOW_P1 += 1

        #Player2
        if hex_list[i].player == 2 and hex_list[i].color == RED:
            Red_P2 += 1
        
        if hex_list[i].player == 2 and hex_list[i].color == BLUE:
            BLUE_P2 += 1
        
        if hex_list[i].player == 2 and hex_list[i].color == WHITE:
            WHITE_P2 += 1

        if hex_list[i].player == 2 and hex_list[i].color == GREEN:
            GREEN_P2 += 1
        
        if hex_list[i].player == 2 and hex_list[i].color == CYAN:
            CYAN_P2 += 1
        
        if hex_list[i].player == 2 and hex_list[i].color == ORANGE:
            ORANGE_P2 += 1

        if hex_list[i].player == 2 and hex_list[i].color == YELLOW:
            YELLOW_P2 += 1

        if  Red_P1 == 7:
            return(True)
            print("Player 1 win!!")

        if  BLUE_P1 == 7:
            p=1
            return(p)
            print("Player 1 win!!")

        if  WHITE_P1 == 7:
            p=1
            return(p)
            print("Player 1 win!!")
        
        if  YELLOW_P1 == 7:
            p=1
            return(p)
            print("Player 1 win!!")

        if  ORANGE_P1 == 7:
            p=1
            return(p)
            print("Player 1 win!!")

        if  CYAN_P1 == 7:
            p=1
            return(p)
            print("Player 1 win!!")


        if  Red_P2 == 7:
            p=2
            return(p)
            print("Player 2 win!!")

        if  BLUE_P2 == 7:
            p=2
            return(p)
            print("Player 2 win!!")

        if  WHITE_P2 == 7:
            p=2
            return(p)
            print("Player 2 win!!")
        
        if  YELLOW_P2 == 7:
            p=2
            return(p)
            print("Player 2 win!!")

        if  ORANGE_P2 == 7:
            p=2
            return(p)
            print("Player 2 win!!")

        if  CYAN_P2 == 7:
            p=2
            return(p)
            print("Player 2 win!!")

        print(WHITE_P2)



    
def check_pieces(i):
    global turn
    if turn == 0:
        if i % 2 == 0 and i<25 :
            if hex_list[i].color == hex_list[i+1].color:
                hex_list[i+1].hitbox = (860, ((i+1)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+1].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-1].color:
                hex_list[i-1].hitbox = (860, ((i-1)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-1].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+6].color:
                hex_list[i+6].hitbox = (860, ((i+6)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+6].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+7].color:
                hex_list[i+7].hitbox = (860, ((i+7)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+7].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-6].color:
                hex_list[i-6].hitbox = (860, ((i-6)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-6].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-5].color:
                hex_list[i-5].hitbox = (860, ((i-5)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-5].player = 2
                hex_list[i].isPlayed = True

        if i % 2 == 1 and i<25:
            if hex_list[i].color == hex_list[i+1].color:
                hex_list[i+1].hitbox = (860, ((i+1)* 25) +8 , box_size/3, box_size/3)
                hex_list[i+1].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-1].color:
                hex_list[i-1].hitbox = (860, ((i-1)* 25) +8 , box_size/3, box_size/3)
                hex_list[i-1].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-6].color:
                hex_list[i-6].hitbox = (860, ((i-6)* 25) +8 , box_size/3, box_size/3)
                hex_list[i-6].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-7].color:
                hex_list[i-7].hitbox = (860, ((i-7)* 25) +8 , box_size/3, box_size/3)
                hex_list[i-7].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+6].color:
                hex_list[i+6].hitbox = (860, ((i+6)* 25) +8 , box_size/3, box_size/3)
                hex_list[i+6].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+5].color:
                hex_list[i+5].hitbox = (860, ((i+5)* 25) +8 , box_size/3, box_size/3)
                hex_list[i+5].player = 2
                hex_list[i].isPlayed = True

        if i % 2 == 0 and i>25 and i<43:
            if hex_list[i].color == hex_list[i+1].color:
                hex_list[i+1].hitbox = (890, ((i-24)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+1].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-1].color:
                hex_list[i-1].hitbox = (890, ((i-26)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-1].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+6].color:
                hex_list[i+6].hitbox = (890, ((i-19)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+6].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+7].color:
                hex_list[i+7].hitbox = (890, ((i-18)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+7].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-6].color:
                hex_list[i-6].hitbox = (890, ((i-31)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-6].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-5].color:
                hex_list[i-5].hitbox = (890, ((i-30)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-5].player = 2
                hex_list[i].isPlayed = True

        if i % 2 == 1 and i>25 and i<43:
            if hex_list[i].color == hex_list[i+1].color:
                hex_list[i+1].hitbox = (890, ((i-24)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+1].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-1].color:
                hex_list[i-1].hitbox = (890, ((i-26)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-1].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+6].color:
                hex_list[i+6].hitbox = (890, ((i-19)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+6].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+7].color:
                hex_list[i+7].hitbox = (890, ((i-18)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+7].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-6].color:
                hex_list[i-6].hitbox = (890, ((i-31)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-6].player = 2
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-5].color:
                hex_list[i-5].hitbox = (890, ((i-30)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-5].player = 2
                hex_list[i].isPlayed = True
        if i==48:
            if hex_list[i].color == hex_list[i-6].color:
                hex_list[i-6].hitbox = (890, ((i-6)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-6].player = 2
                hex_list[i].isPlayed = True

    if turn == 1:
        if i % 2 == 0 and i<25:
            if hex_list[i].color == hex_list[i+1].color:
                hex_list[i+1].hitbox = (740, ((i+1)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+1].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-1].color:
                hex_list[i-1].hitbox = (740, ((i-1)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-1].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+6].color:
                hex_list[i+6].hitbox = (740, ((i+6)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+6].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+7].color:
                hex_list[i+7].hitbox = (740, ((i+7)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+7].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-6].color:
                hex_list[i-6].hitbox = (740, ((i-6)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-6].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-5].color:
                hex_list[i-5].hitbox = (740, ((i-5)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-5].player = 1
                hex_list[i].isPlayed = True
            
        if i % 2 == 0 and i>25 and i<43:
            if hex_list[i].color == hex_list[i+1].color:
                hex_list[i+1].hitbox = (770, ((i-24)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+1].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-1].color:
                hex_list[i-1].hitbox = (770, ((i-26)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-1].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+6].color:
                hex_list[i+6].hitbox = (770, ((i-19)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+6].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+7].color:
                hex_list[i+7].hitbox = (770, ((i-18)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+7].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-6].color:
                hex_list[i-6].hitbox = (770, ((i-31)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-6].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-5].color:
                hex_list[i-5].hitbox = (770, ((i-30)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-5].player = 1
                hex_list[i].isPlayed = True


        if i % 2 == 1 and i>25 and i<43:
            if hex_list[i].color == hex_list[i+1].color:
                hex_list[i+1].hitbox = (770, ((i-24)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+1].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-1].color:
                hex_list[i-1].hitbox = (770, ((i-26)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-1].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+6].color:
                hex_list[i+6].hitbox = (770, ((i-19)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+6].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+7].color:
                hex_list[i+7].hitbox = (770, ((i-18)* 25) +10 , box_size/3, box_size/3)
                hex_list[i+7].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-6].color:
                hex_list[i-6].hitbox = (770, ((i-31)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-6].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-5].color:
                hex_list[i-5].hitbox = (770, ((i-30)* 25) +10 , box_size/3, box_size/3)
                hex_list[i-5].player = 1
                hex_list[i].isPlayed = True


        if i % 2 == 1 and i<25:
            if hex_list[i].color == hex_list[i+1].color:
                hex_list[i+1].hitbox = (740, ((i+1)* 25) +8 , box_size/3, box_size/3)
                hex_list[i+1].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-1].color:
                hex_list[i-1].hitbox = (740, ((i-1)* 25) +8 , box_size/3, box_size/3)
                hex_list[i-1].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-6].color:
                hex_list[i-6].hitbox = (740, ((i-6)* 25) +8 , box_size/3, box_size/3)
                hex_list[i-6].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i-7].color:
                hex_list[i-7].hitbox = (740, ((i-7)* 25) +8 , box_size/3, box_size/3)
                hex_list[i-7].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+6].color:
                hex_list[i+6].hitbox = (740, ((i+6)* 25) +8 , box_size/3, box_size/3)
                hex_list[i+6].player = 1
                hex_list[i].isPlayed = True
            if hex_list[i].color == hex_list[i+5].color:
                hex_list[i+5].hitbox = (740, ((i+5)* 25) +8 , box_size/3, box_size/3)
                hex_list[i+5].player = 1
                hex_list[i].isPlayed = True
        if i == 48:
            if hex_list[i].color == hex_list[i-6].color:
                hex_list[i-6].hitbox = (740, ((i-6)* 25) +8 , box_size/3, box_size/3)
                hex_list[i-6].player = 1
                hex_list[i].isPlayed = True



def move():
    
    global turn
    turn += 1
    turn = turn % 2
    for i in range(SPACES):
        if hex_list[i].isSelected and turn == 0 and not hex_list[i].isPlayed:
            if i < 25:    
                hex_list[i].hitbox = (860 , (i* 25) + 10 , box_size/3, box_size/3)
                hex_list[i].player = 2 
                check_pieces(i)        
            else:
                hex_list[i].hitbox = (890 , ((i-25)*25) + 10 , box_size/3, box_size/3)
                hex_list[i].player = 2 
                check_pieces(i)
            hex_list[i].isSelected = False
            hex_list[i].isPlayed = True

        elif hex_list[i].isSelected and turn == 1 and not hex_list[i].isPlayed:
            if i < 25:    
                hex_list[i].hitbox = (740 , (i* 25) + 10 , box_size/3, box_size/3)
                hex_list[i].player = 1
                check_pieces(i)  
            else:
                hex_list[i].hitbox = (770 , ((i-25)*25) + 10 , box_size/3, box_size/3)
                hex_list[i].player = 1
                check_pieces(i)
            hex_list[i].isSelected = False
            hex_list[i].isPlayed = True
    
    


    
        
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
