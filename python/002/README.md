# Clase 3: Estructuras de Control y Listas en Python

## Contenidos

### Condicionales (`if-elif-else`)

Los condicionales permiten tomar decisiones en un programa según una condición.

#### Ejemplo

```python
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

### Bucles (`while`)

El bucle `while` permite repetir acciones hasta que una condición deje de cumplirse.

#### Ejemplo: Validación de contraseña

```python
password = "python123"
intentos = 3

while intentos > 0:
    ingreso = input("Ingresa la contraseña: ")
    if ingreso == password:
        print("Acceso permitido.")
        break
    else:
        intentos -= 1
        print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")

if intentos == 0:
    print("Has agotado los intentos. Acceso denegado.")
```

### Listas en Python (`list`)

Las listas permiten almacenar múltiples valores en una sóla variable.

#### Ejemplo

```python
frutas = ["manzana", "banana", "cereza"]
print("Lista de frutas:", frutas)

# Acceder a elementos de la lista
print("Primera fruta:", frutas[0])

# Modificar un elemento
frutas[1] = "pera"
print("Lista actualizada:", frutas)

# Agregar un nuevo elemento
frutas.append("uva")
print("Lista con nueva fruta:", frutas)

# Eliminar un elemento
frutas.remove("cereza")
print("Lista después de eliminar cereza:", frutas)
```

