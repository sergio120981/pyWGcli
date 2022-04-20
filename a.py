from __future__ import print_function, unicode_literals
from helpers.menu import Menu


def main ():
    print("\033[H\033[3J", end="")
    menu=Menu()
    menu.headMenu()
    a=menu.mainMenu(1)
    
    while(a['opcion']!=4):
        print("\033[H\033[3J", end="")
        menu.headMenu()
        a=menu.mainMenu(a['opcion'])

main()