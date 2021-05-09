class TextBox:
    def __init__(self, text, text_color, font, x, y, is_center_coordinates, window, background_color=None):
        """Creates and shows a text box on a pygame window
        """
        if background_color != None:
            text_field = font.render(text, True, text_color, background_color)
        else:
            text_field = font.render(text, True, text_color)
        
        text_field_rect = text_field.get_rect()
        if is_center_coordinates:
            text_field_rect.center = (x, y)
        else:
            text_field_rect.left = x
            text_field_rect.top = y
        window.blit(text_field, text_field_rect)