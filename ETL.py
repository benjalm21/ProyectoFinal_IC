# Import packages
from typing import final
import requests
from bs4 import BeautifulSoup
import urllib # Una forma estandard de descargar datos
import os  # Para manejo de archivos y directorios
# Specify url
url = 'http://www.dgis.salud.gob.mx/contenidos/basesdedatos/da_nacimientos_gobmx.html'

baseURL='http://www.dgis.salud.gob.mx/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc, features="html5lib")

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags=soup.find_all('a')
finalUrl=[]
# Print the URLs to the shell
for link in a_tags:
    finalUrl.append(str(link.get('href')))

Links=''
xD=''
LinksFinales=[]
for x in finalUrl:
    Links=str(x).replace('../../',baseURL)
    if Links.__contains__("sinac_2"):
        xD=Links
        LinksFinales.append(xD)

nacimientos_archivo = "../Datos/"
    
      
for item in LinksFinales:
    nacimiento_archivo=str(item).split(sep='/')
    filename=nacimiento_archivo[len(nacimiento_archivo)-1]
    filename=filename[0 :len(filename)-6]
    if not os.path.exists("./datos/"+filename):
        dl,site=urllib.request.urlretrieve(item,'./datos/'+filename)




    