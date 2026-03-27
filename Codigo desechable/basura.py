#Probando codigo

#Herramientas
perfil_bajo= 1
perfil_estandar=2
perfil_alto= 3

#Enseñando a usar las herramientas
def perfil(eleccion):

   if perfil_bajo==eleccion:
    print("Te hare lucir espectacular sin sobresalir, confia en mi socio")

   elif perfil_estandar== eleccion:
    print ("Te preparas para lo comodo, que buena eleccion")  

   elif perfil_alto== eleccion:
    print ("Ohhh veo que alguien quiere ser el alma de la fiesta, confia en mi yo me encargo de la ropa")

   else:
    print ("Lo lamento pero solo tenemos los niveles 1, 2 y 3")

#Encendiendo el motor
Contador_de_usos=0

while True:
   eleccion= int(input("Que nivel te gustaria llevar hoy?:  "))
   if eleccion==0:
      print(f"Hoy has usado la app {Contador_de_usos} veces")
      break
   perfil(eleccion)
   Contador_de_usos +=1

print("Gracias por usar nuestra app ¡Vuelve pronto!")