import pygame

class button:
    def __init__(self, main_window, button_name, text_font, x_pos, y_pos):
        self.main_window = main_window
        self.button_name = button_name
        self.text_font = text_font
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = "black" # default color
        self.button_text_font = pygame.font.SysFont(self.text_font, 35)
        self.button_text = self.button_text_font.render(self.button_name, True, self.color)
        self.button_rect = self.button_text.get_rect(center=(self.x_pos, self.y_pos))
        self.main_window.blit(self.button_text, self.button_rect)

    def change_color(self, color):
        self.color = color
        self.button_text = self.button_text_font.render(self.button_name, True, self.color)
        self.main_window.blit(self.button_text, self.button_rect)