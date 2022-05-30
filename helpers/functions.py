
from tokenize import Number


class Functions:
    def __init__(self) -> None:
        self.__menuChoices={
        1.1: self.__interfaceNuevo(),
        1.2: self.__interfaceListado(),
        2.1: self.__peerNuevo(),
        2.2: self.__peerListado(),
        3.1: self.__fileServidor(),
        3.2: self.__fileUsuario()
        }

    def getOption(self, id) -> Number:
        return self.__menuChoices.get(id)

    def __interfaceNuevo (self) -> Number :
        return 1.1

    def __interfaceListado (self) -> Number:
        return 1.2

    def __peerNuevo (self) -> Number :
        return 2.1

    def __peerListado (self) -> Number :
        return 2.2
    
    def __fileServidor (self) -> Number :
        return 3.1

    def __fileUsuario (self) -> Number :
        return 3.2