#BIENVENIDAAAAAAAAAAAAaAA

#Primer bloque de bienvenida
print("Hola veo que es tu primera vez en Brunette, es un placer tenerte aqui, ¡Bienvenido! ")
print("Seamos un equipo, estas listo/a")
respuesta= input("Si o No?: ")
if respuesta.capitalize() == "Si":
    print("Muy bien, te hare unas preguntas para conocerte, espero que seas sincero/a")
elif respuesta.capitalize()== "No":
    print("Okkk esperare el momento en el que estes aqui otra vez, No te tardes.")
#Segundo bloque de la bienvenida
if respuesta.capitalize()== "Si":
 
 #Caracteristicas del usuario
 sexo= input("Hombre o Mujer?: ")
 nombre=input("¿Como te llamas?: ")
 altura=float(input(f"Tu altura en metros {nombre.capitalize()} ej: 1.70: "))
 peso=float(input(f"Dime tu peso actual en kg {nombre.capitalize()}: "))

 #CALCULO DEL IMC.
 imc= peso/ (altura**2)
 if 18 <= imc < 18.7 :
    recomendacion_fit= "Slim fit"
 elif 18.7 <= imc <= 24.9:
    recomendacion_fit= "Regular fit"
 elif 25 <= imc <=29.9:
    recomendacion_fit= "Relaxed fit"
 else:
    recomendacion_fit= "Structure fit"
 
 print(f"\n--- RECOMENDACION DE ESTILO PARA {nombre.upper()} ---")
 print(f"Basado en tu perfil, tu corte ideal es {recomendacion_fit}")
 print(f"No te preocupes si no entiendes de que hablo {nombre.capitalize()}, mas adelante veras de que hablo.")

#CALIFICA SI ES MESO; ECTO O ENDO.
 print(f"Valee perfecto, para continuar con la personalizacion de Brunette; intenta rodear tu muñeca como se ve en la imagen y seleciona la opcion que mas este cerca de tu realidad")
 A=print("Opcion A, tus dedos sobrepasan tu muñeca.")
 B=print("Opcion B, tus dedos apenas se tocan.")
 C=print("Opcion C, tus dedos no se tocan.")
 opcion_elegida=input(f"Cual se acerca a tu realidad {nombre.capitalize()} la A/B o C?: ")

#tercer bloque de la bienvenida
if opcion_elegida.capitalize()== "A" and sexo.capitalize()== "Mujer":
   operacion_matematica_de_A= altura*0.22
   print(f"Muy bien mi amor, ahora si estoy lista para ayudarte a verte mejor, Confia en mi")

elif opcion_elegida.capitalize()== "B" and sexo.capitalize()== "Mujer":
   operacion_matematica_de_B= altura*0.25
   print(f"Perfecto {nombre.capitalize()}, ahora si estoy lista para ayudarte a verte preciosa, Tu solo confia en mi.")

elif opcion_elegida.capitalize()== "C"and sexo.capitalize()== "Mujer":
   operacion_matematica_de_C= altura*0.28
   print(f"Muyyy Bien {nombre.capitalize()}, preparate para ver cada dia a tu mejor version, Confia en mi ¿va?")

#SII ES HOMBRE

if opcion_elegida.capitalize()== "A" and sexo.capitalize()== "Hombre":
   operacion_matematica_de_A= altura*0.22
   print(f"Perfecto {nombre.capitalize()}, espero tambien estes preparado para ver a tu mejor version cada dia, Confia en mi")

elif opcion_elegida.capitalize()== "B" and sexo.capitalize()== "Hombre":
   operacion_matematica_de_B= altura*0.25
   print(f"Perfecto {nombre.capitalize()}, ahora si estamos listos para ser un equipo, Tu confia en mi, y yo en ti.")

elif opcion_elegida.capitalize()== "C"and sexo.capitalize()== "Hombre":
   operacion_matematica_de_C= altura*0.28
   print(f"Muyyy Bien {nombre.capitalize()}, preparate para ver cada dia a tu mejor version, Confia en mi ¿va?")


print(f"Oye {nombre}, tu estilo ideal es {recomendacion_fit}, pero podrias decirme si quieres seguir mi recomendacion o probar algo nuevo.")
print("Quieres seguir la recomendacion que te sugeri o prefieres proyectar algo nuevo?")
eleccion_usuario= input("La seguiras, Si/No?: ")

if eleccion_usuario.capitalize()== "Si":
   print(f"Muy bien {nombre}, una vez mas te digo, confia en mi, te veras increible. ")

elif eleccion_usuario.capitalize()== "No":
   print("Muy bien, no te preocupes, que no sea mi recomendacion, no significa que te quedara mal, aun lograremos que te veas espectacular a tu modo")
   
   print(f"Dime que quieres proyectar hoy {nombre.capitalize()}")
   print("Opcion 1, Slim fit ")
   print("Opcion 2, Regular fit")
   print("Opcion 3, Relaxed fit")
   print("Opcion 4, Structure fit")

   estilo_de_hoy= input(f"Y bien {nombre.capitalize()}, cual te animas a probar; 1, 2, 3 o 4?: ")

if estilo_de_hoy== "1":
   print(f"Muy buena eleccion {nombre.capitalize()}, hoy te veras muy elegante")

elif estilo_de_hoy=="2":
   print(f"Perfecta eleccion {nombre.capitalize()}, estaras muy a gusto hoy")

elif estilo_de_hoy== "3":
   print(f"Ufff creeme que te veras espectacular {nombre}")

else:
   print(f"Buenoo {nombre} veo que te encanta estas comoda, no te arrepentiras de como te veras hoy")
