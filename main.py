# two player chess in python with pygame
# part one, set up variables images and game loop 

import pygame 

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60 
# Game variables and images 
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'] # Keeps track of all pieces on board
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)] # Where the pieces are. Top left is 0,0, bottom right is 7,7
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
# 0 - whites turn, no selection; 1 - whites turn, piece selected; 2 - blacks turn, no selection; 3 - blacks turn, piece selected 
turn_step = 0
selection = 100 # Stores what piece location is selected. When no piece is selected make it big enough so others aren't accidently selected
valid_moves = [] 
# load in game piece images (queen, king, rook, bishop, knight, pawn) x2
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80)) # Bigger pieces need a bigger board, smaller pieces smaller board
black_queen_small = pygame.transform.scale(black_queen, (45, 45)) # For when piece is taken and is on the side
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80)) 
black_king_small = pygame.transform.scale(black_king, (45, 45))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80)) 
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (65, 65)) 
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80)) 
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80)) 
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80)) 
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80)) 
white_king_small = pygame.transform.scale(white_king, (45, 45))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80)) 
white_knight_small = pygame.transform.scale(white_knight, (45, 45))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (65, 65)) 
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80)) 
white_queen_small = pygame.transform.scale(white_queen, (45, 45))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80)) 
white_rook_small = pygame.transform.scale(white_rook, (45, 45))
white_images = [white_pawn, white_queen, white_king, white_knight, white_bishop, white_rook]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, 
                      white_bishop_small, white_rook_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_bishop, black_rook]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, 
                      black_bishop_small, black_rook_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
# Check variables/flashing counter


# Draw main game board
def draw_board():    
    for i in range(32): # Get away with every other rectangle being background color so we don't need 64 only 32
        column = i % 4 # % is modulo operator. Checks what the remainder is 
        row = i // 4 # Round down to the nearest whole integer
        if row % 2 == 0: # makes checkers on checkerboard                   
            pygame.draw.rect(screen, 'light gray', [600 - (column * 200), row * 100, 100, 100])
        else :                          
            pygame.draw.rect(screen, 'light gray', [700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100]) # draw borders for bottom and top
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5) # border for it 
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5) # golden rectangle on right side going up and down
        status_text = ['White: Select a Piece to Move', 'White: Select a Destination',
                       'Black: Select a Piece to Move', 'Black: Select a Destination'] # 31:49
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820)) # when rendering a font in pygame you need 3 arguments. True is for antialiasing
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2) # For horizontal lines to better show checkerboard
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2) # For vertical lines 


# draw pieces onto board
def def_pieces():
       for i in range(len(white_pieces)): # can't just say 16. Needs to check how many pieces are actually on the board
            index = piece_list.index(white_pieces[i]) # gets the index of whatever piece is currently being looked at
            if white_pieces[i] == 'pawn': # have to do a seperate for pawns because they are different sizes
                screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30)) # 22 and 30 offsets pawns to make them look right
            else: 
                screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
                
        for i in range(len(white_pieces)): # can't just say 16. Needs to check how many pieces are actually on the board
            index = piece_list.index(white_pieces[i]) # gets the index of whatever piece is currently being looked at
            if white_pieces[i] == 'pawn': # have to do a seperate for pawns because they are different sizes
                screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30)) # 22 and 30 offsets pawns to make them look right
            else: 
                screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))    
            # 38:34
                      
# main game loop 
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray') # Background color 
    draw_board()
    draw_pieces()
    
    # Event handling
    for event in pygame.event.get(): # gets keyboard, mouse, etc from computer 
        if event.type == pygame.QUIT: # Checks to see if X at top of game window was clicked
            run = False
            
    pygame.display.flip()
pygame.quit()