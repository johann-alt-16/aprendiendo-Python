#-----------------------------------------------------BIENVENIDA__A__BRUNETTE-----------------------------------------------------------------

#PRIMER BLOQUE, en donde se crea la entrada de datos que el usuario rellenara la primera ves que inicie sesion en la app.
def obtener_datos_del_usuario():
#limpiamos un poco la terminal al iniciar
 print("\n" * 2)
 print("=" * 50)
 print("       WELCOME TO MAISON BRUNETTE       ")
 print("     Consultoria de Imagen y Estilo      ")
 print("=" * 50)
 
 print("\nEs un honor recibirte. Para comenzar con tu transformacion,")
 print("necesitaremos definir los pilares de tu perfil fisico.\n")

 #Registro de identidad
 nombre= input("¿Con quien tengo el placer de hablar hoy?: ").strip().capitalize()
 print(f"Perfecto, {nombre}. Comenzemos con tus dimensiones metricas.")

 #Datos antropometricos y reinicia si ahi error de escritura en cuanto a numeros.
 try:
    altura=float(input("¿Cual es tu estatura actual en metros? (Ej: 1.75): "))
    peso=float(input("¿Podrias indicarme tu peso en kilogramos?: "))
 except ValueError:
    print("\n[!] Por favor, usa numeros y puntos para las medidas (ej: 1,70 o 1.80).")
    return obtener_datos_del_usuario()
 
 sexo= input("¿Tu perfil de estilo es Masculino o Femenino?: ").strip().capitalize()

 #Evaluacion de estructura osea
 print("\n" + "-"*40)
 print("    EVALUACION DE ESTRUCTURA ÓSEA     ")
 print("-"*40)
 print("Esta prueba nos dirá de cómo se vé la ropa en tu cuerpo.")
 print("Rodea tu muñeca con tus dedos índice y pulgar:")
 print("    [A] Los dedos se sobreponen claramente (Estructura Fina)")
 print("    [B] Los dedos apenas logran tocarse (Estructura Media)")
 print("    [C] los dedos no llegan a encontrarse (Estructura Robusta)")

 opcion_muneca= input(f"\n¿Qué resultado obtuviste, {nombre}? (A/B/C): ").strip().capitalize()

#Seleccion de nivel de estilo
 print ( "\n" + "-"*40 )
 print("    DEFINICIÓN DE SILUETA (OUFFIT)   ")
 print("-"*40)
 print("¿Qué nivel de ajuste buscas para tu imagen hoy?")
 print("1. Slim fit    -> Ajuste definido y apretado")
 print("2. Regular fit    -> El equilibrio clásico y versátil.")
 print("3. Relaxed fit    -> Comodidad moderna y holgada.")
 print("4. Structure fit   -> Máxima presensia y volumen visual.")

 estilo_de_hoy=input("\nSelecciona tu preferencia (1-4): ").strip()

 print(f"\n{'*'*50}")
 print(f" ¡Todo listo, {nombre}! Tus datos han sido registrados.")
 print(" Iniciando ánalisis de proporciones en el sistema...")
 print(f"{'*'*50}\n")

 return nombre, altura, sexo, peso, opcion_muneca, estilo_de_hoy
