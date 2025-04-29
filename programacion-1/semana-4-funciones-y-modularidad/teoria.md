## 🔹 Programación Modular

### ¿Qué es?

La **programación modular** es una técnica fundamental en el desarrollo de software que consiste en **dividir un programa grande en partes más pequeñas**. Estas partes, conocidas como **módulos** o **componentes**, son más manejables y reutilizables. Cada módulo se **encarga de resolver un problema o realizar una tarea específica** y contiene todo lo necesario para cumplir su funcionalidad. La idea es que estos módulos sean **autónomos y lógicos**.

En Python, un módulo es simplemente un **archivo que contiene código Python**. El nombre del archivo es el nombre del módulo. Por ejemplo, un archivo llamado `math.py` contendría funciones matemáticas.

### Utilidad y Beneficios

Este enfoque mejora significativamente el proceso de desarrollo por varias razones:

- **Facilita el manejo y la organización del código**.
- **Mejora la legibilidad**.
- **Mejora el mantenimiento**: si hay errores, es más fácil encontrarlos y corregirlos. Un módulo puede modificarse radicalmente sin afectar a otros, incluso sin alterar su función principal.
- **Mejora la escalabilidad del software**.
- **Facilita la reutilización** de código.
- **Permite el trabajo en equipo**: diferentes programadores pueden trabajar simultáneamente en distintos módulos del mismo programa.

### El Principio "Divide y Vencerás"

La programación modular se basa en el principio de "divide y vencerás". Un programa principal (o módulo principal) controla la ejecución y transfiere el control a submódulos para tareas específicas. Si una tarea es compleja, un submódulo puede dividirla a su vez, creando una estructura jerárquica de módulos hasta obtener tareas específicas individuales. Cada módulo puede ser diseñado de forma independiente.

### Ejemplo Conceptual

Un programa para una tienda en línea podría dividirse en módulos como: gestión de usuarios, inventario, pagos y reportes. Cada uno gestiona una parte del sistema de forma independiente pero colaboran entre sí.

---

## 🔹 Funciones

### ¿Qué son?

Una **función** es un **bloque de código diseñado para realizar una tarea específica**. Se define una sola vez y **puede ser ejecutada o "llamada" múltiples veces** desde otras partes del programa. Las funciones, junto con las clases y otros componentes, se utilizan en Python para encapsular lógica del programa en unidades independientes y reutilizables.

### Ventajas

El uso de funciones ofrece varias ventajas importantes:

- **Evita repetir código**.
- **Hace más clara la intención del programa**.
- **Facilita el mantenimiento y la depuración**.

### Estructura Típica (Conceptual)

Independientemente del lenguaje, la estructura básica de una función suele ser:

```
definir función nombre_de_la_función(parámetros):
    realizar operaciones
    devolver resultado (opcional)
```

### Variaciones en la Definición y Uso de Funciones

#### 🔹 Funciones lambda (funciones anónimas)

Son funciones que se definen **sin un nombre explícito**. Tienen una sintaxis concisa (`lambda argumentos: acción`). Son útiles para tareas sencillas y puntuales, a menudo como argumentos para otras funciones (`map`, `filter`, `sorted`). Ahorran memoria si solo se van a usar una vez.

#### 🔹 Funciones con argumentos por omisión

Permiten definir funciones donde **uno o más argumentos tienen valores predeterminados**. Estos valores se utilizan si no se proporciona un valor específico al llamar a la función. El valor por omisión se evalúa una sola vez.

#### 🔹 Funciones con argumentos con palabras clave

Los argumentos se identifican por su nombre, lo que permite **pasarlos en cualquier orden** al llamar a la función. Esto mejora la legibilidad del código.

#### 🔹 Funciones con argumentos especiales

Se pueden usar símbolos (`/` y `*`) en la definición para indicar cómo deben enviarse los argumentos (por posición o por palabra clave).

#### 🔹 Funciones con argumentos arbitrarios

Permiten que una función reciba un **número variable de argumentos**:

- `*args`: argumentos posicionales → se reciben como **tupla**.
- `**kwargs`: argumentos con palabra clave → se reciben como **diccionario**.

---

## 🔹 3. Parámetros

### ¿Qué son?

Los **parámetros** son los **valores que se envían a una función**. Actúan como las **"entradas"** que la función utiliza para realizar sus operaciones. Al definir una función, se especifican los parámetros que espera recibir.

### Tipos de Parámetros

- **Parámetros obligatorios:** deben ser proporcionados al llamar la función.
- **Parámetros opcionales:** tienen un valor por defecto; si no se proporciona, se usa ese valor.

Los mecanismos como `*args`, `**kwargs` o los argumentos por palabras clave, permiten una gestión flexible del paso de parámetros.

---

## 🔹 4. Retorno de Valores

### ¿Qué es?

Una función puede, opcionalmente, **devolver o "retornar" un valor** al finalizar su ejecución. Este valor es el **resultado de la operación** que realizó la función.

### ¿Cómo funciona?

Se usa una instrucción como `return` para indicar qué valor se quiere devolver. Este valor se puede guardar o usar inmediatamente en otra parte del código.

### Funciones sin retorno

Si no se especifica un valor de retorno, se devuelve un valor nulo (por ejemplo, `None` en Python). Estas funciones suelen hacer tareas como imprimir o guardar datos, sin devolver resultados.

---

## 🔹 5. Ámbito de las Variables (Scope)

### ¿Qué es?

El **ámbito (scope)** de una variable se refiere a la **parte del programa donde esa variable puede ser accedida o modificada**.

### Tipos Comunes

- **Ámbito local:** la variable solo existe dentro de la función o bloque donde fue creada.
- **Ámbito global:** la variable se define fuera de cualquier función y puede ser usada en todo el programa. Modificarla desde dentro de funciones requiere cuidado.

### Ejemplo Conceptual

```python
x = 10  # variable global

def ejemplo():
    y = 5  # variable local
    print(x + y)
```

---

## 🔍 Desafío: ¿Cuál es la forma de importación recomendada?

En Python, existen varias formas de importar módulos, pero **la forma recomendada por la comunidad (PEP 8)** es:

```python
import modulo
```

Esta forma:

- Es clara y explícita.
- Evita colisiones de nombres.
- Hace fácil identificar de dónde viene una función o clase (`modulo.funcion()`).

### Evitar:
```python
from modulo import *
```
Porque **contamina el espacio de nombres global** y hace más difícil rastrear el origen de los símbolos.

### Recomendaciones:

- Usa `import modulo` o `from modulo import funcion_especifica`.
- Agrupa las importaciones por bloques: estándar, terceros, propios.
- Ordena alfabéticamente dentro de cada bloque.

---

## ❓¡Investiga! ¿Podemos construir nuestro programa principal sin `__main__`?

Sí, es **posible construir un programa que funcione sin `if __name__ == "__main__":`**, pero **no es recomendable** en programas más grandes o cuando se usan módulos.

### ¿Por qué usarlo es buena práctica?

- Permite que un archivo se use **como módulo o como programa principal**.
- **Evita que cierto código se ejecute cuando se importa el archivo desde otro módulo.**
- Mejora la organización y reusabilidad del código.

### ¿Qué pasa si no lo usamos?

Todo el código se ejecutará incluso si el archivo se importa desde otro lugar, lo que **puede causar errores** o comportamientos no deseados.

---

## ❓ Si estamos trabajando toda la lógica en un mismo archivo...

### ¿Puedo definir las funciones luego del bloque `__main__`?

**No es recomendable.** Aunque Python permite definir funciones en cualquier parte del archivo, **estas deben estar definidas antes de ser llamadas**. Si defines funciones luego del bloque `__main__`, y tratas de usarlas antes, obtendrás un **error de nombre no definido** (`NameError`).

### Mejor práctica:

- Define **todas tus funciones al inicio del archivo** o antes del bloque `__main__`.
- Usa el bloque `__main__` solo para la ejecución principal del programa.
