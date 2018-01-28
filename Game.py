#pygame quit pour fermer fenetre + capture du clic etoile
#! /usr/bin/env python3
# coding: utf-8
"""modules to import"""
import pygame
from pygame.locals import *
from class_board import *

pitch = BoardGame.initialize_board(1)#load layout #1

gyver = McGyver()
game_on = True# true means games is on
#close_board  = False

print(pitch)

pygame.init()#pygame initialization



while game_on:

    pygame.time.Clock().tick(30)#avoid  pitcture to blink
    pitch = BoardGame.load_board(pitch) ##load object on the board
    pygame.display.flip()

## to play without graph
##    action = input("L for left/R for right / U for up / D for down")
##
##    if action.upper() == "L":
##        gyver.new_position_x = gyver.position_x
##        gyver.new_position_y = gyver.position_y - 1
##    elif action.upper() == "R":
##        gyver.new_position_x = gyver.position_x
##        gyver.new_position_y = gyver.position_y + 1
##    elif action.upper() == "U":
##        gyver.new_position_x = gyver.position_x + 1
##        gyver.new_position_y = gyver.position_y
##    elif action.upper() == "D":
##        gyver.new_position_x = gyver.position_x - 1
##        gyver.new_position_y = gyver.position_y
##    else:
##        print("problem, you should enter L for left/R for right / U for up / D for down")

#now with Pygame
    for event in pygame.event.get():##wait for keyboard events to move gyver position
        if event.type == KEYDOWN and event.key == K_LEFT:
            gyver.new_position_x = gyver.position_x
            gyver.new_position_y = gyver.position_y - 1

        if event.type == KEYDOWN and event.key == K_RIGHT:
            gyver.new_position_x = gyver.position_x
            gyver.new_position_y = gyver.position_y + 1

        if event.type == KEYDOWN and event.key == K_DOWN:
            gyver.new_position_x = gyver.position_x + 1
            gyver.new_position_y = gyver.position_y

        if event.type == KEYDOWN and event.key == K_UP:
            gyver.new_position_x = gyver.position_x - 1
            gyver.new_position_y = gyver.position_y

        if event.type == QUIT:
            game_on = False
            #close_board = True

    print(gyver.new_position_x)
    print(gyver.new_position_y)
    #on passe posution avec les x, y et le board
    next_move = Position(gyver.new_position_x, gyver.new_position_y,pitch) # not sur we need this one TBC

    next_move = Position.new_position(next_move)#
    #print(str(next_move) + "ttttr")

    if next_move == 0: # wall or out of boundary
        print("can't go that way !")
        continue

    elif next_move == 1:
        pitch[gyver.position_x][gyver.position_y] = 1#current position is set to 1 mcgyver is gone
        gyver.position_x = gyver.new_position_x#old position is now new postion
        gyver.position_y = gyver.new_position_y
        pitch[gyver.new_position_x][gyver.new_position_y] = 5#5 is mc_giver

    elif next_move == 2:
        pitch[gyver.position_x][gyver.position_y] = 1#current position is set to 1 mcgyver is gone
        gyver.position_x = gyver.new_position_x#old position is now new postion
        gyver.position_y = gyver.new_position_y
        pitch[gyver.new_position_x][gyver.new_position_y] = 5#5 is mc_giver
        gyver.goodies += 1#keep the item, incrementation
        print("nice you have just collected a new goodies")#for the console
        print("you need " + str((3 - gyver.goodies)) + \
        " more iterms to walk out !!")#for the console

    elif next_move == 3:#fight and sortie
        out = gyver.fight()

        if out == 1:
            print("well you are out!!")#for the console
            BoardGame.ending_game(1)#to display a end popup

        else:
            print("you lost! remember to collect  3 items first !!")#for the console
            BoardGame.ending_game(0)#to display a end popup

        game_on = False #breaking the while to stop the game

    else:
        print("problem move")#shouldn't enter here


    print(pitch)

   #affiche le board
   # fin boucle
#pygame.quit()#to close the board
