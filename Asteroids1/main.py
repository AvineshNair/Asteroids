#importing values from constants.py
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} ")
    print(f"Screen height: {SCREEN_HEIGHT} ")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2, shots)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        time_passed = clock.tick(60)
        dt = time_passed/1000

        screen.fill(color = "black")

        updatable.update(dt)
        
        for item in drawable:
            item.draw(screen)
        
        for item in asteroids:
            if item.collision(player):
                print ("Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    
                    shot.kill()     
                
        #player.draw(screen)
        #player.update(dt)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
