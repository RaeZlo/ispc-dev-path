# Sistemas Gestores de Bases de Datos (SGBD)
Un Sistema Gestor de Bases de Datos (SGBD), o *Database Management System* (DBMS) en inglés, es un **conjunto de programas diseñado para crear, mantener y manipular bases de datos**. Actúa como intermediario entre los usuarios y la base de datos, permitiendo el acceso y la manipulación de datos sin necesidad de conocer su estructura interna. Es una herramienta esencial para la **gestión eficiente de grandes volúmenes de información**.

Las operaciones sobre la base de datos son realizadas por el **motor de la base de datos**, el cual interpreta y ejecuta comandos SQL. Este motor está compuesto por dos partes principales: el **motor de almacenamiento** y el **procesador de consultas**.

Un SGBD ofrece diversas **funcionalidades clave**, que pueden agruparse en las siguientes categorías:

## 1. Definición, construcción y manipulación de datos
- **Definición de la base de datos**: Mediante un Lenguaje de Definición de Datos (DDL), permite especificar tipos de datos, estructuras y restricciones. Estas definiciones se almacenan como metadatos en el catálogo del SGBD.
- **Construcción de la base de datos**: Almacena los datos en un medio físico controlado por el sistema.
- **Manipulación de datos**: Incluye operaciones como consulta, actualización, inserción y eliminación de registros, generalmente utilizando un Lenguaje de Manipulación de Datos (DML), como SQL.

## 2. Acceso y concurrencia
- **Compartición de datos**: Facilita el acceso simultáneo de múltiples usuarios y aplicaciones a la base de datos.
- **Control de acceso**: Gestiona los permisos de los usuarios y evita accesos no autorizados mediante un Lenguaje de Control de Datos (DCL).

## 3. Seguridad, integridad y recuperación
- **Seguridad**: Protege la información ante fallos del sistema o accesos indebidos.
- **Copia de seguridad y recuperación**: Permite recuperar datos ante pérdidas o daños.
- **Restricciones de integridad**: Aplica reglas como unicidad, tipos de datos válidos y relaciones entre registros para asegurar la coherencia de la información.

## 4. Personalización, mantenimiento y soporte
- **Creación de vistas**: Define tablas virtuales personalizadas para los usuarios.
- **Procedimientos almacenados**: Permite guardar bloques de código reutilizable directamente en la base de datos.
- **Exportación e importación de datos**: Facilita el intercambio de datos con otros sistemas.
- **Mantenimiento y evolución**: Asegura la adaptabilidad del sistema conforme cambian los requisitos.
- **Soporte para múltiples vistas de los datos**: Permite que distintos usuarios visualicen la misma información de diferentes formas.

## 5. Características técnicas
- **Naturaleza autodescriptiva**: Almacena no solo los datos, sino también su descripción (metadatos) en un catálogo del sistema.
- **Independencia de datos**: Separa los programas de los detalles de almacenamiento, facilitando su mantenimiento.
- **Abstracción de datos**: Oculta la complejidad interna del almacenamiento a los usuarios.
- **Estructuras de almacenamiento**: Incluye mecanismos como índices para optimizar el acceso y las consultas.
- **Relaciones complejas entre datos**: Representa eficazmente asociaciones entre múltiples entidades.

La **arquitectura interna** de un SGBD se organiza en tres niveles:

* **Nivel físico**: Describe cómo se almacenan los datos en los dispositivos.
* **Nivel lógico**: Define la estructura organizativa (tablas, campos, relaciones).
* **Nivel de vista**: Muestra al usuario una representación abstracta de los datos.


# Bases de Datos Relacionales

Las bases de datos relacionales se basan en el **modelo relacional**, propuesto por Edgar F. Codd en 1970. Este modelo organiza los datos en **tablas** y permite establecer **relaciones entre ellas** mediante claves.

## Estructura de las tablas
- **Tablas**: Estructuras fundamentales del modelo relacional. Representan entidades (objetos o conceptos del mundo real) o relaciones entre ellas. Los datos están organizados en filas y columnas.
  - **Filas** (o tuplas): Representan instancias individuales de una entidad.
  - **Columnas** (o atributos): Representan propiedades o características de las entidades.

## Claves y relaciones
- **Clave primaria**: Identificador único de cada fila. Permite acceder a los datos de forma lógica y precisa.
- **Clave foránea**: Atributo que referencia una clave primaria en otra tabla. Se utiliza para establecer relaciones entre entidades.

Por ejemplo, en una relación uno a muchos (1\:N), la clave primaria de la tabla del lado “uno” se replica como clave foránea en la tabla del lado “muchos”.

## Relaciones entre tablas
Las relaciones entre entidades se representan a través de **atributos comunes**. Por ejemplo, en una base de datos universitaria, un estudiante puede estar relacionado con varias calificaciones mediante una clave compartida. El SGBD debe permitir representar, consultar y mantener estas relaciones de manera eficiente.
