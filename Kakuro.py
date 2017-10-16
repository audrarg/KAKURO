import random
import DictionaryLib


class Kakuro:
    matriz = []
    Diccionario = DictionaryLib.Dictionary()

    def CrearKakuro(self, filas, columnas):
        self.matriz = []
        self.LlenarMatrix(filas, columnas)
        for index, fila in enumerate(self.matriz):
            if index > 0:
                disponibles = self.CeldasDisponibles(index)
                while disponibles[0] >= 3:
                    disponibles = self.CeldasDisponibles(index)
                    if disponibles[0] >= 3:
                        posicion = random.randint(disponibles[1], columnas - 3)
                        self.Diccionario.SacarCombinaciones(2, random.randint(2, columnas - posicion - 1))
                        indice = random.randrange(0, len(self.Diccionario.combinaciones), 2)
                        self.RellenarFila(index, posicion, self.Diccionario.combinaciones[indice],
                                          self.Diccionario.combinaciones[indice + 1])
                        if index > 1:
                            while self.Sumas() == False:
                                self.LimpiarFila(index, posicion, len(self.Diccionario.combinaciones[indice + 1]) + 1)
                                self.Diccionario.combinaciones.pop(indice)
                                self.Diccionario.combinaciones.pop(indice)
                                if len(self.Diccionario.combinaciones) > 0:
                                    indice = random.randrange(0, len(self.Diccionario.combinaciones), 2)
                                    self.RellenarFila(index, posicion, self.Diccionario.combinaciones[indice],
                                                      self.Diccionario.combinaciones[indice + 1])
        self.PrintMatriz(self.matriz)
        self.SumasVerticales(self.matriz)
        return self.matriz

    def LlenarMatrix(self, filas, columnas):
        for i in range(filas):
            self.matriz.append([-1] * columnas)

    def SumasVerticales(self, resultado):
        for indiceF, fila in enumerate(resultado):
            array = [fila[indiceF] for fila in resultado]
            iniciado = False
            suma = 0
            indice = 0
            arraysuma = []
            for index, elemento in enumerate(array):
                if elemento < 0:
                    iniciado = True
                    if suma > 0 and len(arraysuma) > 1:
                        if array[indice] > -1:
                            resultado[indice][indiceF] = (suma, resultado[indice][indiceF])
                        else:
                            resultado[indice][indiceF] = (suma,)
                    suma = 0
                    indice = index
                    arraysuma = []
                if elemento > 0 and iniciado == True:
                    suma += elemento
                    arraysuma.append(elemento)
                if index == len(array)-1 and len(arraysuma) > 1:
                    if array[indice] != -1:
                        resultado[indice][indiceF] = (suma, resultado[indice][indiceF])
                    else:
                        resultado[indice][indiceF] = (suma,)
                    suma = 0
                    arraysuma = []

        self.PrintMatriz(resultado)

    def CeldasDisponibles(self, i):
        numero = 0
        indice = 0
        iniciado = False
        for index, columna in enumerate(self.matriz[i]):
            if columna == -1:
                numero += 1
                if iniciado == False:
                    indice = index
                    iniciado = True
            if columna != -1:
                numero = 0
                iniciado = False
        return numero, indice

    def Sumas(self):
        column = []
        for index1, columna in enumerate(self.matriz[1]):
            for index, fila in enumerate(self.matriz):
                if self.matriz[index][index1] > 0:
                    column.append(self.matriz[index][index1])
                else:
                    m = [i for i, x in enumerate(column) if column.count(x) > 1]
                    if len(m) > 0:  ##and len(column) < 10:
                        return False
                    column = []
        return True

    def RellenarFila(self, i, j, numero, valores):
        iniciado = False
        index = 0
        for ind, columna in enumerate(self.matriz[i]):
            if ind == j or iniciado == True:
                if iniciado == False:
                    self.matriz[i][ind] = -numero
                    iniciado = True
                elif iniciado == True and index < len(valores):
                    self.matriz[i][ind] = valores[index]
                    index += 1

    def LimpiarFila(self, i, j, tam):
        iniciado = False
        for index, columna in enumerate(self.matriz[i]):
            if index == j or iniciado == True:
                if tam != 0:
                    self.matriz[i][index] = -1
                    tam -= 1
                    iniciado = True
                else:
                    return

    def PrintMatriz(self, matriz):
        for fila in matriz:
            for columna in fila:
                print columna,
            print
        print
        print
