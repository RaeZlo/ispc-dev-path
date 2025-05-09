# Diseño Lógico de Bases de Datos
El **Diseño Lógico** es una etapa fundamental en el proceso de diseño de bases de datos, que se puede descomponer en distintas fases. Surge a partir del diseño conceptual, transformando el esquema conceptual. Su objetivo es definir la **estructura de la base de datos** que puede soportar un sistema gestor de bases de datos (SGBD), independientemente del producto de SGBD concreto que se vaya a utilizar. Representa la estructura de la base de datos de forma **abstracta** pero lista para ser implementada. Además, busca asegurar que la base de datos refleje correctamente las reglas del negocio y sin redundancias.

## Esquema Lógico
El resultado del diseño lógico es el **Esquema Lógico**. El esquema lógico es la **representación detallada del modelo lógico** de una base de datos. Define qué **tablas** habrá, qué **campos** tendrá cada una, cómo se **relacionan** entre sí, y qué **restricciones** existen, como claves primarias (PK - Primary Key), claves foráneas (FK - Foreign Key), y dominios de datos.

Por ejemplo, un esquema lógico podría detallar una tabla `Clientes` con:

* `id_cliente` (PK)
* `nombre`
* `correo`
* `fecha_registro`

Y una tabla `Pedidos` con:

* `id_pedido` (PK)
* `fecha`
* `id_cliente` (FK) que referencia a `Clientes.id_cliente`.

## Modelo Lógico
Un **Modelo Lógico** representa los datos de acuerdo con un modelo formal. El **modelo relacional** es el más común. En el modelo relacional, la información se organiza en **tablas** (también llamadas relaciones).

## Transformación del DER al Modelo Relacional
Al realizar el diseño lógico, después de obtener el esquema conceptual (como un Diagrama Entidad Relación - DER), se deben tener en cuenta varios conceptos fundamentales antes de transformar el DER a un modelo relacional. Estos conceptos incluyen qué son y cómo se estructuran las **tablas**, las **reglas de normalización** y las **12 reglas de Codd**.

### Reglas de transformación:
- Todas las **entidades se convierten en tablas**.
- Los **atributos** de las entidades se convierten en las **columnas** de la tabla correspondiente.
- El **identificador** de la entidad se convierte en la **clave primaria** (PK) de la tabla.
- Las **relaciones Muchos a Muchos (N\:M)** dan lugar a la creación de una **nueva tabla** cuya clave primaria estará compuesta por las claves primarias de las entidades asociadas.
- En las **relaciones Uno a Muchos (1\:N)**, la clave primaria de la tabla con cardinalidad 1 pasa a la tabla con cardinalidad N como **clave foránea** (FK), relacionando así ambas tablas.
- En las **relaciones Uno a Uno (1:1)**, las dos tablas involucradas **deberán fusionarse** en una sola, definiendo un identificador común como clave primaria.

## Las 12 reglas de Codd
Las **12 reglas de Codd** son un conjunto de normas establecidas por Edgar Codd para que una base de datos basada en el modelo relacional se considere verdaderamente relacional. Cuantas más reglas se cumplan, más relacional será la base de datos.

### Reglas:
1. **Regla 0 (Fundación)**: El sistema debe utilizar su estructura relacional exclusivamente para gestionar bases de datos.
2. **Regla 1 (Información)**: Toda la información debe estar representada de forma unidireccional por los valores en posiciones dentro de las filas, dentro de las tablas (a nivel lógico).
3. **Regla 2 (Acceso garantizado)**: Todos los datos deben ser accesibles; cada valor escalar individual debe ser lógicamente direccionable especificando el nombre de la tabla, la columna que lo contiene y la clave primaria.
4. **Regla 3 (Tratamiento sistemático de los valores nulos)**: El SGBD debe manejar valores nulos, reconociéndolos como distintos de cualquier otro valor, independientemente del tipo de datos de la columna.
5. **Regla 4 (Catálogo en línea relacional)**: El catálogo en línea (diccionario de datos) debe poder consultarse utilizando las mismas técnicas que para los datos (usando la estructura de la base de datos) y debe ser accesible para usuarios autorizados.
6. **Regla 5 (Sublenguaje de datos completo)**: Debe existir al menos un lenguaje capaz de realizar todas las funciones del SGBD, permitiendo también que otras tareas se realicen con este lenguaje principal. SQL es un ejemplo de lenguaje que sirve para gestionar y organizar datos en una base de datos relacional y permite definir, manipular e integrar datos, así como controlar transacciones, seguridad y crear vistas.
7. **Regla 6 (Actualización de vistas)**: Todas las vistas deben mostrar información actualizada, y los datos no pueden ser diferentes entre las vistas y las tablas base.
8. **Regla 7 (Inserciones, modificaciones y eliminaciones de alto nivel)**: El sistema debe permitir la manipulación de datos a un alto nivel, es decir, sobre conjuntos de registros (tuplas o tablas simultáneamente).
9. **Regla 8 (Independencia física de los datos)**: Los cambios físicos realizados en la base de datos no afectan a las aplicaciones ni a los esquemas lógicos.
10. **Regla 9 (Independencia lógica de los datos)**: Los cambios realizados sobre el esquema lógico (nombres de tablas/columnas, modificación de registros) no afectan al resto de los esquemas ni a las aplicaciones externas.
11. **Regla 10 (Independencia de integridad)**: Las reglas de integridad deben ser gestionadas y almacenadas por el SGBD, permitiendo cambios sin afectar a las aplicaciones existentes.
12. **Regla 11 (Independencia de distribución)**: Las bases de datos pueden gestionarse o almacenarse de forma distribuida en distintos servidores sin afectar al uso ni a la programación del usuario; el esquema lógico debe mantenerse idéntico.
13. **Regla 12 (No subversión)**: No se permitirán lenguajes o formas de acceso que ignoren o eviten las reglas anteriores.

## Normalización

Además de las reglas de Codd, la **normalización** es otra consideración crucial en el diseño lógico. Es una técnica para estandarizar y validar datos al diseñar tablas y sus relaciones, ayudando a eliminar la redundancia de datos y a proteger su integridad.
