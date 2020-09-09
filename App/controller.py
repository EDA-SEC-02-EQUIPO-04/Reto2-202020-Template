"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
from App import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""
#Opción 1
"""
# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalog_movies():
    """
    Llama la función de inicialización del catalogo de películas del modelo.
    
    """
    # catalog_movies es utilizado para interactuar con el modelo de películas
    catalog_movies = model.newCatalog_movies()
    # catalog_casting es utilizado para interactural con l modelo de casting
    return catalog_movies

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________



def loadData(catalog_movies, movies):
    """
    Carga los datos de los archivos del modelo

    Args:
        movies (csv): Archivo  que contiene las películas
        casting (csv): Archivo que contiene el casting de las películas
    """
    loadMovies(catalog_movies, movies)


def loadMovies(catalog, moviesfile):
    """
    Carga cada una de las lineas del archivo de movies o casting.
    - Se agrega cada película al catalogo de películas
    - Por cada película se encuentran su vote average
    """
    dialect = csv.excel()
    dialect.delimiter =';'
    with open(moviesfile,encoding='utf-8-sig') as input_file:
        file_reader = csv.DictReader(input_file, dialect=dialect)
        for movie in file_reader:
            model.addMovie(catalog, movie)    
    

def movies_size(catalog):
    """
    Número de películas leídas
    """
    return model.moviesSize(catalog)


def movies_data(catalog, position):
    """
    Devuelve el vote average de la película
    """ 
    return model.movie_name(catalog,position),model.movie_relase_date(catalog,position),model.movie_vote_average(catalog,position), model.movie_vote_count(catalog,position),model.movie_language(catalog, position)

"""
