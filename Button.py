class Button:
    def __init__(self, text, text_color, font, x, y, is_center_coordinates, window, background_color=None):
        """Creates and shows a button on a pygame window

        Args:
            text (String): text for button
            text_color (Color): text color
            font (pygame.font): text font
            x (int): x position of button
            y (int): y position of button
            is_center_coordinates (bool): use x and y as center coordinates if true
            window (pygame window): window to display button on
            background_color (Color, optional): if given, a retangle will be shown around text with this color.. Defaults to None.
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

        Args:
            mouse_position (tuple): position of mouse

        Returns:
            bool: returns if the button has been clicked
        """
        return self.button_rect.collidepoint(mouse_position)
        