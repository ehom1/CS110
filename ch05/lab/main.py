import pygame

def threenp1(n):
    count = 0
    while n > 1.0:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        count = count + 1
    
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for n in range(2, upper_limit + 1):
        iters = threenp1(n)
        objs_in_sequence[n] = iters
    return objs_in_sequence

def graph_coordinates(threenplus1_iters_dict):
    pygame.init()
    
    factor = 5
    coordinates = []
    
    max_so_far = 0
    
    window = pygame.display.set_mode((900, 600))
    window.fill("white")
    
    for key, value in threenplus1_iters_dict.items():
        x = key * factor
        y = value * factor
        coordinates.append((x, y))
        pygame.draw.circle(window, "blue", (x, y), 1)
        
        if value > max_so_far:
            max_so_far = max(max_so_far, value)
    
    if len(coordinates) >= 2:
        pygame.draw.lines(window, "black", False, coordinates, 1)
    
    width, height = window.get_size()
    
    font = pygame.font.Font(None, 40)
    msg = font.render("Max So Far: " + str(max_so_far), True, "blue")
    
    new_display = pygame.transform.scale(window, (width * factor, height * factor))
    window.blit(new_display, (0, 0))
    
    new_display = pygame.transform.flip(window, False, True)
    window.blit(new_display, (0, 0))
    window.blit(msg, (10, 10))
    
    pygame.display.flip()

def main():
    upper_limit = 25
    threenplus1_iters_dict = threenp1range(upper_limit)
    print(threenplus1_iters_dict)
    graph_coordinates(threenplus1_iters_dict)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
    
main()