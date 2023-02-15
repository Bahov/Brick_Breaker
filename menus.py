import pygame
from button import button

class game_menus:
    pygame.init()

    def __init__(self):
        self.button_clicked = False
        self.level = ""

    def main_menu(self, main_window):
        while True:
            self.menu_title(main_window, 100, "Main Menu", "black")

            mouse_position = pygame.mouse.get_pos()

            play_game_button = button(main_window, "Play Game", "comicsans", main_window.get_width()/2, 200)
            game_options_button = button(main_window, "Game Options", "comicsans", main_window.get_width()/2, 300)
            game_info_button = button(main_window, "Game Info", "comicsans", main_window.get_width()/2, 400)
            quit_game_button = button(main_window, "Quit Game", "comicsans", main_window.get_width()/2, 500)           

            if play_game_button.button_rect.collidepoint(mouse_position):
                play_game_button.change_color("white")
                if pygame.mouse.get_pressed()[0] == 1 and self.button_clicked == False: # left mouse butoon [1] middle [2] right
                    self.button_clicked = True
                    while True:
                        main_window.fill("gray")
                        self.menu_title(main_window, 100, "Choose Level", "black")
                        # levels
                        level1_button = button(main_window, "Level 1", "comicsans", main_window.get_width()/2, 200)
                        level2_button = button(main_window, "Level 2", "comicsans", main_window.get_width()/2, 300)
                        level3_button = button(main_window, "Level 3", "comicsans", main_window.get_width()/2, 400)
                        level4_button = button(main_window, "Level 4", "comicsans", main_window.get_width()/2, 500)
                        if pygame.mouse.get_pressed()[0] == 0:
                            self.button_clicked = False
                            mouse_position = pygame.mouse.get_pos()
                            for game_event in pygame.event.get():
                                if game_event.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()
                            if level1_button.button_rect.collidepoint(mouse_position):
                                level1_button.change_color("white")
                                if pygame.mouse.get_pressed()[0] == 1 and self.button_clicked == False:
                                    self.button_clicked = True 
                                    self.level = "level1"
                                    break
                            elif level2_button.button_rect.collidepoint(mouse_position):
                                level2_button.change_color("white")
                                if pygame.mouse.get_pressed()[0] == 1 and self.button_clicked == False:
                                    self.button_clicked = True
                                    self.level = "level2"
                                    break   
                            elif level3_button.button_rect.collidepoint(mouse_position):
                                level3_button.change_color("white")
                                if pygame.mouse.get_pressed()[0] == 1 and self.button_clicked == False:
                                    self.button_clicked = True
                                    self.level = "level3"
                                    break   
                            elif level4_button.button_rect.collidepoint(mouse_position):
                                level4_button.change_color("white")
                                if pygame.mouse.get_pressed()[0] == 1 and self.button_clicked == False:
                                    self.button_clicked = True
                                    self.level = "level4"
                                    break   
                        for game_event in pygame.event.get():
                            if game_event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        pygame.display.update()
                    return True, self.level # exit to main_loop (return the selected level as well)
            if game_options_button.button_rect.collidepoint(mouse_position):
                game_options_button.change_color("white")
            if game_info_button.button_rect.collidepoint(mouse_position):
                game_info_button.change_color("white")
            if quit_game_button.button_rect.collidepoint(mouse_position):
                quit_game_button.change_color("white")
                if pygame.mouse.get_pressed()[0] == 1:
                    pygame.quit()
                    quit()

            for game_event in pygame.event.get():
                if game_event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            pygame.display.update()
    
    def menu_title(self, main_window, y_pos, menu_name, menu_color):
        text_font = pygame.font.SysFont("comicsans", 50)
        x_pos = main_window.get_width()/2
        menu_text = text_font.render(menu_name, True, menu_color)
        menu_rect = menu_text.get_rect(center=(x_pos, y_pos))
        main_window.blit(menu_text, menu_rect)