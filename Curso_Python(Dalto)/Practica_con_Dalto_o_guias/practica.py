texto = "progrmr"
for letra in texto:
    if letra == "a":
        continue  # Salta las letras 'a'
    print(letra)
else:
    print("Bucle finalizado sin interrupciones")