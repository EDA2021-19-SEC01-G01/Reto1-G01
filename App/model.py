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
    days1 = lt.getElement(video1,4)
    days2 = lt.getElement(video2,4)
    if days1 == days2:
        rat1 = lt.getElement(video1,3)
        rat2 = lt.getElement(video2,3)
        if type(rat1) != float or type(rat2) != float:
            rta = (days1 > days2)
        else:
            rta = (rat1 > rat2)
    else:
        rta = (days1 > days2)
    return rta

def cmpR4(v1,v2):
    return (int(v1['comment_count']) > int(v2['comment_count']))

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

def comoOrdenar2 (sub_list, cmpVideosByTrend,ordAlg):
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

def comoOrdenar3(sub_list, cmpR4,ordAlg):
    if ordAlg == 1:
        return sa.sort(sub_list, cmpR4)
    elif ordAlg == 2:
        return ins.sort(sub_list, cmpR4)
    elif ordAlg == 3:
        return sls.sort(sub_list, cmpR4)
    elif ordAlg == 4:
        return mrg.sort(sub_list, cmpR4)
    elif ordAlg == 5:
        return qck.sort(sub_list, cmpR4)

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

def sortVideos3 (listaFinal,ordAlg,cmp):
    sortedList=comoOrdenar2(listaFinal,cmp,ordAlg)
    if lt.size(sortedList) == 0:
        return "No hay ningún video con ese ratio de likes/dislikes"
    else:
        top_trend=lt.firstElement(sortedList)
        return top_trend

def sv4(lista,oa,cmp):
    sortedList=comoOrdenar3(lista,cmp,oa)
    rta= lt.firstElement(sortedList)
    return rta

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
    return [listaFinal,id]


def filtroPais(catalog, country):
    soloCountry = lt.newList("ARRAY_LIST")
    ids = []
    vid = catalog['videos']
    for i in range(1,lt.size(vid)+1):
        ele = lt.getElement(vid,i)
        c1 = ele['country']
        id1 = ele['video_id']
        if c1 == country:
            lt.addLast(soloCountry, ele)

    return soloCountry

def filtroPais2(catalog, country):
    soloCountry = lt.newList("ARRAY_LIST")
    ids = []
    vid = catalog['videos']
    tamano = lt.size(vid)
    for i in range(0,tamano):
        ele = lt.getElement(vid,tamano-i)
        c1 = ele['country']
        id1 = ele['video_id']
        if c1 == country and (id1 in ids) == False:
            lt.addLast(soloCountry, ele)
            ids.append(id1)
    return soloCountry

def req1(catalog, country, category,n):
    "Agrupa todas las funciones que desarrollan el requerimiento 1"
    listaPais = filtroPais2(catalog,country)
    listaOrdenar = (filtroCategory(catalog,category, listaPais))[0]
    listaLista = sortVideos2(listaOrdenar, 4,n)
    listaImprimir = printReq1(listaLista, ['trending_date','title','channel_title','publish_time','views','likes','dislikes'])
    return listaImprimir

def printReq1(lista, criterios):
    listaFinalFinal = lt.newList('ARRAY_LIST')
    for j in range(1,lt.size(lista)+1):
        listaPorVideo = lt.newList('ARRAY_LIST')
        for crit in criterios:
            video = lt.getElement(lista,j)
            lt.addLast(listaPorVideo,video[crit])
        lt.addLast(listaFinalFinal,listaPorVideo)
    return listaFinalFinal

def ratioLikesDislikes (lista, umbral):
    #Calcula los vídeos con un rating mayor a umbral.
    dict_id={}
    lista_id_top=lt.newList("ARRAY_LIST")
    for j in range(1,lt.size(lista)+1):
        ele=lt.getElement(lista,j)
        vid_id=ele['video_id']
        likes=int(ele["likes"])
        dislikes=int(ele["dislikes"])
        title = ele['title']
        channel_title = ele['channel_title']
        if vid_id not in dict_id:
            count=0 
            dict_id[vid_id]=[likes,dislikes,count+1,title,channel_title]
        else:
            dict_id[vid_id][0]=likes
            dict_id[vid_id][1]=dislikes
            dict_id[vid_id][2]+=1
    for i in dict_id:
        if dict_id[i][1]==0 and dict_id[i][0]>0:
            xd = lt.newList("ARRAY_LIST")
            lt.addLast(xd,dict_id[i][3])
            lt.addLast(xd,dict_id[i][4])
            lt.addLast(xd,"no tiene dislikes")
            lt.addLast(xd,dict_id[i][2])
            lt.addLast(xd,i)
            lt.addLast(lista_id_top,xd)
        elif dict_id[i][0]==0:
            pass
        else:
            ratio=dict_id[i][0]/dict_id[i][1]
            if ratio>umbral:
                xd = lt.newList("ARRAY_LIST")
                lt.addLast(xd,dict_id[i][3])
                lt.addLast(xd,dict_id[i][4])
                lt.addLast(xd,ratio)
                lt.addLast(xd,dict_id[i][2])
                lt.addLast(xd,i)
                lt.addLast(lista_id_top,xd)
    return lista_id_top

def req2 (catalog,country):
        "Agrupa todas las funciones que desarrollan el requerimiento 2"
        listaPais = filtroPais(catalog,country)
        listaRating = ratioLikesDislikes(listaPais, 10)
        listaImprimir =sortVideos3(listaRating, 4, cmpVideosByTrend)
        return listaImprimir

def requerimiento3(catalog, category):
    listaCat = filtroCategory(catalog, category, catalog['videos'])
    id = listaCat[1]
    filtroRatio = ratioLikesDislikes(listaCat[0], 20)
    listaFinal = sortVideos3(filtroRatio, 4, cmpVideosByTrend)
    return listaFinal,id
 
def req4(c,p,n,t):
    clas = lt.newList("ARRAY_LIST")
    ids = []
    vid = c['videos']
    dicc= {}
    for i in range(1,lt.size(vid)+1):
        ele = lt.getElement(vid,i)
        c1 = ele['country']
        id = ele['video_id']
        tag = ele["tags"]
        a1,a2,a3= (c1==p),(id not in ids), (t in tag)
        if a1 and a2 and a3 :
            ids.append(id)
            e= lt.newList("ARRAY_LIST")
            dicc[id]= e
            lt.addLast(dicc[id],ele)
        elif a1 and a3:
            lt.addLast(dicc[id],ele)
        
    for i in dicc.keys():
        if lt.size(dicc[i]) > 0:
            d= sv4(dicc[i],4,cmpR4)
            lt.addLast(clas,d)
        else:
            print(dicc[i])
            lt.addLast(clas,lt.firstElement(dicc[i]))
    
    l_final= comoOrdenar3(clas,cmpR4,4)
    rta= []
    for i in range(1,n+1):
        rta.append(lt.getElement(l_final,i))
    rta2 = lt.newList('ARRAY_LIST')
    for diccionario in rta:
        lt.addLast(rta2,diccionario)

    rtaF = printReq1(rta2,['title', 'channel_title','publish_time','views','likes','dislikes','comment_count','tags'])
    finaliza = []
    for indice in range(1,lt.size(rtaF)+1):
        dato = lt.getElement(rtaF,indice)
        finaliza.append(dato['elements'])
    return finaliza
