import pygame

class game_menus:
    space_between_buttons = 20
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

            play_game_rect = self.play_game(main_window)
            if play_game_rect.collidepoint(mouse_position):
                if pygame.mouse.get_pressed()[0] == 1: # left mouse butoon [1] middle [2] right
                    return True # continue main loop (exit_game_menu)
            self.game_options(main_window)
            self.game_info(main_window)
            self.quit_game(main_window)

            for game_event in pygame.event.get():
                if game_event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            pygame.display.update()

    
    def play_game(self, main_window):
        play_game_text_font = pygame.font.SysFont("comicsans", 35)
        play_game_text_x_pos = main_window.get_width()/2
        play_game_menu_text_y_pos = 200
        play_game_text = play_game_text_font.render("Play Game", True, "black")
        play_game_rect = play_game_text.get_rect(center=(play_game_text_x_pos, play_game_menu_text_y_pos))
        main_window.blit(play_game_text, play_game_rect)
        return play_game_rect

    def game_options(self, main_window):
        game_options_text_font = pygame.font.SysFont("comicsans", 35)
        game_options_text_x_pos = main_window.get_width()/2
        game_options_menu_text_y_pos = 300
        game_options_text = game_options_text_font.render("Game Options", True, "black")
        game_options_rect = game_options_text.get_rect(center=(game_options_text_x_pos, game_options_menu_text_y_pos))
        main_window.blit(game_options_text, game_options_rect)

    def game_info(self, main_window):
        game_info_text_font = pygame.font.SysFont("comicsans", 35)
        game_info_text_x_pos = main_window.get_width()/2
        game_info_menu_text_y_pos = 400
        game_info_text = game_info_text_font.render("Game Info", True, "black")
        game_info_rect = game_info_text.get_rect(center=(game_info_text_x_pos, game_info_menu_text_y_pos))
        main_window.blit(game_info_text, game_info_rect)

    def quit_game(self, main_window):
        quit_game_text_font = pygame.font.SysFont("comicsans", 35)
        quit_game_text_x_pos = main_window.get_width()/2
        quit_game_menu_text_y_pos = 500
        quit_game_text = quit_game_text_font.render("Quit Game", True, "black")
        quit_game_rect = quit_game_text.get_rect(center=(quit_game_text_x_pos, quit_game_menu_text_y_pos))
        main_window.blit(quit_game_text, quit_game_rect)