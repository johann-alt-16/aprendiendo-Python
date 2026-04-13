import math
#Constante del cuerpo
constantes={ 
  #Constantes promedio en hombres
  "ancho_de_hombros_H": 0.230, 
  "ancho_de_cadera_H": 0.175,
  "ancho_cara_H": 0.088,
  "ancho_cintura_H": 0.155,
  "ancho_pecho_H": 0.195,
  "altura_pecho_H": 0.720,
  "altura_de_ojos_H": 0.936,
  "altura_del_hombro_H": 0.818,
  "altura_del_codo_H" : 0.630,
  "altura_de_cintura_H": 0.600,
  "altura_muñeca_H": 0.485,
  "altura_rodilla_H": 0.285,
  
  #Constantes promedio en mujeres
  "ancho_de_hombros_M": 0.215,
  "ancho_de_cadera_M": 0.190,
  "ancho_cara_M": 0.085,
  "ancho_cintura_M": 0.140,
  "ancho_pecho_M": 0.185,
  "altura_pecho_M": 0.705,
  "altura_de_ojos_M": 0.930,
  "altura_del_hombro_M": 0.810,
  "altura_del_codo_M" : 0.615,
  "altura_de_cintura_M": 0.585,
  "altura_muñeca_M": 0.475,
  "altura_rodilla_M": 0.273,
  }

usuario_silueta={
  "Reloj de arena":{
    "hombros": 1.05, #Ligero enfasis
    "pecho": 1.02,#enfasis en busto
    "cintura": 0.85, #Cintura avispa
    "cadera": 1.05 #Curva suave
  },
  "Triangulo":{
    "hombros": 0.92, #Hombros estrechos
    "pecho": 0.95,#torso superior mas bajo que el inferior
    "cintura": 1.05, #Cintura estandar (Cómun)
    "cadera": 1.15 #EL volumen mas notorio esta en esta zona
  },
  "Triangulo invertido":{
    "hombros": 1.12, #Hombros anchos
    "pecho": 1.08, #PEcho ancho y estetico
    "cintura": 0.92, #CIntura que se reduce
    "cadera": 0.90 # Cadera muy estrecha
  },
  "Rectangulo":{
    "hombros": 1.00, #Todo alineado
    "pecho": 1.00, #Alineacion perfcta
    "cintura": 1.00, #Poca definicion de cintura
    "cadera": 1.00 #Alineado con hombros
  },
  "Ovalado":{
    "hombros": 0.95, #Hombros redondeados
    "pecho": 1.05, #volumen redondeado
    "cintura": 1.15, #Volumen maximo en la zona abdominal
    "cadera": 1.00 #Piernas suelen ser mas delgadas en proporcion a lo demas
  }
}

factores_sagitales={
  "Reloj de arena": {"hombro":0.80, "pecho":0.85, "cintura":0.70, "cadera": 0.95},
  "Triangulo":{"hombro":0.80,"pecho": 0.80, "cintura":0.75, "cadera": 1.05},
  "Triangulo invertido":{"hombro":0.85,"pecho":1.10, "cintura":0.70, "cadera": 0.80},
  "Rectangulo": {"hombro":0.80, "pecho":0.85, "cintura":0.80, "cadera":0.85},
  "Ovalado":{"hombro":0.80,"pecho":0.95, "cintura":1.20, "cadera": 0.90}
}
def calcular_imc_y_estilo(peso,altura):

 imc= peso / (altura**2)

 if imc < 18.5:
   factor_relleno= 1.05

 elif 18.5<= imc <25 :
   factor_relleno= 1.15
   
 elif 25<= imc <30:
   factor_relleno= 1.25

 else:
   factor_relleno= 1.35

 return factor_relleno
"""SIrve para encontar tu tipo de somatipo"""
def calcular_medida_osea(opcion):
   diccionario_de_medidas={
      "A": 0.88, # Estructura pequeña
      "B": 1.00, # Estructura media
      "C": 1.12 # Estructura grande
    }
   multiplicador= diccionario_de_medidas.get(opcion.upper(), 1.00)
   return multiplicador
# PARTE TRANVERSAL (ANCHURA)
def calcular_plano_transversal_del_cuerpo(altura, constantes, sexo):

  if sexo== "Masculino":
    ancho_de_hombros= altura * constantes['ancho_de_hombros_H']
    ancho_de_cadera= altura * constantes['ancho_de_cadera_H']
    ancho_cara= altura * constantes['ancho_cara_H']
    ancho_cintura= altura* constantes['ancho_cintura_H']
    ancho_pecho= altura* constantes['ancho_pecho_H']
    altura_pecho= altura* constantes['altura_pecho_H']
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
    ancho_pecho= altura*constantes['ancho_pecho_M']
    altura_pecho=altura*constantes['altura_pecho_M']
    altura_de_ojos= altura * constantes['altura_de_ojos_M']
    altura_del_hombro= altura * constantes['altura_del_hombro_M']
    altura_del_codo= altura* constantes['altura_del_codo_M']
    altura_de_cintura= altura* constantes['altura_de_cintura_M']
    altura_muñeca= altura * constantes['altura_muñeca_M']
    altura_rodilla= altura* constantes['altura_rodilla_M']
  return ancho_de_hombros, ancho_de_cadera, ancho_cara, ancho_cintura,ancho_pecho,altura_pecho, altura_de_ojos, altura_del_hombro, altura_del_codo, altura_de_cintura, altura_muñeca, altura_rodilla
def calcular_plano_transversal(altura, constantes,sexo,opcion_muneca, factor_relleno, usuario_silueta, tipo_cuerpo):
  ajuste= usuario_silueta[tipo_cuerpo]
  s="_M" if sexo == "Femenino"  else "_H"

  #Hombros
  hombros_final= (altura*constantes['ancho_de_hombros'+s])*opcion_muneca* factor_relleno *ajuste['hombros']
  print(hombros_final*100 )
  pecho_final= (altura*constantes['ancho_pecho'+s])*opcion_muneca*factor_relleno*ajuste['pecho']
  print(pecho_final*100)
  cintura_final= (altura*constantes['ancho_cintura'+s])*opcion_muneca* factor_relleno *ajuste['cintura']
  print(cintura_final*100 )
  cadera_final = (altura*constantes['ancho_de_cadera'+s])*opcion_muneca* factor_relleno *ajuste['cadera']
  print(cadera_final*100 )

 

  return hombros_final, cintura_final, cadera_final
def eje_tranversal_X(hombros_final,pecho_final, cintura_final, cadera_final):
 centro=0
 radio_total_HOM= hombros_final/ 2
  #EJE (X) POSITIVO(+)
 derecha_hom= radio_total_HOM+ centro
 #EJE NEGATIVO(-)
 izquierda_hom=centro -radio_total_HOM

 radio_total_PE= pecho_final/2
 derecha_pe= radio_total_PE +centro
 izquierda_pe=centro- radio_total_PE

 radio_total_CIN=cintura_final /2
 derecha_cin= radio_total_CIN+centro
 izquierda_cin= centro- radio_total_CIN

 radio_total_CA= cadera_final/2
 derecha_ca=radio_total_CA+centro
 izquierda_ca= centro-radio_total_CA

 return (radio_total_HOM, derecha_hom, izquierda_hom), (radio_total_PE, derecha_pe, izquierda_pe), (radio_total_CIN, derecha_cin, izquierda_cin), (radio_total_CA, derecha_ca, izquierda_ca)

#PARTE SAGITAL(GROSOR)
def calcular_plano_sagital(radio_total_HOM, radio_PE, radio_CIN, radio_CA, tipo_cuerpo):
  factores= factores_sagitales[tipo_cuerpo]
  z_radio_hom= radio_total_HOM*factores['hombros']
  z_radio_pe= radio_PE * factores["pecho"]
  z_radio_cin= radio_CIN* factores["cintura"]
  z_radio_ca=radio_CA*factores["cadera"]


  return z_radio_hom,z_radio_pe, z_radio_cin, z_radio_ca
def calcular_eje_sagial_Z(z_radio_hom,z_radio_pe, z_radio_cin, z_radio_ca):
  centro_Z=0
#PARA HOMBROS
  adelante_hom= centro_Z + z_radio_hom
  atras_hom= centro_Z- z_radio_hom
#PARA PECHO
  adelante_pe= centro_Z + z_radio_pe
  atras_pe= centro_Z-z_radio_pe
#PARA CINTURA
  adelante_cin= centro_Z+z_radio_cin
  atras_cin= centro_Z-z_radio_cin
#PARA CADERA
  adelante_ca= centro_Z+z_radio_ca
  atras_ca= centro_Z- z_radio_ca
  return (adelante_hom, atras_hom),(adelante_pe,atras_pe), (adelante_cin,atras_cin), (adelante_ca, atras_ca)
def calcular_elipse_contorno(radio_total_HOM, radio_total_PE, radio_total_CIN, radio_total_CA,z_radio_hom, z_radio_pe, z_radio_cin, z_radio_ca):
  def ramanujan(a,b):
    h= ((a-b)**2)/ ((a+b)**2)
    perimetro= math.pi *(a+b)*(1+(3*h)/ (10 + math.sqrt(4-3 * h)))
    return perimetro
  perimetro_hombro= ramanujan(radio_total_HOM, z_radio_hom)
  print(perimetro_hombro)
  perimetro_pecho= ramanujan(radio_total_PE, z_radio_pe)
  print(perimetro_pecho)
  perimetro_cintura= ramanujan(radio_total_CIN, z_radio_cin)
  print(perimetro_cintura)
  perimetro_cadera=ramanujan(radio_total_CA, z_radio_ca)
  print(perimetro_cadera)
  return perimetro_hombro, perimetro_pecho, perimetro_cintura, perimetro_cadera

def calculo_ICC(cintura_final, cadera_final):
 ICC = cintura_final/cadera_final
 print(ICC)


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
calculo_ICC(66.20313847205836,126.21852031406245 )

