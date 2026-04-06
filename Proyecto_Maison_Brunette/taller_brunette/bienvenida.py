#-----------------------------------------------------BIENVENIDA__A__BRUNETTE-----------------------------------------------------------------

#PRIMER BLOQUE, en donde se crea la entrada de datos que el usuario rellenara la primera ves que inicie sesion en la app.
def obtener_datos_del_usuario():
 print("Hola veo que es tu primera vez en Brunette, es un placer tenerte aqui, ¡Bienvenido! ")
 print("Seamos un equipo, estas listo/a? ")
 respuesta= input("Si o No?: ")
 if respuesta.capitalize() == "Si":
     print("Muy bien, te hare unas preguntas para conocerte, espero que seas sincero/a conmigo.")
 elif respuesta.capitalize()== "No":
     print("Okkk esperare el momento en el que estes aqui otra vez, No te tardes.")
     exit()

#Caracteristicas del usuario.
 if respuesta.capitalize()== "Si":
  sexo= input("Masculino o Femenino?: ")
 nombre=input("¿Como te llamas?: ")
 altura=float(input(f"Tu altura en metros {nombre.capitalize()} ej: 1.70: "))
 peso=float(input(f"Dime tu peso actual en kg {nombre.capitalize()}: "))


 #SEGUNDO BLOQUE, donde se calcula el IMC del usuario y se le recomienda un estilo que le podria quedar bien.
 imc= peso / (altura**2)
 if 18 <= imc < 18.7 :
    recomendacion_fit= "Slim fit"
 elif 18.7 <= imc <= 24.9:
    recomendacion_fit= "Regular fit"
 elif 25 <= imc <=29.9:
    recomendacion_fit= "Relaxed fit"
 else:
    recomendacion_fit= "Structure fit"
 print(f"{nombre.capitalize()} basado en tu perfil, tu corte ideal es {recomendacion_fit}")
 print(f"Pero si quieres probar cosas diferentes a lo que te recomiendo no pasa nada, igual trabajare junto a ti para que siempre te veas bien.")

#TERCER BLOQUE donde se le have pruebas al usuario para saber su tipo de cuerpo.
 print(f"Muy bien {nombre.capitalize()}, para continuar con la personalizacion de Brunette; intenta rodear tu muñeca como se ve en la imagen y seleciona la opcion que mas este cerca de tu realidad.")
 A=print("Opcion A, tus dedos sobrepasan tu muñeca.")
 B=print("Opcion B, tus dedos apenas se tocan.")
 C=print("Opcion C, tus dedos no se tocan.")
 opcion_elegida=input(f"Cual es la correcta en tu caso {nombre.capitalize()} la A/B o C?: ")

#CUARTO BLOQUE donde se crea la personalidad de la app en diferentes caso, si es hombre o mujer.
 if opcion_elegida.capitalize()== "A" and sexo.capitalize()== "Femenino":
    operacion_matematica_de_A= altura*0.22
    print(f"Muy bien mi amor, ahora si estoy lista para ayudarte a verte mejor, Confia en mi")

 elif opcion_elegida.capitalize()== "B" and sexo.capitalize()== "Femenino":
    operacion_matematica_de_B= altura*0.25
    print(f"Perfecto {nombre.capitalize()}, ahora si estoy lista para ayudarte a verte preciosa, Tu solo confia en mi.")

 elif opcion_elegida.capitalize()== "C"and sexo.capitalize()== "Femenino":
    operacion_matematica_de_C= altura*0.28
    print(f"Muyyy Bien {nombre.capitalize()}, preparate para ver cada dia a tu mejor version, Confia en mi ¿va?")

#SII ES HOMBRE
 if opcion_elegida.capitalize()== "A" and sexo.capitalize()== "Masculino":
    operacion_matematica_de_A= altura*0.22
    print(f"Perfecto {nombre.capitalize()}, espero tambien estes preparado para ver a tu mejor version cada dia, Confia en mi")

 elif opcion_elegida.capitalize()== "B" and sexo.capitalize()== "Masculino":
    operacion_matematica_de_B= altura*0.25
    print(f"Perfecto {nombre.capitalize()}, ahora si estamos listos para ser un equipo, Tu confia en mi, y yo en ti.")

 elif opcion_elegida.capitalize()== "C"and sexo.capitalize()== "Masculino":
    operacion_matematica_de_C= altura*0.28
    print(f"Muyyy Bien {nombre.capitalize()}, preparate para ver cada dia a tu mejor version, Confia en mi ¿va?")

#QUINTO BLOQUE, donde el usuario elige su estilo para el Dia.
 print(f"Recuerda {nombre.capitalize()} que tu estilo ideal es {recomendacion_fit}, pero podrias decirme si quieres seguir mi recomendacion o probar algo nuevo.")
 print("Quieres seguir la recomendacion que te sugeri o prefieres proyectar algo nuevo?")
 eleccion_usuario= input("La seguiras, Si/No?: ")

 if eleccion_usuario.capitalize()== "Si":
    print(f"Muy bien {nombre}, has decidido hacerme caso y creeme que no te arrepentiras.")
    estilo_de_hoy={recomendacion_fit}
    print(f"Vale como sigues mi recomendacion crearemos tu ouffit a partir de un estilo a lo {recomendacion_fit}.")
   

 elif eleccion_usuario.capitalize()== "No":
    print(f"Ok {nombre.capitalize()} como te dije antes aunque no sea mi recomendacion, creeme que igual te veras increible.")
   
    print(f"Dime que quieres proyectar hoy {nombre.capitalize()}.")
    print("Opcion 1, Slim fit. ")
    print("Opcion 2, Regular fit.")
    print("Opcion 3, Relaxed fit.")
    print("Opcion 4, Structure fit.")

    estilo_de_hoy= input(f"Y bien {nombre.capitalize()}, cual te animas a probar; 1, 2, 3 o 4?: ")

    if eleccion_usuario.capitalize()== "No" and estilo_de_hoy== "1":
     print(f"Muy buena eleccion {nombre.capitalize()}, hoy te veras muy elegante.")

    elif eleccion_usuario.capitalize()== "No" and estilo_de_hoy=="2":
     print(f"Perfecta eleccion {nombre.capitalize()}, estaras muy a gusto hoy.")

    elif eleccion_usuario.capitalize()== "No" and estilo_de_hoy== "3":
     print(f"Ufff creeme que te veras espectacular {nombre}.")

    elif eleccion_usuario.capitalize()== "No" and estilo_de_hoy== "4":
     print(f"Bueno me parece una eleccion muy atrevida, sin embargo confia en que te veras increible.")

    else: 
     print(f"Lo siento {nombre.capitalize()} no contamos con esa eleccion.")
obtener_datos_del_usuario()
 #return nombre, altura, sexo, peso, estilo_de_hoy
