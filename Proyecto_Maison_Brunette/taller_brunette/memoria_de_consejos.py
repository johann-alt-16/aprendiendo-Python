
def obtener_mensaje_estilo(nombre,estilo_numero):
    """
    Consejos llenos de amor y cariño
    """
    biblioteca= {
        "1": f"¡Amo cómo te va a quedar el estilo Slim Fit {nombre}! Es la opcion ideal para resaltar tu cuerpo y que te veas con mucho estilo.",
       
        "2": f"Que buena eleccion {nombre}, el Regular Fit es lo clasico que nunca falla, creeme que te veras increible.",

        "3": f"¡Qué buen estilo tienes {nombre}, el Relaxed Fit es lo mejor si quieres tener estilo y a la ves toda la comodidad posible.",

        "4": f"Uff {nombre} desde el fondo del corazon, esta combinacion te quedara brutal. ¡¡Me encanta!!"

    }
    return biblioteca.get(estilo_numero, f"¡Oye me gusto mucho lo que elegiste, estoy seguro que te veras espectaculaar.")

def dar_apoyo_segun_fisico(nombre, categoria_imc, altura):
    if altura < 1.70:
        apoyo_altura= "Y recuerda esto, con que seas bajito no significa que no puedes verte bien, asi que ni se te ocurra compararte con personas altas, porque TÚ eres suficiente ¡Animo!"

    elif altura > 1.80:
        apoyo_altura= f"¡Que buena altura tienes! Creeme que con casi todo te veras espectacular, pero cuidadito con descuidar la vestimenta."

    else:
        apoyo_altura= f"Tienes una altura muy bien equilibrada, asi que enfocate en ropas que alargen mas tu figura, Confia en mi que el trabajo que hago siempre sera a tu favor."

    #Logica de consejos para flacos y gordos
    if categoria_imc== "Delgada":
        mensaje_cuerpo= f"Oye si te sientes mal con tu cuerpo, creeme que no pasa nada, para eso me tienes a mi, para ayudarte a sacar siempre tu mejor version."

    elif categoria_imc == "Atletica":
        mensaje_cuerpo= f" Estas en un buen estado fisico {nombre} ¡Te felicito!, mi consejo es que te atrevas a probar colores nuevos, creeme que casi todo te quedara super bien."

    elif categoria_imc == "Robusta":
        mensaje_cuerpo= f"Oye {nombre} si te preocupa que se te vea barriga, el secreto esta en ropa que no te quede tan pegada al cuerpo ni una que te haga ver mas grande, el estilo Regular fit sera tu mejor aliado, creeme."

    elif categoria_imc == "Grande":
        mensaje_cuerpo= f"Hablemos claro {nombre}, para las personas grandes, la clave esta en un buen balance de estructura y colores mas oscuros y eso esta en mis manos, asi que no te preocupes si tienes panza de más."

    else:
        mensaje_cuerpo= f"{nombre} lo mas importante es que siempre camines con la frente en alto. Tú seguridad es lo que hara que la ropa se va realmente bien."

    return f"{mensaje_cuerpo}\n\n{apoyo_altura}"

def bienvenida_al_informe(nombre):
    return f"¡Listo {nombre}! Aquí no andamos con rodeos ni soluciones inutiles. Asi que siempre con la frente muy en alto, somos un equipo y creeme que no te fallare."

