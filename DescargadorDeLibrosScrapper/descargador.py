#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import urllib

categoria = input("Ingrese interes o categoria: ")




origen ="https://link.springer.com"

print('Descargando libros...')
print("=====================")

with open('direcciones.csv',encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for linea in csv_reader:
        
        nombreLibro = linea[1]
        if categoria.lower() in linea[3].lower() or categoria.lower() in linea[1].lower():
            print(f"...{linea[1]}, de {linea[2]}...")
            
            url = linea[4]
            
            link = urlopen(url)
            
            pagina = BeautifulSoup(link, 'html.parser')
            
            contenido = pagina.find('a', {"class": "c-button c-button--blue c-button__icon-right test-download-book-options test-bookpdf-link"})
            try:
                libro = contenido.get('href')
            except:
                try:
                    contenido = pagina.find('a', {"class": "c-button c-button--blue c-button__icon-right test-bookpdf-link"})
                    libro = contenido.get('href')
                except:
                    print("el libro {linea[1]}, no se puede descargar")
                
            linkDescarga = origen + libro
            
            descarga = '/Users/vince/Documents/LibrosMega/Libros/' + nombreLibro + ".pdf"
            urllib.request.urlretrieve(linkDescarga, descarga)
            print("       --Descargado...")
        else:
            print(".")
        
print("Libros descargados")
        