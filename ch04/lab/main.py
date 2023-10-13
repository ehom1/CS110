import pygame
import random
import math

pygame.init()
window = pygame.display.set_mode((700, 700))
window.fill("cornflowerblue")

center = (pygame.display.get_window_size()[0] / 2 , pygame.display.get_window_size()[1] / 2)
radius = (pygame.display.get_window_size()[0] / 2)
rect1 = pygame.Rect(20, 665, 35, 35)
rect2 = pygame.Rect(90, 665, 35, 35)

p1_hit = "red"
p1_miss = "black"
p1_score = 0
p1_turn = True
p2_hit = "blue"
p2_miss = "white"
p2_score = 0

bet_font = pygame.font.Font(None, 17)
game_round = 1
user_bet = None

bet_p1 = bet_font.render("Bet Player 1", True, "White")
bet_p2 = bet_font.render("Bet Player 2", True, "White")
ask = bet_font.render("Bet on who wil win.", True, "White")
window.blit(bet_p1, (5, 650))
window.blit(bet_p2, (80, 650))
window.blit(ask, (5, 630))

pygame.draw.circle(window, "lightpink", center, radius)
pygame.draw.circle(window, "black", center, radius, 2)
pygame.draw.line(window, "black", (350, 0), (350, 700), 1)
pygame.draw.line(window, "black", (0, 350), (700, 350), 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect1.collidepoint(pygame.mouse.get_pos()):
                user_bet = "Player 1"
            elif rect2.collidepoint(pygame.mouse.get_pos()):
                user_bet = "Player 2" 
            
    if user_bet == None:
        bet_on_p1 = pygame.draw.rect(window, "red", rect1)
        bet_on_p2 = pygame.draw.rect(window, "blue", rect2)
        pygame.display.flip()
        continue
    
    while game_round <= 10 and user_bet is not None:         
        for _ in range(2):
            x = random.randrange(0, pygame.display.get_window_size()[0])
            y = random.randrange(0, pygame.display.get_window_size()[1])
            distance_from_center = math.hypot(x - center[0], y - center[1])
            is_in_circle = distance_from_center <= radius
            
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
            
        pygame.display.update()   
        pygame.time.wait(1000)
        game_round += 1
    
    score_font = pygame.font.Font(None, 23)
    text_p1 = score_font.render("Player 1 Score: " + str(p1_score), True, "White", "Black")
    text_p2 = score_font.render("Player 2 Score: "+ str(p2_score), True, "White", "Black")
    window.blit(text_p1, (10, 10))  
    window.blit(text_p2, (10, 50)) 
                
    if user_bet == "Player 1" and p1_score > p2_score:
        final_text = "Player 1 Wins! Your bet was correct."
    elif user_bet == "Player 2" and p1_score > p2_score:
        final_text = "Player 1 Wins! Your bet was incorrect."
    elif user_bet == "Player 2" and p1_score < p2_score:
        final_text = "Player 2 Wins! Your bet was correct."
    elif user_bet == "Player 1" and p1_score < p2_score:
        final_text = "Player 2 Wins! Your bet was incorrect."
    else:
        final_text = "Game ended in a tie."

    font = pygame.font.Font(None, 40)
    text = font.render(final_text, True, "White")
    window.blit(text, (100, 330))
    pygame.display.flip()
        
pygame.quit()