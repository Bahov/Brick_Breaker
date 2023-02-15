import pygame

class slider:
    def __init__(self, x_pos, main_window):
        self.width = 120
        self.height = 15
        self.x_pos = x_pos - self.width/2
        self.y_pos = main_window.get_height() - 20 # 20 pixels of the screen bottom
        self.color = "black"
        self.rectangle = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.speed = 6

    def visualize_slider(self, main_window):
        pygame.draw.rect(main_window, self.color, self.rectangle)

    def move_slider(self, direction:int):
        # do not let slider go out of main window
        if (self.rectangle.x + self.width < 800 and direction == -1) or (self.rectangle.x > 0 and direction == 1):
            self.rectangle.x = self.rectangle.x - self.speed * direction

    def pressed_keys(self):
        used_keys = pygame.key.get_pressed()
        if used_keys[pygame.K_a] or used_keys[pygame.K_LEFT]:
            self.move_slider(direction = 1) # move left
        if used_keys[pygame.K_d] or used_keys[pygame.K_RIGHT]:
            self.move_slider(direction = -1) # move right