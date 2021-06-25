"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import sys 
from DISClib.ADT import list as lt
assert cf
default_limit=1000
sys.setrecursionlimit(default_limit*3002)



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Ordenar los videos por likes, categoría y país")
    print("0- Salir")

catalog = None

"""
Menu principal
"""

def initCatalog(tipo):
    return controller.initCatalog(tipo)


def loadData(catalog):
    controller.loadData(catalog)

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        correcto = False
        while correcto == False:
            print('Seleccione el tipo de representación de la lista: \n1- ArrayList\n2- LinkedList')
            tipoLista = int(input('Ingrese 1 o 2\n'))
            if tipoLista == 1:
                tipoLista = 'ARRAY_LIST'
                correcto = True
            elif tipoLista == 2:
                tipoLista = 'SINGLE_LINKED'
                correcto = True
            else:
                print('No es una opción válida :)\n')
        print("Cargando información de los archivos ....")
        catalog = initCatalog(tipoLista)
        loadData(catalog)
        size = lt.size(catalog['videos'])
        print ("Total de registros de videos cargados: " + str(size))
        print ("Información primer video: ", lt.firstElement(catalog['videos']))
        print ("Categorías cargadas: ", (catalog['categorias']))

    elif int(inputs[0]) == 2:
        correcto = False
        while correcto == False:
            tamano = int(input("Indique tamaño de la muestra: "))
            if tamano <= size:
                correcto = True
            else:
                print('No es una opción válida :)\n')
        centinela=False
        while centinela==False:
            print('Seleccione el tipo de representación de la lista: \n1- ShellSort\n2- InsertionSort\n3- SelectionSort\n4- MergeSort\n5- QuickSort ')
            ordAlg = int(input('Ingrese 1, 2, 3, 4 o 5\n'))
            if (ordAlg in (1,2,3,4,5))==False:
                print('No es una opción válida :)\n')
            else:
                centinela=True
        result = controller.sortVideos(catalog, int(tamano), ordAlg)
        print(result)
    else:
        sys.exit(0)
sys.exit(0)
