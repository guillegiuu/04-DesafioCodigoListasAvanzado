import os

print("Hello world from ...")
os.system("python --version")

# A Cada Tres Números:
"""
Crea una función llamada "cada_tres_numeros" que tenga un parámetro llamado "inicio".

La función debe devolver (return) una "lista" de cada tres números entre inicio y 100 (ambos inclusive). Por ejemplo, cada_tres_numeros(91) debe devolver la lista [91, 94, 97, 100]. Si "start" es mayor que 100, la función debe devolver una lista vacía.

1 - Definir la función para que acepte un parámetro para nuestro número inicial.

2 - Calcular los números entre el número inicial y 100 incrementándolos de 3 en 3.

3 - Almacenar los números en una lista.

4 - Devolver la lista.

Para convertir la secuencia de rangos en una lista, podemos pasarla a la función list().

"""
def cada_tres_numeros(inicio):
    if inicio > 100:
        return [] # Devuelve una "lista vacía []", si el número inicial es mayor que 100.

    numeros = list(range(inicio, 101, 3)) # Calcula los números entre el número inicial y 100, incrementándolos de 3 en 3.
    return numeros # Devuelve la lista de números.

inicio = 91 # Numero inicial.
resultado = cada_tres_numeros(inicio)
print(resultado)

"""
Resumen:

Define una función llamada "cada_tres_numeros" que toma un parámetro "inicio".
Comprueba si el número inicio es mayor que 100. Si lo es, devuelve una lista vacía []. Esto es para asegurarse de que la función solo trabaje con valores hasta 100.
Si "inicio" es válido (menor o igual a 100):
Genera una lista de números utilizando list(range(inicio, 101, 3)). Esta línea crea una secuencia de números que comienza desde inicio y avanza de 3 en 3 hasta llegar a 100.
Devuelve esta lista de números.

2)
Se asigna el valor 91 a la variable inicio.
Se llama a la función cada_tres_numeros con el valor de inicio como argumento.
La función es ejecutada y el resultado se almacena en la variable resultado.
Finalmente, se imprime el contenido de la variable resultado.

En resumen, este código define una función que genera una lista de números incrementados de 3 en 3, comenzando desde un número inicial dado hasta llegar a 100 (inclusive), siempre que el número inicial no sea mayor que 100. Luego, muestra la lista resultante cuando se llama a la función con inicio = 91.
"""

# B - Retirar el Centro:
"""

Crea una función llamada remove_middle que tenga tres parámetros llamados my_list, start y end.

La función debe devolver una lista en la que se hayan eliminado todos los elementos de mi_lista con un índice comprendido entre inicio y fin (ambos inclusive).

1 - Defina la función para que acepte tres parámetros: "mi_lista", "índice" y "índice_final".

2 - Obtener todos los elementos antes del índice inicial, en una variable.

3 - Obtener todos los elementos después del índice final, en una variable.

4 - Obtener todos los elementos después del índice final, en una variable.

5 - Combinar las dos listas parciales en una nueva variable.

6 - Devolver el resultado.

"""
def quitar_centro(mi_lista, indice, indice_final):
    elementos_antes = mi_lista[:indice]
    elementos_despues = mi_lista[indice_final + 1:]
    resultado = elementos_antes + elementos_despues
    return resultado
    
print(quitar_centro([4, 8, 15, 16, 23, 42], 1, 3))

"""
Resumen:

Recibiendo la lista y los índices:
La función toma tres argumentos: la lista mi_lista y los índices indice e indice_final.

Extracción de elementos antes y después del rango a eliminar:
"elementos_antes" toma todos los elementos desde el principio de la lista hasta el índice indice, pero excluyendo el elemento en el índice "indice".

"elementos_despues" toma todos los elementos desde el índice indice_final + 1 hasta el final de la lista.

Eliminación del rango y obtención del resultado:
La variable "resultado se convierte en una nueva lista que contiene todos los elementos antes del rango a eliminar (elementos_antes) concatenados con todos los elementos después del rango (elementos_despues). Esta concatenación efectivamente elimina el rango especificado.
"""

# C Artículo Más Frecuente
"""
Crea una función llamada "elemento_más_frecuente" que tenga tres parámetros llamados: A) mi_lista, B) elemento1 y C) elemento2.

Devuelve elemento1 o elemento2 dependiendo de qué elemento aparece más a menudo en mi_lista.

Si los dos elementos aparecen el mismo número de veces, devuelve elemento1.

1 - Define la función para que acepte tres parámetros: A) la lista, B) primer elemento y C) segundo elemento.

2 - Contar el número de veces que el elemento1 aparece en nuestra lista.

3 - Contar el número de veces que el elemento2 aparece en nuestra lista.

4 - Devuelve el elemento que aparece con más frecuencia en mi_lista - si ambos elementos aparecen el mismo número de veces, devuelve el elemento1.

"""

def elemento_mas_frecuente(mi_lista, elemento1, elemento2):
    # Cuenta cuántas veces aparece cada elemento en la lista
    num_1 = mi_lista.count(elemento1)
    num_2 = mi_lista.count(elemento2)
    # Compara los recuentos y devuelve el elemento más frecuente
    if num_1 > num_2: # A
        return elemento1
    elif num_1 == num_2: # B
        return elemento1
    else: # C
        return elemento2

# Prueba la función con una lista y elementos de ejemplo
print(elemento_mas_frecuente([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

"""
Resumen:
Este código define una función llamada "elemento_mas_frecuente" que toma una lista (mi_lista) y dos elementos (elemento1 y elemento2). Lo que hace la función es contar cuántas veces aparece cada uno de los dos elementos en la lista y luego devuelve el elemento que aparece con más frecuencia.
"""

# D Doble índice
"""
Crea una función llamada "doble_índice" que tenga dos parámetros: A) una lista llamada mi_lista y B) un único número llamado índice.

La función debe devolver (return) una nueva lista donde todos los elementos son los mismos que en mi_lista excepto el elemento en el índice. El elemento en el índice debe ser el doble del valor del elemento en el índice de mi_lista original.

1 - Define la función para que acepte dos parámetros, uno para la lista y otro para el índice del valor que vamos a duplicar.

2 - Comprueba si el índice no es válido. Si no es válido, devuelve la lista original.

3 - Si el índice es válido, obtiene todos los valores hasta el índice y los almacena como una nueva lista.

4 - Añade el valor del índice multiplicado por 2 a la nueva lista.

"""
def doble_indice(mi_lista, indice):
    if indice >= len(mi_lista):
        return mi_lista # Si el índice es inválido, devuelve la lista original
    else:
        valores_hasta_indice = mi_lista[:indice] # Obtiene los valores hasta el índice
        valores_hasta_indice.append(mi_lista[indice] * 2) # Añade el valor del índice multiplicado por 2
        valores_hasta_indice = valores_hasta_indice + mi_lista[indice + 1:] 
        return valores_hasta_indice # Devuelve la nueva lista
    

print(doble_indice([3, 8, -10, 12], 2))

"""
Resumen:
Esto define una función llamada "doble_indice" que toma dos argumentos: mi_lista, que es la lista de números, y indice, que es el índice que se quiere modificar.

Verificación del índice:
Esta parte verifica si el índice proporcionado (indice) es mayor o igual que la longitud de la lista (len(mi_lista)). Si el índice es mayor o igual al tamaño de la lista, significa que el índice es inválido y la función devuelve la lista original.

Procesamiento si el índice es válido:
Si el índice es válido, se ejecuta esta parte del código:

A) valores_hasta_indice = mi_lista[:indice]: Crea una nueva lista (valores_hasta_indice) que contiene los elementos de mi_lista desde el inicio hasta el índice especificado, sin incluir el elemento en el índice.

B) valores_hasta_indice.append(mi_lista[indice] * 2): Añade a la lista valores_hasta_indice el elemento en la posición del índice multiplicado por 2.

C) valores_hasta_indice = valores_hasta_indice + mi_lista[indice + 1:]: Une la lista valores_hasta_indice con los elementos de mi_lista que están después del elemento en el índice, creando así una lista que contiene todos los elementos hasta el índice dado, con el valor en esa posición duplicado.

D) return valores_hasta_indice: Devuelve la nueva lista con los elementos originales hasta el índice dado, pero con el valor en esa posición duplicado.
"""

