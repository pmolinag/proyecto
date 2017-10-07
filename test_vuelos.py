import requests
from bs4 import BeautifulSoup
import re

class ciudad_origen():
    def __init__(self):
        self.corigen = []

    corigen = ["Granada", "Madrid", "Almeria", "Barcelona", "Paris", "Londres", "Valencia", "Albacete", "Roma", "Milan", "Berlin"]

    def muestra_ciudades_origen(self):
        for i in corigen:
            print ("Ciudad" + corigen[i])

def main():
    a = ciudad_origen()
    a.muestra_ciudades_origen()

if __name__ == "__main__":
    main()
