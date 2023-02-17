import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, GREY, WHITE
from checkers.game import Game
from alphabeta.algorithm import alphabeta

FPS = 60

Window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Game')


def get_row_col(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(Window)
    while run:
        clock.tick(FPS)
        if game.turn == WHITE:
            value, new_board = alphabeta(game.get_board(), 1, WHITE, game)
            game.ai_move(new_board)
        if game.winner() != None:
            print(game.winner())
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col(pos)
                game.select(row, col)
        game.update()
    pygame.quit()


main()
