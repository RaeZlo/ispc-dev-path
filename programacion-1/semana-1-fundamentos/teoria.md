# ¿Qué es Python?  

Python es un **lenguaje de programación de alto nivel** conocido por su sintaxis simple, legible y cercana al lenguaje humano. Fue creado por **Guido van Rossum** a finales de los años 1980 y lanzado públicamente en **1991**. Su diseño prioriza la **facilidad de uso** y la **productividad**, lo que lo ha convertido en uno de los lenguajes más populares en áreas como desarrollo web, inteligencia artificial, ciencia de datos y automatización.  

---

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

---

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

---

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

### Conclusión  
Python es ideal para **aprendizaje, desarrollo ágil y proyectos multidisciplinarios**, aunque requiere evaluar sus limitaciones en rendimiento para casos específicos. Su crecimiento continúa gracias a su comunidad y adaptabilidad.

---

# Tipos de Datos en Programación: Clasificación y Características

## Introducción
Los tipos de datos son el fundamento de todo lenguaje de programación. Determinan la naturaleza de la información, cómo se almacena, qué operaciones permite y cómo se comporta a nivel de memoria. Esta guía presenta una clasificación global, con ejemplos conceptuales y comparativas entre lenguajes modernos.

---

## 1. Tipos de Datos Primitivos (Primarios)
Son los tipos más básicos, nativamente soportados por los lenguajes. Representan valores simples.

### 🔢 Tipos Numéricos

#### Enteros (`int`, `Integer`)
- **Descripción**: Números sin parte decimal (ej. 5, -42)
- **Rango común (32-bit)**: -2,147,483,648 a 2,147,483,647
- **Variantes**:
  - `short`, `long` (según cantidad de bits)
  - `unsigned` (solo valores positivos)

#### Punto Flotante (`float`, `double`)
- **Descripción**: Números reales con parte decimal
- **Precisión**:
  - `float`: precisión simple (~6-9 dígitos, 32-bit)
  - `double`: precisión doble (~15-17 dígitos, 64-bit)
- **Uso típico**: Cálculos científicos, representación de valores fraccionarios

#### Tipos Numéricos Especializados

| Tipo         | Lenguajes         | Uso                          |
|--------------|-------------------|------------------------------|
| `decimal`    | Python, C#        | Finanzas (alta precisión)    |
| `complex`    | Python, MATLAB    | Cálculo numérico avanzado    |
| `BigInteger` | Java, .NET        | Criptografía, grandes valores|

---

### 🔡 Texto

#### Cadenas de texto (`String`)
- **Descripción**: Secuencias de caracteres
- **Codificación**: Unicode (UTF-8, UTF-16)
- **Operaciones clave**: Concatenación, comparación, búsqueda, substring

#### Caracteres (`char`)
- **Unidad mínima de texto**: Un solo símbolo
- **Tamaño**: 1 byte (ASCII) o 2 bytes (Unicode)

---

### ✅ Booleanos (`bool`)
- **Valores posibles**: `true` o `false`
- **Representación interna**: Aunque conceptualmente es 1 bit, suele ocupar 1 byte por eficiencia
- **Uso típico**: Condicionales, validaciones lógicas, control de flujo

---

## 2. Tipos de Datos Compuestos (Estructurados)
Tipos que agrupan múltiples valores, homogéneos o heterogéneos.

### 🔁 Colecciones Secuenciales

| Tipo     | Mutabilidad | Orden | Duplicados | Acceso             |
|----------|-------------|-------|------------|--------------------|
| Arreglo  | No          | Sí    | Sí         | Por índice         |
| Lista    | Sí          | Sí    | Sí         | Índice, iteración  |
| Tupla    | No          | Sí    | Sí         | Por posición       |

---

### 🗃️ Colecciones No Secuenciales

#### Conjuntos (`Set`)
- **Propiedades**: Elementos únicos, sin orden
- **Implementaciones**: HashSet, TreeSet (ordenado)

#### Diccionarios (`Map`, `Dict`)
- **Estructura**: Pares clave-valor
- **Acceso eficiente**: Generalmente O(1) con tablas hash
- **Sin duplicación de claves**

---

## 3. Tipos Especiales

### 🕳️ Valores Nulos
- **Propósito**: Representar ausencia de valor o indefinición
- **Por lenguaje**:
  - `null` (Java, C#)
  - `None` (Python)
  - `undefined` / `null` (JavaScript)

> 🔐 *Buena práctica*: Validar siempre antes de operar sobre variables que pueden ser nulas.

---

### 🏷️ Enumeraciones (`enum`)
- **Descripción**: Conjuntos de constantes simbólicas
- **Ventajas**:
  - Código más legible
  - Mayor seguridad de tipo
  - Validación en tiempo de compilación

---

## 4. Tipos Abstractos de Datos (TAD)
Modelos lógicos implementados sobre tipos básicos. No son nativos de los lenguajes pero se usan ampliamente.

### 🧮 Estructuras Lineales

| Estructura | Orden     | Operaciones básicas     | Uso común                  |
|------------|-----------|--------------------------|----------------------------|
| Pila       | LIFO      | `push()`, `pop()`        | Call stack, deshacer       |
| Cola       | FIFO      | `enqueue()`, `dequeue()` | Impresoras, procesamiento por turnos |
| Lista enlazada | Secuencial | Inserciones, eliminaciones | Navegadores, estructuras dinámicas |

---

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

## Conclusión
El dominio de los tipos de datos no solo mejora la eficiencia del programa, sino también su claridad, mantenimiento y robustez. Comprender sus características y limitaciones te permite:

- Escribir código más eficiente
- Evitar errores comunes
- Elegir la estructura óptima según el problema
- Adaptarte fácilmente a distintos lenguajes

**📌 Recomendación final**: Aunque los fundamentos son universales, cada lenguaje tiene sus particularidades. Siempre vale la pena revisar su documentación oficial para detalles específicos.

---

# Operadores Comunes en Lenguajes de Programación

## Introducción

Los **operadores** son símbolos o palabras clave que permiten realizar operaciones sobre variables y valores. Son esenciales para escribir expresiones, tomar decisiones, realizar cálculos y manipular datos. Aunque su sintaxis puede variar ligeramente entre lenguajes, su función suele ser similar.

---

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

---

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

---

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

---

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

---

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

---

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

---

## 7. Operadores Ternarios / Condicionales

Permiten realizar una evaluación condicional en una sola línea.

- **Sintaxis general** (lenguajes C-like):  
  `condición ? valor_si_verdadero : valor_si_falso`

- **Python**:  
  `valor_si_verdadero if condición else valor_si_falso`

---

## 8. Operadores Especiales (por lenguaje)

| Operador        | Lenguaje     | Uso                             |
|-----------------|--------------|----------------------------------|
| `??`            | C#, JS       | Coalescencia nula (valor por defecto) |
| `?:`            | C/C++, Java  | Ternario condicional             |
| `===`, `!==`    | JavaScript   | Comparación estricta (valor y tipo) |
| `=>`            | JS, C#       | Funciones lambda / expresiones flecha |
| `as`, `instanceof` | Python, Java | Conversión / verificación de tipo |

---

## Comparativa entre Lenguajes (Operadores Básicos)

| Categoría      | C/C++     | Java       | Python     | JavaScript |
|----------------|-----------|------------|------------|------------|
| Aritméticos    | Sí        | Sí         | Sí         | Sí         |
| Asignación     | Sí        | Sí         | Sí         | Sí         |
| Comparación    | Sí        | Sí         | Sí         | Sí         |
| Lógicos        | `&&`, `||`, `!` | Igual | `and`, `or`, `not` | Igual     |
| Bit a bit      | Sí        | Sí         | Sí         | Sí         |
| Identidad      | Punteros  | Referencia | `is`       | `===`      |
| Pertenencia    | Manual    | Manual     | `in`       | `in`, `hasOwnProperty` |
| Ternario       | `?:`      | `?:`       | `if else` (inline) | `? :`     |

---

## Conclusión

El dominio de los operadores permite escribir código más claro, conciso y eficiente. Conocer sus particularidades entre distintos lenguajes es clave para evitar errores y mejorar la expresividad del código.

**💡 Recomendación**: Practicá resolviendo problemas simples (calculadoras, filtros, validaciones) usando operadores en diferentes contextos para interiorizarlos de manera natural.
