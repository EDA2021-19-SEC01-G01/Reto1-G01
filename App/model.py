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


from DISClib.DataStructures.arraylist import getElement
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

def printCategories(catalog):
    categorias = catalog['categorias']
    listaNombres = []
    for llave in range(1,lt.size(categorias)+1):
        line = lt.getElement(categorias,llave)
        nombre = line['name']
        listaNombres.append(nombre)
    return listaNombres

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

def cmpVideosByTrend(video1, video2):
    """
    Devuelve verdadero (True) si los TrendDays :) de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor días en Trend
    video2: informacion del segundo video que incluye su valor días en Trend
    """
    rta=(lt.lastElement(video1))> (lt.lastElement(video2))
    return rta


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

def comoOrdenar2 (sub_list, cmpVideosByLikes,ordAlg):
    if ordAlg == 1:
        return sa.sort(sub_list, cmpVideosByTrend)
    elif ordAlg == 2:
        return ins.sort(sub_list, cmpVideosByTrend)
    elif ordAlg == 3:
        return sls.sort(sub_list, cmpVideosByTrend)
    elif ordAlg == 4:
        return mrg.sort(sub_list, cmpVideosByTrend)
    elif ordAlg == 5:
        return qck.sort(sub_list, cmpVideosByTrend)

def sortVideos(catalog, size, ordAlg):
    sub_list = lt.subList(catalog['videos'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = comoOrdenar(sub_list, cmpVideosByLikes,ordAlg)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg

def sortVideos2(listaFinal, ordAlg, n):
    sorted_list = comoOrdenar(listaFinal, cmpVideosByLikes,ordAlg)
    subList = lt.subList(sorted_list,1,n)
    return subList

def sortVideos3 (listaFinal,ordAlg):
    sortedList=comoOrdenar2(listaFinal,cmpVideosByTrend,ordAlg)
    top_trend=lt.firstElement(sortedList)
    return top_trend

def filtroCategory(catalog, category, lista):
    categorias = catalog['categorias']
    listaFinal = lt.newList("ARRAY_LIST")
    for llave in range(1,lt.size(categorias)+1):
        line = lt.getElement(categorias,llave)
        if category in (line['name']):
            id = line['id']
    for i in range(1,lt.size(lista)+1):
        video = lt.getElement(lista,i)
        if video['category_id'] == id:
            lt.addLast(listaFinal, video)
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
    criterios = ['trending_date','title','channel_title','publish_time','views','likes','dislikes']
    for j in range(1,lt.size(lista)+1):
        listaPorVideo = lt.newList('ARRAY_LIST')
        for crit in criterios:
            video = lt.getElement(lista,j)
            lt.addLast(listaPorVideo,video[crit])
        lt.addLast(listaFinalFinal,listaPorVideo)
    return listaFinalFinal

def filtroPaiscompleto(catalog, country):
    soloCountry = lt.newList("ARRAY_LIST")
    ids = []
    vid = catalog['videos']
    for i in range(1,lt.size(vid)+1):
        ele = lt.getElement(vid,i)
        c1 = ele['country']
        id1 = ele['video_id']
        if c1 == country:
            lt.addLast(soloCountry, ele)
            ids.append(id1)

    return soloCountry

def ratioLikesDislikes (lista, umbral):
    #Calcula los vídeos con un rating mayor a umbral.
    for j in range(1,lt.size(lista)+1):
        ele=lt.getElement(lista,j)
        vid_id=ele['video_id']
        likes=int(ele["likes"])
        dislikes=int(ele["dislikes"])
        dict_id={}
        if vid_id not in dict_id:
            count=0 
            dict_id[vid_id]=[likes,dislikes,count+1]
        else:
            dict_id[vid_id][0]=likes
            dict_id[vid_id][1]=dislikes
            dict_id[vid_id][2]+=1

    for i in dict_id:
        
        lista_id_top=[]
        if dict_id[i][1]==0 and dict_id[i][0]>0:
            lista_id_top.append([i,"no tiene dislikes",dict_id[i][2]])
        else:
            ratio=dict_id[i][0]/dict_id[i][1]
            if ratio>umbral:
                lista_id_top.append([i,ratio,dict_id[i][2]])
    return lista_id_top

def printReq2(lista,listatop):                 
    lista_final=lt.newList(datastructure="ARRAY_LIST")
    criterios=["country","channel_title","title"]
    for j in listatop:
        id=j[0]
        ratio=j[1]
        trendTotal=j[2]
        ids=[]
        listaPorVideo=lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(listaPorVideo,ratio)
        lt.addLast(listaPorVideo,trendTotal)
        for i in range(1,lt.size(lista)+1):
            ele=lt.getElement(lista,i)
            vid_id=ele['video_id']
            if id == vid_id and (id in ids) == False:
                ids.append(id)
                for crit in criterios:
                    lt.addFirst(listaPorVideo,ele[crit])
                break
            lt.addLast(lista_final,listaPorVideo)
    return lista_final

def req2 (catalog,country):
        "Agrupa todas las funciones que desarrollan el requerimiento 2"
        listaPais = filtroPais(catalog,country)
        listaRating = ratioLikesDislikes(listaPais, 10)
        listaTop=printReq2(listaPais,listaRating)
        listaImprimir =sortVideos3(listaTop, 4)
        return listaImprimir

def requerimiento3(catalog, category):
    listaCat = filtroCategory(catalog, category, catalog['videos'])
    filtroRatio = ratioLikesDislikes(listaCat, 20)
 


        
            



