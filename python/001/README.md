
# Clase 2

## Concatenación de Strings

La __concatenación__ de strings es la unión de dos o más cadenas de texto.

### Métodos de concatenación:

1. **Uso del operador `+`**:
   - Se puede usar `+` para unir dos cadenas de texto.
   - Se debe agregar un espacio manualmente si es necesario.

```python
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido
print("Tu nombre completo es: " + nombre_completo)
```

2. **Uso de `f-strings`** (Python 3.6):
   - Permite insertar variables dentro de un string de manera más sencilla.

```python
nombre = "Ana"
edad = 17
print(f"Hola, {nombre}, tienes {edad} años.")
```

### Reglas y restricciones:

- **Permitido:**
    - Concatenar únicamente `str + str`.
    - Usar `f-strings` para evitar conversiones manuales.

- **No permitido:**
    - Concatenar un `str` con un número directamente. Esto genera un error.

Ejemplo **incorrecto**:
```python
edad = 20
print("Tienes " + edad + " años.")  # Error
```

Ejecución correcta:
```python
edad = 20
print("Tienes " + str(edad) + " años.")  # Convertimos el número a string
```


## Operadores Matemáticos en Python

Python permite realizar operaciones matemáticas básicas con los siguientes operadores:

| Operador | Descripción        | Ejemplo (`a = 10, b = 3`) | Resultado |
|----------|--------------------|--------------------------|-----------|
| `+`      | Suma               | `a + b`                  | `13`      |
| `-`      | Resta              | `a - b`                  | `7`       |
| `*`      | Multiplicación      | `a * b`                  | `30`      |
| `/`      | División (decimal)  | `a / b`                  | `3.3333`  |
| `//`     | División entera     | `a // b`                 | `3`       |
| `%`      | Módulo (residuo)    | `a % b`                  | `1`       |
| `**`     | Potencia           | `a ** b`                 | `1000`    |

### Ejemplo:

```python
# Se convierten las entradas de string a int para operar con ellas
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

suma = num1 + num2
print(f"La suma de {num1} y {num2} es {suma}")
```

### Reglas y restricciones:

- **Permitido:**
    - Operar solo entre números (`int` o `float`).
    - Usar `//` si se quiere obtener solo la parte entera de una división.

- **No permitido:**
    - Dividir entre `0`. Esto genera un error.
    - Intentar operar un número con un string sin conversión previa.

## Importante: `input()` siempre devuelve un string

Cuando usamos `input()`, **Python siempre devuelve un string (`str`)**, sin importar si el usuario ingresa un número.

```python
dato = input("Escribe un número: ")
print(type(dato))  # Siempre será <class 'str'>
```

Para usar números, debemos convertirlos por medio de _type casting_:

```python
num1 = int(input("Ingresa un número entero: "))
num2 = float(input("Ingresa un número decimal: "))

resultado = num1 + num2
print(f"La suma es: {resultado}")
```

## Programa Final: Calculadora Sencilla

Vamos a combinar `print()`, `input()`, concatenación de strings y operadores matemáticos para crear una **calculadora básica**.

```python
print("¡Bienvenido a la calculadora sencilla!")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir entre cero"

print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multiplicacion}")
print(f"La división es: {division}")
```

