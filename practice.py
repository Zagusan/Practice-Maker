import config
import random
import time
from datetime import timedelta

data = config.datos
categories = config.categorias

print(config.instrucciones)
print("¿Estás listo/a? Y/n")

match str(input()).lower():
    case "sí" | "si" | "y" | "yes" | "sim" | "s":
        pass
    case "n" | "no" | "não" | "nao":
        print("¡Hasta la próxima!")
        time.sleep(2)
        exit()
    case _:
        print("No entendí así que voy a asumir que eso es un sí")

print(f'\n{random.choice(config.consejos)}\n')

def check_answer(response, answers: list[str], i):
    split_answers = answers[i].split("/")
    correct = False

    for answer in split_answers:
        if response == answer:
            correct = True

    # \033[A mueve el cursor a la línea superior, \r al inicio y \033[nC lo mueve hacia adelante n cantidad de caracteres
    print("\033[A\r" + f'\033[{categories[i].__len__() + len(response)}C', end="")
    if correct:
        print(" ✓")
    else:
        print(" ✗")
        print("===============================")
        print(f'La respuesta es {answers[i].capitalize()}')
        print("===============================")
    return correct

startTime = time.time()

mistakes = {}

def begin_round():
    global data

    practice_length = data.__len__()
    progress = 0
    correct_responses = 0

    data = list(data.items())
    random.shuffle(data)

    print("===============================")
    print("3..")
    time.sleep(1)
    print("2..")
    time.sleep(1)
    print("1..")
    time.sleep(1)
    print("¡Ya!")
    print("===============================\n")

    for word, answers in data:
        progress += 1
        print(f'{progress}/{practice_length}')

        print(word.capitalize())

        all_correct = True
        previous_line = word
        for i in range(categories.__len__()):
            cat = categories[i]
            print(cat, end="")

            response = input().lower()
            if response == ".":
                response = previous_line
                print(f'\033[A\r{cat}{response}')


            if check_answer(response, answers, i):
                correct_responses += 1
            else:
                all_correct = False
            previous_line = response
        
        if not all_correct:
            if word not in mistakes:
                mistakes[word] = answers

        # print("Past tense: ", end="")
        # if check_past_answer(i, input().lower()):
        #     correct_responses += 1
        # else:
        #     mistakes_infinitives.append(infinitives[i])
        #     mistakes_past.append(past[i])
        #     mistakes_participles.append(participles[i])

        # print("Participle: ", end="")
        # if check_participle_answer(i, input().lower()):
        #     correct_responses += 1
        # elif mistakes_infinitives.__len__() < 1 or mistakes_infinitives[-1] != infinitives[i]:
        #     mistakes_infinitives.append(infinitives[i])
        #     mistakes_past.append(past[i])
        #     mistakes_participles.append(participles[i])

        # infinitives.pop(i)
        # past.pop(i)
        # participles.pop(i)
        print()
    
    formattedTime = timedelta(seconds=(time.time() - startTime))

    total_length = categories.__len__() * practice_length
    total_mistakes = total_length - correct_responses

    print("===============================")
    print(f'Tiempo total: {(str(formattedTime.days) + ":") if formattedTime.days > 0 else ""}{(str(formattedTime.seconds // 3600) + ":") if formattedTime.seconds // 3600 > 0 else ""}{formattedTime.seconds // 60}:{formattedTime.seconds % 60}')
    print(f'Respuestas Correctas: {correct_responses}/{total_length}')
    print(f'Errores: {total_mistakes}')
    print(f'Precisión: {round(correct_responses / total_length * 100)}%')
    print("===============================\n")

begin_round()

if mistakes.__len__() < 1:
    print("Wow! :O")
    time.sleep(2)
    print("¡No tienes errores!")
    time.sleep(1)
    print("No habrá ronda de repaso ╰(*°▽°*)╯")
    time.sleep(3)
    exit()

while mistakes.__len__() > 0:
    data = mistakes
    mistakes = {}

    print("\nLa próxima ronda te permitirá corregir tus errores.")
    print("¿Deseas continuar? Y/n")
    match str(input()).lower():
        case "sí" | "si" | "y" | "yes" | "sim" | "s":
            pass
        case "n" | "no" | "não" | "nao":
            print("¡Hasta la próxima!")
            time.sleep(2)
            exit()
        case _:
            print("No entendí así que voy a asumir que eso es un sí")

    begin_round()

print("¡Felicidades! Has terminado la práctica y respondido a todo correctamente.")
input()