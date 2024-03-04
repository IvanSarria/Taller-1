palabra = input("Digite la cadena que desea ordenar alfabeticamente: ")
def devolver_cadena(palabra):
    chart = list(set(palabra))
    chart.sort()
    palabra_ordenada = "".join(chart)
    return palabra_ordenada
print(f"La cadena ordenada alfabeticamente sin duplicados es: {devolver_cadena(palabra)}")

