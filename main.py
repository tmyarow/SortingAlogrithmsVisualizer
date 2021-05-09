import pygame
from List import List
from Button import Button
from TextBox import TextBox

#Create constants
WIDTH = 1000
HEIGHT = 700
FPS = 60
MAX_ELEMENT_HEIGHT = 450
MAX_LIST_WIDTH = 900

#Setup Pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sorting Algorithms Visualizer')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

#Create variables used in run loop
list = List()
bottom_left_pos = (50, 500)
current_ticks = 0
is_first_run = True
sort_type = ""
speed = 10

run = True

while run:
    current_ticks += 1
    clock.tick(FPS)
    window.fill(pygame.Color('Black'))

    #Draw line seperating control panel
    pygame.draw.line(window, pygame.Color('White'), (0, HEIGHT - 150), (WIDTH, HEIGHT - 150), 1)
    
    #Draw border for list display
    pygame.draw.rect(window, pygame.Color("Red"), (49, 49, 902, 452))
    pygame.draw.rect(window, pygame.Color("Black"), (50, 50, 900, 450))

    #Create buttons
    bubble_sort_button = Button(pygame.Color("Grey"), "Bubble Sort", font, 130, 575, True, window)
    selection_sort_button = Button(pygame.Color("Grey"), "Selection Sort", font, 370, 575, True, window)
    insertion_sort_button = Button(pygame.Color("Grey"), "Insertion Sort", font, 650, 575, True, window)
    bogo_sort_button = Button(pygame.Color("Grey"), "Bogo Sort", font, 880, 574, True, window)

    increase_button = Button(pygame.Color("Grey"), "Increase", font, WIDTH // 2 + 100, 625, True, window)
    decrease_button = Button(pygame.Color("Grey"), "Decrease", font, WIDTH // 2 - 100, 625, True, window)
    
    slower_button = Button(pygame.Color("Yellow"), "Slower", font, WIDTH // 2 - 150, 680, True, window)
    stop_button = Button(pygame.Color("Red"), "Stop", font, WIDTH // 2, 680, True, window)
    faster_button = Button(pygame.Color("Green"), "Faster", font, WIDTH // 2 + 150, 680, True, window)

    reset_button = Button(pygame.Color("Grey"), "Reset", font, 10, HEIGHT - 40, False, window)

    #Show sort type being done
    if sort_type:
        sort_type_text = TextBox(sort_type.capitalize() + "Sort", pygame.Color("Grey"), font, WIDTH // 2,  25, True, window)
    
    #Draw list
    list.display_list(window, bottom_left_pos, MAX_ELEMENT_HEIGHT, MAX_LIST_WIDTH)
    
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN: #Respond to button presses
            if bubble_sort_button.is_clicked(event.pos):
                sort_type = "bubble"
            elif selection_sort_button.is_clicked(event.pos):
                sort_type = "selection"
            elif insertion_sort_button.is_clicked(event.pos):
                sort_type = "insertion"
            elif bogo_sort_button.is_clicked(event.pos):
                sort_type = "bogo"
            elif stop_button.is_clicked(event.pos):
                sort_type = ""
                is_first_run = True
            elif slower_button.is_clicked(event.pos):
                if speed < 40:
                    speed *= 2
            elif faster_button.is_clicked(event.pos):
                if speed // 4 != 0:
                    speed //= 4
                elif speed // 2 != 0:
                    speed //= 2
            elif reset_button.is_clicked(event.pos):
                is_first_run = True
                sort_type = ""
                length = list.length
                list = List(length)
            elif increase_button.is_clicked(event.pos):
                is_first_run = True
                sort_type = ""
                list.increase_size()
            elif decrease_button.is_clicked(event.pos):
                is_first_run = True
                sort_type = ""
                list.decrease_size()

    
    #Run sorting algorithm
    if sort_type and not list.sorted and current_ticks % speed == 0:
        if sort_type == "bubble":
            list.bubble_sort(is_first_run)
        elif sort_type == "selection":
            list.selection_sort(is_first_run)
        elif sort_type == "insertion":
            list.insertion_sort(is_first_run)
        elif sort_type == "bogo":
            list.bogo_sort(is_first_run)

        is_first_run = False

    pygame.display.update()