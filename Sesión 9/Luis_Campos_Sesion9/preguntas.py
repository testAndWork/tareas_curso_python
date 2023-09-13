preguntas = {
    "¿cual es el lugar mas frio de la tierra?":"La antartida",
    "¿Cual es el rio mas largo del mundo?":"Amazonas",
    "¿De que color es la bandera de El Salvador?":"Azul y Blanco",
    "¿Cual es la capital de El salvador?":"San Salvador",
}

puntos = 0 

for preguntas, respuestas in preguntas.items():
    print(preguntas)
    respuestas_correctas = input('Tu respusta:')

    if respuestas_correctas.lower() == respuestas.lower():
        print('Correcto!!!!')
        puntos += 1

    else: 
        print('Incorrecto, la respuesta es :',respuestas)
print(f'Fin del juego obtuviste {puntos} puntos')