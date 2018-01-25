#! /usr/bin/env python3
# coding: utf-8

"""modules to import"""
from random import randint
import pygame

class BoardGame:
    """in order to create the board game + loading items"""
    BOARD = []
    SIZE = 16
    WINDOW = pygame.display.set_mode((600, 600))#window create 600 as (15*40px =600px)
    #loading all the pictures for the board
    WALL = pygame.image.load("picture/wall.png").convert_alpha()
    FLOOR = pygame.image.load("picture/floor.png").convert_alpha()
    ETHER = pygame.image.load("picture/ether.jpg").convert_alpha()
    TUBE = pygame.image.load("picture/tube.png").convert_alpha()
    NEEDLE = pygame.image.load("picture/needle.jpg").convert_alpha()
    WAYOUT = pygame.image.load("picture/exit.png").convert_alpha()
    MCGYVER = pygame.image.load("picture/macgyver.png").convert_alpha()
    #loading picture for end of the game popup
    GAMEOVER = pygame.image.load("picture/gameover.png").convert_alpha()
    WIN = pygame.image.load("picture/win.png").convert_alpha()


    def __init__(self):
        pass

    @classmethod
    def initialize_board(cls, layout):
        """initializion : load the layout from file to build a 2D maze (lists in lists)
        + loading 3 items at random position + loading pictures
        """
        #path where to get the maze layout
        path_to_file = "layout/" + str(layout) + "_layout.txt"
        with open(path_to_file, 'r') as file:
            board = []
            for line in file:
                i = 0
                list_second = [] # slice line in a list
                while i < 15: #not working for class variable - to avoid newline caracter
                    list_second.append(int(line[i]))# in integer rather str for later
                    i += 1
                board.append(list_second)#add line to the global list

        i = 1
        while i < 4: #3 items to drop (4 -1)
            random_x = randint(0, 14) # random coordinate in the board
            random_y = randint(0, 14)

            random_item = board[random_x][random_y] #check the value

            if random_item == 1: # if not a wall
                board[random_x][random_y] = i + 1 # change from 1 to other int
                i += 1#incrementation - find a place for next item

            else:
                continue # it's a wall back to the while, no incrementaton another try/

        return board

    @classmethod#to get load_board to work
    def load_board(cls, board):
        """load pictures using pygame - wall, floor needle, tube, mcgyver, wayout
         according to values in the list (from the layout file)"""
        line_x = 0#first line
        for cases in board:
            cell_y = 0#first column
            for case in cases:
                if case == 0:
                    cls.WINDOW.blit(cls.WALL, (cell_y, line_x))
                    cell_y += 40#40 because cell is 40 px => so go to next cell

                elif case == 1:#if corridor
                    cls.WINDOW.blit(cls.FLOOR, (cell_y, line_x))
                    cell_y += 40

                elif case == 2:#if ether
                    cls.WINDOW.blit(cls.ETHER, (cell_y, line_x))
                    cell_y += 40

                elif case == 3:#if needle
                    cls.WINDOW.blit(cls.NEEDLE, (cell_y, line_x))
                    cell_y += 40

                elif case == 4:#if tube
                    cls.WINDOW.blit(cls.TUBE, (cell_y, line_x))
                    cell_y += 40

                elif case == 9:#wayout
                    cls.WINDOW.blit(cls.WAYOUT, (cell_y, line_x))
                    cell_y += 40

                elif case == 5:#mcgyver
                    cls.WINDOW.blit(cls.MCGYVER, (cell_y, line_x))
                    pygame.display.flip()
                    cell_y += 40

                else:
                    cell_y += 40
            line_x += 40#line_x is the line, so go to next line
        return(board)

    @classmethod
    def ending_game(cls, result):
        """to display a popup when games ends - see fct fight from McGyver"""
        if result == 1:#would come from fct fight
            cls.WINDOW.blit(cls.WIN, (20, 20))
            pygame.display.flip()
        elif result == 0:
            cls.WINDOW.blit(cls.GAMEOVER, (20, 20))
            pygame.display.flip()
        else:
            print('result should be 0 or 1')#fight should return 0 or 1.


class McGyver:
    """mc_gyver set with positions (0,0 to start), items and fct fight to exit
    """

    def __init__(self):
        """Mcgyver starts at 0,0 corner up and left and 0 items/goodies"""
        self.goodies = 0 # items collected
        self.position_x = 0 # starting position with board[x][y]
        self.position_y = 0
        self.new_position_x = 0 # with board[x][y]
        self.new_position_y = 0

    def fight(self):
        """to win gyvwe must have collected 3 items"""
        if self.goodies == 3:
            win = 1
        else:
            win = 0
        return win


class Position:
    """to manage mcgyver's movement"""

    def __init__(self, position_x, position_y, board):
        """position is set with x and y + a board game"""
        self.position_x = position_x #
        self.position_y = position_y
        self.board = board # board to check new position, wall, item or exit

    def new_position(self):
        """to check if a move is allowed"""
        if self.position_x < 0 or self.position_y < 0 or self.position_x > 14 or self.position_y > 14: # out the board
            move = 0#no move before cell assignation to avoid out of range error

        else:#if in the board we check if we can move
            cell = self.board[self.position_x][self.position_y]
            if cell == 0: # wall ! can't move
                move = 0#no move
            elif cell == 2 or cell == 3 or cell == 4:
                move = 2#move +you got an item?
            elif cell == 9:
                move = 3#means fight to exit
            else:
                move = 1#RAS move that's it

        return move