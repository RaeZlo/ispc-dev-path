# Diseño de Bases de Datos: Introducción y Etapas del Diseño
El **diseño de una base de datos** es un proceso estructurado cuyo objetivo es construir un sistema capaz de satisfacer los requisitos de información de una organización o aplicación. Este proceso se divide en distintas etapas, que abordan el diseño desde diferentes niveles de abstracción y pueden tratarse de forma independiente.

Las principales etapas del diseño de bases de datos son:
1. **Diseño conceptual**: Parte de la recopilación de los requisitos del usuario. Define los elementos fundamentales de la información sin considerar detalles técnicos.
2. **Diseño lógico**: Traduce el diseño conceptual a estructuras que puedan ser implementadas por un tipo de SGBD (por ejemplo, relacional), pero sin depender de un producto específico.
3. **Diseño físico**: Define cómo se almacenarán los datos de manera eficiente en un SGBD concreto, incluyendo detalles como índices, particiones y métodos de acceso.

Además, el proceso completo incluye el **mapeo entre modelos**, como la conversión del modelo conceptual al modelo relacional.

# Diseño Conceptual: Requisitos, Esquema y Modelo
## Especificación de Requisitos
El diseño conceptual comienza con la **especificación de requisitos**, una etapa en la que los diseñadores se comunican con los usuarios para identificar sus necesidades de información y procesos. Esta información se documenta y constituye la base para definir la estructura lógica del sistema.

## Esquema Conceptual
A partir de los requisitos, se construye el **esquema conceptual**, que describe la **estructura global de la base de datos** desde la perspectiva de los usuarios. Este esquema:

- Es **independiente de la tecnología** o del sistema gestor específico.
- Oculta los detalles del almacenamiento físico.
- Se enfoca en **entidades**, **relaciones**, **atributos**, operaciones requeridas y restricciones de integridad.
- Se define durante la fase de diseño y **no debería cambiar frecuentemente**.

## Modelo Conceptual
El **modelo conceptual** es el conjunto de conceptos y notaciones que se utiliza para representar el esquema conceptual. También se le denomina **modelo de datos de alto nivel** porque está diseñado para ser comprensible por usuarios no técnicos.

Entre sus componentes más comunes están:
- **Entidades**: Objetos distinguibles del mundo real.
- **Atributos**: Propiedades que describen las entidades.
- **Relaciones**: Asociaciones entre entidades.

El objetivo de esta etapa no es definir cómo se almacenarán físicamente los datos, sino **qué información se debe representar**.

# Diagrama Entidad-Relación (DER)
El **Diagrama Entidad-Relación (DER)** es una herramienta gráfica que se utiliza para representar el modelo conceptual de una base de datos. Facilita la visualización de la estructura de la información y las relaciones entre los elementos principales.

## Elementos del DER
- **Entidades**: Representan objetos o conceptos del mundo real, como “Cliente”, “Producto” o “Empleado”. Se representan mediante **rectángulos**.
- **Atributos**: Son las propiedades de una entidad, como “nombre”, “dirección” o “número de teléfono”. Se conectan a las entidades mediante **líneas** y se representan con **óvalos**.
- **Relaciones**: Definen asociaciones entre dos o más entidades. Por ejemplo, una relación "Realiza" puede vincular a “Cliente” con “Pedido”. Se representan mediante **rombos**.
- **Cardinalidad**: Indica la cantidad de instancias de una entidad que pueden estar asociadas con una instancia de otra. Por ejemplo:
  - **1:1** (uno a uno)
  - **1\:N** (uno a muchos)
  - **N\:M** (muchos a muchos)
- **Claves primarias**: Identifican de forma única a cada instancia de una entidad. Son fundamentales para la implementación del modelo relacional posterior, ya que permiten direccionar los datos de manera lógica.

# Transformación del Modelo ER al Modelo Relacional
El modelo Entidad-Relación proporciona una base sólida para la creación de bases de datos relacionales. Durante el proceso de transformación:

- Las **entidades** se convierten en **tablas**.
- Los **atributos** se traducen en **columnas**.
- La **clave primaria** de una entidad se mantiene como identificador de la tabla.
- Las **relaciones** se representan como:
  - **Claves foráneas**, cuando hay relaciones 1\:N.
  - **Tablas intermedias**, cuando las relaciones son N\:M.

Esta transformación permite implementar el diseño conceptual en un **Sistema Gestor de Bases de Datos Relacional (SGBDR)**, garantizando que se mantenga la integridad y lógica de los datos definidos originalmente.
