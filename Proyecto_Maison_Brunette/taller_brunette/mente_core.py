#Se convoca las herramientas del corazon
from corazon_core import ropa_caracteristica
from corazon_core import ropa_caracteristica2
#Se crea diccionario con el valor de luz que reflejan los colores
VALOR_DE_BRILLO= {
    "negro": 0,
    "marino":2,
    "cafe":3,
    "gris":5,
    "azul":6,
    "verde":6,
    "rojo": 7,
    "naranja":8,
    "amarillo":9,
    "blanco": 10
    }
#Se le enseña que hacer con las herramientas
def resultado_de_mezcla(color1, color2):

    recetario_de_colores ={
        ("azul" , "amarillo"): "verde",
        ("rojo", "azul"): "morado",
        ("rojo", "amarillo"): "naranja",
        ("blanco", "negro"): "gris",
        ("blanco", "rojo"): "rosado"
    }
#Es util para detectar que "azul , amarillo" es igual a "amarillo , azul"
    resultado= recetario_de_colores.get((color1 , color2)) or recetario_de_colores.get((color2 , color1))

#Solo comprimi el if/else para no ocupar mas espacio, no cambia absolutamente nada.
    return resultado if resultado else "combinacion libre"

def genera_veredicto_final(prenda_superior, prenda_inferior):
    prenda_superior = ("color").lower()
    prenda_inferior= ("color").lower()

    luz_total= VALOR_DE_BRILLO.get(prenda_superior , 5 ) + VALOR_DE_BRILLO.get(prenda_inferior , 5)
    mezcla= resultado_de_mezcla(prenda_superior , prenda_inferior)

    if luz_total >= 16:
        mensaje="¡MUYYY BRILLANTE , estas proyectando muchos colores"
    elif luz_total<= 4:
        mensaje= "Elegancia profunda..."

    else:
        mensaje= "Equilibrio maestro"

    return f"Resultado visual: {mezcla} | Energia: {luz_total} /20\nConsejo:{mensaje}"

prenda_superior = {"nombre": "camisa" , "color": "negro"}
prenda_inferior = {"nombre": "pantalon" , "color": "rojo"}

resultado=genera_veredicto_final(prenda_superior , prenda_inferior)
print(resultado)