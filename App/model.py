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
from DISClib.Algorithms.Sorting import quicksort as qck
from DISClib.Algorithms.Sorting import mergesort as mrg

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
    elif ordAlg == 4:
        return mrg.sort(sub_list, cmpVideosByLikes)
    elif ordAlg == 5:
        return qck.sort(sub_list, cmpVideosByLikes)

def sortVideos(catalog, size, ordAlg):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = comoOrdenar(sub_list, cmpVideosByLikes,ordAlg)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg

def sortVideos2(listaFinal, ordAlg, n):
    sorted_list = comoOrdenar(listaFinal, cmpVideosByLikes,ordAlg)
    subList = lt.subList(sorted_list,0,n)
    return subList

def filtroCategory(catalog, category, lista):
    categorias = catalog['categorias']
    listaFinal = lt.newList("ARRAY_LIST")
    for llave in categorias.keys():
        if categorias[llave] == category:
            id = llave
    for i in lista:
        if i['category_id'] == id:
            lt.addLast(listaFinal, i)
    return listaFinal


def filtroPais(catalog, country):
    soloCountry = lt.newList("ARRAY_LIST")
    ids = []
    vid = catalog['videos']
    for i in range(1,lt.size(vid)+1):
        ele = lt.getElement(vid,i)
        c1 = ele['country']
        id1 = ele['video_id']
        if c1 == country and (id1 in ids) == False:
            lt.addLast(soloCountry, ele)
            ids.append(id1)

    return soloCountry

def req1(catalog, country, category,n):
    "Agrupa todas las funciones que desarrollan el requerimiento 1"
    listaPais = filtroPais(catalog,country)
    listaOrdenar = filtroCategory(catalog,category, listaPais)
    listaLista = sortVideos2(listaOrdenar, 4,n)
    listaImprimir = printReq1(listaLista)
    return listaImprimir

def printReq1(lista):
    listaFinalFinal = lt.newList('ARRAY_LIST')
    criterios = ['trending_date','title','cannel_title','publish_time','views','likes','dislikes']
    for j in lista['elements']:
        listaPorVideo = lt.newList('ARRAY_LIST')
        for crit in criterios:
            lt.addLast(listaPorVideo,j[crit])
        lt.addLast(listaFinalFinal,listaPorVideo)
    return listaFinalFinal



