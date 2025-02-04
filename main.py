import pygame
import sys
from constants import *
from player import * 
from asteroid import * 
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatable, drawable)

    
    
    

    while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return
    
       for obj in updatable:
           obj.update(dt)

       for asteroid in asteroids:
           if asteroid.collision_check(player_1):
               print("Game over!")
               sys.exit()
            
           for bullet in shots:
               if asteroid.collision_check(bullet):
                   asteroid.split()
                   bullet.kill()

       screen.fill((0, 0, 0))
       for obj in drawable:
           obj.draw(screen)

       pygame.display.flip()

       # limits framerate to 60fps
       dt = (clock.tick(60)) / 1000

if __name__=="__main__":
    main()