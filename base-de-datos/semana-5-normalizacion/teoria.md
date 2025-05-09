# Normalización en Bases de Datos

La **Normalización** es un proceso y una técnica utilizada para **organizar los datos** de una base de datos de manera más eficiente. Es una técnica de estandarización y validación de datos que se aplica al diseñar las tablas y establecer las relaciones entre ellas.

## Objetivos de la Normalización

El **objetivo principal** de la normalización es:

- **Reducir la redundancia de datos**.
- **Mejorar la integridad de los datos**.
- **Evitar errores en la manipulación de la información**.
- Lograr una **mayor organización**.
- **Proteger la integridad** de los datos.

## Problemas de la No Normalización

Los **problemas de la no normalización** surgen de la **redundancia de datos**. Sin la normalización, tendríamos datos redundantes que traen aparejados problemas de mantenimiento, además de ocupar espacio en el disco duro, y dependencias incoherentes.

## Formas Normales

La normalización se divide en diferentes niveles llamados **formas normales**. Existen 6 formas normales, pero las primeras 3 (1FN, 2FN y 3FN) fueron desarrolladas por Edgard Codd y son consideradas las más importantes porque aseguran la integridad de la base de datos y deben aplicarse sí o sí. Luego surgieron otras como la Forma Normal de Boyce-Codd (FNBC), 4FN, y 5FN.

### Primera Forma Normal (1FN)

La Primera Forma Normal (1FN) es el primer nivel de normalización. Para cumplir con ella:

- Cada tabla debe tener una **clave primaria única**.
- No se deben permitir **valores repetidos en las columnas**.
- Cada columna debe tener un **solo valor en cada fila**. Esto significa que los **atributos deben ser atómicos**, es decir, cada atributo tiene su propia celda.
- Sirve para **eliminar los grupos repetidos**.

La 1FN es importante porque garantiza que cada tabla tenga una estructura bien definida y que cada fila tenga información única y no redundante. Además, permite que las tablas sean unidas y relacionadas correctamente mediante claves primarias y foráneas.

**Ejemplo de violación y corrección de 1FN:**

Una tabla `ventas` con columnas `id_venta`, `id_producto`, `fecha_venta` y `cantidad`. Esta tabla no cumple con la 1FN si la columna `id_producto` puede contener múltiples valores en la misma fila (porque cada venta generalmente se compone de varios productos). Esto dificulta la búsqueda y el análisis de los datos. Para corregirlo, se puede crear una nueva tabla llamada `detalle_ventas` con las columnas `id_venta`, `id_producto` y `cantidad`. De esta forma, cada fila de `detalle_ventas` tendría un solo producto asociado a ella y cumpliría con la 1FN.

Otra forma de violar la 1FN es tener un atributo multivalor, como un campo `Email` que almacena múltiples correos electrónicos separados por coma. Esto se soluciona creando un registro por cada email o, preferiblemente, creando una tabla separada `Emails` con `Email` (PK) y `Id_Cliente` (FK).

### Segunda Forma Normal (2FN)

Para estar en la Segunda Forma Normal (2FN), una tabla debe cumplir con la Primera Forma Normal. Además, establece que **cada atributo no clave de una tabla debe depender funcionalmente de la clave primaria completa**. Esto significa que si una tabla tiene una clave primaria compuesta por múltiples atributos, cada atributo no clave debe depender completamente de *todas* las partes de la clave primaria y no solo de una parte de ellas.

La 2FN sirve para **eliminar los datos redundantes**. Es importante destacar que la aplicación de la segunda forma normal puede generar una mayor cantidad de tablas, lo que puede hacer que la base de datos sea más compleja de manejar, pero garantiza una mayor integridad y consistencia de los datos.

**Ejemplo conceptual de 2FN:**

Si tenemos una tabla `Pedidos` con clave primaria compuesta por `numero_pedido` y otro atributo. Para que esté en 2FN, todos los atributos no clave deben depender de la combinación de `numero_pedido` y el otro atributo. Si un atributo solo dependiera de `numero_pedido` (una parte de la clave primaria), no estaría en 2FN.

### Tercera Forma Normal (3FN)

Para cumplirse la Tercera Forma Normal (3FN), una tabla debe cumplir con las dos condiciones anteriores (1FN y 2FN). Además, **los atributos que no son clave no pueden depender de manera transitiva de una clave candidata**. Esto se enfoca en la **eliminación de las dependencias transitivas**. Una dependencia transitiva ocurre cuando un atributo no clave depende de otro atributo no clave, y este último depende de la clave primaria (A -> B y B -> C, donde C depende transitivamente de A a través de B).

Para aplicar la tercera forma normal, debemos asegurarnos de que cada atributo no clave de una tabla dependa **solo de la clave primaria de la tabla o de otros atributos clave**. Si un atributo depende de otro atributo no clave, debemos separarlo en una tabla diferente. La 3FN es considerada como el **estándar a cumplir por los esquemas relacionales** y logra una mejor organización y eficiencia en la base de datos.

**Ejemplo de violación y corrección de 3FN:**

Supongamos una tabla `ventas` donde la clave primaria es `id_venta`. Si tenemos columnas como `nombre_producto` y `cantidad`, y estas dependen del `id_producto` (que no es la clave primaria en esta estructura de ejemplo) en lugar de `id_venta`, existe una dependencia transitiva. Para aplicar la 3FN, esta información se separa en una nueva tabla llamada `Productos`. De esta manera, cada tabla tiene su propia clave primaria y la información está organizada de manera más eficiente y sin dependencias transitivas.

Otro ejemplo es una tabla `Clientes` que contenga atributos como `Id_Localidad`, `Nombre_Localidad`, `Id_Provincia`, `Nombre_Provincia`. Aquí, `Nombre_Localidad` depende de `Id_Localidad`, y `Id_Localidad` depende de `Id_Cliente`. También `Nombre_Provincia` depende de `Id_Provincia`, y `Id_Provincia` podría depender de `Id_Localidad`. Para estar en 3FN, se crearían tablas separadas como `Localidades` y `Provincias`, eliminando las columnas dependientes transitivamente de la tabla `Clientes`.
