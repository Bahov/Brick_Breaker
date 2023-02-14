import pygame
from button import button

class game_menus:
    pygame.init()

    def __init__(self):
        pass

    def main_menu(self, main_window):
        while True:
            main_menu_text_font = pygame.font.SysFont("comicsans", 50)
            main_menu_text_x_pos = main_window.get_width()/2
            main_menu_text_y_pos = 100
            main_menu_text = main_menu_text_font.render("Main Menu", True, "black")
            main_menu_rect = main_menu_text.get_rect(center=(main_menu_text_x_pos, main_menu_text_y_pos))
            main_window.blit(main_menu_text, main_menu_rect)

            mouse_position = pygame.mouse.get_pos()

            play_game_button = button(main_window, "Play Game", "comicsans", main_window.get_width()/2, 200)
            game_options_button = button(main_window, "Game Options", "comicsans", main_window.get_width()/2, 300)
            game_info_button = button(main_window, "Game Info", "comicsans", main_window.get_width()/2, 400)
            quit_game_button = button(main_window, "Quit Game", "comicsans", main_window.get_width()/2, 500)

            if play_game_button.button_rect.collidepoint(mouse_position):
                play_game_button.change_color("white")
                if pygame.mouse.get_pressed()[0] == 1: # left mouse butoon [1] middle [2] right
                    return True # continue main loop (exit_game_menu)
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