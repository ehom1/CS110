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
    
    factor = 3
    coordinates = []
    for key, points in threenplus1_iters_dict.items():
        x = key
        y = points 
        coordinates.append((x, y))
    
    window = pygame.display.set_mode((900, 600))
    window.fill("white")
    pygame.draw.lines(window, "black", False, coordinates, 2)
    
    new_display = pygame.transform.flip(window, False, True)
    width, height = new_display.get_size()
    
    new_display = pygame.transform.scale(window, (width * factor, height * factor))
    window.blit(new_display, (0, 0))
    
    pygame.display.flip()

def main():
    threenplus1_iters_dict = threenp1range(20)
    print(threenplus1_iters_dict)
    graph_coordinates(threenplus1_iters_dict)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
main()