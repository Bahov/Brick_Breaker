import pygame

class brick:
    def __init__(self, x_pos, y_pos, width, height, duration, color, difficulty):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.duration = duration
        self.color = color
        self.difficulty = difficulty
        self.rectangle = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.duration_color_dict = {5:"purple",4:"red",3:"orange",2:"yellow",1:"green"}

    def visualize_brick(self, main_window):
        pygame.draw.rect(main_window, self.color, self.rectangle)
    
    def ball_hit_brick(self, ball_object):
        if not (ball_object.x_pos - ball_object.radius <= self.x_pos + self.width and ball_object.x_pos + ball_object.radius >= self.x_pos):
            return
        if not (ball_object.y_pos - ball_object.radius <= self.y_pos +self.height and ball_object.y_pos + ball_object.radius >= self.y_pos):
            return
        self.duration -= 1
        ball_object.change_speed(ball_object.x_speed, ball_object.y_speed * - 1) # reverse the vertical direction of the ball