import pygame

class start_menu:
    space_between_buttons = 20
    pygame.init()

    def __init__(self):
        self.font = pygame.font.SysFont("comicsans", 28)
    
    def start_button(self, main_window, enable_clic = False):
        text_start_button = self.font.render(f"Start Game", True, "black")
        main_window.blit(text_start_button, (main_window.get_width()/2 - text_start_button.get_width()/2, 100))
        text_start_button_rect = pygame.Rect(main_window.get_width()/2 - text_start_button.get_width()/2, 100, text_start_button.get_width(), text_start_button.get_height())
        if not enable_clic:
            pygame.display.update()
        if enable_clic:
            clicked = False
            mouse_position = pygame.mouse.get_pos()
            if text_start_button_rect.collidepoint(mouse_position):
                if pygame.mouse.get_pressed()[0] == 1 and clicked == False: #[0] left mouse butoon [1] middle [2] right
                    clicked = True
            return clicked