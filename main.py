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
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player_1 = Player(X, Y)
    

    while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return
       screen.fill((0, 0, 0))
       for player in updatable:
          player.update(dt)
       
       for player in drawable:
           player.draw(screen)
       pygame.display.flip()
       dt = (clock.tick(60)) / 1000

if __name__=="__main__":
    main()