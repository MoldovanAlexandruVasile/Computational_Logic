'''

@author: Moldovan Alexandru-Vasile
Group: 915

'''

from ui import *
from controller import *
        

def mainMenu():

    command = -1

    while command != 0:

        menu()

        command = readCommand()

        if validMenuCommand(command) == True:

            if command == 1:

                x = input ("\n \t Number 1: ")
                print("\n \t             +")
                y = input ("\n \t Number 2: ")
                base = readBase()

                print("\n \t Result: ", addition(x,y,base)," base: ", base)

            elif command == 2:

                x = input("\n \t Number 1: ")
                print("\n \t             -")
                y = input("\n \t Number 2: ")
                base = readBase()

                print("\n \t Result: ", subtraction(x, y, base), " base: ", base)

            elif command == 3:

                x = input("\n \t Number 1: ")
                print("\n \t             *")
                y = input("\n \t Number 2: ")
                base = readBase()

                print("\n \t Result: ", multiplication(x, y, base), " base: ", base)

            elif command == 4:

                x = input("\n \t Number 1: ")
                print("\n \t             /")
                y = input("\n \t Number 2: ")
                base = readBase()

                print("\n \t Result: ", division(x, y, base)[0], "remainder: ",division(x, y, base)[1], " base: ", base)

            elif command == 5: conversion()


        else: print("\n Invalid data !")


mainMenu()
