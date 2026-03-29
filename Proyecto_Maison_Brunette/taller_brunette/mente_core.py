#Se convoca las herramientas del corazon
from corazon_core import ropa_caracteristica
from corazon_core import ropa_caracteristica2

#se le dan herramientas 
ropa_caracteristica("camisa", "azul", 4)
ropa_caracteristica2("pantalon", "rojo", 11)

# se enseña que hacer con las herramientas
# Recuerda que se utilizan las llaves del diccionario (Keys)
def juzgar_ropa(mod1, mod2):
    suma= mod1["intensidad"] + mod2["intensidad"]
    if suma <= 10:
        return "Perfectos colores mi amor, este ouffit te quera super bien"
    else: 
        return "Busquemos otros colores, te parece?"
    
ropa1= ropa_caracteristica("camisa", "azul", 4)
ropa2= ropa_caracteristica2("pantalon", "negro", 0)

resultado= juzgar_ropa(ropa1 , ropa2)

print(resultado)