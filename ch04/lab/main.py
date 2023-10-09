import pygame
import random
import math

pygame.init()
window = pygame.display.set_mode((700, 700))
window.fill("cornflowerblue")

center = (pygame.display.get_window_size()[0] / 2 , pygame.display.get_window_size()[1] / 2)
radius = (pygame.display.get_window_size()[0] / 2)
rect1 = pygame.Rect(0, 0, 350, 700)
rect2 = pygame.Rect(350, 0, 350, 700)

p1_hit = "red"
p1_miss = "black"
p1_score = 0
p1_turn = True
p2_hit = "blue"
p2_miss = "white"
p2_score = 0

game_round = 1

# pygame.draw.rect(window, "blue", rect1)
# pygame.draw.rect(window, "red", rect2)
# pygame.draw.line(window, "black", (350, 0), (350, 700), 3)

# pygame.display.flip()
# pygame.time.wait(1000)
# window.fill("cornflowerblue")
# pygame.display.flip()

# running = True
while game_round <= 10:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            done = True
        
    # pygame.draw.rect(window, "blue", rect1)
    # pygame.draw.rect(window, "red", rect2)
    # pygame.draw.line(window, "black", (350, 0), (350, 700), 3)

    # pygame.display.flip()
    # pygame.time.wait(2000)
    # window.fill("cornflowerblue")
    # pygame.display.flip()
    
        pygame.draw.circle(window, "lightpink", center, radius)
        pygame.draw.circle(window, "black", center, radius, 2)
        pygame.draw.line(window, "black", (350, 0), (350, 700), 1)
        pygame.draw.line(window, "black", (0, 350), (700, 350), 1)
            
        for _ in range(2):
            x = random.randrange(0, pygame.display.get_window_size()[0])
            y = random.randrange(0, pygame.display.get_window_size()[1])
            distance_from_center = math.hypot(x - center[0], y - center[1])
            is_in_circle = distance_from_center <= pygame.display.get_window_size()[0] / 2
            
            if is_in_circle:
                if p1_turn:
                    color = p1_hit
                    p1_score += 1
                    p1_turn = False
                else:
                    color = p2_hit
                    p2_score += 1
                    p1_turn = True                           
            else:
                if p1_turn:
                    color = p1_miss    
                    p1_turn = False      
                else:
                    color = p2_miss   
                    p1_turn = True          
                
            pygame.draw.circle(window, color, (x, y), 4)

        pygame.display.flip()
        pygame.time.wait(1000)
        game_round += 1

# if p1_score > p2_score:
#     winner = "Player 1 Wins!"
# elif p1_score < p2_score:
#     winner = "Player 2 Wins!"
# else:
#     winner = "Game ends in a tie."

# font = pygame.font.Font(None, 48)
# text = font.render(winner, True, "white")
# window.blit(text, (225, 325))