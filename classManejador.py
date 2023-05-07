import csv
from classregistro import Registro

class manejador:
    __lista=[]
    __fila = 0
    __columna = 0
    def __init__(self, fil=30, col=24): #filas -> dias | columnas -> horas
        self.__fila = fil
        self.__columna = col
    
    def cargadatos(self):   #CARGA DE LA MATRIZ
        for i in range(self.__fila):    #DEFINICION DE LA MATRIZ EN LA CUAL SE ALMACENAN LAS INSTANCIAS
            lista = []
            for j in range(self.__columna):
                lista.append(None)
            self.__lista.append(lista)
        with open('variablesmeteorologicas.csv') as archivo:
            lector = csv.reader(archivo, delimiter=',')
            next(lector)
            for row in lector:
                fila = int(row[0])   #DIA -> FILAS DE LA MATRIZ
                colum = int(row[1])  #HORAS -> COLUMNAS DE LA MATRIZ
                t = float(row[2])      #TEMPERATURA
                h = int(row[3])      #HUMEDAD
                p = int(row[4])      #PRESION
                vm = Registro(t, h, p)
                self.__lista[fila-1][colum] = vm
    
    def opcion1(self):  #FUNCIONAL -> CON ERRORES
        #MAX Y MIN PARA LA VARIABLE TEMPERATURA
        maxT = 0
        minT = 9999
        #MAX Y MIN PARA LA VARIABLE HUMEDAD
        maxH = 0
        minH = 9999
        #MAX Y MIN PARA LA VARIABLE PRESION
        maxP = 0
        minP = 9999
        xi_min = 0      # -> indice para el dia (valor minimo)
        xi_max = 0      # -> indice para el dia (valor maximo)
        xj_min = 0      # -> indice para la hora (valor minimo)
        xj_max = 0      # -> indice para la hora (valor maximo)

        #TEMPERATURA
        print("VALORES MAXIMOS Y MINIMOS -> TEMPERATURA")
        i = 0
        j = 0
        for i in range(len(self.__lista)):  #dias (filas)
            for j in range(len(self.__lista[i])):  #horas (columnas)
                if (self.__lista[i][j].gettemp() > maxT):
                    maxT = self.__lista[i][j].gettemp()
                    xi_max = i  #dia maximo
                    xj_max = j  #hora maxima
                if self.__lista[i][j].gettemp() < minT:
                    minT = self.__lista[i][j].gettemp()
                    xi_min = i  #dia minimo
                    xj_min = j  #hora minima
        print("El dia {} a las {} horas se registro la temperatura maxima ({}°C)".format(xi_max+1, xj_max, maxT))
        print("El dia {} a las {} horas se registro la temperatura minima ({}°C)".format(xi_min+1, xj_min, minT))

        print("VALORES MAXIMOS Y MINIMOS -> HUMEDAD")
        for i in range(len(self.__lista)):  #dias (filas)
            for j in range(len(self.__lista[i])):  #horas (columnas)
                if self.__lista[i][j].gethumedad() > maxH:
                    maxH = self.__lista[i][j].gethumedad()
                    xi_max = i
                    xj_max = j
                if self.__lista[i][j].gethumedad() < minH:
                    minH = self.__lista[i][j].gethumedad()
                    xi_min = i
                    xj_min = j
        print("El dia {} a las {} horas se registro la humedad maxima ({}%)".format(xi_max+1, xj_max, maxH))
        print("El dia {} a las {} horas se registro la humedad minima ({}%)".format(xi_min+1, xj_min, minH))

        print("VALORES MAXIMOS Y MINIMOS -> PRESION ATMOSFERICA")
        for i in range(len(self.__lista)):  #dias (filas)
            for j in range(len(self.__lista[i])):  #horas (columnas)
                if self.__lista[i][j].getpresion() > maxP:
                    maxP = self.__lista[i][j].getpresion()
                    xi_max = i
                    xj_max = j
                if self.__lista[i][j].getpresion() < minP:
                    minP = self.__lista[i][j].getpresion()
                    xi_min = i
                    xj_min = j
        print("El dia {} a las {} horas se registro la presion maxima ({}mb)".format(xi_max+1, xj_max, maxP))
        print("El dia {} a las {} horas se registro la presion minima ({}mb)".format(xi_min+1, xj_min, minP))
        print("----------------------------------------")
        print("\n")

    def opcion2(self):  #NO INICIADO
        i = 0   #dia -> fila
        j = 0   #hora -> columna
        for j in range(len(self.__lista[j])):
            sum = float(0)
            for i in range(len(self.__lista)):
                sum += self.__lista[i][j].gettemp()
            prom = round(sum/30, 2)
            print("Temperatura promedio (Hora: {}) -> {}".format(j, prom))
        print("----------------------------------------")
        print("\n")

    
    def opcion3(self, d):   #FUNCIONAL -> SIN ERRORES
        print("___________________________________________")
        print("{:^10} {:^10} {:^10} {:^10}".format('Hora', 'Temperatura', 'Humedad', 'Presion'))
        for j in range(len(self.__lista[d-1])):
            print("{:^10} {:^10} {:^10} {:^10}".format(j, self.__lista[d-1][j].gettemp(), self.__lista[d-1][j].gethumedad(), self.__lista[d-1][j].getpresion()))
        print("___________________________________________")