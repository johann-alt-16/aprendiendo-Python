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

try:
    while True:
        entrada = input("¿Qué nivel te gustaría llevar hoy? (1, 2, 3 o 0 para salir): ")
        if not entrada.isdigit():
            print("Por favor, introduce un número válido.")
            continue
        
        eleccion = int(entrada)
        if eleccion == 0:
            print(f"Hoy has usado la app {Contador_de_usos} veces.")
            break
        perfil(eleccion)
        Contador_de_usos += 1
except KeyboardInterrupt:
    print("\nPrograma finalizado por el usuario.")

print("Gracias por usar nuestra app ¡Vuelve pronto!")