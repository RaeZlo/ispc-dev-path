## **Diseño Lógico**

El **diseño lógico** es una etapa crucial en el proceso de creación de bases de datos. Su objetivo es transformar el **diseño conceptual** (como el diagrama Entidad Relación) en un **modelo lógico**. Este diseño describe **cómo se organizarán los datos** dentro de un Sistema Gestor de Bases de Datos (SGBD), pero sin incluir detalles físicos específicos como índices o almacenamiento.

El resultado del diseño lógico es la estructura de la base de datos. Se determina según el SGBD que se vaya a utilizar, aunque sin depender del producto concreto. La meta es representar la estructura de forma **abstracta**, lista para ser implementada, asegurando que refleje las reglas del negocio correctamente y sin redundancias.

Durante el diseño lógico, se considera la transformación de un Diagrama Entidad Relación (DER) a un modelo relacional, teniendo en cuenta conceptos como tablas, reglas de normalización y las 12 reglas de Codd. Por ejemplo:

- Las **entidades** se convierten en **tablas**
- Los **atributos** en **columnas**
- El **identificador de la entidad** en la **clave primaria**
- Las relaciones:
  - **Muchos a Muchos (N:M):** crean una nueva tabla
  - **Uno a Muchos (1:N):** implican claves foráneas
  - **Uno a Uno (1:1):** pueden resultar en la fusión de tablas

## **Diseño Lógico: Esquema Lógico y Modelos Lógicos**

### **Esquema Lógico**

Es la **representación detallada del modelo lógico** de una base de datos. Define qué **tablas** habrá, qué **campos** tendrá cada una, cómo se **relacionan** entre sí y qué **restricciones** existen (como claves primarias, foráneas, dominios de datos, etc.). Es el resultado concreto del diseño lógico.

**Ejemplo de un esquema lógico:**

- **Tabla: Clientes**
  - `id_cliente` (PK)
  - `nombre`
  - `correo`
  - `fecha_registro`

- **Tabla: Pedidos**
  - `id_pedido` (PK)
  - `fecha`
  - `id_cliente` (FK) → `Clientes.id_cliente`

### **Modelos Lógicos**

Son el **lenguaje que determina el esquema lógico**. Representan los datos de acuerdo con un modelo formal.

- El **modelo más común** es el **modelo relacional**.
- Otros modelos:
  - Jerárquico
  - De red
  - Orientado a objetos

### **Modelo Relacional**

Organiza la información en **tablas** (relaciones), utiliza:

- **Tuplas** (filas) para representar registros
- **Atributos** (columnas) para representar propiedades o campos

## **Tablas: Estructura, Filas, Columnas, Registros y Campos**

### **Tablas**

Son la **estructura fundamental del modelo relacional**, donde se guardan los datos. Representan **entidades o relaciones** y organizan los datos en **filas y columnas**.

### **Estructura de una Tabla**

- **Filas:** Representan un **registro** (una entrada completa en la tabla). También conocidas como **registros** o **tuplas**. Pueden almacenar valores nulos.
- **Columnas:** Representan un **campo** (una propiedad de la entidad). También conocidas como **campos** o **atributos**.

### **Definiciones clave**

- **Registro:** Sinónimo de **fila**.
- **Campo:** Sinónimo de **columna**.

### **Ejemplo práctico de una tabla**

**Tabla: Estudiantes**

| id_estudiante | nombre      | carrera     | edad |
|---------------|-------------|-------------|------|
| 1             | Laura Díaz  | Ingeniería  | 21   |
| 2             | Pablo Rojas | Medicina    | 23   |

- Cada estudiante es una **fila** (o **registro** o **tupla**).
- "id_estudiante", "nombre", "carrera", y "edad" son **columnas** (o **campos** o **atributos**).
- Toda la información de Laura Díaz es un **registro**.
- "nombre" es un **campo** que almacena el nombre del estudiante.

## **Normalización**

La **normalización** es una técnica del diseño lógico para:

- Organizar tablas y relaciones
- Eliminar redundancia
- Proteger la integridad de los datos

Se clasifica en **formas normales**:

- 1FN
- 2FN
- 3FN
- 4FN
- 5FN
