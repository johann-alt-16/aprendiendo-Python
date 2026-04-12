#Constante del cuerpo
constantes={ 
  #Constantes promedio en hombres
  "ancho_de_hombros_H": 0.228, 
  "ancho_cara_H": 0.088,
  "ancho_de_cadera_H": 0.191,
  "ancho_cintura_H": 0.145,
  "altura_de_ojos_H": 0.936,
  "altura_del_hombro_H": 0.818,
  "altura_del_codo_H" : 0.630,
  "altura_de_cintura_H": 0.600,
  "altura_muñeca_H": 0.485,
  "altura_rodilla_H": 0.285,
  
  #Constantes promedio en mujeres
  "ancho_de_hombros_M": 0.210,
  "ancho_cara_M": 0.085,
  "ancho_cintura_M": 0.138,
  "ancho_de_cadera_M": 0.215,
  "altura_de_ojos_M": 0.930,
  "altura_del_hombro_M": 0.810,
  "altura_del_codo_M" : 0.615,
  "altura_de_cintura_M": 0.585,
  "altura_muñeca_M": 0.475,
  "altura_rodilla_M": 0.273,
  }

usuario_silueta={
  "Reloj de arena":{
    "hombros": 1.25, #Ligero enfasis
    "cintura": 0.85, #Cintura avispa
    "cadera": 1.25 #Curva suave
  },
  "Triangulo":{
    "hombros": 0.90, #Hombros estrechos
    "cintura": 1.10, #Cintura estandar (Cómun)
    "cadera": 1.45 #EL volumen mas notorio esta en esta zona
  },
  "Triangulo invertido":{
    "hombros": 1.45, #Hombros anchos
    "cintura": 0.95, #CIntura que se reduce
    "cadera": 0.90 # Cadera muy estrecha
  },
  "Rectangulo":{
    "hombros": 1.15, #Todo alineado
    "cintura": 1.12, #Poca definicion de cintura
    "cadera": 1.15 #Alineado con hombros
  },
  "Ovalado":{
    "hombros": 0.82, #Hombros redondeados
    "cintura": 1.45, #Volumen maximo en la zona abdominal
    "cadera": 1.20 #Piernas suelen ser mas delgadas en proporcion a lo demas
  }
}
def calcular_imc_y_estilo(peso,altura):

 imc= peso / (altura**2)

 if imc < 18.5:
   factor_relleno= 1.10

 elif 18.5<= imc <25 :
   factor_relleno= 1.20
   
 elif 25<= imc <30:
   factor_relleno= 1.32

 else:
   factor_relleno= 1.45

 return factor_relleno

def calcular_medida_osea(opcion, altura):
   diccionario_de_medidas={
      "A": 0.92, # Estructura pequeña
      "B": 1.00, # Estructura media
      "C": 1.08 # Estructura grande
    }
   multiplicador= diccionario_de_medidas.get(opcion.upper(), 1.00)
   return multiplicador


def calcular_anchura_del_cuerpo(altura, constantes, sexo):

  if sexo== "Masculino":
    ancho_de_hombros= altura * constantes['ancho_de_hombros_H']
    ancho_de_cadera= altura * constantes['ancho_de_cadera_H']
    ancho_cara= altura * constantes['ancho_cara_H']
    ancho_cintura= altura* constantes['ancho_cintura_H']
    altura_de_ojos= altura * constantes['altura_de_ojos_H']
    altura_del_hombro= altura * constantes['altura_del_hombro_H']
    altura_del_codo= altura* constantes['altura_del_codo_H']
    altura_de_cintura= altura* constantes['altura_de_cintura_H']
    altura_muñeca= altura * constantes['altura_muñeca_H']
    altura_rodilla= altura* constantes['altura_rodilla_H']
  elif sexo== "Femenino": 
    ancho_de_hombros= altura * constantes['ancho_de_hombros_M']
    ancho_de_cadera= altura * constantes['ancho_de_cadera_M']
    print(ancho_de_cadera)
    ancho_cara= altura * constantes['ancho_cara_M']
    ancho_cintura= altura * constantes['ancho_cintura_M']
    print(ancho_cintura)
    altura_de_ojos= altura * constantes['altura_de_ojos_M']
    altura_del_hombro= altura * constantes['altura_del_hombro_M']
    altura_del_codo= altura* constantes['altura_del_codo_M']
    altura_de_cintura= altura* constantes['altura_de_cintura_M']
    altura_muñeca= altura * constantes['altura_muñeca_M']
    altura_rodilla= altura* constantes['altura_rodilla_M']
  return ancho_de_hombros, ancho_de_cadera, ancho_cara, ancho_cintura, altura_de_ojos, altura_del_hombro, altura_del_codo, altura_de_cintura, altura_muñeca, altura_rodilla

def calcular_anchura_final(altura, constantes,sexo,opcion_muneca, factor_relleno, usuario_silueta, tipo_cuerpo):
  ajuste= usuario_silueta[tipo_cuerpo]

  s="_M" if sexo == "Femenino"  else "_H"

  #Hombros
  hombros_final= (altura*constantes['ancho_de_hombros'+s])*opcion_muneca* factor_relleno *ajuste['hombros']
  print(hombros_final*100 )
  cintura_final= (altura*constantes['ancho_cintura'+s])*opcion_muneca* factor_relleno *ajuste['cintura']
  print(cintura_final*100 )
  cadera_final = (altura*constantes['ancho_de_cadera'+s])*opcion_muneca* factor_relleno *ajuste['cadera']
  print(cadera_final*100 )
  return hombros_final, cintura_final, cadera_final

def calculo_ICC(cintura_final, cadera_final):
 ICC = cintura_final/cadera_final
 print(ICC *100)

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
calcular_medida_osea("A", 1.80)

calcular_anchura_final(1.80, constantes, "Femenino",1.02, 1.10, usuario_silueta, "triangulo")