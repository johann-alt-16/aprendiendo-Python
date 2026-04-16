import math
#Constante del cuerpo
constantes={ 
  #Constantes promedio en hombres
  "ancho_de_hombros_H": 0.230, 
  "ancho_de_cadera_H": 0.175,
  "ancho_cara_H": 0.088,
  "ancho_cintura_H": 0.155,
  "ancho_pecho_H": 0.195,
  "ancho_brazo_H": 0.058,      # Bíceps
  "ancho_antebrazo_H": 0.048,   # Parte más gruesa del antebrazo       
  "altura_pecho_H": 0.720,
  "altura_de_ojos_H": 0.936,
  "altura_del_hombro_H": 0.818,
  "altura_del_codo_H" : 0.630,
  "altura_de_cintura_H": 0.600,
  "altura_muñeca_H": 0.485,
  "altura_rodilla_H": 0.285,
  "longitud_brazo_H": 0.186,      # Hombro hasta el codo
  "longitud_muslo_H": 0.245,  # Codo hasta la muñeca
  "longitud_antebrazo_H": 0.145,  # Codo hasta la muñeca
  "ancho_muslo_H": 0.092,     # Circunferencia en la parte ancha
  
  #Constantes promedio en mujeres
  "ancho_de_hombros_M": 0.215,
  "ancho_de_cadera_M": 0.190,
  "ancho_cara_M": 0.085,
  "ancho_cintura_M": 0.140,
  "ancho_pecho_M": 0.185,
  "ancho_brazo_M": 0.054,      # Bíceps
  "ancho_antebrazo_M": 0.045,   # Parte más gruesa del antebrazo
  "altura_pecho_M": 0.705,
  "altura_de_ojos_M": 0.930,
  "altura_del_hombro_M": 0.810,
  "altura_del_codo_M" : 0.615,
  "altura_de_cintura_M": 0.585,
  "altura_muñeca_M": 0.475,
  "altura_rodilla_M": 0.273,
  "longitud_brazo_M": 0.182,      # Hombro hasta el codo
  "longitud_muslo_M": 0.240,  # Codo hasta la muñeca
  "longitud_antebrazo_M": 0.141,  # Codo hasta la muñeca
  "ancho_muslo_M": 0.105     # Suele ser mayor por distribución de tejido
  }

usuario_silueta={
  "Reloj de arena":{
    "hombros": 1.05, #Ligero enfasis
    "pecho": 1.02,#enfasis en busto
    "brazo": 1.00, 
    "antebrazo": 1.00, 
    "muslo": 1.05,
    "cintura": 0.85, #Cintura avispa
    "cadera": 1.05 #Curva suave
  },
  "Triangulo":{
    "hombros": 0.92, #Hombros estrechos
    "pecho": 0.95,#torso superior mas bajo que el inferior
    "brazo": 0.95, 
    "antebrazo": 0.95,
    "muslo": 1.15,
    "cintura": 1.05, #Cintura estandar (Cómun)
    "cadera": 1.15 #EL volumen mas notorio esta en esta zona
  },
  "Triangulo invertido":{
    "hombros": 1.12, #Hombros anchos
    "pecho": 1.08, #PEcho ancho y estetico
    "brazo": 1.10, 
    "antebrazo": 1.05,
    "muslo": 0.90,
    "cintura": 0.92, #CIntura que se reduce
    "cadera": 0.90 # Cadera muy estrecha
  },
  "Rectangulo":{
    "hombros": 1.00, #Todo alineado
    "pecho": 1.00, #Alineacion perfcta
    "brazo": 1.00,
    "antebrazo": 1.00,  
    "muslo": 1.00,
    "cintura": 1.00, #Poca definicion de cintura
    "cadera": 1.00 #Alineado con hombros
  },
  "Ovalado":{
    "hombros": 0.95, #Hombros redondeados
    "pecho": 1.05, #volumen redondeado
    "brazo": 1.05,
    "antebrazo": 1.00, 
    "muslo": 0.95,
    "cintura": 1.15, #Volumen maximo en la zona abdominal
    "cadera": 1.00 #Piernas suelen ser mas delgadas en proporcion a lo demas
  }
}

factores_sagitales={
  "Reloj de arena": {"hombro":0.80, "pecho":0.85,"brazo": 0.85, "antebrazo": 0.80, "muslo": 0.90, "cintura":0.70, "cadera": 0.95},
  "Triangulo":{"hombro":0.80,"pecho": 0.80,"brazo": 0.80, "antebrazo": 0.80, "muslo": 1.10 ,"cintura":0.75, "cadera": 1.05},
  "Triangulo invertido":{"hombro":0.85,"pecho":1.10,"brazo": 0.95, "antebrazo": 0.85, "muslo": 0.80, "cintura":0.70, "cadera": 0.80},
  "Rectangulo": {"hombro":0.80, "pecho":0.85,"brazo": 0.85, "antebrazo": 0.80, "muslo": 0.85, "cintura":0.80, "cadera":0.85},
  "Ovalado":{"hombro":0.80,"pecho":0.95,"brazo": 0.90, "antebrazo": 0.85, "muslo": 0.95, "cintura":1.20, "cadera": 0.90}
}

import math

# ==========================================================
# MAISON BRUNETTE - MOTOR LÓGICO BIOMÉTRICO (VERSIÓN FINAL)
# ==========================================================


#PLAN B PARA CALCULAR LA SILUETA BASADA EN IMC peso y altura
def ejecutar_plan_b_maestro(altura, peso, tipo_cuerpo=None):
    """
    Este es el Comandante. Decide el tipo de cuerpo usando nombres claros.
    """
    
    # 1. CREAMOS EL MANIQUÍ INVISIBLE (Para comparar)
    # Convertimos la altura a centímetros para que sea más fácil
    altura_en_cm = altura * 100
    
    # Calculamos anchos teóricos (lo que debería medir alguien estándar)
    ancho_hombros_base = altura_en_cm * 0.11
    ancho_cadera_base = ancho_hombros_base * 0.95
    
    # Ajustamos según el peso (IMC)
    indice_masa_corporal = peso / (altura** 2)
    multiplicador_de_masa = indice_masa_corporal / 22
    
    # Estos son los centímetros que la app 'imagina'
    hombros_imaginados = ancho_hombros_base * multiplicador_de_masa
    cadera_imaginada = ancho_cadera_base * multiplicador_de_masa
    cintura_imaginada = hombros_imaginados * 0.75
    
    # 2. DECIDIMOS EL TIPO DE CUERPO (La Etiqueta)
    if tipo_cuerpo and tipo_cuerpo != "desconocido":
        # Si el usuario seleccionó un tipo de cuerpo, lo usamos
        tipo_cuerpo = tipo_cuerpo
    else:
        # Si no hay foto, comparamos los hombros con la cadera
        relacion_hombro_cadera = hombros_imaginados / cadera_imaginada
        
        if relacion_hombro_cadera > 1.05:
            tipo_cuerpo = "Triangulo_invertido"
        elif relacion_hombro_cadera < 0.95:
            tipo_cuerpo = "Triangulo"
        else:
            tipo_cuerpo = "Rectangulo"
            
    # Devolvemos la etiqueta y los radios con nombres fáciles
    return tipo_cuerpo, hombros_imaginados, cintura_imaginada, cadera_imaginada

# 1. CÁLCULO DE IMC Y FACTOR DE RELLENO
def calcular_imc_y_factor_relleno(peso, altura):
    imc = peso / (altura**2)
    if imc < 18.5:
        factor_relleno = 1.05
    elif 18.5 <= imc < 25:
        factor_relleno = 1.15
    elif 25 <= imc < 30:
        factor_relleno = 1.25
    else:
        factor_relleno = 1.35
    return imc, factor_relleno

# 2. DETERMINAR ESTRUCTURA ÓSEA
def obtener_multiplicador_oseo(opcion_muneca):
    medidas = {"A": 0.88, "B": 1.00, "C": 1.12}
    return medidas.get(opcion_muneca.upper(), 1.00)

# 3. PLANO TRANSVERSAL BASE Y EXTREMIDADES
def calcular_proporciones_base(altura, constantes, sexo):
    s = "_M" if sexo == "Femenino" else "_H"
    
    # Coincidiendo con tus llaves del diccionario 'constantes'
    ancho_hombros = altura * constantes[f'ancho_de_hombros{s}']
    ancho_cadera = altura * constantes[f'ancho_de_cadera{s}']
    ancho_cara = altura * constantes[f'ancho_cara{s}']
    ancho_cintura = altura * constantes[f'ancho_cintura{s}']
    ancho_pecho = altura * constantes[f'ancho_pecho{s}']
    ancho_brazo = altura * constantes[f'ancho_brazo{s}']
    ancho_antebrazo = altura * constantes[f'ancho_antebrazo{s}']
    ancho_muslo = altura * constantes[f'ancho_muslo{s}']
    
    # Alturas de referencia
    altura_pecho = altura * constantes[f'altura_pecho{s}']
    altura_ojos = altura * constantes[f'altura_de_ojos{s}']
    altura_hombro = altura * constantes[f'altura_del_hombro{s}']
    altura_codo = altura * constantes[f'altura_del_codo{s}']
    altura_cintura = altura * constantes[f'altura_de_cintura{s}']
    altura_muñeca = altura * constantes[f'altura_muñeca{s}']
    altura_rodilla = altura * constantes[f'altura_rodilla{s}']
    
    # Medidas de extremidades 
    longitud_brazo = altura * constantes[f'longitud_brazo{s}']
    longitud_antebrazo = altura * constantes[f'longitud_antebrazo{s}']
    ancho_muslo = altura * constantes[f'ancho_muslo{s}']

    return (ancho_hombros, ancho_cadera, ancho_cara, ancho_cintura, ancho_pecho), \
           (altura_pecho, altura_ojos, altura_hombro, altura_codo, altura_cintura, altura_muñeca, altura_rodilla), \
           (longitud_brazo, longitud_antebrazo, ancho_muslo), (ancho_brazo, ancho_antebrazo)
# 4. PLANO TRANSVERSAL FINAL (AJUSTE SEGÚN 'usuario_silueta')
def calcular_transversal_final(altura, constantes, sexo, mult_oseo, factor_relleno, usuario_silueta, tipo_cuerpo):
    s = "_M" if sexo == "Femenino" else "_H"
    # Accedemos al diccionario 'usuario_silueta' que nos pasaste
    ajuste = usuario_silueta[tipo_cuerpo]
    
    hombros_f = (altura * constantes[f'ancho_de_hombros{s}']) * mult_oseo * factor_relleno * ajuste['hombros']
    pecho_f = (altura * constantes[f'ancho_pecho{s}']) * mult_oseo * factor_relleno * ajuste['pecho']
    brazo_f = (altura * constantes[f'ancho_brazo{s}']) * mult_oseo * factor_relleno * ajuste['brazo']
    antebrazo_f = (altura * constantes[f'ancho_antebrazo{s}']) * mult_oseo * factor_relleno * ajuste['antebrazo']
    muslo_f = (altura * constantes[f'ancho_muslo{s}']) * mult_oseo * factor_relleno * ajuste['muslo']
    cintura_f = (altura * constantes[f'ancho_cintura{s}']) * mult_oseo * factor_relleno * ajuste['cintura']
    cadera_f = (altura * constantes[f'ancho_de_cadera{s}']) * mult_oseo * factor_relleno * ajuste['cadera']
    
    return hombros_f, pecho_f,brazo_f, antebrazo_f, muslo_f,cintura_f, cadera_f

# 5. EJE TRANSVERSAL X
def calcular_eje_x(hombros_f, pecho_f, brazo_f, antebrazo_f, muslo_f,cintura_f, cadera_f):
    def obtener_puntos(medida):
        radio = medida / 2
        return {"radio": radio, "derecha": radio, "izquierda": -radio}
    return obtener_puntos(hombros_f), obtener_puntos(pecho_f), obtener_puntos(brazo_f), obtener_puntos(antebrazo_f), obtener_puntos(muslo_f), obtener_puntos(cintura_f), obtener_puntos(cadera_f)

# 6. PLANO Y EJE SAGITAL (AJUSTE SEGÚN 'factores_sagitales')
def calcular_profundidad_sagital(radio_h, radio_p, radio_mus,radio_bra, radio_ante, radio_ci, radio_ca, tipo_cuerpo, factores_sagitales):
    # Accedemos a tu diccionario 'factores_sagitales'
    f = factores_sagitales[tipo_cuerpo]
    # OJO: En tu diccionario usaste 'hombro' (singular) aquí lo corregimos para que coincida:
    z_hombros = radio_h * f['hombro'] 
    z_pecho = radio_p * f['pecho']
    z_brazo = radio_bra * f['brazo']
    z_antebrazo = radio_ante * f['antebrazo']
    z_muslo = radio_mus * f['muslo']
    z_cintura = radio_ci * f['cintura']
    z_cadera = radio_ca * f['cadera']
    return z_hombros, z_pecho, z_brazo, z_antebrazo, z_muslo, z_cintura, z_cadera

# 7. ELIPSE DE CONTORNO (RAMANUJAN)
def calcular_contornos_elipse(radio_h, radio_p,radio_mus,radio_ante,radio_bra ,radio_ci, radio_ca,z_cintura, z_hombros, z_pecho, z_brazo, z_antebrazo, z_muslo, z_cadera):
    def formula_ramanujan(a, b):
        h = ((a - b)**2) / ((a + b)**2)
        return math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
    
    perimetro_hombros= formula_ramanujan(radio_h, z_hombros)
    perimetro_pecho= formula_ramanujan(radio_p, z_pecho)
    perimetro_brazo= formula_ramanujan(radio_bra, z_brazo)
    perimetro_antebrazo= formula_ramanujan(radio_ante, z_antebrazo)
    perimetro_muslo= formula_ramanujan(radio_mus, z_muslo)
    perimetro_cintura= formula_ramanujan(radio_ci, z_cintura)
    perimetro_cadera= formula_ramanujan(radio_ca, z_cadera)
    return perimetro_hombros, perimetro_pecho, perimetro_brazo, perimetro_antebrazo, perimetro_muslo, perimetro_cintura, perimetro_cadera
# 8. CÁLCULO DE ICC e IMCO (OPCIONAL)
def calcular_icc(cintura_f, cadera_f):
    return round(cintura_f / cadera_f, 2)

# 9. PROPORCIÓN DE TERCIOS
def Regla_de_tercios(altura, altura_hombros, altura_cadera):
    """
    Calcula la proporción 30/70 ajustada a la anatomía real del usuario.
    """
    # 1. CONVERSIÓN Y DATOS BASE
    altura_cm = altura * 100
    
    # Buscamos el centro real entre donde terminan sus hombros y empieza su cadera
    punto_equilibrio_seo = (altura_hombros + altura_cadera) / 2
    
    # 2. DEFINICIÓN DEL OBJETIVO ESTÉTICO (El "Deber Ser")
    if altura <= 1.77:
        porcentaje_objetivo = 0.30  # Queremos que el torso se vea del 30%
    else:
        porcentaje_objetivo = 0.33  # Queremos equilibrio del 33%

    # 3. EL CÁLCULO MAESTRO (Uso de los parámetros)
    # Calculamos cuánto mide el torso visual ideal
    camisa_cm = altura_cm * porcentaje_objetivo
    
    # Calculamos la diferencia entre su cuerpo real y el objetivo estético
    # (Esto servirá para que tu módulo de instrucciones diga cuánto subir el pantalón)
    desvio_anatomico = punto_equilibrio_seo - (altura_cm - camisa_cm)

    # 4. RESULTADOS FINALES
    pantalon_cm = altura_cm - camisa_cm
    
    # --- SALIDA TÉCNICA A TERMINAL ---
    print(f"\n--- INGENIERÍA DE PROPORCIONES BRUNETTE ---")
    print(f"Altura Real: {altura_cm} cm")
    print(f"Punto de Equilibrio Óseo: {round(punto_equilibrio_seo, 2)} cm")
    print(f"Objetivo Camisa ({porcentaje_objetivo*100}%): {round(camisa_cm, 2)} cm")
    print(f"Objetivo Pantalón ({round((1-porcentaje_objetivo)*100)}%): {round(pantalon_cm, 2)} cm")
    print(f"Ajuste Necesario: {round(desvio_anatomico, 2)} cm")
    print(f"------------------------------------------\n")

    return round(camisa_cm, 2)

Regla_de_tercios(1.88, 161.0, 105.0)

