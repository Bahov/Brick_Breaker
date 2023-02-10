import pygame
import math
import time

class Game_utils:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("comicsans", 28)

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
    
    def populate_bricks_list(self, rows, columns, main_window):
        brick_between_space = 5
        bricks_top_space = 30
        brick_width = main_window.get_width() // columns - brick_between_space
        brick_height = 20
        duration_color_dict = {5:"purple",4:"red",3:"orange",2:"yellow",1:"green"}

        bricks = []
        for row in range(rows):
            for col in range(columns):
                if row == 0:
                    brick_duration = 5
                    current_brick = Brick(brick_width * col + brick_between_space * (col + 1), \
                                        brick_height * row + bricks_top_space, \
                                        brick_width, brick_height, brick_duration, duration_color_dict[brick_duration], brick_difficulty=brick_duration)
                else:
                    if row == 1:
                        brick_duration = 5
                    elif row in (2,3):
                        brick_duration = 4
                    elif row in (4,5):
                        brick_duration = 3
                    elif row in (6,7):
                        brick_duration = 2
                    else:
                        brick_duration = 1
                    current_brick = Brick(brick_width * col + brick_between_space * (col + 1), \
                                        brick_height * row + brick_between_space * row + bricks_top_space, \
                                        brick_width, brick_height, brick_duration, duration_color_dict[brick_duration], brick_difficulty=brick_duration)
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

class Slider:
    def __init__(self, x_screen_position, slider_width):
        self.x_screen_position = x_screen_position - slider_width/2
        self.y_screen_position = 580
        self.slider_width = slider_width
        self.slider_height = 15
        self.slider_color = "black"
        self.rectangle = pygame.Rect(self.x_screen_position, self.y_screen_position, self.slider_width, self.slider_height)
        self.speed = 6

    def visualize_slider(self, main_window):
        pygame.draw.rect(main_window, self.slider_color, self.rectangle)

    def move_slider(self, direction:int):
        # do not let slider go out of main window
        if (self.rectangle.x + self.slider_width < 800 and direction == -1) or (self.rectangle.x > 0 and direction == 1):
            self.rectangle.x = self.rectangle.x - self.speed * direction

    def pressed_keys(self):
        used_keys = pygame.key.get_pressed()
        if used_keys[pygame.K_a] or used_keys[pygame.K_LEFT]:
            self.move_slider(direction = 1) # move left
        if used_keys[pygame.K_d] or used_keys[pygame.K_RIGHT]:
            self.move_slider(direction = -1) # move right

class Ball:
    velocity = 6
    def __init__(self, x_screen_position):
        self.x_screen_position = x_screen_position
        self.y_screen_position = 570
        self.ball_radius = 9
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
        if not (slider_object.rectangle.x <= self.x_screen_position + self.ball_radius and slider_object.rectangle.x + slider_object.slider_width >= self.x_screen_position - self.ball_radius):
            return
        if not self.y_screen_position + self.ball_radius >= slider_object.rectangle.y:
            return

        slider_middle = slider_object.rectangle.x + slider_object.slider_width/2
        distance_from_slider_middle = self.x_screen_position - slider_middle # if negative ball is to the left, if positive ball is to the right of slider middle
        percent_from_slider_middle = distance_from_slider_middle / slider_object.slider_width
        bounce_angle = percent_from_slider_middle * 90
        bounce_angle_radians = math.radians(bounce_angle)
        new_x_speed = math.sin(bounce_angle_radians) * self.velocity
        new_y_speed = math.cos(bounce_angle_radians) * self.velocity * -1

        self.change_speed(new_x_speed, new_y_speed)

class Brick:
    def __init__(self, x_screen_position, y_screen_position, brick_width, brick_height, brick_duration, brick_color, brick_difficulty):
        self.x_screen_position = x_screen_position
        self.y_screen_position = y_screen_position
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_duration = brick_duration
        self.brick_color = brick_color
        self.brick_difficulty = brick_difficulty
        self.rectangle = pygame.Rect(self.x_screen_position, self.y_screen_position, self.brick_width, self.brick_height)
        self.duration_color_dict = {5:"purple",4:"red",3:"orange",2:"yellow",1:"green"}

    def visualize_brick(self, main_window):
        pygame.draw.rect(main_window, self.brick_color, self.rectangle)
    
    def ball_hit_brick(self, ball_object):
        if not (ball_object.x_screen_position - ball_object.ball_radius <= self.x_screen_position + self.brick_width and ball_object.x_screen_position + ball_object.ball_radius >= self.x_screen_position):
            return
        if not (ball_object.y_screen_position - ball_object.ball_radius <= self.y_screen_position +self.brick_height and ball_object.y_screen_position + ball_object.ball_radius >= self.y_screen_position):
            return
        self.brick_duration -= 1
        ball_object.change_speed(ball_object.x_speed, ball_object.y_speed * - 1) # reverse the vertical direction of the ball
              
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
        self.bricks = self.utilities.populate_bricks_list(10, 11, self.main_window)

        self.lives = 3
        self.points = 0

        self.seconds = 3

    def main_loop(self):
        game_running = True
        game_over = False
        while game_running:
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
            game_over = self.ball_object.bounce_ball_wall()
            if game_over:
                self.lives -= 1
                if self.lives > 0:
                    # continue and reposition ball in center of slider
                    self.ball_object.x_screen_position = self.slider_object.rectangle.x + self.slider_object.slider_width/2
                    self.ball_object.y_screen_position = self.slider_object.rectangle.y - self.slider_object.slider_height
                    self.main_loop() 
                else:
                    game_running = False
                    self.utilities.game_over_util(self.main_window)
            for game_event in pygame.event.get():
                if game_event.type == pygame.QUIT:
                    game_running = False
            for brick in self.bricks:
                brick.ball_hit_brick(self.ball_object) # will decrease duration by one
                if brick.brick_duration <= 0:
                    self.bricks.remove(brick)
                    self.points += brick.brick_difficulty
                else:
                    brick.brick_color = brick.duration_color_dict[brick.brick_duration] # update color of brick
        while game_over:
            for game_over_event in pygame.event.get():
                if game_over_event.type == pygame.KEYDOWN:
                    if game_over_event.key == pygame.K_SPACE:
                        game_over = False
                        self.ball_object = Ball(self.width/2)
                        self.slider_object = Slider(self.width/2, 120)
                        self.bricks = self.utilities.populate_bricks_list(10, 11, self.main_window)
                        self.lives = 3
                        self.points = 0
                        self.main_loop()
                elif game_over_event.type == pygame.QUIT:
                    game_over = False
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

##################################################
brick_breaker_game = Brick_Breaker()
brick_breaker_game.main_loop()