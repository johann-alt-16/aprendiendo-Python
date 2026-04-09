from bienvenida import obtener_datos_del_usuario
from cerebro_del_color import obtener_subtono_piel, verificar_prenda_usuario
import mente_logica
import memoria_de_consejos

import mente_visual_brillo

import corazon_core

def lanzar_maison_brunette():
    #0. Opcional 
    

    #1. Entrada de datos
    nom, alt, sex, pes, color_ven, color_acc, mun, est= obtener_datos_del_usuario()
    mensaje , color_sub= obtener_subtono_piel(nom, color_ven, color_acc)
    print(f"\n{mensaje}")

    #2. Proceso logico
    val_imc, fit_tec, cat_hum = mente_logica.calcular_imc_y_estilo(pes,alt)
    medida_hueso=mente_logica.calcular_medida_osea(mun, alt)
    largo_prenda= mente_logica.calcular_proporcion_prenda(alt,est)

    #Proceso visual y de armario
    print("---REGISTRO DE PRENDAS---")
    corazon_core.registrar_ropa()
    corazon_core.registrar_ropa()
    print(f"\n--- REVISANDO TU ARMARIO, {nom.upper()} ---")

    estilos_nombres= {"1": "Slim fit", "2": "Regular fit", "3": "Relaxed fit", "4": "Structure fit"}
    nombre_estilo= estilos_nombres.get(est)

    lista_opciones= corazon_core.armario.get(nombre_estilo,[])

    if len(lista_opciones) < 2:
        print(f"Oye {nom} necesitas al menos dos prendas en tu seccion '{nombre_estilo}' para mezclar.")
        return
    
    #seleccion real de prendas
    for i, p in enumerate(lista_opciones):
        print(f"{i}. {p['nombre']} ({p['color']})")

    while True:
     try:
      id1= int(input("\nElige el numero de tu prenda superior: "))
      id2= int(input("Elige el numero de tu prenda inferior: "))
     except:
        print("Por favor elige un numero, no esta permitido las letras.")
        return lanzar_maison_brunette()
     prenda_sup= lista_opciones[id1]
     prenda_inf= lista_opciones[id2]
     
     _, _, opinion_estilo= verificar_prenda_usuario(nom, prenda_sup['color'], prenda_inf['color'],color_sub)
     print(f"\n--- Brunette dice: ---")
     print(opinion_estilo)
     if "Mira" in opinion_estilo:
        opcion = input("\n ¿Quieres intentar otra combinacion? (Si/No): ").lower()
        if opcion == "si":
           continue
     break   

    #SE ejecuta el veredicto
    veredicto_final = mente_visual_brillo.genera_veredicto_final(prenda_sup, prenda_inf)

    #Entra en accion la bilioteca de consejos

    saludo= memoria_de_consejos.bienvenida_al_informe(nom)
    mensaje_estilo= memoria_de_consejos.obtener_mensaje_estilo(nom, est, cat_hum)
    apoyo_fisico= memoria_de_consejos.dar_apoyo_segun_fisico(nom, est, cat_hum, alt)

    #REPORTE FINaL
    print("\n" + "*"*35)
    print(f"      {saludo}")
    print(" " + "*" *35)

    print(f"\n RESULTADO VISUAL:")
    print(veredicto_final)

    print(f"\n TU ASESORIA PERSONAL:")
    print(f"{mensaje_estilo}")
    print(f"\n{apoyo_fisico}")

    print("\n" + "-" * 45)
    print(f" FICHA TECNICA:")
    print(f" > Ajuste Sugerido: {val_imc}")
    print(f" > Medida ósea: {medida_hueso}m")
    print(f" > Largo de prenda: {largo_prenda}cm")
    print("-" * 45)

    print(f"\n¡Listo, {nom}! Ya puedes dormir como un master. ¡Maison Brunette la romperaaa!")

if __name__ =="__main__":
 lanzar_maison_brunette()