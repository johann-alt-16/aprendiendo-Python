
def calcular_imc_y_estilo(peso,altura):

 imc= peso / (altura**2)

 if imc < 18.5:
   recomendacion_fit = "Slim fit"
   categoria= "Delgada"

 elif 18.5 <= imc < 25:
   recomendacion_fit= "Regular fit"
   categoria= "Atletica"

 elif 25<= imc <30:
   recomendacion_fit="Relaxed fit"
   categoria="Robusta"

 else:
   recomendacion_fit= "Structure fit"
   categoria= "Grande"

 return round(imc , 2), recomendacion_fit, categoria


def calcular_medida_osea(opcion, altura):
   diccionario_de_medidas={
      "A": 0.22, # Estructura pequeña
      "B": 0.25, # Estructura media
      "C": 0.28  # Estructura grande
    }
   multiplicador= diccionario_de_medidas.get(opcion.upper(), 0.25)
   resultado= altura * multiplicador
   return round(resultado, 2)


def calcular_proporcion_prenda(altura, estilo_elegido):
  """ calcula el largo ideal de la prenda en centimetros"""
  reglas_estilo={
    "1": 0.38, 
    "2": 0.40,
    "3": 0.42,
    "4": 0.45
  }

  porcentaje= reglas_estilo.get(estilo_elegido, 0.40)
  largo_cm= (altura *100) * porcentaje

  return round(largo_cm, 1)