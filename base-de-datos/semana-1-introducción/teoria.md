# Conceptos fundamentales
## **Sistemas de información (SI)**
Son un conjunto ordenado de mecanismos diseñados para **administrar y procesar datos de manera fácil y rápida**. Están compuestos por una serie de recursos interconectados (humanos, hardware, software, datos, actividades). Su objetivo común es **organizar y optimizar la información de una organización**. No todos los SI requieren informática, aunque a menudo los sistemas informáticos constituyen la mayor parte de uno.
Existen diferentes tipos de SI según su uso principal, como:

- Sistemas de Procesamiento de Transacciones (TPS) para gestionar información de transacciones.
- Sistemas de Información Ejecutiva (EIS) para monitorear variables gerenciales.
- Sistemas de Información Gerencial (MIS) para información general de la empresa.
- Sistemas de Soporte a Decisiones (DSS) para la toma de decisiones.

## **Almacenamiento de datos**
Es el proceso mediante el cual se guardan datos de manera persistente en dispositivos físicos o virtuales. Este almacenamiento puede ser físico (discos duros, SSD, cintas magnéticas) o virtualizado en entornos como la nube.

Existen diferentes estructuras de almacenamiento:
- Almacenamiento en bloque
- Almacenamiento de archivos
- Almacenamiento de objetos

El almacenamiento de objetos, por ejemplo, permite guardar datos como unidades individuales (objetos) con metadatos y un identificador único, siendo ideal para datos no estructurados como archivos multimedia. Este tipo de almacenamiento se usa ampliamente en servicios como Amazon S3.

El almacenamiento es gestionado por el **DBMS**, que organiza los datos lógicamente (tablas, índices, vistas) y los traduce en operaciones sobre los dispositivos físicos.

## **Diferencia entre datos e información**
- Los **datos** son hechos, cifras u observaciones sin procesar que por sí solos no tienen significado completo. Por ejemplo, “42” o “2025-05-09” son datos.
- La **información**, en cambio, surge cuando los datos son procesados, organizados o interpretados para adquirir un contexto útil. Por ejemplo, “42 unidades vendidas el 9 de mayo de 2025” es información, porque comunica algo comprensible y relevante.

En un sistema informático, el proceso central es convertir datos en información para apoyar la toma de decisiones. En este contexto, los datos reflejan aspectos del mundo real o “minimundo” que la base de datos modela, y el objetivo es representarlos con fidelidad y precisión.

# Bases de datos: Definición, objetivos y usos generales
## **Definición**

Una base de datos es una **colección de datos relacionados**. Son los repositorios donde se almacenan los datos relacionados entre sí, almacenados sistemáticamente para su posterior procesamiento para entregar información al usuario. Una base de datos computerizada se crea y mantiene con un grupo de aplicaciones específicas o mediante un sistema de administración de bases de datos (DBMS).

## **Objetivos y usos generales**
Las bases de datos tienen como propósito central organizar grandes volúmenes de datos de manera eficiente, segura y accesible, facilitando su procesamiento y análisis.

Entre las funciones clave de una base de datos, se destacan:

- **Definición**: Especificar qué datos se almacenarán, cómo se estructurarán y qué restricciones aplican.
- **Construcción**: Guardar físicamente los datos en un medio controlado por el DBMS.
- **Manipulación**: Incluir operaciones como:

  - **Consulta**: Recuperar información específica según criterios.
  - **Actualización**: Agregar, modificar o eliminar datos para reflejar cambios en el mundo real.
  - **Generación de informes**: Crear salidas estructuradas con fines analíticos o administrativos.
  - **Acceso concurrente**: Permitir que múltiples usuarios o procesos interactúen con los datos sin conflictos.

Las bases de datos son esenciales en negocios, salud, justicia, bibliotecas, comercio electrónico, sistemas financieros, IoT y más. Además, la tecnología de bases de datos permite automatizar tareas, reducir errores, proteger datos sensibles y facilitar la toma de decisiones estratégicas.

# Tipos de bases de datos (Enfoque técnico): SQL vs NoSQL
La clasificación principal de los DBMS se basa en los modelos de datos. A lo largo del tiempo, han surgido diferentes tipos de bases de datos, siendo los principales las bases de datos relacionales (SQL) y las bases de datos no relacionales (NoSQL).
El término NoSQL, acuñado a mediados/finales de la década de 2000, significa "no solo SQL" o "sin SQL", y a menudo se usa indistintamente con "no relacional".

## **Bases de datos relacionales (SQL)**

- Se basan en el **modelo relacional** propuesto por Edgar F. Codd en 1970.
- Utilizan **tablas** para almacenar datos y **relaciones** para establecer conexiones entre ellas. Las tablas están compuestas por un conjunto de **campos o columnas** y **registros o filas**. Las relaciones entre tablas se establecen mediante **claves primarias y claves foráneas**.
- El modelo relacional **normaliza** los datos en tablas y un **esquema define estrictamente** las tablas, filas, columnas, índices, relaciones y otras restricciones. La base de datos **impone la integridad referencial**.
- Se utiliza **Structured Query Language (SQL)** para crear y editar estas tablas relacionales. SQL es un lenguaje de consulta de alto nivel que puede especificar y recuperar muchos registros con una sola sentencia (orientado a conjuntos). A menudo especifica *qué* datos recuperar, no *cómo*. SQL incluye construcciones para definición de esquema (DDL), manipulación de datos (DML), definición de vistas (VDL), control de transacciones, seguridad y posibilidad de ser incrustado en otros lenguajes.
- Están diseñadas para **aplicaciones de procesamiento de transacciones en línea (OLTP) altamente coherentes y transaccionales**, y son buenas para procesamiento analítico en línea (OLAP).
- Ejemplos de motores comerciales: SQLite, MySQL, Microsoft SQL Server, Oracle, MariaDB.

## **Bases de datos no relacionales (NoSQL)**

- Surgieron para abordar desafíos de las aplicaciones modernas, como el **procesamiento de grandes volúmenes de datos de fuentes dispares** que no encajan perfectamente en el modelo relacional.
- **No requieren estructuras de datos fijas (tablas)** y proporcionan **esquemas flexibles** que permiten un desarrollo más rápido e iterativo.
- Ofrecen una **variedad de modelos de datos** optimizados para el rendimiento y la escala, como **clave-valor, documentos, gráficos y columnas**.
- Se utilizan en **entornos distribuidos** que requieren disponibilidad y operatividad constantes, gestionando **grandes volúmenes de datos**.
- Priorizan el **rendimiento por encima de una sólida coherencia de los datos** y mantener las relaciones (integridad referencial). Permiten un **escalado horizontal** mediante fragmentación de servidores. Soportan **datos semiestructurados y sin estructurar**.
- Las API suelen ser **basadas en objetos**, permitiendo almacenar y recuperar estructuras de datos fácilmente.
- Están diseñadas para **varios patrones de acceso a datos, incluyendo aplicaciones de baja latencia**.
  Los casos de uso típicos incluyen:
  - Aplicaciones móviles
  - IoT
  - Juegos
  - Aplicaciones web de alto rendimiento
  - Redes sociales
  - Motores de recomendaciones
  - Detección de fraude
  - Análisis sobre datos semiestructurados
- Ejemplos de motores:
  - MongoDB (orientado a documentos/ficheros)
  - Redis (clave-valor, usado para caché)
  - Amazon DynamoDB (clave-valor, rendimiento consistente)
  - Amazon Neptune (grafos)
  - Amazon OpenSearch Service (búsqueda, datos no estructurados/semiestructurados)

> Es posible emplear una combinación de bases de datos SQL y NoSQL en las aplicaciones (enfoque híbrido) para optimizar la relación precio-rendimiento para cada carga de trabajo.

# Tipos de bases de datos (Enfoque teórico): Según su variabilidad y Según su contenido

Las bases de datos pueden clasificarse de distintas formas.

## **Según su variabilidad**
- **Bases de datos estáticas**: Son aquellas cuyos datos **no pueden modificarse**, estando diseñadas especialmente para la **lectura** de sus datos. Suelen utilizarse para almacenar **datos históricos** que no cambiarán, realizar proyecciones estadísticas y ayudar a la toma de decisiones.
- **Bases de datos dinámicas**: A diferencia de las estáticas, sus datos **se pueden actualizar**, ya sea agregando, modificando o eliminando los mismos durante el transcurso del tiempo.

## **Según el contenido**
- **Relacionales**: Estructuran los datos en tablas interrelacionadas. Son el modelo predominante hoy.
- **Jerárquicas**: Organizan la información en forma de árbol, donde cada registro tiene un único padre. Usadas históricamente en sistemas legados.
- **De red**: Permiten relaciones más complejas (varios padres por nodo), siendo una evolución del modelo jerárquico.
- **Multidimensionales**: Optimizadas para análisis de grandes volúmenes (OLAP), representan datos en cubos de dimensiones múltiples.
- **Deductivas**: Incorporan lógica de inferencia para derivar nuevos datos a partir de reglas.
- **Bibliográficas**: Contienen referencias de documentos, comúnmente usadas en investigación académica.
- **Texto completo**: Permiten búsquedas y consultas sobre documentos extensos no estructurados.

> Estas clasificaciones no son excluyentes. Una misma base de datos puede combinar varias características según el sistema y sus objetivos.
