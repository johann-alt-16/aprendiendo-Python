import math

factores_sagitales={
    "Rectangular": {"hombros": 0.9, "pecho": 0.9, "cintura": 0.9, "cadera": 0.9},
    "Reloj de arena / Triangulo invertido": {"hombros": 1.1, "pecho": 1.1, "cintura": 0.8, "cadera": 1.0},
    "Triangulo": {"hombros": 0.8, "pecho": 0.8, "cintura": 1.0, "cadera": 1.2},
    "Ovalado": {"hombros": 1.0, "pecho": 1.0, "cintura": 1.2, "cadera": 1.2}
}

def calcular_IMC(peso,altura):

 """
 Calcula el Índice de Masa Corporal (IMC) y determina un factor de relleno
 basado en el resultado.
 
 Args:
 peso (float): El peso del usuario en kilogramos.
 altura (float): La altura del usuario en metros.
 """
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
def calcular_medida_osea(opcion):
 """
 Determina un multiplicador basado en la estructura ósea del usuario
 (fina, media o robusta), evaluada por la opción de la muñeca.
 
 Args:
 opcion(str): La opción seleccionada por el usuario para la medida de la muñeca ("A", "B", "C").
 """
 diccionario_de_medidas={
      "A": 0.88, # Estructura pequeña
      "B": 1.00, # Estructura media
      "C": 1.12 # Estructura grande
    }
 multiplicador= diccionario_de_medidas.get(opcion.upper(), 1.00)
 return multiplicador

# PARTE TRANVERSAL (ANCHURA)
def calcular_plano_transversal_del_cuerpo(altura, constantes, sexo):
#Calcular las medidas transversales del cuerpo (hombros, cadera, cara, cintura, pecho) y las alturas de referencia (pecho, ojos, hombro, codo, cintura, muñeca, rodilla) a partir de la altura y el sexo del usuario.
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
 """
 Calcula las coordenadas en el eje X (derecha e izquierda) para hombros, pecho, cintura y cadera,
 asumiendo un centro en 0.
 
 Args:
 hombros_final (float): Medida final de los hombros.
 pecho_final (float): Medida final del pecho.
 cintura_final (float): Medida final de la cintura.
 cadera_final (float): Medida final de la cadera.
 """
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
 """
 Calcula los radios sagitales (profundidad) para hombros, pecho, cintura y cadera,
 aplicando factores específicos según el tipo de cuerpo.
 
 Args:
 radio_total_HOM (float): Radio transversal de los hombros.
 radio_PE (float): Radio transversal del pecho.
 radio_CIN (float): Radio transversal de la cintura.
 radio_CA (float): Radio transversal de la cadera.
 tipo_cuerpo (str): El tipo de cuerpo del usuario.
 """
 factores= factores_sagitales[tipo_cuerpo]
 z_radio_hom= radio_total_HOM*factores['hombros']
 z_radio_pe= radio_PE * factores["pecho"]
 z_radio_cin= radio_CIN* factores["cintura"]
 z_radio_ca=radio_CA*factores["cadera"]


 return z_radio_hom,z_radio_pe, z_radio_cin, z_radio_ca
def calcular_eje_sagial_Z(z_radio_hom,z_radio_pe, z_radio_cin, z_radio_ca):
 """
 Calcula las coordenadas en el eje Z (adelante y atrás) para hombros, pecho, cintura y cadera,
 asumiendo un centro en 0.
 
 Args:
 z_radio_hom (float): Radio sagital de los hombros.
 z_radio_pe (float): Radio sagital del pecho.
 z_radio_cin (float): Radio sagital de la cintura.
 z_radio_ca (float): Radio sagital de la cadera.
 """
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
 """
 Calcula el perímetro de las elipses que representan los contornos del cuerpo
 en hombros, pecho, cintura y cadera, utilizando la aproximación de Ramanujan.
 
 Args:
 radio_total_HOM (float): Radio transversal de los hombros.
 radio_total_PE (float): Radio transversal del pecho.
 radio_total_CIN (float): Radio transversal de la cintura.
 radio_total_CA (float): Radio transversal de la cadera.
 z_radio_hom (float): Radio sagital de los hombros.
 z_radio_pe (float): Radio sagital del pecho.
 z_radio_cin (float): Radio sagital de la cintura.
 z_radio_ca (float): Radio sagital de la cadera.
 """
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
"""PLAN B POR SI ES USUARIO DESCONOCE SU TIPO DE CUERPO"""
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


def estimar_tipo_cuerpo(peso,altura):
 IMC= peso / (altura**2)

 if IMC < 18.5:
   tipo_cuerpo= "Rectangular"

 elif 18.5<= IMC <25 :
   tipo_cuerpo= "Reloj de arena / Triangulo invertido"
   
 elif 25<= IMC <30:
    tipo_cuerpo= "Triangulo"

 else:
    tipo_cuerpo= "Ovalado"

 return tipo_cuerpo