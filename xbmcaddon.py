# -*- coding: utf-8 -*-

# librería que simula xbmc para evitar errores en módulos que lo usen en mediaserver
# y no tener que poner excepciones en el código del addon

class Addon:
    def __init__(self, id):
        self.id = id

    def getSetting(self, id):
        if id =='language':
            return "it"
        return "true"
