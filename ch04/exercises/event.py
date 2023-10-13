import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
width, height = pygame.display.get_window_size()  # tuple

hit_box_width = width / 2
hit_box_height = height / 2

hitboxes = {
    "red": pygame.Rect(0, 0, hit_box_width, hit_box_height),
    "green": pygame.Rect(0, 0, hit_box_width, hit_box_height), 
    "blue": pygame.Rect(0, 0, hit_box_width, hit_box_height), 
    "purple": pygame.Rect(0, 0, hit_box_width, hit_box_height),
}

# Position Hitboxes
hitboxes["blue"].topleft = hitboxes["red"].topright

# Define main colors
main_colors = {
    "red": (200, 0, 0),
    "green": (0, 200, 0),
    "blue": (0, 0, 200),
    "purple": (200, 0, 200),
}

#Define highlight colors 
highlight_colors = {
    "red": (250, 0, 0),
    "green": (0, 250, 0),
    "blue": (0, 0, 250),
    "purple": (250, 0, 250),
}

running = True
while running:  # mainloop - 1 frame
    # 1. event loop 
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

pygame.quit()