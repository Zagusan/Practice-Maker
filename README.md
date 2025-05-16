Este programa permite crear prácticas de vocabulario personalizadas.

# Cómo usar
## 1. Descargar Python
Este programa requiere Python 3.13. Se puede descargar en <https://www.python.org/downloads/>
## 2. Compilar el vocabulario
Primero, se requieren tener las listas con los verbos y las respuestas de lo que se solicita, con cada elemento separado por comas
### Verbos
```
abide, arise, awake, is ...
```
### Respuestas del "Past tense"
```
abode/abided, arose, awoke, was
```
### Respuestas del "Participle"
```
abode/abided, arisen, awoken, been
```
Para indicar que hay varias respuestas correctas, se usa un "/"
## 2. Ejecutar `convert.py`
Este programa formateará los verbos y las respuestas de manera apropiada. Responde a lo que el programa solicita
### Instrucciones
Este es un mensaje que aparece todas las veces que se inicia la práctica e indican qué se debe de hacer en la práctica
```
A continuación, un verbo irregular en inglés aparecerá en pantalla. Deberás responder correctamente y en la menor cantidad de tiempo posible.
```
### Categorías
Esto es lo que se le pedirá al usuario que responda para cada palabra
```
Pretérito perfecto, Participio en pasado
```
### Verbos
Primero, el programa te pedirá la lista de verbos en infinitivo, como se ejemplificó anteriormente. Asimismo, para cada categoría, te pedirá las respuestas de esta
## 3. Copia y pega el código en `config.py`
Copia y pega el código generado por `convert.py` en `config.py`, sobrescribiendo cualquier contenido previo
## 4. Toques finales
Es recomendado revisar y ajustar `config.py` manualmente para verificar que esté todo en orden y hacer cualquier otro cambio necesario
## 4 ¡Listo!
La práctica ya está lista. Ejecuta `practice.py` para iniciar la práctica
