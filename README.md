Este programa permite crear prácticas de vocabulario personalizadas.

# Cómo usar
## 1. Compilar el vocabulario
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
## 3. Copia y pega el código en `config.py`
Copia y pega el código generado por `convert.py` en `config.py`, sobrescribiendo cualquier contenido previo
## 4 ¡Listo!
La práctica ya está lista. Ejecuta `practice.py` para iniciar la práctica
