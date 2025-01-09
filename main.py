import pygame
from constants import *
from player import * 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    X = SCREEN_WIDTH / 2 
    Y = SCREEN_HEIGHT / 2 
    player_1 = Player(X, Y)
     
    while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return
       screen.fill((0, 0, 0))
       player_1.draw(screen)
       pygame.display.flip()
       dt = (clock.tick(60)) / 1000

    

    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__=="__main__":
    main()