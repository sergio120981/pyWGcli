from __future__ import print_function, unicode_literals
from helpers.menu import Menu
from helpers.functions import Functions

def main ():
    print("\033[H\033[3J", end="")
    menu=Menu()
    menu.headMenu()
    opcion=menu.mainMenu(1)
    func = Functions()

    while( opcion !=4 ):
        print("\033[H\033[3J", end="")

        print(func.getOption(opcion))

        menu.headMenu()
        opcion=menu.mainMenu(opcion)
        
main()