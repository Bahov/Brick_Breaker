import pygame
import math
from game_utils import game_utils

class ball:
    velocity = 6
    def __init__(self, x_pos):
        self.x_pos = x_pos
        self.y_pos = 570
        self.radius = 9
        self.color = "blue"
        self.x_speed = 0
        self.y_speed = - self.velocity
        self.utilities = game_utils()

    def visualize_ball(self, main_window):
        pygame.draw.circle(main_window, self.color, (self.x_pos, self.y_pos), self.radius)  

    def move_ball(self):
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed
    
    def change_speed(self, x_direction_speed, y_direction_speed):
        self.x_speed = x_direction_speed
        self.y_speed = y_direction_speed
    
    def bounce_ball_wall(self):
        if self.x_pos + self.radius >= 800 or self.x_pos - self.radius <= 0:
            self.change_speed(self.x_speed * -1, self.y_speed)
            return False
        elif self.y_pos - self.radius <= 0:
            self.change_speed(self.x_speed, self.y_speed * -1)
            return False
        elif self.y_pos >= 600:
            return True
    
    def bounce_ball_slider(self, slider_object):
        if not (slider_object.rectangle.x <= self.x_pos + self.radius and slider_object.rectangle.x + slider_object.width >= self.x_pos - self.radius):
            return
        if not self.y_pos + self.radius >= slider_object.rectangle.y:
            return

        slider_middle = slider_object.rectangle.x + slider_object.width/2
        distance_from_slider_middle = self.x_pos - slider_middle # if negative ball is to the left, if positive ball is to the right of slider middle
        percent_from_slider_middle = distance_from_slider_middle / slider_object.width
        bounce_angle = percent_from_slider_middle * 90
        bounce_angle_radians = math.radians(bounce_angle)
        new_x_speed = math.sin(bounce_angle_radians) * self.velocity
        new_y_speed = math.cos(bounce_angle_radians) * self.velocity * -1

        self.change_speed(new_x_speed, new_y_speed)