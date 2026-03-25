#El calculador de descuentos premium
precio_original= 250 
descuento_porcentaje= 15

ahorro= precio_original//10 * (descuento_porcentaje/ 10)
precio_final= precio_original-ahorro

resultado= (f"¡El precio era de {precio_original} y te ahorraste {ahorro}$ asi que obtuviste ese pantalon por solo {precio_final}$")
print(resultado)