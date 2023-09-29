import pygame
import random
import math

pygame.init()
window = pygame.display.set_mode((700, 700))
window.fill("cornflowerblue")

center = (pygame.display.get_window_size()[0] / 2 , pygame.display.get_window_size()[1] / 2)
radius = (pygame.display.get_window_size()[0] / 2)

for event in pygame.event.get():
    if event.type == pygame.quit:
        done = True  
    pygame.draw.circle(window, "lightpink", center, radius)
    pygame.draw.circle(window, "black", center, radius, 2)
    pygame.draw.line(window, "black", (350, 0), (350, 700), 1)
    pygame.draw.line(window, "black", (0, 350), (700, 350), 1)
    
for _ in range(10):
    x = random.randrange(0, pygame.display.get_window_size()[0])
    y = random.randrange(0, pygame.display.get_window_size()[1])
    distance_from_center = math.hypot(x - center[0], y - center[1])
    is_in_circle = distance_from_center <= pygame.display.get_window_size()[0] / 2
    
    if is_in_circle:
        color = "chartreuse"
    else:
        color = "red"
        
    pygame.draw.circle(window, color, (x, y), 4)
    
pygame.display.flip()

pygame.time.wait(5000)