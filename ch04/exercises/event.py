import pygame
import random

pygame.init()
screen = pygame.display.set_mode()
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
hitboxes["green"].topright = hitboxes["red"].bottomright
hitboxes["purple"].topleft = hitboxes["red"].bottomright

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

font = pygame.font.Font(None, 48)

done = False
result = []
turns = 0
order = list(hitboxes.keys())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                random.shuffle(order)
                turns = len(order)
                result = []
                for color in order:
                    for c, hb in hitboxes.items():
                        pygame.draw.rect(screen, main_colors[c], hb)
                    pygame.draw.rect(screen, highlight_colors[color], hitboxes[color])
                    pygame.display.flip()
                    pygame.time.delay(1000)
            elif event.key == pygame.K_q:
                done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            turns = turns - 1
            if hitboxes["red"].collidepoint(event.pos):
                result.append("red")
            elif hitboxes["purple"].collidepoint(event.pos):
                result.append("purple")
            elif hitboxes["green"].collidepoint(event.pos):
                result.append("green")
            elif hitboxes["blue"].collidepoint(event.pos):
                result.append("blue")
            
    # Update data 
    if len(result) == len(order):
        msg = [
            f"You entered: {result}",
            f"the correct pattern was: {order}",
        ]
        if result == order:
            msg.append("Yay! You won.")
        else:
            msg.append("Um, no.")
        msg.append("Press spacebar to play again.")
    elif turns:
        msg = ["Your turn"]
    else:
        msg = ["Press spacebar to play the game...(q to quit)"]
    
    # Draw screen
    screen.fill("black")
    for c, hb in hitboxes.items():
        pygame.draw.rect(screen, main_colors[c], hb)
        
    if result:
        pygame.draw.rect(screen, highlight_colors[result[-1]], hitboxes[result[-1]])
        
    ypos = 60
    for m in msg:
        text = font.render(m, True, "white")
        screen.blit(text, (20, ypos))
        ypos += 60
        
    pygame.display.flip()