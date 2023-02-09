import pygame

class Slider:
    def __init__(self):
        self.x_screen_position = 400
        self.y_screen_position = 580
        self.slider_width = 100
        self.slider_height = 15
        self.slider_color = "black"
        self.rectangle = pygame.Rect(self.x_screen_position, self.y_screen_position, self.slider_width, self.slider_height)
        self.speed = 5

    def visualize_slider(self, main_window):
        pygame.draw.rect(main_window, self.slider_color, self.rectangle)

    def move_slider(self, direction:int):
        # do not let slider go out of main window
        if (self.rectangle.x + self.slider_width < 800 and direction == -1) \
            or (self.rectangle.x > 0 and direction == 1):
            self.rectangle.x = self.rectangle.x - self.speed * direction

class Ball:
    def __init__(self):
        self.x_screen_position = 450
        self.y_screen_position = 570
        self.ball_radius = 10
        self.ball_color = "blue"
        self.x_speed = 5
        self.y_speed = - self.x_speed

    def visualize_ball(self, main_window):
        pygame.draw.circle(main_window, self.ball_color, (self.x_screen_position, self.y_screen_position), self.ball_radius)  

    def move_ball(self):
        self.x_screen_position += self.x_speed
        self.y_screen_position += self.y_speed
    
    def change_speed(self, x_direction_speed, y_direction_speed):
        self.x_speed = x_direction_speed
        self.y_speed = y_direction_speed
    
    def bounce_ball(self, slider_object):
        if slider_object.rectangle.x <= self.x_screen_position <= slider_object.rectangle.x + slider_object.slider_width \
            and slider_object.rectangle.y - slider_object.slider_height/2 <= self.y_screen_position:
            self.change_speed(self.x_speed, self.y_speed * -1)
        elif self.x_screen_position in (800, 0):
            self.change_speed(self.x_speed * -1, self.y_speed)
        elif self.y_screen_position in (600, 0):
            self.change_speed(self.x_speed, self.y_speed * -1)

class Brick_Breaker:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.main_window = pygame.display.set_mode((self.width, self.height))
        self.game_name = pygame.display.set_caption("Brick Breaker")

        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.slider_object = Slider()
        self.ball_object = Ball()

    def main_loop(self):
        game_running = True
        while game_running:
            for game_event in pygame.event.get():
                if game_event.type == pygame.QUIT:
                    game_running = False
            self.clock.tick(self.FPS)
            self.apply_visuals()
            self.pressed_keys() # move slider
            self.ball_object.move_ball()
            self.ball_object.bounce_ball(self.slider_object)
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