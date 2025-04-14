# Fundamentos de Programación: Python, Tipos de Datos, Operadores y Estructuras de Control

---

## ¿Qué es Python?  
Python es un **lenguaje de programación de alto nivel** conocido por su sintaxis simple, legible y cercana al lenguaje humano. Fue creado por **Guido van Rossum** a finales de los años 1980 y lanzado públicamente en **1991**. Su diseño prioriza la **facilidad de uso** y la **productividad**.  

## Características Principales  

### 1. **Interpretado**  
   - No requiere compilación previa: el código se ejecuta directamente mediante un intérprete.  
   - Ventajas:  
     - Desarrollo más rápido (sin pasos intermedios).  
     - Portabilidad (funciona en múltiples sistemas sin modificaciones).  
     - Facilidad para depurar errores.  
### 2. **Alto Nivel**  
   - Abstracón del hardware: no maneja detalles complejos como el lenguaje máquina (binario).  
   - Sintaxis intuitiva, similar al inglés.  
### 3. **Propósito General**  
   - Versatilidad: aplicable en diversos campos:  
     - **Web** (frameworks como Django, Reflex).  
     - **Ciencia de Datos** (bibliotecas como Pandas, NumPy).  
     - **IA y Machine Learning** (TensorFlow, PyTorch).  
     - **Videojuegos** (Pygame).  
     - **Automatización y scripting**.  
### 4. **Multiparadigma**  
   - Soporta múltiples estilos de programación:  
     - **Orientado a Objetos (POO)**.  
     - **Funcional** (funciones como `map()`, `filter()`).  
     - **Imperativo** (instrucciones secuenciales).  
### 5. **Multiplataforma**  
   - Compatible con **Windows, Linux, macOS** y otros sistemas operativos.  
### 6. **Gran Comunidad y Ecosistema**  
   - Miles de bibliotecas y frameworks disponibles (`pip` como gestor de paquetes).  
   - Comunidad activa con recursos como foros, tutoriales y conferencias (PyCon).  


## Filosofía de Python (Los 4 Pilares)  

1. **Legibilidad y Simplicidad**  
   - Código claro y comprensible "como un texto en inglés".  
   - Uso de indentación (sangría) para estructurar el código.  
2. **Código Abierto**  
   - Proyecto de libre acceso y colaborativo (licencia **PSFL**).  
3. **Productividad**  
   - Ideal para prototipado rápido y tareas cotidianas.  
   - Menos líneas de código vs. lenguajes como C++ o Java.  
4. **Equilibrio entre Facilidad y Poder**  
   - Simple para principiantes, pero robusto para proyectos complejos.  


## Desventajas  

1. **Rendimiento**  
   - Al ser interpretado, es **más lento** que lenguajes compilados (C, Rust).  
   - Soluciones: integración con C o uso de herramientas como **Cython**.  
2. **Multihilo Limitado**  
   - Debido al **GIL (Global Interpreter Lock)**, el multihilo no es óptimo para tareas CPU-intensivas.  
3. **Consumo de Memoria**  
   - Mayor uso de recursos vs. lenguajes de bajo nivel.  
4. **Bibliotecas Inmaduras**  
   - Algunos paquetes de nicho pueden estar poco mantenidos o desactualizados.  

---
# Tipos de datos
## Introducción
Los tipos de datos son el fundamento de todo lenguaje de programación. Determinan la naturaleza de la información, cómo se almacena, qué operaciones permite y cómo se comporta a nivel de memoria.

## 1. Tipos de Datos Primitivos (Primarios)
Son los tipos más básicos, nativamente soportados por los lenguajes. Representan valores simples.

### 🔢 Tipos Numéricos
#### 📌 Enteros (`int`, `Integer`)
Los enteros representan **números sin parte decimal**, como `5`, `0` o `-42`.  
- **Rango común en 32 bits**: desde `-2,147,483,648` hasta `2,147,483,647`
- **Variantes**:
  - `short`, `long`: dependiendo de la cantidad de bits y el rango requerido
  - `unsigned`: versión sin signo, solo valores positivos (mayor rango positivo)

#### 📌 Punto Flotante (`float`, `double`)
Se usan para representar **números reales con decimales**.  
- **`float`**: precisión simple (~6 a 9 dígitos, 32 bits)  
- **`double`**: precisión doble (~15 a 17 dígitos, 64 bits)

#### 📌 Tipos Numéricos Especializados
| Tipo         | Lenguajes         | Uso                          |
|--------------|-------------------|------------------------------|
| `decimal`    | Python, C#        | Finanzas (alta precisión)    |
| `complex`    | Python, MATLAB    | Cálculo numérico avanzado    |
| `BigInteger` | Java, .NET        | Criptografía, grandes valores|

### 🔡 Texto
📌 Cadenas de texto (`string`)
Son **secuencias de caracteres** y se utilizan para representar palabras, frases o cualquier texto.  
- **Codificación común**: Unicode (UTF-8 o UTF-16)
- **Operaciones comunes**: concatenación, comparación, búsqueda, extracción de subcadenas (substring)

> 🔁 **Dato útil**: En algunos lenguajes como C o Java, las cadenas están compuestas por múltiples `char`.

### 📌 Caracteres (`char`)
Representa un **único símbolo o carácter**, como `'a'`, `'9'` o `'%'`.  
- Tamaño típico: **1 byte** (ASCII) o **2 bytes** (Unicode)
- Útil para manipular texto a nivel de carácter individual (por ejemplo, recorrer letra por letra una palabra)

> 💡 Aunque `char` puede parecer un tipo independiente, muchas veces es la **unidad básica** a partir de la cual se forman las cadenas (`string`).

### ✅ Booleanos (`bool`)
- **Valores posibles**: `true` o `false`
- **Representación interna**: Aunque conceptualmente es 1 bit, suele ocupar 1 byte por eficiencia
- **Uso típico**: Condicionales, validaciones lógicas, control de flujo

#### 🕳️ Valores Nulos
Representan **la ausencia de un valor** o el hecho de que una variable aún no ha sido definida.

| Lenguaje    | Valor nulo        |
|-------------|-------------------|
| Java, C#    | `null`            |
| Python      | `None`            |
| JavaScript  | `null`, `undefined` |

> 🔐 **Buena práctica**: Siempre validar si una variable es nula antes de operar con ella, para evitar errores de ejecución (como `NullPointerException` en Java).


## 2. Tipos de Datos Compuestos (Estructurados)
Tipos que agrupan múltiples valores, homogéneos o heterogéneos.

### 🔁 Colecciones Secuenciales

| Tipo     | Mutabilidad | Orden | Duplicados | Acceso             |
|----------|-------------|-------|------------|--------------------|
| Arreglo  | No          | Sí    | Sí         | Por índice         |
| Lista    | Sí          | Sí    | Sí         | Índice, iteración  |
| Tupla    | No          | Sí    | Sí         | Por posición       |

### 🗃️ Colecciones No Secuenciales

#### Conjuntos (`Set`)
- **Propiedades**: Elementos únicos, sin orden
- **Implementaciones**: HashSet, TreeSet (ordenado)

#### Diccionarios (`Map`, `Dict`)
- **Estructura**: Pares clave-valor
- **Acceso eficiente**: Generalmente O(1) con tablas hash
- **Sin duplicación de claves**

## 3. Tipos Abstractos de Datos (TAD)
Modelos lógicos implementados sobre tipos básicos. No son nativos de los lenguajes pero se usan ampliamente.

### 🧮 Estructuras Lineales

| Estructura | Orden     | Operaciones básicas     | Uso común                  |
|------------|-----------|--------------------------|----------------------------|
| Pila       | LIFO      | `push()`, `pop()`        | Call stack, deshacer       |
| Cola       | FIFO      | `enqueue()`, `dequeue()` | Impresoras, procesamiento por turnos |
| Lista enlazada | Secuencial | Inserciones, eliminaciones | Navegadores, estructuras dinámicas |

### 🌳 Estructuras Jerárquicas

#### Árboles
- **Uso**: Representar relaciones padre-hijo
- **Variantes comunes**:
  - Árbol binario de búsqueda (ABB)
  - AVL (autobalanceado)
  - Heap (prioridades)

#### Grafos
- **Descripción**: Colección de nodos conectados por aristas
- **Representaciones**: Matriz de adyacencia, lista de adyacencia
- **Algoritmos comunes**: Dijkstra, BFS, DFS

---
# Operadores y Expresiones
## Introducción
Los **operadores** son símbolos o palabras clave que permiten realizar operaciones sobre variables y valores. Son esenciales para escribir expresiones, tomar decisiones, realizar cálculos y manipular datos. Aunque su sintaxis puede variar ligeramente entre lenguajes, su función suele ser similar.

## 1. Operadores Aritméticos

Permiten realizar operaciones matemáticas básicas.

| Operador | Descripción        | Ejemplo       |
|----------|--------------------|---------------|
| `+`      | Suma               | `a + b`       |
| `-`      | Resta              | `a - b`       |
| `*`      | Multiplicación     | `a * b`       |
| `/`      | División (real)    | `a / b`       |
| `//`     | División entera    | `a // b` (Python) |
| `%`      | Módulo (resto)     | `a % b`       |
| `**`     | Potencia           | `a ** b` (Python) |
| `^`      | Potencia o XOR     | Depende del lenguaje |

> ⚠️ En algunos lenguajes como C/C++, `^` representa una operación lógica XOR, no potencia.

## 2. Operadores de Asignación

Usados para asignar o actualizar valores.

| Operador | Descripción                  | Ejemplo       |
|----------|------------------------------|---------------|
| `=`      | Asignación simple            | `x = 5`       |
| `+=`     | Suma y asignación            | `x += 2` → `x = x + 2` |
| `-=`     | Resta y asignación           | `x -= 3`      |
| `*=`     | Multiplicación y asignación  | `x *= 4`      |
| `/=`     | División y asignación        | `x /= 2`      |
| `%=`     | Módulo y asignación          | `x %= 3`      |

## 3. Operadores de Comparación (Relacionales)

Comparan valores y devuelven un valor booleano (`true` o `false`).

| Operador | Significado             | Ejemplo        |
|----------|--------------------------|----------------|
| `==`     | Igual a                  | `a == b`       |
| `!=`     | Distinto de              | `a != b`       |
| `>`      | Mayor que                | `a > b`        |
| `<`      | Menor que                | `a < b`        |
| `>=`     | Mayor o igual que        | `a >= b`       |
| `<=`     | Menor o igual que        | `a <= b`       |

> 💡 Algunos lenguajes como Python y JavaScript también permiten comparar cadenas o fechas con estos operadores.

## 4. Operadores Lógicos

Se utilizan para combinar expresiones booleanas.

| Operador | Descripción     | Ejemplo             |
|----------|------------------|---------------------|
| `&&`     | AND (y lógico)   | `cond1 && cond2` (C/Java/JS) |
| `||`     | OR (o lógico)    | `cond1 || cond2`             |
| `!`      | NOT (negación)   | `!cond`                     |
| `and`    | AND lógico       | `cond1 and cond2` (Python)  |
| `or`     | OR lógico        | `cond1 or cond2`            |
| `not`    | Negación lógica  | `not cond`                  |

## 5. Operadores Bit a Bit (Bitwise)

Trabajan a nivel de bits. Usados en programación de bajo nivel, sistemas embebidos, criptografía, etc.

| Operador | Descripción        | Ejemplo   |
|----------|--------------------|-----------|
| `&`      | AND bit a bit      | `a & b`   |
| `|`      | OR bit a bit       | `a | b`   |
| `^`      | XOR bit a bit      | `a ^ b`   |
| `~`      | NOT bit a bit      | `~a`      |
| `<<`     | Desplazamiento izq | `a << 1`  |
| `>>`     | Desplazamiento der | `a >> 1`  |

> 🛠️ Muy usados en manipulación de flags y optimización de operaciones matemáticas.

## 6. Operadores de Identidad y Pertenencia (en lenguajes dinámicos)

### Identidad (Python)

| Operador | Significado        | Ejemplo        |
|----------|--------------------|----------------|
| `is`     | Mismo objeto       | `a is b`       |
| `is not` | Objeto distinto    | `a is not b`   |

### Pertenencia (Python, JavaScript)

| Operador | Significado             | Ejemplo           |
|----------|--------------------------|-------------------|
| `in`     | Contenido en colección  | `'x' in lista`    |
| `not in` | No contenido             | `'z' not in texto`|


## 7. Operadores Ternarios / Condicionales

Permiten realizar una evaluación condicional en una sola línea.

- **Sintaxis general** (lenguajes C-like):  
  `condición ? valor_si_verdadero : valor_si_falso`
- **Python**:  
  `valor_si_verdadero if condición else valor_si_falso`

## 8. Operadores Especiales (por lenguaje)

| Operador        | Lenguaje     | Uso                             |
|-----------------|--------------|----------------------------------|
| `??`            | C#, JS       | Coalescencia nula (valor por defecto) |
| `?:`            | C/C++, Java  | Ternario condicional             |
| `===`, `!==`    | JavaScript   | Comparación estricta (valor y tipo) |
| `=>`            | JS, C#       | Funciones lambda / expresiones flecha |
| `as`, `instanceof` | Python, Java | Conversión / verificación de tipo |

---
# Estructuras de Control
## Introducción
Las **estructuras de control** permiten modificar el flujo de ejecución de un programa. Gracias a ellas, podemos tomar decisiones, repetir acciones y reaccionar ante condiciones dinámicas. Se dividen en dos grandes grupos:

- **Condicionales**: Permiten tomar decisiones.
- **Repetitivas**: Permiten ejecutar bloques múltiples veces.

Estas estructuras están presentes en prácticamente todos los lenguajes de programación, aunque con ligeras variaciones en la sintaxis.

## 1. Estructuras Condicionales

Permiten ejecutar ciertos bloques de código si se cumple una condición lógica.

### 🔹 if / else

- **Función**: Evalúa una condición y ejecuta un bloque si es verdadera; puede tener una alternativa para el caso falso.

| Estructura      | Descripción                         |
|----------------|-------------------------------------|
| `if`           | Ejecuta si la condición es verdadera |
| `else`         | Alternativa si `if` no se cumple     |
| `else if` / `elif` | Otras condiciones posibles        |

> 💡 En Python se usa `elif` en lugar de `else if`.

### 🔹 switch / match

- **Función**: Permite evaluar una expresión contra múltiples valores posibles, como alternativa a múltiples `if-else`.

| Lenguaje     | Palabra clave  |
|--------------|----------------|
| C, Java      | `switch`       |
| Python (3.10+)| `match`       |
| JavaScript   | `switch`       |

> ⚠️ En muchos lenguajes, es necesario un `break` para evitar ejecutar todos los casos siguientes.

## 2. Estructuras Repetitivas (Bucles)

Permiten ejecutar un bloque de código varias veces, ya sea mientras se cumple una condición o para recorrer estructuras de datos.

### 🔁 while

- **Función**: Repite un bloque mientras una condición sea verdadera.
- **Uso típico**: Cuando no se conoce de antemano cuántas repeticiones serán necesarias.

### 🔁 do...while

- **Función**: Igual que `while`, pero garantiza al menos una ejecución porque la condición se evalúa **después** del bloque.
- **Presente en**: C, C++, Java, JavaScript

> ⚠️ No existe en Python, aunque se puede simular.

### 🔁 for

- **Función**: Repite un bloque un número determinado de veces o sobre los elementos de una colección.
- **Dos variantes comunes**:
  - **Basado en contador**: `for (i = 0; i < n; i++)`
  - **Basado en colección**: `for item in lista`

| Lenguaje     | Variante basada en colección     |
|--------------|----------------------------------|
| Python       | `for elemento in iterable`       |
| JavaScript   | `for...of`, `for...in`           |
| Java         | `for (tipo var : colección)`     |

### 🔁 foreach (lectura secuencial)

- **Función**: Itera sobre los elementos de una colección sin necesidad de usar índices manuales.
- **Presente en**: Java, C#, PHP, Python (como `for-in`)

## 3. Palabras Clave de Control de Flujo
Permiten alterar el comportamiento interno de los bucles y condicionales.

| Palabra clave | Función                                      |
|---------------|----------------------------------------------|
| `break`       | Sale inmediatamente del bucle                |
| `continue`    | Salta a la siguiente iteración               |
| `return`      | Sale de una función (opcionalmente con valor)|
| `pass`        | (Python) No hace nada; útil como placeholder |

## 5. Buenas Prácticas

1. **Evitar bucles infinitos**:
   - Siempre asegurarse de que las condiciones cambien eventualmente.
2. **Usar `break` y `continue` con criterio**:
   - Mejoran la legibilidad, pero su uso excesivo puede confundir.
3. **Elegir la estructura adecuada**:
   - `for`: cuando se conoce la cantidad de repeticiones.
   - `while`: cuando la condición depende de algo externo.
4. **Evitar estructuras anidadas complejas**:
   - Dividir en funciones o aplicar lógica más clara.
5. **Usar `match` / `switch` para múltiples condiciones comparativas**:
   - Mejora la legibilidad respecto a múltiples `if`.
