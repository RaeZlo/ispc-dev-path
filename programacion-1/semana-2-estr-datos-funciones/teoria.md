# Estructuras de Datos y sus Operaciones en Python

## Listas (list)

| Nombre     | Operación                                   | Sintaxis                        |
|------------|---------------------------------------------|---------------------------------|
| `append()` | Agrega un elemento al final                 | `lista.append(valor)`           |
| `extend()` | Agrega múltiples elementos                  | `lista.extend(iterable)`        |
| `insert()` | Inserta un elemento en un índice            | `lista.insert(i, valor)`        |
| `remove()` | Elimina la primera ocurrencia de un valor   | `lista.remove(valor)`           |
| `pop()`    | Elimina y devuelve un elemento (por índice o último) | `lista.pop(i)` o `lista.pop()` |
| `index()`  | Devuelve el índice de un valor              | `lista.index(valor)`            |
| `count()`  | Cuenta las ocurrencias de un valor          | `lista.count(valor)`            |
| `sort()`   | Ordena la lista                             | `lista.sort()`                  |
| `reverse()`| Invierte el orden de la lista               | `lista.reverse()`               |
| `copy()`   | Crea una copia de la lista                  | `lista.copy()`                  |
| `clear()`  | Elimina todos los elementos                 | `lista.clear()`                 |

## Tuplas (tuple)

| Nombre     | Operación                                   | Sintaxis                        |
|------------|---------------------------------------------|---------------------------------|
| `count()`  | Cuenta las ocurrencias de un valor          | `tupla.count(valor)`            |
| `index()`  | Devuelve el índice de un valor              | `tupla.index(valor)`            |

## Conjuntos (set)

| Nombre               | Operación                                               | Sintaxis                               |
|----------------------|---------------------------------------------------------|----------------------------------------|
| `add()`              | Agrega un elemento al conjunto                          | `conjunto.add(valor)`                 |
| `remove()`           | Elimina un elemento (error si no existe)                | `conjunto.remove(valor)`              |
| `discard()`          | Elimina un elemento (sin error si no existe)            | `conjunto.discard(valor)`             |
| `pop()`              | Elimina y devuelve un elemento aleatorio                | `conjunto.pop()`                       |
| `clear()`            | Elimina todos los elementos                             | `conjunto.clear()`                     |
| `union()`            | Une dos conjuntos                                       | `conjunto.union(otro)`                 |
| `intersection()`     | Elementos comunes en ambos conjuntos                    | `conjunto.intersection(otro)`         |
| `difference()`       | Elementos en A pero no en B                             | `conjunto.difference(otro)`           |
| `symmetric_difference()` | Elementos no comunes en ambos conjuntos                | `conjunto.symmetric_difference(otro)` |

## Diccionarios (dict)

| Nombre               | Operación                                               | Sintaxis                               |
|----------------------|---------------------------------------------------------|----------------------------------------|
| `keys()`             | Devuelve las claves del diccionario                     | `diccionario.keys()`                   |
| `values()`           | Devuelve los valores del diccionario                    | `diccionario.values()`                 |
| `items()`            | Devuelve pares clave-valor                              | `diccionario.items()`                  |
| `get()`              | Obtiene el valor de una clave (sin error)               | `diccionario.get(clave, defecto)`      |
| `pop()`              | Elimina y devuelve un valor                             | `diccionario.pop(clave)`               |
| `popitem()`          | Elimina y devuelve el último par clave-valor            | `diccionario.popitem()`                |
| `update()`           | Agrega o actualiza claves con valores                   | `diccionario.update(otro_dict)`       |
| `setdefault()`       | Obtiene el valor o lo asigna si no existe               | `diccionario.setdefault(clave, valor)`|
| `copy()`             | Crea una copia del diccionario                          | `diccionario.copy()`                   |
| `clear()`            | Elimina todos los elementos                             | `diccionario.clear()`                  |

---

# Manejo de Excepciones en Programación

## Concepto Fundamental
El manejo de excepciones constituye un mecanismo esencial en el desarrollo de software que permite gestionar situaciones anómalas durante la ejecución de programas. Este paradigma ofrece un enfoque estructurado para interceptar, procesar y recuperarse de condiciones excepcionales sin interrumpir abruptamente el flujo normal de la aplicación.

## Casos de Uso Recomendados

### 1. Gestión de Incertidumbres Operativas
- Operaciones con recursos externos (archivos, bases de datos, APIs)
- Procesamiento de entradas de usuario o datos no estructurados
- Acceso a sistemas periféricos (impresoras, dispositivos de red)

### 2. Control de Errores Externos
- Fallos de conectividad o timeout en comunicaciones
- Problemas de hardware o limitaciones del sistema
- Violaciones de permisos o restricciones de seguridad

### 3. Mejora de la Experiencia de Usuario
- Presentación de mensajes de error contextualizados
- Conservación del estado de la aplicación ante fallos
- Opciones de recuperación o rutas alternativas

### 4. Mantenimiento de la Estabilidad
- Prevención de terminaciones abruptas
- Liberación segura de recursos reservados
- Registro estructurado de incidentes

## Arquitectura Básica

### Bloque de Intento (Try)
Contiene el código susceptible a generar excepciones. Marca el ámbito donde se monitorean posibles anomalías durante la ejecución.

### Bloque de Captura (Catch/Except)
Provee handlers especializados para tipos específicos de excepciones. Permite:
- Clasificación de errores por categorías
- Implementación de lógicas de recuperación
- Generación de métricas de fallos

### Bloque de Finalización (Finally)
Garantiza la ejecución de código crítico para:
- Liberación de recursos (memoria, conexiones)
- Cierre seguro de transacciones
- Mantenimiento de invariantes del sistema

## Impacto en la Calidad del Software
La implementación adecuada de manejo de excepciones contribuye a:
- Mayor robustez del sistema
- Mejor capacidad de diagnóstico
- Experiencia de usuario profesional
- Mantenibilidad del código
- Seguridad en operaciones críticas

---

# Funciones en Programación

## Definición y Propósito
Las funciones son bloques de código que realizan una tarea específica y que se pueden reutilizar a lo largo de un programa. En lugar de escribir el mismo código una y otra vez, se define una función una sola vez, y luego se puede invocar (llamar) múltiples veces cuando se necesite ejecutar ese conjunto de instrucciones. Esto mejora la organización, reutilización y claridad del código, lo que facilita tanto el desarrollo como el mantenimiento del programa.

## Casos de Uso Recomendados
### 1. Organización de Código
- Agrupación lógica de operaciones relacionadas
- Reducción de complejidad cognitiva
- Mejora de la navegabilidad del código fuente
### 2. Reutilización Eficiente
- Eliminación de patrones repetitivos
- Centralización de lógica común
- Minimización de errores por duplicación
### 3. Abstracción de Complejidad
- Ocultamiento de implementaciones detalladas
- Exposición de interfaces claras
- Simplificación de flujos de control principales
### 4. Mejora de Legibilidad
- Nomenclatura semántica de operaciones
- Reducción de anidamiento excesivo
- Documentación implícita mediante estructura
### 5. Desarrollo Colaborativo
- División natural de responsabilidades
- Integración de contribuciones paralelas
- Pruebas unitarias focalizadas

## Estructura básica de una función

### 1. Definición de la función:
Se usa una palabra clave específica para definir la función (como def en Python o function en JavaScript), seguida de un nombre descriptivo de la función, y entre paréntesis, los parámetros (si la función los requiere).
### 2. Cuerpo de la función:
El cuerpo de la función es donde se coloca el código que realiza la tarea o el procesamiento. Este bloque de código se ejecutará cuando se invoque la función.
### 3. Valor de retorno (opcional):
Si la función necesita devolver un resultado, se utiliza la palabra clave return para retornar el valor calculado. Si la función no necesita devolver nada, no es necesario usar return, y la función simplemente realizará la tarea.

## Tipos de funciones
### Funciones sin parámetros:
Estas funciones no reciben ningún valor de entrada. Realizan una tarea que no depende de valores externos.
### Funciones con parámetros:
Estas funciones reciben valores de entrada (llamados parámetros o argumentos) para realizar su tarea. Los parámetros son pasados entre paréntesis cuando se llama a la función.
### Funciones con valor de retorno:
Estas funciones realizan una tarea y devuelven un resultado. El valor de retorno se especifica mediante la palabra clave return. Cuando se llama a la función, el valor retornado puede ser almacenado en una variable o utilizado directamente.
### Funciones sin valor de retorno:
Son aquellas funciones que realizan una acción, pero no devuelven un valor. En lugar de eso, solo ejecutan su tarea (como imprimir un mensaje o modificar un valor global).
### Funciones recursivas:
Son funciones que se llaman a sí mismas dentro de su propio cuerpo. Se utilizan comúnmente en problemas donde la solución puede ser dividida en subproblemas más pequeños, como el cálculo de factoriales o el recorrido de estructuras de datos como árboles.
### Funciones lambda (anónimas):
Son funciones pequeñas y de una sola línea que no requieren un nombre. Se usan principalmente para operaciones rápidas y simples que no necesitan una definición formal de función.

## Principios de Diseño
1. **Responsabilidad Única**  
   Cada función debe resolver un problema específico
2. **Acoplamiento Débil**  
   Minimizar dependencias externas
3. **Cohesión Fuerte**  
   Mantener operaciones relacionadas
4. **Transparencia Referencial**  
   Mismos inputs → mismos outputs
5. **Composición sobre Herencia**  
   Preferir pequeñas funciones combinables

## Beneficios Estratégicos
- Reducción de errores por factorización
- Mejor escalabilidad de soluciones
- Mayor facilidad de pruebas
- Optimización del rendimiento
- Evolución mantenible del código

Las funciones constituyen la piedra angular del desarrollo de software moderno, permitiendo la construcción de sistemas complejos mediante la composición de componentes simples y bien definidos.
