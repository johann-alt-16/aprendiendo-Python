

#CAJA DE GUARDADO
armario={
    "Slim fit": [],
    "Regular fit": [],
    "Relaxed fit": [],
    "Structure fit": [],
}

#BUCLE PARA QUE EL USUARIO AGREGUE LA ROPA AL ARMARIO VACIO

def registrar_ropa():
  while True:
    ropa_agregada= input("Que prenda vas a agregar?: (escribe Salir para terminar) ")
    if ropa_agregada.capitalize() == "Salir":
             
             break

    color= input(f"¿De que color es tu {ropa_agregada.capitalize()}?: ")

    print("Que corte tiene tu prenda? 1. Slim fit | 2. Regular fit | 3. Relaxed fit | 4. Structure fit")
    opcion=input("Dime cual corte tiene: ")

    info_prenda={"nombre": ropa_agregada,"color": color}

#CLASIFICACION

    if opcion == "1":
     armario["Slim fit"].append(info_prenda)

    elif opcion == "2":
     armario["Regular fit"].append(info_prenda)

    elif opcion == "3":
     armario["Relaxed fit" ].append(info_prenda)

    elif opcion == "4":
     armario["Structure fit"].append(info_prenda)
     
    else:
     print("Lo siento esa opcion no esta disponible")
     
#MOSTRARR ROPA AGREGADA.
 
    for estilo, lista_ropa in armario.items():
       if len(lista_ropa)>0:
           print(f"{estilo} : {','.join([f'{p["nombre"]} ({p["color"]})'for p in lista_ropa])}")
       else:
           print(f"{estilo} : (vacio)")

pass
if __name__== "__main__":
   registrar_ropa()