"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as sls
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(tipo):
    
    catalog = {'videos': None,
               'categorias': None}

    catalog['videos'] = lt.newList(tipo)
    catalog['categorias'] = lt.newList('ARRAY_LIST')
    return catalog

# Funciones para agregar informacion al catalogo
def addCategory(catalog, id):
    """
    Adiciona una categoría a la lista de categorias.
    """
    lt.addLast(catalog['categorias'], id)

def addVideo(catalog, video):
    lt.addLast(catalog['videos'],video)


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByLikes(video1, video2):
    """
    Devuelve verdadero (True) si los likes de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'likes'
    video2: informacion del segundo video que incluye su valor 'likes'
    """
    return (int(video1['likes']) > int(video2['likes']))


# Funciones de ordenamiento
def comoOrdenar (sub_list, cmpVideosByLikes,ordAlg):
    if ordAlg == 1:
        return sa.sort(sub_list, cmpVideosByLikes)
    elif ordAlg == 2:
        return ins.sort(sub_list, cmpVideosByLikes)
    elif ordAlg == 3:
        return sls.sort(sub_list, cmpVideosByLikes)

def sortVideos(catalog, size, ordAlg):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = comoOrdenar(sub_list, cmpVideosByLikes,ordAlg)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list