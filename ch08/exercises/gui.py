import pygame

class Background:
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.image = pygame.image.load("image.jpg")
        
class Character:
    def __init__(self, x, y, lives, score):
        self.x_pos = x
        self.y_pos = y
        self.lives = lives
        self.score = score 
        
class Blocks:
    def __init__(self, x, y):
        self.isBrick = True
        self.x_pos = x
        self.y_pos = y
        