import pygame
import copy

WHITE = (255, 255, 255)
BLUE = (189,0,200)
# Define the Blokus pieces using a 2D array
board = [
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None,None,None, None,None,None]]


pieces = {
    "I": [
        [1, 1, 1, 1]
    ],
    "O": [
        [1, 1],
        [1, 1]
    ],
    "T": [
        [0, 1, 0],
        [1, 1, 1]
    ],
    "S": [
        [0, 1, 1],
        [1, 1, 0]
    ],
    "Z": [
        [1, 1, 0],
        [0, 1, 1]
    ],
    "L": [
        [1, 0, 0],
        [1, 1, 1]
    ],
    "J": [
        [0, 0, 1],
        [1, 1, 1]
    ],
    "F": [
        [0, 1, 1],
        [1, 1, 0],
        [0, 1, 0]
    ],
    "X": [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    "P": [
        [1, 1],
        [1, 0],
        [1, 1]
    ],
    "Y": [
        [1, 0],
        [1, 1],
        [0, 1],
        [0, 1]
    ],
    "N": [
        [1, 0, 0],
        [1, 1, 1],
        [0, 0, 1]
    ],
    "U": [
        [1, 0, 1],
        [1, 1, 1]
    ]
}

# Initialize Pygame
pygame.init()

# Set the screen size and create a new Pygame window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the background color of the window
BACKGROUND_COLOR = (255, 255, 255)

# Define the colors for each player
PLAYER_COLORS = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255)
}

# Set the size of each cell in the grid
CELL_SIZE = 50

# Define the size of the game board
BOARD_WIDTH = 20
BOARD_HEIGHT = 20

# Define a function to draw a Blokus piece on the screen
def draw_piece(piece, x, y, color):
    # Get the dimensions of the piece
    rows = len(piece)
    cols = len(pieces)

    # Loop through each cell in the piece and draw it on the screen
    for row in range(rows):
        for col in range(cols):
            if piece.get(row,col) == 1:
                pygame.draw.rect(screen, color, (x + col * CELL_SIZE, y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Define a function to draw the game board
def draw_board():
    screen.fill(WHITE)

    # Draw the grid lines
    for i in range(BOARD_WIDTH + 1):
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, BOARD_HEIGHT * CELL_SIZE))
    for i in range(BOARD_HEIGHT + 1):
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (BOARD_WIDTH * CELL_SIZE, i * CELL_SIZE))

    # Draw the starting squares for each player
    pygame.draw.rect(screen, (255, 0, 0), (0, 0, CELL_SIZE * 2, CELL_SIZE * 2))
    pygame.draw.rect(screen, (0, 0, 255),
                     ((BOARD_WIDTH - 2) * CELL_SIZE, (BOARD_HEIGHT - 2) * CELL_SIZE, CELL_SIZE * 2, CELL_SIZE * 2))

def main():
    game_over = True
    while game_over:
        draw_board()
        draw_piece(pieces,1,1,BLUE)

main()