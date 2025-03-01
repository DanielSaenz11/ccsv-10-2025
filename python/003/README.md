# Clase 3: Listas Avanzadas y Bucle `for`

## Métodos de Listas en Python

| Método | Descripción | Parámetros |
|--------|------------|------------|
| `append(x)` | Agrega un elemento al final de la lista. | `x`: elemento a agregar. |
| `clear()` | Elimina todos los elementos de la lista. | Ninguno |
| `copy()` | Devuelve una copia de la lista. | Ninguno |
| `count(x)` | Devuelve el número de veces que aparece un elemento en la lista. | `x`: valor a contar. |
| `extend(iterable)` | Agrega los elementos de un iterable (lista, tupla, conjunto) al final de la lista. | `iterable`: elementos a agregar. |
| `index(x [,start [,end]])` | Devuelve el índice de la primera aparición de un elemento. | `x`: elemento a buscar, `start` (opcional): inicio de búsqueda, `end` (opcional): fin de búsqueda. |
| `insert(i, x)` | Inserta un elemento en la posición especificada. | `i`: índice, `x`: elemento a insertar. |
| `pop([i])` | Elimina el elemento en la posición especificada y lo devuelve. Si no se especifica índice, elimina el último elemento. | `i` (opcional): índice a eliminar. |
| `remove(x)` | Elimina la primera aparición del valor especificado. | `x`: elemento a eliminar. |
| `reverse()` | Invierte el orden de la lista. | Ninguno |
| `sort([key [,reverse]])` | Ordena los elementos de la lista. | `key` (opcional): función de ordenación, `reverse` (opcional): `True` para orden descendente. |

## Slicing en Listas

El **slicing** permite extraer porciones de una lista sin modificar la original.

### Sintaxis de slicing

```python
lista[inicio:fin:paso]
```
- `inicio`: Índice donde comienza el corte (incluido).
- `fin`: Índice donde termina el corte (excluido).
- `paso`: Cada cuántos elementos seleccionar (opcional).

### Ejemplos de slicing

#### Extraer una porción de una lista
```python
numeros = [10, 20, 30, 40, 50, 60, 70]
sublista = numeros[1:5]  # Desde el índice 1 hasta el 4
print(sublista)
```

#### Obtener los primeros N elementos
```python
numeros = [1, 2, 3, 4, 5]
primeros_tres = numeros[:3]  # Desde el inicio hasta el índice 2
print(primeros_tres)
```


#### Obtener los últimos N elementos
```python
numeros = [1, 2, 3, 4, 5]
ultimos_tres = numeros[-3:]  # Desde el tercer último hasta el final
print(ultimos_tres)
```

#### Slicing con paso
```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = numeros[::2]  # Tomar cada segundo elemento
print(pares)
```

#### Invertir una lista con slicing
```python
numeros = [1, 2, 3, 4, 5]
invertida = numeros[::-1]  # Paso negativo para recorrer en reversa
print(invertida)
```

## Introducción al Bucle `for`

El bucle `for` en Python se utiliza para recorrer una secuencia (lista, tupla, conjunto, cadena de caracteres, entre otros).

### Sintaxis
```python
for elemento in secuencia:
    # Código a ejecutar en cada iteración
```

## Uso de `break` y `continue` en `for`

```python
for numero in range(10):
    if numero == 5:
        print("Se encontró el 5, deteniendo...")
        break
    print(numero)
```

```python
for numero in range(5):
    if numero == 2:
        continue  # Salta el número 2
    print(numero)
```

## Uso de `else` en `for`

```python
for numero in range(5):
    print(numero)
else:
    print("Bucle terminado correctamente.")
```

```python
for numero in range(5):
    print(numero)
    if numero == 2:
        break
else:
    print("Bucle terminado correctamente.")
```

## Bucles `for` anidados (`nested for loops`)

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
```

```python
for i in range(1, 6):
    print("*" * i)
```

