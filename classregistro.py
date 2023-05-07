class Registro:
    __temperatura = 0
    __humedad = 0
    __presion = 0
    def __init__(self, t, h, p):
        self.__temperatura = t
        self.__humedad = h
        self.__presion = p
    def gettemp(self):
        return self.__temperatura
    def gethumedad(self):
        return self.__humedad
    def getpresion(self):
        return self.__presion