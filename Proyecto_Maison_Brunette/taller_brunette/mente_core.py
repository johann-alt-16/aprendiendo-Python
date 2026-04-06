
#Se crea diccionario con el valor de luz que reflejan los colores
VALOR_DE_BRILLO= {
    "negro": 0,
    "petroleo": 1.5,
    "marino":2,
    "cafe":2,
    "vino": 2,
    "oliva": 3,
    "gris":5,
    "azul":6,
    "verde":6,
    "beige": 6,
    "mostaza": 6,
    "cian": 7,
    "rojo": 7,
    "naranja":8,
    "lila": 8,
    "arena": 8,
    "rosa_pastel": 8,
    "amarillo":9,
    "plata": 9.5,
    "blanco": 10
    }
#Se crea una maquina con las intrucciones para la mezcla de colores.
def resultado_de_mezcla(color1, color2):

    recetario_de_colores ={
        ("azul" , "amarillo"): "verde",
        ("rojo", "azul"): "morado",
        ("rojo", "amarillo"): "naranja",
        ("blanco", "negro"): "gris",
        ("blanco", "rojo"): "rosado"
    }
#Es util para detectar que "azul , amarillo" es igual a "amarillo , azul"
    resultado= recetario_de_colores.get(color1 , color2) or recetario_de_colores.get((color2 , color1))

#Solo comprimi el if/else para no ocupar mas espacio, no cambia absolutamente nada.
    return resultado  if resultado else "combinacion libre"

#Se crea una maquina con la finalidad de verificar el nivel de brillo de las prendas a combinar
def genera_veredicto_final(prenda_superior, prenda_inferior):
    color_sup= prenda_superior ["color"].lower()
    color_inf= prenda_inferior ["color"].lower()

    luz_total= VALOR_DE_BRILLO.get(color_sup , 5 ) + VALOR_DE_BRILLO.get(color_inf , 5)
    mezcla= resultado_de_mezcla(color_sup , color_inf)

    if luz_total >= 16:
        mensaje="¡MUYYY BRILLANTE , estas proyectando muchos colores"
    elif luz_total<= 4:
        mensaje= "Elegancia profunda..."

    else:
        mensaje= "Equilibrio maestro"

    return f"Resultado visual: {mezcla} | Energia: {luz_total} /20\nConsejo:{mensaje}"

if __name__ == "__main__":
  prenda_superior = {"nombre": "camisa" , "color": "lila"}
  prenda_inferior = {"nombre": "pantalon" , "color": "petroleo"}

  resultado=genera_veredicto_final(prenda_superior , prenda_inferior)
  print(resultado)