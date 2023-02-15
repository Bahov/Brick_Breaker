import pygame
import math
import time
from menus import game_menus
from game_utils import game_utils
from slider import slider
from ball import ball
              
class Brick_Breaker:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.main_window = pygame.display.set_mode((self.width, self.height))
        self.game_name = pygame.display.set_caption("Brick Breaker")
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.game_menus = game_menus()
        self.slider_object = slider(self.width/2, self.main_window)
        self.ball_object = ball(self.width/2)
        self.utilities = game_utils()
        self.bricks = self.utilities.populate_bricks_list(10, 11, self.main_window)
        self.lives = 3
        self.points = 0
        self.seconds = 3
        self.game_menu_on = True
        self.game_over = False

    def main_loop(self):
        self.main_window.fill("gray")
        game_running = True
        game_over = False
        while game_running:
            while self.game_menu_on:
                exit_game_menu = self.game_menus.main_menu(self.main_window)
                if exit_game_menu:
                    self.game_menu_on = False
            self.main_window.fill("gray")
            self.clock.tick(self.FPS)
            self.apply_visuals()
            while self.seconds > 0:
                self.utilities.start_counter(self.seconds, self.main_window)
                time.sleep(1)
                self.apply_visuals()
                self.seconds -= 1
            self.slider_object.pressed_keys() # move slider
            self.ball_object.move_ball()
            self.ball_object.bounce_ball_slider(self.slider_object)
            self.game_over = self.ball_object.bounce_ball_wall()
            if self.game_over:
                self.lives -= 1
                if self.lives > 0:
                    # continue and reposition ball in center of slider
                    self.ball_object.x_pos = self.slider_object.rectangle.x + self.slider_object.width/2
                    self.ball_object.y_pos = self.slider_object.rectangle.y - self.slider_object.height
                    # self.game_menu_on = False
                    self.main_loop() 
                else:
                    game_running = False
                    self.utilities.game_over_util(self.main_window)
            for game_event in pygame.event.get():
                if game_event.type == pygame.QUIT:
                    game_running = False
            for brick in self.bricks:
                brick.ball_hit_brick(self.ball_object) # will decrease duration by one
                if brick.duration <= 0:
                    self.bricks.remove(brick)
                    self.points += brick.difficulty
                else:
                    brick.color = brick.duration_color_dict[brick.duration] # update color of brick
        while self.game_over:
            for game_over_event in pygame.event.get():
                if game_over_event.type == pygame.KEYDOWN:
                    if game_over_event.key == pygame.K_SPACE:
                        self.restart_game()
                    elif game_over_event.key == pygame.K_m:
                        self.game_menu_on = True
                        self.restart_game()
                elif game_over_event.type == pygame.QUIT:
                    self.game_over = False
        pygame.quit()
        quit()
    
    def apply_visuals(self):
        # Main window
        self.main_window.fill("gray")
        # Slider
        self.slider_object.visualize_slider(self.main_window)
        # Ball
        self.ball_object.visualize_ball(self.main_window)
        # Bricks
        for brick in self.bricks:
            brick.visualize_brick(self.main_window)
        # Lives
        self.utilities.track_lives(self.lives, self.main_window)
        # Points
        self.utilities.track_points(self.points, self.main_window)
        # Render
        pygame.display.update()
    
    def restart_game(self):
        self.game_over = False
        self.ball_object = ball(self.width/2)
        self.slider_object = slider(self.width/2, self.main_window)
        self.bricks = self.utilities.populate_bricks_list(10, 11, self.main_window)
        self.lives = 3
        self.points = 0
        self.game_over = False
        self.main_loop()        

##################################################
brick_breaker_game = Brick_Breaker()
brick_breaker_game.main_loop()