import requests
from bs4 import BeautifulSoup
import re

ciudades_con_vuelos = []
ciudades_a_volar = []

def buscadorCiudadOrigen(busqueda):

    ciudad = busqueda.lower()
    ciudad = re.sub(r'\s+', ' ', juego)
    ciudad = juego.replace(" ", "-")


    url_base = "https://www.ryanair.com/es/es/"
    url_juego = url_base + juego
    url_final = requests.get(url_juego, headers=headers)

    if (url_final.status_code == 404 or juego == ''):
        #print("El juego buscado no se encuentra en la base de datos de Metacritic")
        #lista_final.append("El juego introducido no se encuentra en la base de datos de Metacritic")
        return -1
