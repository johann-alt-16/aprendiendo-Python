
def obtener_mensaje_estilo(nombre,estilo_numero,categoria_imc):
    """
    Consejos llenos de amor y cariño
    
    """
    mensaje= ""
#ENFOCADO EN LO SLIM FIT
    if estilo_numero== "1" and categoria_imc == "Delgada":
        mensaje += ("\n" +f"Muy bien {nombre}, el estilo que te gustaria usar hoy si te va a lucir pero cuidado con la ropa muy ajustada.")
        mensaje += ("\n" +"Consejo extra, si lo combinas con un pantalon Regular fit, quedara 10 veces mejor.")

    elif estilo_numero == "1" and categoria_imc == "Atletica":    
        print (f"Vaya {nombre}, este estilo te va a quedar super bien, ¡Como te favorece tu cuerpo! ")

    elif estilo_numero == "1" and categoria_imc == "Robusta":
        mensaje += ("\n" +f"La verdad es que este estilo no te lo recomiendo para nada, mejor vamos por una opcion que te favorezca más.")

    elif estilo_numero == "1" and categoria_imc == "Grande":
        mensaje += ("\n" +f"¡NOOO NI SE TE OCURRA! Como tu amigo mi deber es cuidar de tí, asi que mejor probemos con algo mas Overzised. ")   

#ENFOCADO EN LO REGULAR FIT
    if estilo_numero == "2" and categoria_imc == "Delgada":
        mensaje += ("\n" +f"¡Perfecta elección! Preparate para ver lo bonito que se vera tu cuerpo con este estilo {nombre}.")

    elif estilo_numero == "2" and categoria_imc =="Atletica":
        mensaje += ("\n" +f"Qué te puedo decir {nombre} si cualquier estilo te favorece.")

    elif estilo_numero == "2" and categoria_imc == "Robusta":  
        mensaje += ("\n" +f"¡ESOO! Este estilo le suele quedar bien a todo el mundo, pero para tu contextura fisica es el que más te favorecera.")

    elif estilo_numero == "2" and categoria_imc == "Grande":
        mensaje += ("\n" +f"Muye bien {nombre}, este estilo es mas que perfecto para ti.") 
        mensaje += ("\n" +"Dato extra, siempre que estes un poco inseguro prueba algo con este estio.")

#ENFOCADO EN LO RELAXED FIT
    if estilo_numero =="3" and categoria_imc =="Delgada":
        mensaje += ("\n" +f"Excelente eleccion {nombre}, este estilo hara resaltar mas tu figura.")

    elif estilo_numero == "3" and categoria_imc == "Atletica":
        mensaje += ("\n" +"Me parece una eleccion muy casual y atrevida, ¡Me encanta!")

    elif estilo_numero == "3" and categoria_imc == "Robusta":
        mensaje += ("\n" +f"{nombre}, es un estilo muy comodo, ademas igual que con el Regular fit te lo recomiendo al 100%.")

    elif estilo_numero == "3" and categoria_imc == "Grande":
        mensaje += ("\n" +f"{nombre} la verdad que este tipo de corte en la ropa es uno de los mejores, te quedara muy bien.")

#ENFOCADO EN LO STRUCTURE FIT (OVERSIZED)    
    if estilo_numero == "4" and categoria_imc == "Delgada":
        mensaje += ("\n" +f"Vaya {nombre}, este es un estilo que depende más de tu personalidad que de tu cuerpo, asi que si sientes que puedes llevarlo, ")
        mensaje += ("\n" +"la verdad es que te lo recomiendo un monton.")
        mensaje += ("\n" +"Y recuerda este estilo tiene un corte ideal, asi que no se trata de comprar ropa dos tallas mas grandes ¿Ok?")

    elif estilo_numero == "4" and categoria_imc == "Atletica":
        mensaje += ("\n" +f"{nombre}, pendiente con este estilo, por que es pura personalidad,")
        mensaje += ("\n" +"de que te quedara bien lo hara, pero ten en cuenta que lo que hara que te luzca como debe de ser es tu estado de ánimo.")

    elif estilo_numero == "4" and categoria_imc == "Robusta":
        mensaje += ("\n" +"Siempre suelo decir que depende mucho de la perzonalidad de la persona,")
        mensaje += ("\n" +"asi que si te sientes con ganas de comerte el mundo, quedara más que perfecto.")

    elif estilo_numero == "4" and categoria_imc == "Grande":
        mensaje += ("\n" +f"Ojito aqui {nombre} ya que es el estilo que más domina actualmente te lo recomiendo,")
        mensaje += ("\n" +"pero recuerda que es pura personalidad, es decir que depende mucho de tí y no de tu cuerpo.")

    return mensaje 
def dar_apoyo_segun_fisico(nombre, estilo_numero, categoria_imc, altura):
 apoyo_altura= ""
 apoyo_cuerpo= "" 
   
 if altura < 1.65:
        apoyo_altura= "Y recuerda esto, con que seas bajito no significa que no puedes verte bien, asi que ni se te ocurra compararte con personas altas, porque TÚ eres suficiente ¡Animo!"
        if estilo_numero == "4":
            apoyo_altura += "Pero ojo, cuida que la caida de la ropa no sobrepase el muslo, y combinalo con un pantalon o camisa Regular fit."
        else:
            apoyo_altura+= f"Estas en el punto perfecto para usar estas prendas, pero cuida muy bien que el volumen no sea tan exagerado."
        
        if estilo_numero == "1":
            apoyo_altura+= "El estilo Slim te hara ver imponente, pero cuida que no se vea tan ajustado."

        else:
            apoyo_altura+= "Recuerda combinarlo con una prenda un poco mas grande, para que se vea mejor."

 elif altura > 1.82:
        apoyo_altura= f"¡Que buena altura tienes! Creeme que con casi todo te veras espectacular, pero cuidadito con descuidar la vestimenta."

        if estilo_numero== "4":
            apoyo_altura+= f"Qué te puedo decir {nombre}, Si te veras increible."

        if estilo_numero== "1":
            apoyo_altura+= f"Muy bien {nombre}, recuerda combinarlo con una prenda Regular fit o Relaxed fit."


 if categoria_imc == "Delgada":
        apoyo_cuerpo= "\n[Tip de contextura]: Soy tu amigo y no dejare quue te veas sin forma, asi que no tengas eso en mente."
 elif categoria_imc == "Atletica":
        apoyo_cuerpo = "\n[Tip de contextura]: Tienes un cuerpo atletico y aunque casi todo te quede bien, no uses prendaas tan ajustadas."

 elif categoria_imc == "Robusta":
        apoyo_cuerpo= "\n[Tip de contextura]:Tu cuerpo es ideal para los estilos amplios y si te preocupa que se te vea barriguita te haran ver en forma."

 else:
        apoyo_cuerpo= "\n[Tip de contextura]: Recuerda que la ropa es solo un accesorio para tu personalidad, y tambien recuerda que no dejare que te veas mal."


 return  apoyo_altura + apoyo_cuerpo
def bienvenida_al_informe(nombre):
    return f"¡Listo {nombre}! Aquí no andamos con rodeos ni soluciones inutiles. Asi que siempre con la frente muy en alto, somos un equipo y creeme que no te fallare."

