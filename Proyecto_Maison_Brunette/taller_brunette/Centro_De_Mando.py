from bienvenida import obtener_datos_del_usuario
from corazon_core import registrar_ropa, armario
from mente_core import genera_veredicto_final

def iniciar_maison_brunette():
    print ("---BIENVENIDO A MAISON BRUNETTE---")
#SE LLAMA A LA MENTE
    nombre, altura, sexo, peso, estilo_de_hoy = obtener_datos_del_usuario()

#SEE LLAma AL CORAZON
    registrar_ropa()
    proporcion= round(altura *100 /3, 1)
    estilos={"1": "Slim fit", "2": "Regular fit" ,"3":"Relaxed fit", "4": "Structure fit"}
    estilo_elegido = estilos.get(estilo_de_hoy, "Regular fit")
    
    if armario[estilo_elegido]:
      prenda_final= armario[estilo_elegido][-1]
      pantalon_negro= {"nombre": "Pantalon base", "color": "negro"}

      veredicto= genera_veredicto_final(prenda_final, pantalon_negro)

      print(f"\nOuffit: {prenda_final['nombre']} ({prenda_final['color']}) + Pantalon Negro")
      print(veredicto)
      print(f"Recuerda: que tu {prenda_final['nombre']} mida {proporcion}cm.")

    else:
       print(f"No hay nada en el estilo {estilo_elegido}")

if __name__ =="__main__":
   iniciar_maison_brunette()