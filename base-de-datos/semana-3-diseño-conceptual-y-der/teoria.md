# Diseño de Bases de Datos

El diseño de bases de datos es un proceso complejo que se descompone en distintas etapas: diseño conceptual, diseño lógico y diseño físico. El objetivo es obtener una base de datos que satisfaga los requisitos informacionales de un sistema informático.

## Diseño Conceptual

El diseño conceptual surge de las especificaciones de requisitos del usuario, a partir de lo cual se obtiene el esquema conceptual de la base de datos. Este esquema define la estructura de la base de datos independientemente de la tecnología o el sistema de gestión de bases de datos (SGBD). El modelo conceptual es el lenguaje utilizado para describir el esquema conceptual. El objetivo principal de esta etapa es describir la información de la base de datos en sí misma y no cómo se almacenará.

## Diagrama Entidad-Relación (DER)

El Diagrama Entidad-Relación (DER) es una herramienta gráfica utilizada para diseñar modelos de bases de datos. Este modelo representa la estructura de la base de datos en términos de entidades, atributos y relaciones.

### Entidades

Una entidad se puede definir como una unidad que tiene atributos y contiene información que conforma una base de datos. Representa un objeto del mundo real, una persona, un lugar o un concepto. Cada entidad debe tener un nombre único. En un DER, una entidad se representa con un rectángulo.

### Atributos

Los atributos son las características o propiedades de cada entidad. Describen las propiedades de la entidad y deben ser únicos y distintos entre sí. En un DER, los atributos se representan mediante un círculo conectado a la entidad con una línea. Para cumplir con la primera forma normal (1FN), cada columna (que corresponde a un atributo) debe tener un solo valor en cada fila (ser atómico).

### Relaciones

Las relaciones definen cómo las entidades están conectadas o asociadas entre sí. Cada relación debe tener un nombre que describa la conexión entre las entidades. En un DER, una relación se representa con un rombo que conecta las entidades relacionadas.

### Cardinalidad

La cardinalidad o multiplicidad indica la cantidad de elementos de una entidad que se relacionan con una instancia de otra entidad. Especifica cuántos objetos de una entidad están relacionados con cuántos objetos de otra entidad a través de la relación. Se puede expresar como uno (1), muchos (*), o un rango específico (ej., 0..1 o 1..N). La cardinalidad se representa en el DER mediante símbolos colocados junto a las líneas que conectan las entidades. Los tipos comunes de cardinalidad son:

- **Uno a Uno (1:1)**: Un elemento de una entidad se relaciona con un solo registro de otra entidad y viceversa.
- **Uno a Muchos (1:M)**: Un registro de una entidad A se puede relacionar con cero o muchos registros de otra entidad B, y cada registro de B se relaciona con un solo registro de A.
- **Muchos a Muchos (N:M)**: Un registro de una entidad se relaciona con cero o varios registros de otra entidad.

Definir correctamente las cardinalidades es crucial para un modelo ER preciso.

## Normalización de Bases de Datos

La normalización es un proceso que aplica reglas para organizar los datos de una base de datos de manera más eficiente. Su objetivo es reducir la redundancia de datos, mejorar la integridad de los datos y evitar errores en la manipulación de la información. La normalización se divide en diferentes niveles o formas normales. Las primeras tres, desarrolladas por Edgard Codd (1FN, 2FN, y 3FN), son las más importantes para asegurar la integridad de la base de datos.

### Primera Forma Normal (1FN)

Requiere que cada tabla tenga una clave primaria única, no se permitan valores repetidos en las columnas, y que cada columna tenga un solo valor atómico en cada fila. El ejemplo de la tabla "ventas" que se corrige creando "detalle_ventas" ilustra cómo eliminar la repetición de productos en una misma venta para cumplir con la 1FN.

### Segunda Forma Normal (2FN)

Establece que cada atributo no clave de una tabla debe depender funcionalmente de la clave primaria completa. Esto es relevante cuando una tabla tiene múltiples claves primarias (clave primaria compuesta), donde cada atributo debe depender de todas las claves primarias y no solo de una parte. El ejemplo de la tabla "Pedidos" con una clave primaria compuesta ("numero_pedido", "fecha_pedido") y el atributo "codigo_cliente" que solo depende de "numero_pedido", muestra la necesidad de dividir la tabla en "Pedidos" y "Clientes" para cumplir con la 2FN.

### Tercera Forma Normal (3FN)

Se enfoca en la eliminación de las dependencias transitivas. Una dependencia transitiva ocurre cuando un atributo depende de otro atributo que no es la clave primaria. Para aplicar la 3FN, se debe asegurar que cada atributo no clave dependa solo de la clave primaria de la tabla o de otros atributos clave. El ejemplo de la tabla "ventas" donde "nombre_producto" y "cantidad" dependen de "id_producto" (un atributo no clave) en lugar de la clave primaria "id_venta", se corrige creando una tabla "Productos" separada.

La aplicación de las formas normales puede llevar a una mayor cantidad de tablas, pero garantiza una mayor integridad y consistencia de los datos.
