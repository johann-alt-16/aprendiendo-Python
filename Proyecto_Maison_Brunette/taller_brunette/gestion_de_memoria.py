import json
import os

def cargar_memoria_existente():
    if os.path.exists("Gestion_de_memoria.json"):
               with open("Gestion_de_memoria.json", "r") as memoria:
                    return json.load(memoria)
    else:         
     return {
      "Slim fit": [],
      "Regular fit": [],
      "Relaxed fit": [],
      "Structure fit": [],
    } 
         
            

def prendas_del_usuario(nombre, armario_recibido):
    try:
        with open("Gestion_de_memoria.json", "w") as memoria:
            json.dump(armario_recibido, memoria, indent=4)
        print(f"\nEl guardado de tu armario se a ejecutado con exito {nombre}.")
    except Exception as e:
        print(f"Error al intentas guardar en la memoria {e}")


  



