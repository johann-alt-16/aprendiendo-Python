#Probando codigo

def colores( ):
   eleccion_de_usuario=input('que color quieres maestro?: ').lower()
   colores_disponibles= ['negro', 'azul', 'verde']

    
    

   if eleccion_de_usuario in colores_disponibles:
      print(f"¡ufff que buen gusto compa! ese {eleccion_de_usuario} te quedara guapisimoo")

   else:
        print(f"Lo siento wey el color {eleccion_de_usuario} no lo tenemos disponible")


def pantalones ():
 Usuario= input(" Que pantalon quieres rey?: ").capitalize()
 Pantalones_Disponible=["De vestir", "Clasico", "Cargo"]
 
 if Usuario in Pantalones_Disponible:
    print(f"Ohhhh con un pantalon {Usuario} vas a ser el centro de atencion")

colores()
pantalones()
