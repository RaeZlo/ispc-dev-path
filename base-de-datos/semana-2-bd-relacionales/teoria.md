# 🗂️ Bases de Datos Relacionales

## 📌 Origen y Concepto
- Se basan en el **modelo relacional** propuesto por *Edgar F. Codd* en **1970**.
- Organizan la información en **tablas** o relaciones.
- Cada tabla contiene:
  - **Filas (registros)**: representan instancias individuales.
  - **Columnas (atributos)**: representan las características de los registros.
- Cada tabla debe tener un **nombre único** dentro de la base de datos.

## 🔑 Claves Primarias y Foráneas

### ✅ Clave Primaria
- Identifica **únicamente** cada registro en una tabla.
- Sus valores **no se repiten**.
- Ejemplo: ID de usuario.

### 🔁 Clave Foránea
- Establece relaciones con otra tabla (**tabla padre**).
- Se coloca en la **tabla hija**.
- Sus valores **pueden repetirse**, pero deben:
  - Existir en la tabla padre.
  - Ser del **mismo tipo de dato** que la clave primaria correspondiente.

### 🧾 Ejemplo de Base de Datos Relacional

#### **Tabla: Usuarios**

| ID (PK) | Nombre     |
|---------|------------|
| 1       | Ana Pérez  |
| 2       | Juan Soto  |
| 3       | Marta Ruiz |

#### **Tabla: Pedidos**

| ID_Pedido (PK) | ID_Usuario (FK) | Fecha       |
|----------------|------------------|-------------|
| 1001           | 1                | 2025-04-10  |
| 1002           | 2                | 2025-04-11  |
| 1003           | 1                | 2025-04-12  |

## ⚙️ Ventajas
- **Simplicidad** en su diseño.
- **Flexibilidad** para estructurar los datos.
- **Integridad y consistencia** de la información:
  - Garantiza que los datos sean **precisos, coherentes y confiables**.

## ⚠️ Limitaciones
- En entornos con **alta demanda** o **grandes volúmenes de datos**:
  - Pueden surgir **problemas de rendimiento y escalabilidad**.
  - El uso excesivo de relaciones puede **ralentizar el acceso a los datos**.

---

# 📦 Bases de Datos No Relacionales (NoSQL)

## 🔍 Características principales
- Basadas en **modelos distintos al relacional**.
- Ofrecen **alta flexibilidad** y **gran escalabilidad**.
- Ideales para aplicaciones con:
  - **Grandes volúmenes de datos**.
  - **Alta demanda de rendimiento**.

## 🧩 Tipos de Modelos NoSQL

### 📄 Modelo de Documentos
- Almacena datos en documentos estructurados: **JSON, XML o BSON**.
- Permite guardar **datos complejos o no estructurados**.
- Muy usado en:
  - Aplicaciones **web**.
  - Aplicaciones **móviles**.

### 🔗 Modelo de Grafos
- Representa los datos como **nodos (entidades)** y **relaciones (conexiones)**.
- Perfecto para modelar **relaciones complejas**.
- Ejemplo de uso: **Redes sociales**, recomendaciones, motores de búsqueda.

### 🗝️ Modelo Clave-Valor
- Almacena datos como pares **clave → valor**.
- Muy eficiente para accesos rápidos.
- Altamente escalable.
- Común en:
  - Aplicaciones **web en tiempo real**.
  - Sistemas con **alto rendimiento**.

## ⚖️ Ventajas vs. Desventajas

### ✅ Ventajas
- **Escalabilidad horizontal** (fácil de distribuir en varios servidores).
- **Flexibilidad** en el tipo y estructura de los datos.
- **Rendimiento** superior en escenarios específicos.

### ❌ Desventajas
- **Mayor complejidad en la administración**.
- **Menor nivel de integridad y consistencia** comparado con bases relacionales.

## 🧠 ¿Cuándo elegir qué tipo?

| Tipo de base de datos       | Ideal para...                                                                 |
|----------------------------|------------------------------------------------------------------------------|
| **Relacional (SQL)**        | Aplicaciones que requieren **alta integridad y consistencia**.              |
| **No Relacional (NoSQL)**   | Aplicaciones con **muchos datos**, **cambios frecuentes en la estructura** o **gran carga de usuarios**. |

---

# 🧰 Sistemas de Gestión de Bases de Datos (SGBD)

Es un software diseñado para crear, administrar y mantener bases de datos. Actúa como un intermediario entre los usuarios o aplicaciones y los datos almacenados, permitiendo la creación, modificación, eliminación y consulta de datos. Además, gestiona aspectos clave como seguridad, control de acceso, integridad de los datos, recuperación ante fallos, y optimización de consultas.

## 🧱 Estructura interna de los SGBD
- **Nivel Interno o Físico**:  
  Se refiere a cómo se almacenan los datos en el sistema, incluyendo detalles sobre los archivos, métodos de acceso, tipos de registros y la longitud de los campos. Es el nivel más cercano al hardware y tiene como objetivo optimizar el almacenamiento y la eficiencia en el acceso a los datos. Este nivel es responsabilidad de los administradores de la base de datos.
- **Nivel Conceptual**:  
  Define la estructura lógica de la base de datos, es decir, cómo se organiza la información de forma abstracta, sin importar cómo se almacena físicamente. En este nivel se describen las entidades, atributos, relaciones, operaciones y restricciones que forman la base de datos. Su objetivo es proporcionar un modelo general y coherente de la base de datos, sin preocuparse por los detalles técnicos de almacenamiento. Los diseñadores o analistas de bases de datos son los encargados de este nivel.
- **Nivel Externo o de Visión**:  
  Representa la forma en que los usuarios ven los datos. Cada grupo de usuarios o aplicación tiene su propia vista de los datos, también conocida como esquema externo. En este nivel, los usuarios no necesitan conocer la estructura interna o las relaciones complejas de la base de datos, ya que se les presenta una interfaz amigable y específica según sus necesidades. Este nivel está a cargo de los programadores, quienes siguen las directrices de los analistas de bases de datos para crear las vistas adecuadas para los usuarios finales.

## ⚙️ Modo de funcionamiento de los SGBD

El modo de funcionamiento de los SGBD se puede dividir en tres fases: la fase de definición DDL, la fase de manipulación DML y la fase de control de acceso DCL.

- **Lenguaje de Definición de Datos (DDL)**:  
  Este lenguaje se usa para crear y modificar la estructura de la base de datos, como las tablas y relaciones entre los datos. Permite a los administradores y diseñadores definir cómo deben organizarse los datos y sus características.

- **Lenguaje de Manipulación de Datos (DML)**:  
  Es el lenguaje que usan los usuarios para trabajar con los datos. Permite hacer operaciones como buscar, agregar, eliminar o modificar información en la base de datos. Hay dos tipos: los lenguajes procedurales, donde el programador especifica las operaciones detalladamente, y los no procedurales, como SQL, que permiten hacer consultas de forma más sencilla.

- **Lenguaje de Control de Datos (DCL)**:  
  Este lenguaje se utiliza para controlar quién tiene acceso a los datos y qué operaciones pueden realizar. Los administradores lo usan para gestionar la seguridad, como dar permisos de lectura o escritura a ciertos usuarios.
