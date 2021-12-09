# Import packages
import pandas as pd
from typing import final
import requests
from bs4 import BeautifulSoup
import urllib # Una forma estandard de descargar datos
import os  # Para manejo de archivos y directorios
import glob
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


natalidad_2017 = pd.read_csv('./datos/sinac2017DatosAbiertos.csv',low_memory=False)
natalidad_2018 = pd.read_csv('./datos/sinac2018DatosAbiertos.csv',low_memory=False)
natalidad_2019 = pd.read_csv('./datos/sinac2019DatosAbiertos.csv',low_memory=False)

natalidad_2017_sonora=natalidad_2017[natalidad_2017['ENT_NAC']==26]
natalidad_2018_sonora=natalidad_2018[natalidad_2018['ENT_NAC']==26]
natalidad_2019_sonora=natalidad_2019[natalidad_2019['ENT_NAC']==26]

natalidad_2017_sonora=natalidad_2017_sonora.drop('Unnamed: 0',axis=1)
natalidad_2018_sonora=natalidad_2018_sonora.drop(labels='Unnamed: 0',axis=1)

natalidadtotal=natalidad_2017_sonora.append(natalidad_2018_sonora)
natalidadtotal=natalidadtotal.append(natalidad_2019_sonora)

natalidadtotal=natalidadtotal.loc[:,['ENT_NACM','MPO_NACM','FECH_NACM','EDADM','CON_INDM','HABLA_INDM','EDOCIVIL','ENT_RES','MPO_RES','LOC_RES','NUM_EMB','NUM_NACMTO','NUM_NACVIVO','HIJO_SOBV','HIJO_ANTE','VIVE_AUN','ORDEN_NAC','ATEN_PREN','TRIM_CONS','TOT_CONS','SOB_PARTO','DERHAB','NIV_ESCOL','OCUPHAB','TRAB_ACT','FECH_NACH','HORA_NACH','SEXOH','GESTACH','TALLAH','PESOH','APGARH','SILVERMAN','BCG','HEP_B','VIT_A','VIT_K','TAM_AUD','PRODUCTO','PROCNAC','FORCEPS','INST_NAC','CLUES','ATENDIO','ENT_NAC','MPO_NAC','LOC_NAC','CERT_POR','ENT_CERT','MPO_CERT','LOC_CERT','FECH_CERT']]

nuevas_columnas = {'ENT_NACM':'ENTIDADNACIMIENTO','MPO_NACM':'MUNICIPIONACIMIENTO','FECH_NACM':'FECHANACIMIENTOMADRE','EDADM':'EDAD','CON_INDM':'SECONSIDERAINDIGENA','HABLA_INDM':'HABLALENGUAINDIGENA','EDOCIVIL':'ESTADOCONYUGAL','ENT_RES':'ENTIDADRESIDENCIA','MPO_RES':'MUNICIPIORESIDENCIA','LOC_RES':'LOCALIDADRESIDENCIA','NUM_EMB':'NUMEROEMBARAZOS','NUM_NACMTO':'HIJOSNACIDOSMUERTOS','NUM_NACVIVO':'HIJOSNACIDOSVIVOS','HIJO_SOBV':'HIJOSSOBREVIVIENTES','HIJO_ANTE':'CONDICIONHIJOANTERIOR','VIVE_AUN':'VIVEHIJOANTERIOR','ORDEN_NAC':'ORDENNACIMIENTO','ATEN_PREN':'ATENCIONPRENATAL','TRIM_CONS':'TRIMESTREPRIMERCONSULTA','TOT_CONS':'TOTALCONSULTAS','SOB_PARTO':'SOBREVIVIOPARTO','DERHAB':'AFILIACION','NIV_ESCOL':'ESCOLARIDAD','OCUPHAB':'Ocupacion_Habitual','TRAB_ACT':'TRABAJAACTUALMENTE','FECH_NACH':'FECHANACIMIENTO','HORA_NACH':'HORANACIMIENTO','SEXOH':'SEXO','GESTACH':'EDADGESTACIONAL','TALLAH':'TALLA','PESOH':'PESO','APGARH':'APGAR','SILVERMAN':'SILVERMAN','BCG':'VACUNA_BCG','HEP_B':'VACUNAHEPATITIS_B','VIT_A':'VITAMINA_A','VIT_K':'VITAMINA_K','TAM_AUD':'TAMIZAUDITIVO','PRODUCTO':'PRODUCTOEMBARAZO','PROCNAC':'TIPOCESAREA','FORCEPS':'UTILIZOFORCEPS','INST_NAC':'LUGARNACIMIENTO','CLUES':'CLUES','ATENDIO':'PERSONALATENDIO','ENT_NAC':'ENTIDADFEDERATIVAPARTO','MPO_NAC':'MUNICIPIOPARTO','LOC_NAC':'LOCALIDADPARTO','CERT_POR':'CERTIFICADOPOR','ENT_CERT':'ENTIDADFEDERATIVACERTIFICA','MPO_CERT':'MUNICIPIOCERTIFICA','LOC_CERT':'LOCALIDADCERTIFICA','FECH_CERT':'FECHACERTIFICADO'}
natalidadtotal.rename(columns=nuevas_columnas,inplace=True)

natalidadtotal.columns
natalidadtotal.to_csv('./datos/Sonora2017_18_19.csv')


natalidad_2020 = pd.read_csv('./datos/sinac_2020.csv',low_memory=False)

natalidad_2020_sonora=natalidad_2020[natalidad_2020['ENTIDADFEDERATIVAPARTO']==26]
natalidad_2020_sonora=natalidad_2020_sonora.loc[:,['ENTIDADNACIMIENTO','MUNICIPIONACIMIENTO','FECHANACIMIENTOMADRE','EDAD','SECONSIDERAINDIGENA','HABLALENGUAINDIGENA','ESTADOCONYUGAL','ENTIDADRESIDENCIA','MUNICIPIORESIDENCIA','LOCALIDADRESIDENCIA','NUMEROEMBARAZOS','HIJOSNACIDOSMUERTOS','HIJOSNACIDOSVIVOS','HIJOSSOBREVIVIENTES','CONDICIONHIJOANTERIOR','VIVEHIJOANTERIOR','ORDENNACIMIENTO','ATENCIONPRENATAL','TRIMESTREPRIMERCONSULTA','TOTALCONSULTAS','SOBREVIVIOPARTO','AFILIACION','ESCOLARIDAD','TRABAJAACTUALMENTE','FECHANACIMIENTO','HORANACIMIENTO','SEXO','EDADGESTACIONAL','TALLA','PESO','APGAR','SILVERMAN','VACUNA_BCG','VACUNAHEPATITIS_B','VITAMINA_A','VITAMINA_K','TAMIZAUDITIVO','PRODUCTOEMBARAZO','TIPOCESAREA','UTILIZOFORCEPS','LUGARNACIMIENTO','CLUES','PERSONALATENDIO','ENTIDADFEDERATIVAPARTO','MUNICIPIOPARTO','LOCALIDADPARTO','CERTIFICADOPOR','ENTIDADFEDERATIVACERTIFICA','MUNICIPIOCERTIFICA','LOCALIDADCERTIFICA','FECHACERTIFICADO']]

natalidad_2020_sonora.to_csv('./datos/Sonora_2020.csv')


