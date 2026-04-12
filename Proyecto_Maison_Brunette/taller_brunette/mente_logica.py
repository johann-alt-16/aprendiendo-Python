#Constante del cuerpo
constantes={ 
  #Constantes promedio en hombres
  "ancho_de_hombros_H": 0.228, 
  "ancho_cara_H": 0.088,
  "ancho_de_cadera_H": 0.191,
  "altura_de_ojos_H": 0.936,
  "altura_del_hombro_H": 0.818,
  "altura_del_codo_H" : 0.630,
  "altura_de_cintura_H": 0.600,
  "altura_muñeca_H": 0.485,
  "altura_rodilla_H": 0.285,
  
  #Constantes promedio en mujeres
  "ancho_de_hombros_M": 0.210,
  "ancho_cara_M": 0.085,
  "ancho_de_cadera_M": 0.215,
  "altura_de_ojos_M": 0.930,
  "altura_del_hombro_M": 0.810,
  "altura_del_codo_M" : 0.615,
  "altura_de_cintura_M": 0.585,
  "altura_muñeca_M": 0.475,
  "altura_rodilla_M": 0.273,
  }
def calcular_imc_y_estilo(peso,altura):

 imc= peso / (altura**2)//1

 if imc < 18.5:
   recomendacion_fit = "Slim fit"
   categoria= "Delgada"
   
 elif 18.5<= imc <25 :
   recomendacion_fit= "Regular fit"
   categoria= "Atletica"
   

 elif 25<= imc <30:
   recomendacion_fit="Relaxed fit"
   categoria="Robusta"
   

 else:
   recomendacion_fit= "Structure fit"
   categoria= "Grande"
   

 return round(imc , 2), recomendacion_fit, categoria
def calcular_medida_osea(opcion, altura):
   diccionario_de_medidas={
      "A": 0.22, # Estructura pequeña
      "B": 0.25, # Estructura media
      "C": 0.28  # Estructura grande
    }
   multiplicador= diccionario_de_medidas.get(opcion.upper(), 0.25)
   resultado= altura * multiplicador
   return round(resultado, 2)
def calcular_proporcion_prenda(altura, estilo_elegido):
  """ calcula el largo ideal de la prenda en centimetros"""
  reglas_estilo={
    "1": 0.38, 
    "2": 0.40,
    "3": 0.42,
    "4": 0.45
  }

  porcentaje= reglas_estilo.get(estilo_elegido, 0.40)
  largo_cm= (altura *100) * porcentaje
  
  return round(largo_cm, 1)
def calcular_anchura_del_cuerpo(altura, constantes, sexo):
  if sexo== "Masculino":
    ancho_de_hombros= altura * constantes['ancho_de_hombros_H']
    ancho_de_cadera= altura * constantes['ancho_de_cadera_H']
    ancho_cara= altura * constantes['ancho_cara_H']
    altura_de_ojos= altura * constantes['altura_de_ojos_H']
    altura_del_hombro= altura * constantes['altura_del_hombro_H']
    altura_del_codo= altura* constantes['altura_del_codo_H']
    altura_de_cintura= altura* constantes['altura_de_cintura_H']
    altura_muñeca= altura * constantes['altura_muñeca_H']
    altura_rodilla= altura* constantes['altura_rodilla_H']
  elif sexo== "Femenino": 
    ancho_de_hombros= altura * constantes['ancho_de_hombros_M']
    ancho_de_cadera= altura * constantes['ancho_de_cadera_M']
    ancho_cara= altura * constantes['ancho_cara_M']
    altura_de_ojos= altura * constantes['altura_de_ojos_M']
    altura_del_hombro= altura * constantes['altura_del_hombro_M']
    altura_del_codo= altura* constantes['altura_del_codo_M']
    altura_de_cintura= altura* constantes['altura_de_cintura_M']
    altura_muñeca= altura * constantes['altura_muñeca_M']
    altura_rodilla= altura* constantes['altura_rodilla_M']
