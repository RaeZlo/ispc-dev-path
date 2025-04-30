# Diseño Lógico

El **diseño lógico** es una etapa fundamental en la creación de bases de datos. Forma parte del esquema conceptual y da como resultado la estructura de la base de datos, definiendo las estructuras de datos que pueden soportar los sistemas gestores de bases de datos (SGBD). A este resultado se le llama **esquema lógico**.

El objetivo del diseño lógico es representar la estructura de la base de datos de forma **abstracta**, pero lista para ser implementada en un SGBD relacional (como MySQL, PostgreSQL, SQL Server, etc.). Busca asegurar que la base de datos refleje las reglas del negocio correctamente y sin redundancias.

El diseño lógico se determina según el SGBD que se vaya a utilizar, sin depender del producto concreto. Luego de obtener el esquema conceptual, se puede obtener el diseño lógico.

## Diseño lógico: Esquema lógico, modelos lógicos

El **esquema lógico** es la **representación detallada del modelo lógico** de una base de datos. Define qué tablas habrá, qué campos tendrá cada una, cómo se relacionan entre sí, y qué restricciones existen (como claves primarias, foráneas, dominios de datos, etc.). Es el resultado del diseño lógico.

El **modelo lógico** es el lenguaje que determina el esquema lógico y representa los datos de acuerdo con un modelo formal.

El modelo lógico más común es el **modelo relacional**. En el modelo relacional, la información se organiza en **tablas** (relaciones), que usan **tuplas** (filas) para representar registros, y **atributos** (columnas) para representar propiedades o campos.

Existen otros modelos lógicos, menos comunes hoy en día, como:

- **Jerárquico**: datos organizados como un árbol.
- **De red**: nodos conectados por múltiples relaciones.
- **Orientado a objetos**: combina estructuras de objetos con persistencia de datos.

## Tablas: Estructura, filas, columnas, registros y campos

Las **tablas** son la estructura fundamental del modelo relacional. Son objetos donde se guardan los datos organizados con un formato de **filas** y **columnas**. Representan entidades o relaciones y almacenan datos relacionados entre sí.

### Estructura de una tabla:

- **Filas** (registros o tuplas):  
  Cada fila representa un registro o una entrada completa en la tabla, representando un solo objeto o entidad.  
  Pueden almacenar valores nulos.  
  Ejemplo: un cliente específico (Juan Pérez).  
  En una tabla de estudiantes, cada estudiante (Laura, Pablo) sería una fila.

- **Columnas** (campos o atributos):  
  Cada columna representa un campo dentro del registro o una propiedad/característica de la entidad.  
  Cada columna debe ser única y tener asociado un tipo de datos.  
  Ejemplo: "correo" o "nombre".  
  En una tabla de estudiantes: `id_estudiante`, `nombre`, `carrera`, `edad` son columnas.

> Un **registro** es un sinónimo de fila.  
> Un **campo** es un sinónimo de columna.

Las tablas en bases de datos relacionales están compuestas por un conjunto de **campos (columnas)** y **registros (filas)**. Se relacionan entre sí mediante **claves primarias** y **claves foráneas**.

## Las 12 reglas de Codd

Las 12 reglas de Codd (numeradas del 0 al 12) son un conjunto de normas establecidas por Edgar Codd para que una base de datos del modelo relacional se considere verdaderamente relacional. A mayor cantidad de reglas cumplidas, más relacional será la base de datos.

### Reglas:

- **Regla 0 - Fundación**:  
   El sistema debe utilizar su estructura relacional solamente para gestionar bases de datos.
- **Regla 1 - Información**:  
   Toda la información debe estar representada unidireccionalmente por los valores en posiciones dentro de las filas, dentro de las tablas. Los valores solo pueden estar representados de una forma: con valores en las tablas, a nivel lógico.
- **Regla 2 - Acceso garantizado**:  
   Todos los datos deben ser accesibles. Cada valor escalar individual debe ser lógicamente direccionable especificando el nombre de la tabla, la columna que lo contiene y la clave primaria.
- **Regla 3 - Tratamiento sistemático de los valores nulos**:  
   El DBMS debe tener la capacidad de manejar valores nulos, reconociéndolos como distintos a cualquier otro valor, independientemente del tipo de datos de la columna.
- **Regla 4 - Catálogo en línea relacional**:  
   El catálogo en línea (diccionario de datos) debe poder consultarse utilizando las mismas técnicas que para los datos. Debe dar acceso a la estructura de la base de datos y ser accesible para los usuarios autorizados.
- **Regla 5 - Sublenguaje de datos completo**:  
   Debe existir, por lo menos, un lenguaje capaz de realizar todas las funciones del DBMS, sin excluir ninguna función.  
   SQL es un lenguaje informático de alto nivel para gestionar y organizar datos de bases de datos relacionales, que posee características como lenguaje de definición y manipulación de datos, control de transacciones, seguridad, etc.
- **Regla 6 - Actualización de vistas**:  
   Todas las vistas deben mostrar información actualizada. Los datos no pueden ser distintos entre las vistas y las tablas base.
- **Regla 7 - Inserciones, modificaciones y eliminaciones de alto nivel**:  
   El sistema debe permitir la manipulación de datos de alto nivel, es decir, sobre conjuntos de registros.
- **Regla 8 - Independencia física de los datos**:  
   Los cambios físicos que se realicen en la base de datos no afectan a las aplicaciones ni a los esquemas lógicos.
- **Regla 9 - Independencia lógica de los datos**:  
    Los cambios que se realicen sobre el esquema lógico no afectan al resto de los esquemas ni a las aplicaciones externas.
- **Regla 10 - Independencia de integridad**:  
    Las reglas de integridad deben ser gestionadas y almacenadas por el DBMS.
- **Regla 11 - Independencia de distribución**:  
    Las bases de datos pueden gestionarse o almacenarse de forma distribuida sin afectar su uso ni la programación.
- **Regla 12 - No subversión**:  
    No se permitirán lenguajes o formas de acceso que salteen las reglas anteriores.
