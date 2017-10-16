import itertools


class Dictionary:
    ##Diccionario con todas las combinaciones
    dictionary = {}
    combinaciones = []

    def __init__(self):
        ##Resultado de las permutaciones
        for a in range(2, 10):
            ##Contiene todas las combinaciones con toda la cantidad de digitos
            lista = [x for x in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], a)]
            ##Suma de los elementos de las combinaciones
            numero = 0

            for i in range(0, len(lista)):
                for j in range(0, len(lista[i])):
                    ##Suma los elementos de la lista[i]
                    numero += lista[i][j]
                if self.dictionary.has_key(str(numero)):
                    ##Agrega la nueva combinacion del numero
                    self.dictionary[str(numero)].append(lista[i])
                else:
                    ##Crea el nuevo item del diccionario
                    self.dictionary[str(numero)] = [lista[i]]
                numero = 0

    def SacarCombinaciones(self, inicio, fin):

        lista2 = []
        for i in range(3, 46):
            lista1 = self.dictionary.get(str(i))
            for j in range(0, len(lista1)):
                for a in range(inicio, fin + 1):
                    if len(lista1[j]) == a:
                        lista2.append(i)
                        lista2.append(lista1[j])

        self.combinaciones = lista2
