color_vena={
        "A": "Verdes",
        "B": "Azules",
        "C": "Ambas"
    }
color_accesorio={
        "A": "Dorado",
        "B": "Plateado",
        "C": "Ambos"
    }

colores_para_el_usuario= {
        "Calido": ["mostaza", "naranja", "verde", "oliva", "cafe", "beige", "arena", "rojo", "amarillo"],
        "Frio": ["verde azulado", "azul marino", "azul", "cian", "lila", "rosa pastel", "plata", "vino"],
        "Neutro": ["negro", "gris", "arena", "blanco"]
    }


#Funciones de piel y colorimetria.
def obtener_subtono_piel(nombre, color_vena, color_accesorio ):
    if color_vena == "A" and color_accesorio== "A":
        mensaje= f"Vaya {nombre}, tu subtono de piel es calido, asi que asegurate de tener ropa con tonos amarrilos o tierra."
        color_subtono= "Calido"
    elif color_vena == "B" and color_accesorio== "B" :
        mensaje=f"Muy bien {nombre} tu subtono de piel es frio, los tonos azules te quedaran como anillo al dedo."
        color_subtono= "Frio"
    else:
        mensaje= f"Ohh casi todos los colores te iran bien {nombre}, que suerte tienes, el subtono neutro es el mas vérsatil."
        color_subtono= "Neutro"
    return mensaje, color_subtono

def color_favorecido():
    colores_para_el_usuario={
        "Calido": ["mostaza", "naranja", "verde", "oliva", "cafe", "beige", "arena", "rojo", "amarillo"],
        "Frio": ["verde azulado", "azul marino", "azul", "cian", "lila", "rosa pastel", "plata", "vino"],
        "Neutro": ["negro", "gris", "arena", "blanco"]
    }
    

def verificar_prenda_usuario (nombre, prenda_sup, prenda_inf, color_subtono):
    color_ideal= colores_para_el_usuario[color_subtono]
    para_neutro= color_ideal + colores_para_el_usuario['Neutro']
    if prenda_sup in color_ideal and prenda_inf in color_ideal:
        opinion_prendas= f"¡Uff, {nombre}! Qué nivel. Esa combinación resalta tu tono de piel al 100%. Te veras increible."

    elif combinaciones_mixtas(prenda_sup, prenda_inf):
        opinion_prendas= f"Oye {nombre} de verdad que me encanta esta combinacion de colores. Admiro mucho tu estilo propio"

    elif prenda_sup in para_neutro or prenda_inf in para_neutro:
        opinion_prendas= f"Que buena eleccion {nombre} los colores neutros quedan muy bien con tu subtono de piel {color_subtono}"

    else:
        opinion_prendas=f"Te recomiendo usar colores mas al estilo de tu subtono {color_subtono}"

    return color_ideal, para_neutro, opinion_prendas

def combinaciones_mixtas(prenda_sup, prenda_inf):
    combo_usuario={prenda_sup.lower(), prenda_inf.lower()}

    combo_maestro=[
        {"mostaza", "azul marino"},
        {"naranja", "azul"},
        {"verde oliva","rosa pastel"},
        {"vino", "beige"},
        {"cafe", "cian"},
        {"azul marino", "arena"},
        {"lila", "cafe"},
        {"rojo", "plata"},
        {"verde oliva", "azul marino"},
        {"verde azulado", "mostaza"}
    ]
    return combo_usuario in combo_maestro
