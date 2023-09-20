import pygame 

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill("white")

for event in pygame.event.get():
    if event.type == pygame.quit:
         done = True   
    pygame.draw.circle(screen, "black", [250, 400], 95, 2)
    pygame.draw.circle(screen, "black", [250, 280], 75, 2)
    pygame.draw.circle(screen, "black", [250, 180], 50, 2)
    pygame.display.flip()

pygame.time.wait(3000)