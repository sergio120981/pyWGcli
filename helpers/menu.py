from tokenize import Number
from PyInquirer import prompt, Separator, style_from_dict, Token
import inquirer
import inquirer.shortcuts
from colorama import Fore

class Menu:
    def __init__(self) -> None:
        self.__choices=[
                    (Fore.GREEN+'1 Gestionar fichero de configuracion', 1),
                    ('1.1 Nuevo', 1.1), 
                    ('1.2 Listado', 1.2),
                    (Fore.GREEN+'2 Gestionar Peer', 2),
                    ('2.1 Nuevo', 2.1),
                    ('2.2 Listado', 2.2),
                    (Fore.GREEN+'3 Generar ficheros', 3),
                    ('3.1 Configuracion para servidor', 3.1),
                    ('3.2 Configuracion del usuario', 3.2),
                    (Fore.RED+'Salir', 4)]

    def headMenu(self) -> None:
        print(Fore.GREEN+'----------------------------------------')
        print(Fore.YELLOW+'Gestion de la configuracion de Wireguard')
        print(Fore.GREEN+'----------------------------------------')

    def mainMenu(self, opt)-> Number:
        questions = [
            inquirer.List(
                'opcion', 
                'Seleccione una opcion', 
                choices=self.__choices,
                default=opt
            )
        ]        
        answer = inquirer.prompt(questions)
        return answer['opcion']