import pygame
import math

class Game_utils:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(None, 36)

    def game_over_util(self, main_window):
        # game over text
        text_game_over = self.font.render("Game Over", True, "black")
        text_rect = text_game_over.get_rect()
        text_x = 800 / 2 - text_rect.width / 2
        text_y = 600 / 3 - text_rect.height / 2
        main_window.blit(text_game_over, [text_x, text_y])
        # restart instruction
        text_restart = self.font.render("To restart press SPACE", True, "black")
        text_rect = text_restart.get_rect()
        text_x = 800 / 2 - text_rect.width / 2
        text_y = 600 / 2 - text_rect.height / 2
        main_window.blit(text_restart, [text_x, text_y])
        pygame.display.update()

class Slider:
    def __init__(self, x_screen_position, slider_width):
        self.x_screen_position = x_screen_position - slider_width/2
        self.y_screen_position = 580
        self.slider_width = slider_width
        self.slider_height = 15
        self.slider_color = "black"
        self.rectangle = pygame.Rect(self.x_screen_position, self.y_screen_position, self.slider_width, self.slider_height)
        self.speed = 5

    def visualize_slider(self, main_window):
        pygame.draw.rect(main_window, self.slider_color, self.rectangle)

    def move_slider(self, direction:int):
        # do not let slider go out of main window
        if (self.rectangle.x + self.slider_width < 800 and direction == -1) or (self.rectangle.x > 0 and direction == 1):
            self.rectangle.x = self.rectangle.x - self.speed * direction

class Ball:
    velocity = 6
    def __init__(self, x_screen_position):
        self.x_screen_position = x_screen_position
        self.y_screen_position = 570
        self.ball_radius = 10
        self.ball_color = "blue"
        self.x_speed = 0
        self.y_speed = - self.velocity
        self.utilities = Game_utils()

    def visualize_ball(self, main_window):
        pygame.draw.circle(main_window, self.ball_color, (self.x_screen_position, self.y_screen_position), self.ball_radius)  

    def move_ball(self):
        self.x_screen_position += self.x_speed
        self.y_screen_position += self.y_speed
    
    def change_speed(self, x_direction_speed, y_direction_speed):
        self.x_speed = x_direction_speed
        self.y_speed = y_direction_speed
    
    def bounce_ball_wall(self):
        if self.x_screen_position + self.ball_radius >= 800 or self.x_screen_position - self.ball_radius <= 0:
            self.change_speed(self.x_speed * -1, self.y_speed)
            return False
        elif self.y_screen_position - self.ball_radius <= 0:
            self.change_speed(self.x_speed, self.y_speed * -1)
            return False
        elif self.y_screen_position >= 600:
            return True
    
    def bounce_ball_slider(self, slider_object):
        if not slider_object.rectangle.x <= self.x_screen_position <= slider_object.rectangle.x + slider_object.slider_width:
            return
        if not 600 >= self.y_screen_position + self.ball_radius >= slider_object.rectangle.y:
            return

        slider_middle = slider_object.rectangle.x + slider_object.slider_width/2
        distance_from_slider_middle = self.x_screen_position - slider_middle # if negative ball is to the left, if positive ball is to the right of slider middle
        percent_from_slider_middle = distance_from_slider_middle / slider_object.slider_width
        bounce_angle = percent_from_slider_middle * 90
        bounce_angle_radians = math.radians(bounce_angle)
        new_x_speed = math.sin(bounce_angle_radians) * self.velocity
        new_y_speed = math.cos(bounce_angle_radians) * self.velocity * -1

        self.change_speed(new_x_speed, new_y_speed)


    def stop_ball(self, main_window):
        self.x_screen_position = main_window.get_width() + 100
        self.y_screen_position = main_window.get_height() + 100

class Brick_Breaker:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.main_window = pygame.display.set_mode((self.width, self.height))
        self.game_name = pygame.display.set_caption("Brick Breaker")

        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.slider_object = Slider(self.width/2, 120)
        self.ball_object = Ball(self.width/2)

        self.utilities = Game_utils()

    def main_loop(self):
        game_running = True
        game_over = False
        while game_running:
            self.clock.tick(self.FPS)
            self.apply_visuals()
            self.pressed_keys() # move slider
            self.ball_object.move_ball()
            self.ball_object.bounce_ball_slider(self.slider_object)
            game_over = self.ball_object.bounce_ball_wall()
            if game_over:
                game_running = False
            for game_event in pygame.event.get():
                if game_event.type == pygame.QUIT:
                    game_running = False
        while game_over:
            self.utilities.game_over_util(self.main_window)
            self.ball_object.stop_ball(self.main_window)
            for game_over_event in pygame.event.get():
                if game_over_event.type == pygame.KEYDOWN:
                    if game_over_event.key == pygame.K_SPACE:
                        game_over = False
                        self.ball_object = Ball(self.width/2)
                        self.slider_object = Slider(self.width/2, 120)
                        self.main_loop()
                elif game_over_event.type == pygame.QUIT:
                    game_over = False
        pygame.quit()
        quit()
    
    def apply_visuals(self):
        # Main window
        self.main_window.fill("white")
        # Slider
        self.slider_object.visualize_slider(self.main_window)
        # Ball
        self.ball_object.visualize_ball(self.main_window)
        # Render
        pygame.display.update()
    
    def pressed_keys(self):
        used_keys = pygame.key.get_pressed()
        if used_keys[pygame.K_a] or used_keys[pygame.K_LEFT]:
            self.slider_object.move_slider(direction = 1) # move left
        if used_keys[pygame.K_d] or used_keys[pygame.K_RIGHT]:
            self.slider_object.move_slider(direction = -1) # move right

##################################################
brick_breaker_game = Brick_Breaker()
brick_breaker_game.main_loop()