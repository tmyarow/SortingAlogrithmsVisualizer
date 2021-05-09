import random
import pygame

class List:
    def __init__(self, length=None, list=None):
        """Creates a new list to be sorted using various algorithms. If a list is passed in, length will be ignored
        if it is also passed in

        Args:
            length (int, optional): length of list to be created. Defaults to None.
            list (list, optional): list of numbers to be used for self.list. Defaults to None.
        """
        #Sets up a list to be sorted
        self.create_valid_lengths(450)
        if list:
            self.list = list
            self.length = len(list)
            self.length_index = self.valid_lengths.index(self.length)
        else:
            if length and length in self.valid_lengths:
                self.length = length
                self.length_index = self.valid_lengths.index(length)
            else:
                self.length_index = 10
                self.length = self.valid_lengths[self.length_index]
            self.generate_random_list()
        #Create variables used in sorting algorithms
        self.sorted = False
        self.red_index = []
        self.green_index = []

    def create_valid_lengths(self, max_element_height):
        """Creates a list called valid_lengths that contains list lengths that will display nicely

        Args:
            max_element_height (int): maximum height of each element on window
        """
        self.valid_lengths = []
        for n in range(1, max_element_height + 1):
            if max_element_height % n == 0:
                self.valid_lengths.append(n)


    def generate_random_list(self):
        """Creates a random list of numbers if non are given, or stores given list
        """
        self.list = []
        for i in range(self.length):
            number = random.randint(1, self.length)
            while number in self.list:
                number = random.randint(1, self.length)
            self.list.append(number)


    def increase_size(self):
        """Increases the size of the list
        """
        if self.length != 450:
            self.length_index += 1
            self.length = self.valid_lengths[self.length_index]
            self.generate_random_list()

    def decrease_size(self):
        """Decreases the size of the list
        """
        if self.length != 5:
            self.length_index -= 1
            self.length = self.valid_lengths[self.length_index]
            self.generate_random_list()
    
    def swap(self, index1, index2):
        """Swaps two elements in a list

        Args:
            index1 (int): first index of the list to be swapped
            index2 (int): second index of the list to be swapped
        """
        self.list[index1], self.list[index2] = self.list[index2], self.list[index1]
    
    def bubble_sort(self, is_first_run):
        """This functions completes one step of the bubble sort algorithm.

        Args:
            is_first_run (bool): This is true if this is the first time bubble sort is being called
        """
        #If this is the first time function is being run, set up global variables
        if is_first_run:
            self.n_passes = 0
            self.step = 0
        
        #Log indexes to be shown in gui
        if not self.sorted:
            self.red_index = [self.step, self.step + 1]
        
        #Complete one step of bubble sort algorithm
        if self.list[self.step] > self.list[self.step + 1]:
            self.swap(self.step, self.step + 1)
        
        #Make necessary changes to self.step and self.n_passes for next iteration
        self.step += 1
        if self.n_passes == self.length - 1 and self.step == 1:
            self.red_index = []
            self.sorted = True
        
        if self.step == self.length - self.n_passes - 1:
            self.step = 0
            self.n_passes += 1

    def selection_sort(self, is_first_run):
        """This function completes one step of the selection sort algorithm

        Args:
            is_first_run (bool): this is true if it is the first time selection sort is being called
        """
        
        #Setup global variables needed for selection_sort if is first run
        if is_first_run:
            self.current_index = self.min_element_index = self.sorted_elements = 0

        #Show current index and index to be swapped in red, and show min element index in green
        if not self.sorted:
            self.red_index = [self.current_index, self.sorted_elements]
            self.green_index = [self.min_element_index]
        
        #If minimum element has been found
        if self.current_index == self.length:
            self.swap(self.sorted_elements, self.min_element_index)
            self.sorted_elements += 1
            self.current_index = self.sorted_elements
            self.min_element_index = self.current_index
        #If current element is smaller than min element, make min index current index
        elif self.list[self.current_index] < self.list[self.min_element_index]:
            self.min_element_index = self.current_index
        
        #Increase current index for next iteration
        self.current_index += 1
        
        #Check if list is sorted
        if self.sorted_elements == self.length:
            self.sorted = True
            self.red_index = []
            self.green_index = []

    def insertion_sort(self, is_first_run):
        """This completes one step of the insertion sort algorithm

        Args:
            is_first_run (bool): this is true if it is the first time insertion sort is being called
        """
        if is_first_run:
            self.current_index = 1
            self.next_index = 2

        self.red_index = [self.current_index - 1]

        if self.current_index == 0:
            self.current_index = self.next_index
        elif self.list[self.current_index] < self.list[self.current_index - 1]:
            self.swap(self.current_index, self.current_index - 1)
            self.current_index -= 1
        else:
            self.current_index = self.next_index
            self.next_index += 1

        if self.current_index == self.length:
            self.sorted = True
            self.red_index = []

    def bogo_sort(self):
        """Completes one step of the bogo sort algorithm
        """
        if not self.is_sorted():
            self.shuffle()
            self.tried_lists.append(self.list)

    def is_sorted(self):
        """This is a helper function for bogo sort. It returns if self.list is sorted in increasing order

        Returns:
            bool: returns if the list is true or not
        """
        for i in range(self.length - 1):
            if self.list[i] > self.list[i + 1]:
                return False
        return True

    def shuffle(self):
        """This is a helper function for bogo sort. It randomly shuffles self.list
        """
        for i in range(self.length):
            self.swap(i, random.randint(0, self.length - 1))


    def display_list(self, window, bottom_left_pos, max_element_height, max_list_width):
        """This function displays self.list on a pygame window

        Args:
            window (Pygame Window): Window to display list on
            bottom_left_pos (tuple): Position of the bottom left of the space that list will be shown at
            max_element_height (int): the maximum height of an element
            max_list_width (int): the width that all elements in the list will take up
        """
        element_width = max_list_width / self.length
        for index, value in enumerate(self.list):
            x = bottom_left_pos[0] + (index * element_width)
            y = bottom_left_pos[1] - ((max_element_height / self.length) * value)
            width = element_width
            height = (max_element_height / self.length) * value
            #Print rectangle for debug
            # print("x: " + str(x) + ", y: " + str(y) + ", width = " + str(width) + ", height = " + str(height))
            if index in self.red_index:
                color = "Red"
            elif index in self.green_index:
                color = "Lime Green"
            else:
                color = "White"
            pygame.draw.rect(window, pygame.Color(color), (x, y, width, height))