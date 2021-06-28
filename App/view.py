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
sys.setrecursionlimit(default_limit)

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
    print("3- Requerimiento 1")
    print("4- Requerimiento 2")
    print("5- Requerimiento 3")
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
    if int(inputs) == 1:
        correcto = False
        while correcto == False:
            print('Seleccione el tipo de representación de la lista: \n1- ArrayList\n2- LinkedList')
            tipoLista = int(input('Ingrese 1 o 2\n'))
            if tipoLista == 1:
                tipoLista = 'ARRAY_LIST (Seleccionar para los requerimientos del reto.)'
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
        print ("Categorías cargadas: ", controller.printCategories(catalog))

    elif int(inputs) == 2:
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

    elif int(inputs) == 3:
        categoria = ' '+ input("Ingrese la categoría a buscar: ")
        pais = input("Ingrese el filtro de país: ")
        n = int(input("Ingrese la cantidad de videos que quiere listar: "))
        rtas = controller.req1(catalog, pais, categoria,n)
        for i in range(1, n+1):
            top = (lt.getElement(rtas,i))['elements']
            print(top)
    elif int(inputs)==4:
        pais = input("Ingrese el filtro de país: ")
        rta= controller.req2(catalog,pais)
        if rta == "No hay ningún video con ese ratio de likes/dislikes":
            print(rta)
        else:
            imprimir = []
            for ind in range(1,lt.size(rta)+1):
               imprimir.append(lt.getElement(rta,ind))
            imprimir = imprimir[:-1]
            imprimir = imprimir[:2]+[pais]+imprimir[2:]
            print(imprimir)
    elif int(inputs) == 5:
        category = input("Ingrese la categoría a consultar: ")
        rtaP = controller.req3(catalog,category)
        rta5 = rtaP[0]
        if rta5 == "No hay ningún video con ese ratio de likes/dislikes":
            print(rta5)
        else:
            imprimir = []
            for ind in range(1,lt.size(rta5)+1):
               imprimir.append(lt.getElement(rta5,ind))
            imprimir = imprimir[:-1]
            imprimir = imprimir[:2]+[rtaP[1]]+imprimir[2:]
            print(imprimir)
    else:
        sys.exit(0)
sys.exit(0)
