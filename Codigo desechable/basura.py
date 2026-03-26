#Probando codigo
def colores(eleccion_de_usuario=input('que color quieres maestro?: ').lower()):
     colores_disponibles= ['negro', 'azul', 'verde']
     print(  )
   

     if eleccion_de_usuario in colores_disponibles:
      print(f"¡ufff que buen gusto compa! ese {eleccion_de_usuario} te quedara guapisimoo")
      
colores()