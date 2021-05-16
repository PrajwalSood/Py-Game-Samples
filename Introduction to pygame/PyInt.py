import pygame
from pygame.constants import QUIT
import os

width, height = 800, 600
fps = 60
cwd = os.chdir('Introduction to pygame')
picture = pygame.image.load(os.path.join('resources', 'image_1.png'))
song = os.path.join('resources', 'song1.mp3')

GScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game 1")

def draw_fn():
    GScreen.fill((255,255,255))
    GScreen.blit(picture, (0,0))
    pygame.display.update()

def main():
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw_fn()
        

if __name__ == "__main__":
    main()