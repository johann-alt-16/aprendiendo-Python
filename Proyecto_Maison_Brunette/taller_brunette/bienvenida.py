#BIENVENIDAAAAAAAAAAAAaAA

#Primer bloque de bienvenida
print("Hola veo que es tu primera ves en Brunette ¿me permites hacerte unas preguntas?")
respuesta= input("Si o No?: ")
if respuesta.capitalize() == "Si":
    print("Valee perfecto, comenzemos a crear a tu compañero brunette")
elif respuesta.capitalize()== "No":
    print("Okkk vuelve cuando estes listo, ¿te parece?")
#Segundo bloque de la bienvenida
if respuesta.capitalize()== "Si":
 
 #Caracteristicas del usuario
 nombre=input("¿Como te llamas compañero?: ")
 altura=float(input(f"tu altura en metros {nombre} ej: 1.70: "))
 peso=float(input(f"Dime tu peso actual en kg {nombre}: "))

 #CALCULO DEL IMC.
 imc= peso/ altura**2
 if imc < 18.5:
    recomendacion_fit= "Slim fit"
 elif 18.5 <= imc <= 24.9:
    recomendacion_fit= "Regular fit"
 else:
    recomendacion_fit= "Structure fit"
 
 print(f"\n--- RECOMENDACION DE ESTILO PARA {nombre.upper()} ---")
 print(f"Basado en tu perfil, tu corte ideal es {recomendacion_fit}")

#CALIFICA SI ES MESO; ECTO O ENDO.
 print(f"Valee perfecto, continuemos con la personalizacion de Brunette; intenta rodear tu muñeca como se ve en la imagen y seleciona la opcion acertada ¿va?")
 A=print("Opcion A, tus dedos sobrepasan tu muñeca")
 B=print("Opcion B, tus dedos apenas se tocan ")
 C=print("Opcion C, tus dedos no se tocan")
 opcion_elegida=input(f"Cual se acerca a tu realidad {nombre} la A/B o C?: ")

#tercer bloque de la bienvenida
if opcion_elegida.capitalize()== "A":
   operacion_matematica_de_A= altura*0.22
   print(f"Perfecto {nombre}, estamos listos para que Brunette te ayude a verte espectacular, Confia en mi")

elif opcion_elegida.capitalize()== "B":
   operacion_matematica_de_B= altura*0.25
   print(f"Perfecto {nombre}, ahora si que estamos listo para que Brunette te ayude a verte Mejor, Tu solo confia en mi.")

elif opcion_elegida.capitalize()== "C":
   operacion_matematica_de_C= altura*0.28
   print(f"Muyyy Bien {nombre}, preparate para ver cada dia a tu mejor version, confia en mi ¿va?")