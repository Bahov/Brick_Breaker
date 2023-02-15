import pygame
from bricks import brick
from yaml_reader import read_yaml_file
import random

class game_utils:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("comicsans", 28)

    def game_over_util(self, main_window):
        # game over text
        text_game_over = self.font.render("Game Over", True, "black")
        text_x = main_window.get_width()/2
        text_y = 200
        text_rect = text_game_over.get_rect(center=(text_x, text_y))
        main_window.blit(text_game_over, text_rect)
        # restart instruction
        text_restart = self.font.render("To restart press SPACE", True, "black")
        text_x = main_window.get_width()/2
        text_y = 300
        text_rect = text_restart.get_rect(center=(text_x, text_y))
        main_window.blit(text_restart, text_rect)
        # back to main menu instruction
        text_back_to_main = self.font.render("To go back to main menu press M", True, "black")
        text_x = main_window.get_width()/2
        text_y = 400
        text_rect = text_back_to_main.get_rect(center=(text_x, text_y))
        main_window.blit(text_back_to_main, text_rect)
        pygame.display.update()
    
    def populate_bricks_list(self, rows, columns, main_window):
        brick_between_space = 3
        brick_width = main_window.get_width() // columns - brick_between_space
        brick_height = 20
        duration_color_dict = {5:"purple",4:"red",3:"orange",2:"yellow",1:"green"}

        brick_models = read_yaml_file("brick_models.yml")
        # get random brick model
        current_model = random.choice(list(brick_models.values()))

        bricks = []
        for row in range(len(current_model)):
            for col in range(len(current_model[row])):
                if current_model[row][col] > 0:
                    brick_duration = current_model[row][col]
                    current_brick = brick(brick_width * col + brick_between_space * (col + 1), \
                                        brick_height * row + brick_between_space * row, \
                                        brick_width, brick_height, brick_duration, duration_color_dict[brick_duration], brick_duration)
                    bricks.append(current_brick)
        return bricks
    
    def track_lives(self, remaining_lives:int, main_window):
        text_lives = self.font.render(f"Lives: {remaining_lives}", True, "black")
        main_window.blit(text_lives, (main_window.get_width() - text_lives.get_width() - 10, main_window.get_height() - text_lives.get_height() - 10))
    
    def track_points(self, points:int, main_window):
        text_points = self.font.render(f"Points: {points}", True, "black")
        main_window.blit(text_points, (10, main_window.get_height() - text_points.get_height() - 10))
    
    def start_counter(self, seconds, main_window):
        text_start_counter = self.font.render(f"{seconds}", True, "black")
        main_window.blit(text_start_counter, (main_window.get_width()/2 - text_start_counter.get_width()/2, main_window.get_height()/2 - text_start_counter.get_height()/2))
        pygame.display.update()