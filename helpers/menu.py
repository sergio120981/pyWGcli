from PyInquirer import prompt, Separator, style_from_dict, Token
import inquirer
import inquirer.shortcuts
from colorama import Fore

class Menu:
    def __init__(self) -> None:
        pass

    def headMenu(self) -> None:
        print(Fore.GREEN+'----------------------------------------')
        print(Fore.YELLOW+'Gestion de la configuracion de Wireguard')
        print(Fore.GREEN+'----------------------------------------')

    def mainMenu(self, opt)-> None:
        questions = [
            inquirer.List(
                'opcion', 
                'Seleccione una opcion', 
                choices=[
                    (Fore.GREEN+'1 Gestionar fichero de configuracion', 1),
                    ('1.1 Nuevo', 1.1), 
                    ('1.2 Listado', 1.2),
                    (Fore.GREEN+'2 Gestionar Peer', 2),
                    ('2.1 Nuevo', 2.1),
                    ('2.2 Listado', 2.2),
                    (Fore.GREEN+'3 Generar ficheros', 3),
                    ('3.1 Configuracion para servidor', 3.1),
                    ('3.2 Configuracion del usuario', 3.2),
                    (Fore.RED+'Salir', 4),
                ],
                default=opt
            )
        ]
        """ {
            'type': 'list',
            'name': 'opcion',
            'message': '',
            'choices': [
                Separator('1. Gestionar fichero de configuracion'),
                {'name':'1.1 Nuevo', 'value':1.1}, 
                {'name':'1.2 Listado', 'value':1.2}, 
                Separator('2. Gestionar Peer'),
                {'name':'2.1 Nuevo', 'value':2.1}, 
                {'name':'2.2 Listado', 'value':2.2}, 
                Separator('3. Generar ficheros'), 
                {'name':'3.1 Configuracion para servidor', 'value':3.1}, 
                {'name':'3.2 Configuracion del usuario', 'value':3.2}, 
                Separator(), 
                {'name':'4. Salir', 'value':0},
            ]
        }] """
        
        answers = inquirer.prompt(questions)
        return answers