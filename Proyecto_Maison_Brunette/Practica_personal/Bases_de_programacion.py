
#git add (nombre del archivo)
#git commt -m "Activo"
# git push
#Bienvenida a la app
print("Hola estas listo para ver tu mejor version?")
respuesta_del_usuario= input("Responde con Si o No: "):
while respuesta_del_usuario =="Si" or respuesta_del_usuario=="No":
  respuesta_del_usuario= input("Responde con Si o No: ")
  if respuesta_del_usuario=="Si":
      print("¡Genial! Vamos a empezar con algunas preguntas para conocerte mejor y así poder darte las mejores recomendaciones de moda") 
  elif respuesta_del_usuario=="No":
      print("¡No te preocupes! Tómate tu tiempo y vuelve cuando estés listo para descubrir tu mejor versión.")
      break
#almacenar los parametros de las condiciones
      color_a_utilizar= input("Dime que colores te gustaria llevar hoy: (Azul, Rojo, Negro) ")
      convertir_a_cap= color_a_utilizar.capitalize()
      tipo_de_cuerpo= input("¿Cuál es tu tipo de cuerpo? (mesomorfo, endomorfo, ectomorfo): ")
      convertir_tipo_de_cuerpo= tipo_de_cuerpo.lower()
      Evento= input("¿A qué evento asistirás hoy? (formal, casual, deportivo): ")
      convertir=Evento.capitalize()

#Aplicando las condiciones en el programa
      if Evento=="Casual" and tipo_de_cuerpo=="mesomorfo" and color_a_utilizar=="Azul":
         print("Te recomiendo usar un pantalon holgado y una camisa de slim fit")

      elif Evento=="Formal" and tipo_de_cuerpo=="ectomorfo" and color_a_utilizar=="Negro":
         print("Te recomiendo usar un traje formal y una camisa de manga larga.")

      elif Evento=="Deportivo" and tipo_de_cuerpo=="endomorfo" and color_a_utilizar=="Rojo":
         print("Te recomiendo usar ropa que sigan la silueta normal de tu cuerpo, el color rojo no te favorece, pero no te preocupes, te tengo una mejor opcion, utiliza mejor un Negro")

      else:
        print("Lo siento, no tengo una recomendación para esa combinación de características.")
 
