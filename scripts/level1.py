
import random
import sys
from msilib.schema import Directory
from tkinter import CENTER
from turtle import color
import os

import pygame
from pygame import mixer
from pygame.math import Vector2
import time
import os
pygame.init()
class SNAKE_right:
    scrore = 0
    def __init__(self):
        
        self.body = [Vector2(14,10), Vector2(15,10), Vector2(16,10)]
        SNAKE_left.scrore = len(self.body) - 3
        
        self.direction = Vector2(0,1)
        
        self.new_block = False
        
        self.head_up = pygame.image.load("images/head_up.png").convert_alpha()
        self.head_down = pygame.transform.rotate(self.head_up, 180)
        self.head_right = pygame.transform.rotate(self.head_up, -90)
        self.head_left = pygame.transform.rotate(self.head_up, 90)

        self.tail_up = pygame.image.load("images/tail_up.png").convert_alpha()
        self.tail_down = pygame.transform.rotate(self.tail_up, 180)
        self.tail_right = pygame.transform.rotate(self.tail_up, -90)
        self.tail_left = pygame.transform.rotate(self.tail_up, 90)

        self.body_vertical = pygame.image.load("images/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.transform.rotate(self.body_vertical, 90)

        self.body_tr = pygame.image.load("images/body_tr.png").convert_alpha()
        self.body_tl = pygame.transform.rotate(self.body_tr, 90)
        self.body_br = pygame.transform.rotate(self.body_tr, -90)
        self.body_bl = pygame.transform.rotate(self.body_tr, 180)
        
    def draw_snake(self):
        
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            
            x_pos = int(block.x *cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            
            if index == 0:
                screen.blit(self.head, block_rect)
            
            elif index == len(self.body) -1:
                screen.blit(self.tail, block_rect)
            
            else:
                
                previous_block = self.body[index + 1] - block
                next_block = self.body[index -1] - block
                
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)


    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down
        
    def move_snake(self):
        
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            
            self.body = body_copy[:]
            self.new_block = False
            
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    def add_block(self):
        self.new_block = True

        #class for fruit property
    def addition_to_loose(self):
        self.game_over_text = game_font.render("Game over", True, (170, 74, 68))
        self.score_text = game_font.render("This application will be closed automatically", True, (255, 255, 255))
        self.menu = game_font.render("Try your skills one more time!", True, (200,200,200))
        screen.blit(LOOSE_SCREEN, (0, 0))
        screen.blit(self.game_over_text, (400 - (self.game_over_text.get_width()/2), (400 + self.menu.get_height()/2)))
        screen.blit(self.score_text, (400 - (self.score_text.get_width()/2), 400 + self.score_text.get_height()* 1.5))
        screen.blit(self.menu, (400 - (self.menu.get_width()/2), 400 + self.menu.get_height()* 2.5))
        pygame.display.update()
        
        time.sleep(5)
        pygame.quit()
        sys.exit()
    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.addition_to_loose()
    
    def you_win(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.game_over_text = game_font.render("You completed the level. Congratulations", True, (127, 255, 212))
        self.score_text = game_font.render("This application will be closed automatically", True, (255, 255, 255))
        self.menu = game_font.render("For you, there other levels of game!", True, (200,200,200))

        screen.blit(LOOSE_SCREEN, (0, 0))
        screen.blit(self.game_over_text, (400 - (self.game_over_text.get_width()/2), (300 + self.menu.get_height()/2)))
        screen.blit(self.score_text, (400 - (self.score_text.get_width()/2), 300 + self.score_text.get_height()* 1.5))
        screen.blit(self.menu, (400 - (self.menu.get_width()/2), 300 + self.menu.get_height()* 2.5))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        sys.exit()
class OBSTACLE_right:
    def __init__(self):
        self.body = [Vector2(10,3), Vector2(10,4), Vector2(10,5)]
        for i in range(6,13,1):
            self.body.append(Vector2(10,i))
        for i in range(7, 14,1):
            self.body.append(Vector2(i, 13))
        for i in range(7, 14,1):
            self.body.append(Vector2(i, 3))
        
    def draw_obtacle(self):
        for index, block in enumerate(self.body):
            #We still need a rect for the positioning
            x_pos = int(block.x *cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            screen.blit(Obstacle_image, block_rect)
class FRUIT_right:
    def __init__(self):
        self.randomize()
        #create an x and y position
        #draw a squire
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(Grape_image, fruit_rect)
        
    def randomize(self):
        self.x = random.randint(0, cell_number -1)
        self.y = random.randint(0, cell_number -1)
        self.pos = Vector2(self.x, self.y)
class MAIN_right:
    def __init__(self):
        self.snake = SNAKE_right()
        self.fruit = FRUIT_right()
        self.obstacle = OBSTACLE_right()
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.progress()
        self.obstacle.draw_obtacle()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            
            self.fruit.randomize()
            self.snake.add_block()
           
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
        for unit in self.obstacle.body[0:]:
            if unit == self.fruit.pos:
                self.fruit.randomize()
    def check_fail(self):
        
        #check if snake is outside of the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y <cell_number:
            self.game_over()
        #gamer over stay for self hit
        for each in self.obstacle.body[0:]:
            if each == self.snake.body[0]:
                self.game_over()
        for block in self.snake.body[1: ]:
            if  block == self.snake.body[0]:
                self.game_over()
                #reverse, conditon for winning
        if int(len(self.snake.body) - 3) >= 10:
            self.you_win_local()
    def game_over(self):
        self.snake.reset()
    def you_win_local(self):
        self.snake.you_win()

    def progress(self):
        score = (int(len(self.snake.body)) - 3) *10
        score_text = str(score) + "% completed"
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number -150)
        score_y = int(cell_size * cell_number -750)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = Grape_image.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width + score_rect.width + 10, apple_rect.height)

        pygame.draw.rect(screen,(167,209, 61),bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(Grape_image, apple_rect)
        pygame.draw.rect(screen,(56, 74, 12), bg_rect, 2)
    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74,12))
        score_x = int(cell_size * cell_number -60)
        score_y = int(cell_size * cell_number -40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = Grape_image.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width + score_rect.width + 10, apple_rect.height)
        
        pygame.draw.rect(screen,(167,209, 61),bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(Grape_image, apple_rect)
        pygame.draw.rect(screen,(56, 74, 12), bg_rect, 2)


class SNAKE_left:
    scrore = 0
    def __init__(self):
        
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        SNAKE_left.scrore = len(self.body) - 3
        
        self.direction = Vector2(0,1)
        
        self.new_block = False
        
        self.head_up = pygame.image.load("images/head_up.png").convert_alpha()
        self.head_down = pygame.transform.rotate(self.head_up, 180)
        self.head_right = pygame.transform.rotate(self.head_up, -90)
        self.head_left = pygame.transform.rotate(self.head_up, 90)

        self.tail_up = pygame.image.load("images/tail_up.png").convert_alpha()
        self.tail_down = pygame.transform.rotate(self.tail_up, 180)
        self.tail_right = pygame.transform.rotate(self.tail_up, -90)
        self.tail_left = pygame.transform.rotate(self.tail_up, 90)

        self.body_vertical = pygame.image.load("images/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.transform.rotate(self.body_vertical, 90)

        self.body_tr = pygame.image.load("images/body_tr.png").convert_alpha()
        self.body_tl = pygame.transform.rotate(self.body_tr, 90)
        self.body_br = pygame.transform.rotate(self.body_tr, -90)
        self.body_bl = pygame.transform.rotate(self.body_tr, 180)
        
    def draw_snake(self):
        
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            
            x_pos = int(block.x *cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            
            if index == 0:
                screen.blit(self.head, block_rect)
            
            elif index == len(self.body) -1:
                screen.blit(self.tail, block_rect)
            
            else:
               
                previous_block = self.body[index + 1] - block
                next_block = self.body[index -1] - block
                
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    
                    screen.blit(self.body_horizontal, block_rect)
                else:
                   
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

#as in the case with body turn graphics, we need to specify conditions for rotating our image(here refer to variable where we did this)
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down
        #funtion for moving the snake
    def move_snake(self):
        
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            
            self.body = body_copy[:]
            self.new_block = False
            
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    def add_block(self):
        self.new_block = True
        
    def addition_to_loose(self):
        self.game_over_text = game_font.render("Game over", True, (170, 74, 68))
        self.score_text = game_font.render("This application will be closed automatically", True, (255, 255, 255))
        self.menu = game_font.render("Try your skills one more time!", True, (200,200,200))
        screen.blit(LOOSE_SCREEN, (0, 0))
        screen.blit(self.game_over_text, (400 - (self.game_over_text.get_width()/2), (400 + self.menu.get_height()/2)))
        screen.blit(self.score_text, (400 - (self.score_text.get_width()/2), 400 + self.score_text.get_height()* 1.5))
        screen.blit(self.menu, (400 - (self.menu.get_width()/2), 400 + self.menu.get_height()* 2.5))
        pygame.display.update()
        
        time.sleep(5)
        pygame.quit()
        sys.exit()
    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.addition_to_loose()
    def addition_to_youwin(self):
        self.game_over_text = game_font.render("You completed the level. Congratulations", True, (127, 255, 212))
        self.score_text = game_font.render("This application will be closed automatically", True, (255, 255, 255))
        self.menu = game_font.render("For you, there other levels of game!", True, (200,200,200))

        screen.blit(LOOSE_SCREEN, (0, 0))
        screen.blit(self.game_over_text, (400 - (self.game_over_text.get_width()/2), (300 + self.menu.get_height()/2)))
        screen.blit(self.score_text, (400 - (self.score_text.get_width()/2), 300 + self.score_text.get_height()* 1.5))
        screen.blit(self.menu, (400 - (self.menu.get_width()/2), 300 + self.menu.get_height()* 2.5))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        sys.exit()
    def you_win(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.addition_to_youwin()
class OBSTACLE_left:
    def __init__(self):
        self.body = [Vector2(10,3), Vector2(10,4), Vector2(10,5)]
        for i in range(6,13,1):
            self.body.append(Vector2(10,i))
        for i in range(7, 14,1):
            self.body.append(Vector2(i, 13))
        for i in range(7, 14,1):
            self.body.append(Vector2(i, 3))
        
    def draw_obtacle(self):
        for index, block in enumerate(self.body):
            #We still need a rect for the positioning
            x_pos = int(block.x *cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            screen.blit(Obstacle_image, block_rect)
class FRUIT_left:
    def __init__(self):
        self.randomize()
        #create an x and y position
        #draw a squire
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(Pear_image, fruit_rect)
        #creating our random x and y position and making them as the verctor
    def randomize(self):
        self.x = random.randint(0, cell_number -1)
        self.y = random.randint(0, cell_number -1)
        self.pos = Vector2(self.x, self.y)
class MAIN_left:
    def __init__(self):
        self.snake = SNAKE_left()
        self.fruit = FRUIT_left()
        self.obstacle = OBSTACLE_left()
        #neccessary event that should be check every time
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.apple_near()
        #drawing all our elemnts by calling the needed function where the style and rect(physical body) was given
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.progress()
        self.obstacle.draw_obtacle()
        #condition for sound effect
    def apple_near(self):
        if self.fruit.pos + pygame.math.Vector2(1) == self.snake.body[0] or self.fruit.pos + pygame.math.Vector2(-1) == self.snake.body[0]:
            self.snake.play_following_sound()
            
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            
            self.fruit.randomize()
            self.snake.add_block()
            
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
        for unit in self.obstacle.body[0:]:
            if unit == self.fruit.pos:
                self.fruit.randomize()
    def check_fail(self):
        
        
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y <cell_number:
            self.game_over()
        
        for each in self.obstacle.body[0:]:
            if each == self.snake.body[0]:
                self.game_over()
        for block in self.snake.body[1: ]:
            if  block == self.snake.body[0]:
                self.game_over()
                
        if int(len(self.snake.body) - 3) >= 10:
            self.you_win_local()
    def game_over(self):
        self.snake.reset()
    def you_win_local(self):
        self.snake.you_win()
    def progress(self):
        score = (int(len(self.snake.body)) - 3) *10
        score_text = str(score) + "% completed"
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number -650)
        score_y = int(cell_size * cell_number -750)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = Pear_image.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width + score_rect.width + 10, apple_rect.height)

        pygame.draw.rect(screen,(167,209, 61),bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(Pear_image, apple_rect)
        pygame.draw.rect(screen,(56, 74, 12), bg_rect, 2)
    #drawing the score
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74,12))
        score_x = int(cell_size * cell_number -660)
        score_y = int(cell_size * cell_number -40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = Pear_image.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width + score_rect.width + 10, apple_rect.height)
        
        pygame.draw.rect(screen,(167,209, 61),bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(Pear_image, apple_rect)
        pygame.draw.rect(screen,(56, 74, 12), bg_rect, 2)
        
pygame.mixer.pre_init(44100, -16, 2, 512)

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
game_font = pygame.font.Font("fonts/Roboto_Mono/static/RobotoMono-Italic.ttf", 25)
main_game_left = MAIN_left()
main_game_right = MAIN_right()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 120)
LOOSE_SCREEN = pygame.transform.scale(pygame.image.load("images/you_lose.jpg"), (800,800))
WIN_SCREEN = pygame.transform.scale(pygame.image.load("images/you_win.jpg"), (800, 800))
Obstacle_image = pygame.transform.scale(pygame.image.load("images/obstacle.jpg"), (40, 40))
Pear_image = pygame.transform.scale(pygame.image.load("images/pear.jpg"), (40, 40))
Grape_image = pygame.transform.scale(pygame.image.load("images/grape.jpg"), (40, 40))
bacground_image = pygame.transform.scale(pygame.image.load("images/background.jpg"), (800, 800))

while True:

    for event in pygame.event.get():
       if  event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        #keydown event of the package gives us to handle direction when the user presses specific keys
       if event.type == SCREEN_UPDATE:
        main_game_left.update()
        main_game_right.update()
       if event.type ==  pygame.KEYDOWN:
        if event.key == pygame.K_w:
            if main_game_left.snake.direction.y != 1:
                main_game_left.snake.direction = Vector2(0,-1)
        if event.key == pygame.K_d:
             if main_game_left.snake.direction.x != -1:
                main_game_left.snake.direction = Vector2(1,0)
        if event.key == pygame.K_s:
             if main_game_left.snake.direction.y != -1:
                main_game_left.snake.direction = Vector2(0,1)
        if event.key == pygame.K_a:
             if main_game_left.snake.direction.x != 1:
                main_game_left.snake.direction = Vector2(-1,0)

        if event.key == pygame.K_UP:
            if main_game_right.snake.direction.y != 1:
                main_game_right.snake.direction = Vector2(0,-1)
        if event.key == pygame.K_RIGHT:
             if main_game_right.snake.direction.x != -1:
                main_game_right.snake.direction = Vector2(1,0)
        if event.key == pygame.K_DOWN:
             if main_game_right.snake.direction.y != -1:
                main_game_right.snake.direction = Vector2(0,1)
        if event.key == pygame.K_LEFT:
             if main_game_right.snake.direction.x != 1:
                main_game_right.snake.direction = Vector2(-1,0)
    #draw all out elements
    screen.fill((175, 215, 70))
    
    main_game_left.draw_elements()
    main_game_right.draw_elements()
    pygame.display.update()
    clock.tick(90)