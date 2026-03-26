#calcular cuantos pantalones hay en el almacen disponibles
compartimentos= int(input('cuantos compartimentos hay?: '))
espacio_de_cada_campartimento= int(input('Cuantos pantalones caben en cada compartimento?:'))
Meta_de_año_nuevo= int(input('cuantos pantalones quieres alcanzar para año nuevo?:'))
#Formula para calcular los pantalones
resultado= espacio_de_cada_campartimento* compartimentos
resultado_de_meta=  resultado-Meta_de_año_nuevo


#Aplicando las condiciones

if resultado >2000 and resultado_de_meta >1900:
    print ('Wow johan tienes suficientes pantalones para vestir a un pais entero')

elif resultado>=1500 and resultado_de_meta >= 1400:
    print (f"No te preocupes socio aunque tu meta haya fallado aun te quedan {resultado_de_meta} pantalones para vender ¡Animoo!")

elif resultado >=23 and resultado_de_meta >=1:
     print (f"No te preocupes socio aunque tu meta haya fallado aun te queda {resultado_de_meta} pantalones para vender ¡Animoo!")
elif resultado <=0 or resultado_de_meta<=0:
     print(f" bro estas seguro que la cuenta de tu negocio fue de {resultado_de_meta} si es asi vamos grave ahi que ver si nos alcanza para lo que pide la gente")
else:
    print(" No hay na' se fracaso pero a seguir adelante")
