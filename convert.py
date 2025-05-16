
print("Este programa te ayudará a crear tu propia práctica. Responde a lo que se te solicita, y presiona Enter/Intro para continuar.")
print("Escribe las instrucciones de la práctica.")
instructions = input()

print("\nAhora, introduce las categorías sobre las cuales quieres preguntar, separadas por comas.")
print("Por ejemplo: Categoría 1, Categoría 2, Categoría 3...")
categories = input()

categories = categories.replace("\"", "")
categories = categories.replace("\'", "")

categories = categories.split(",")

categories = [cat.removeprefix(" ") for cat in categories]
print("\nSeguidamente, introduce las palabras sobre las cuales deseas preguntar, separadas por comas.")
print("Por ejemplo: Hola, Saludos, Bienvenido...")
words = input()

words = words.replace(" ", "")
words = words.replace("\"", "")
words = words.replace("\'", "")

words = words.split(",")

data = {

}
for cat in categories:
    print(f'\nIntroduce las respuestas para la categoría \"{cat}\", separadas por comas')
    print("Utiliza un \"/\" para indicar varias respuestas correctas.")
    answers = input()

    answers = answers.replace(" ", "")
    answers = answers.replace(" ", "")
    answers = answers.replace("\"", "")
    answers = answers.replace("\'", "")

    answers = answers.split(",")

    for i in range(words.__len__()):
        ans = answers[i]
        if not ans: continue
        word = words[i]

        if word not in data:
            data[word] = []
        data[word].append(ans)

categories = [cat + ": " for cat in categories]

print("===============================")
print(f'''
# El 1er mensaje que muestra la aplicación
instrucciones = \"{instructions}\"

# Todos los posibles consejos que el programa puede dar al principio.
consejos = [
    "Pro tip: Presiona Ctrl + C para terminar la práctica en cualquier momento",
    "Pro tip: Presiona ⊞ Windows + Ctrl + ⇧ Shift + Alt + L si ocupas revisar LinkedIn",
    "Pro tip: Puedes escribir solamente \\\".\\\" si quieres introducir la línea previa como respuesta",
    "Pro tip: Venus es el planeta más caliente del sistema solar",
    "Pro tip: Si te sientes frustrado, toma un descanso de 5 minutos antes de continuar",
    "Pro tip: Me quedé sin consejos que dar. ¡Buena suerte! ^_^"
]

# Aquí va lo que se le solicita al usuario
# Se vincula a las respuestas por posición, entonces si tengo una pregunta en categorias[1],
# esta se vincula con datos[dato][1].
categorias = {str(categories)}

# Aquí se especifican las preguntas y respuestas con el formato:
# {{"dato": ["respuesta1", "respuesta2" ...]}}
datos = {str(data).replace("{", "{\n").replace("],", "],\n").replace("]}", "]\n}")}
''')
print("===============================")
print("Copia y pega el código de arriba en \"config.py\"")
input()