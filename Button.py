class Button:
    def __init__(self, text_color, text, font, x, y, is_center_coordinates, window, background_color=None):
        """Creates and shows a button on a pygame window
        """
        if background_color != None:
            button_text = font.render(text, True, text_color, background_color)
        else:
            button_text = font.render(text, True, text_color)
        self.button_rect = button_text.get_rect()
        if is_center_coordinates:
            self.button_rect.center = (x, y)
        else:
            self.button_rect.left = x
            self.button_rect.top = y
        window.blit(button_text, self.button_rect)
        
    def is_clicked(self, mouse_position):
        """Returns if the button was clicked from inputted mouse position
        """
        return self.button_rect.collidepoint(mouse_position)
        