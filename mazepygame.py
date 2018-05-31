"""Welcome yo the Macgyver Game, the code bellow
preent all composant of the game, using OOP"""


#Here All necessary imports for the project
import random

import pygame 

from pygame.locals import *

from constants import *


class Game:
    def __init__(self):
        """initialising pygame"""
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.maze = list(list())
        # Creation of all the elements
        self.macgyver = Player()
        self.wall = Element("wall")
        self.path = Element("path")
        self.tube = Element("tube")
        self.ether = Element("ether")
        self.needle = Element("needle")
        self.guardian = Element("guardian")
        self.store_map()
        self.macgyver.move_y = self.find_pos(self.macgyver)[0]
        self.macgyver.move_x = self.find_pos(self.macgyver)[1]
        self.show_map_pygame()
        # Random position for MacGyver and other items
        self.random_pos(self.tube)
        self.random_pos(self.ether)
        self.random_pos(self.needle)
        self.random_pos(self.macgyver)
        self.show_map_pygame()
        self.show_map_pygame()
        #The game loop, keep the game running while end condition is not completed.
        self.keep_run = True
        while self.keep_run:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.keep_run = 0
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.update_pos("S")
                        self.show_map_pygame()
                    if event.key == K_UP:
                        self.update_pos("N")
                        self.show_map_pygame()
                    if event.key == K_RIGHT:
                        self.update_pos("E")
                        self.show_map_pygame()
                    if event.key == K_LEFT:
                        self.update_pos("W")
                        self.show_map_pygame()
                        
    def store_map(self):
        """Stocking the map in a 2D list""" 
        with open("my-map.txt", "r") as file_r:
            for line in file_r:
                self.maze.append([char for char in line if char != "\n"])

    def show_map_pygame(self):
        """show the maze with pygame interface"""
        for i, line in enumerate(self.maze):

            for j, char in enumerate(line):
                if char == self.wall.letter:
                    self.window.blit(self.wall.image, (SPRITE_SIZE * j, SPRITE_SIZE * i))
                if char == self.macgyver.letter:
                    self.window.blit(self.macgyver.image, (SPRITE_SIZE * j, SPRITE_SIZE * i))
                if char == self.path.letter:
                    self.window.blit(self.path.image, (SPRITE_SIZE * j, SPRITE_SIZE * i))
                if char == self.ether.letter:
                    self.window.blit(self.ether.image, (SPRITE_SIZE * j, SPRITE_SIZE * i))
                if char == self.needle.letter:
                    self.window.blit(self.needle.image, (SPRITE_SIZE * j, SPRITE_SIZE * i))
                if char == self.tube.letter:
                    self.window.blit(self.tube.image, (SPRITE_SIZE * j, SPRITE_SIZE * i))
                if char == self.guardian.letter:
                    self.window.blit(self.guardian.image, (SPRITE_SIZE * j, SPRITE_SIZE * i))
        pygame.display.flip()

    def find_pos(self, elt):
        """ Find the position of a letter in the maze """
        m_line = 0
        m_col = 0
        for i, line in enumerate(self.maze):
            for j, char in enumerate(line):
                if char == elt.letter:
                    m_line = i
                    m_col = j
        return m_line, m_col

    def random_pos(self, elt):
        """give a position to Macgyver in the maze"""
        line, col = self.find_pos(elt)
        char = ""
        rand_line = 0
        rand_char = 0
        # Check if it is a wall or not
        while char != "-":
            rand_line = random.randint(0, len(self.maze)-1)
            rand_char = random.randint(0, len(self.maze[0])-1)
            char = self.maze[rand_line][rand_char]
        self.maze[line][col] = "-"
        self.maze[rand_line][rand_char] = elt.letter
        elt.x = rand_char
        elt.y = rand_line
        #print(elt.x, elt.y, elt.letter)
    def update_pos(self, direction):
        """This method subject is updating the position after moving"""
        self.old_x_pos = self.macgyver.move_x
        self.old_y_pos = self.macgyver.move_y
        self.macgyver.move(direction)
        if self.maze[self.macgyver.move_y][self.macgyver.move_x] == "W":
            self.macgyver.move_x = self.old_x_pos
            self.macgyver.move_y = self.old_y_pos
            print("Can't across a wall")
        else:
            if self.maze[self.macgyver.move_y][self.macgyver.move_x] in ["T", "E", "N"]:
                self.macgyver.list_obj.append(self.maze[self.macgyver.move_y][self.macgyver.move_x])
                print(self.macgyver.list_obj)
            if self.maze[self.macgyver.move_y][self.macgyver.move_x] == "G":
                if len(self.macgyver.list_obj) == 3:
                    self.macgyver.move_x = self.old_x_pos
                    self.macgyver.move_y = self.old_y_pos
                    print("GAME OVER : You Won, Congrats !")
                    self.keep_run = False
                else:
                    self.macgyver.move_x = self.old_x_pos
                    self.macgyver.move_y = self.old_y_pos
                    print("GAME OVER : You Lose!")
                    self.keep_run = False

            self.maze[self.macgyver.move_y][self.macgyver.move_x] = "M"
            self.maze[self.old_y_pos][self.old_x_pos] = "-"


class Element:
    """This class made to make and upload all elemnts of the game (loots, hero ..etc)"""
    def __init__(self, elt):
        """Define the initiale emplacemnt of all elements"""

        if elt == "macgyver":
            self.image = pygame.image.load(MACGYVER_PIC).convert()
            self.letter = "M"
        elif elt == "wall":
            self.image = pygame.image.load(WALL_PIC).convert()
            self.letter = "W"
        elif elt == "path":
            self.image = pygame.image.load(PATH_PIC).convert()
            self.letter = "-"
        elif elt == "ether":
            self.image = pygame.image.load(ETHER_PIC).convert()
            self.letter = "E"
        elif elt == "tube":
            self.image = pygame.image.load(TUBE_PIC).convert()
            self.letter = "T"
        elif elt == "needle":
            self.image = pygame.image.load(NEEDLE_PIC).convert()
            self.letter = "N"
        elif elt == "guardian":
            self.image = pygame.image.load(GUARDIAN_PIC).convert()
            self.letter = "G"

        self._position_x = 0
        self._position_y = 0

    def _get_position_x(self):
        return self._position_x

    def _set_position_x(self, new_x):
        self._position_x = new_x

    def _get_position_y(self):
        return self._position_y

    def _set_position_y(self, new_y):
        self._position_y = new_y

    x = property(_get_position_x, _set_position_x)
    y = property(_get_position_y, _set_position_y)

    
class Player(Element):

    def __init__(self):
        """Creat a list to stock the loots in"""
        Element.__init__(self, "macgyver")
        self.list_obj = []


    def move(self, direction):
        """a method to define the mouvements of Macgyver"""


        if direction == "N":
            self.move_y = self.move_y - 1
        elif direction == "S":
            self.move_y = self.move_y + 1
        elif direction == "E":
            self.move_x = self.move_x + 1
        elif direction == "W":
            self.move_x = self.move_x - 1

if __name__ == "__main__":
    GAME = Game()


