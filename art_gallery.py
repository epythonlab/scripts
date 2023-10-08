# Create Digital Art Gallery using pygame Library

import pygame
import os

# Set up the display
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Kids' Art Gallery")

# Path to the folder containing the art images
art_folder = "/home/noh/Pictures/gallery/"
art_files = os.listdir(art_folder)
art_files = [f for f in art_files if f.endswith(".png") or f.endswith(".jpg")]

# Load and display images
current_art_index = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_art_index = (current_art_index - 1) % len(art_files)
            elif event.key == pygame.K_RIGHT:
                current_art_index = (current_art_index + 1) % len(art_files)

    screen.fill((255, 255, 255))
    
    current_art_path = os.path.join(art_folder, art_files[current_art_index])
    art_image = pygame.image.load(current_art_path)
    screen.blit(art_image, (0, 0))

    pygame.display.flip()

pygame.quit()






