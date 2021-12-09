import pandas as pd
def formatearCSV2015_2016 ():
        files=['sinac_2015.zip','sinac_2016.zip']
        df=pd.DataFrame
        for file in files:
            df.append(pd.read_csv(file))
            df.loc(['edo_nac_madre','mpo_nac_madre','fecha_nac_madre','edad_madre','madre_se_considera_indigena','madre_habla_lengua_indigena','estado_conyugal','entidad_residencia_madre','municipio_residencia_madre','localidad_residencia_madre','numero_embarazos','hijos_nacidos_muertos','hijos_nacidos_vivos','hijos_sobrevivientes','el_hijo_anterior_nacio','vive_aun_hijo_anterior','orden_nacimiento','recibio_atencion_prenatal','trimestre_recibio_primera_consulta','total_consultas_recibidas','madre_sobrevivio_al_parto','afiliacion_serv_salud','escolaridad_madre','ocupacion_habitual_madre','trabaja_actualmente','fecha_nacimiento_nac_vivo','hora_nacimiento_nac_vivo','sexo_nac_vivo','semanas_gestacion_nac_vivo','talla_nac_vivo','peso_nac_vivo','valoracion_apgar_nac_vivo','valoracion_silverman_nac_vivo','recibio_vacuna_bcg','recibio_vacuna_hep_b','recibio_vit_a','recibio_vit_k','se_realizo_tamiz_auditivo','producto_de_un_embarazo','procedimiento_utilizado','se_utilizaron_forceps','lugar_de_nacimiento','clues','quien_atendio_parto','entidad_nacimiento','municipio_nacimiento','localidad_nacimiento','certificado_por','entidad_certifico','municipio_certifico','localidad_certifico','fecha_certificacion'])
            df.to_csv(file)
         

formatearCSV2015_2016()