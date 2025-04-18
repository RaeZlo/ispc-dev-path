# **Sistema de Información (SI)**
Un **sistema de información** es un conjunto organizado de **personas, procesos y herramientas** que se utilizan para 
**recolectar, clasificar, procesar, almacenar y recuperar datos e información** de forma rápida y eficiente.

Estos sistemas están formados por **recursos interconectados**, que trabajan en conjunto con un propósito informativo específico, 
como puede ser procesar estadísticas, organizar archivos o ayudar en la toma de decisiones. Los recursos pueden ser:
- Humanos  
- Hardware (equipos)  
- Software (programas)  
- Datos  
- Actividades o procesos  

Aunque muchas veces se asocian con la tecnología, **no todos los sistemas de información son sistemas informáticos**. La informática puede ser una parte importante, pero también son fundamentales la organización, las personas y los procesos.  
Los sistemas de información se usan en una gran variedad de contextos: empresas, gobiernos, universidades, museos, bibliotecas, redes sociales o aplicaciones digitales.

---

## **Tipos de Sistemas de Información**
### 🧾 **1. TPS – Sistemas de Procesamiento de Transacciones**
**¿Qué hacen?**  
Registran y gestionan las **transacciones cotidianas** de una empresa. Se centran en operaciones básicas del día a día.
**Ejemplos:**
- Registrar una venta en una tienda  
- Procesar un pago con tarjeta de crédito  
- Actualizar inventario después de una compra  
- Cargar horarios o datos logísticos
**Tip para recordarlo:**  
Piensa en las cosas que pasan **todos los días** en una empresa: vender, comprar, pagar... ¡eso lo maneja el TPS!

### 📊 **2. MIS – Sistemas de Información Gerencial**
**¿Qué hacen?**  
Organizan y resumen **información interna** para ayudar a los gerentes de nivel medio a **planificar, gestionar y tomar decisiones**.
**Ejemplos:**
- Informes de ventas mensuales  
- Estadísticas de producción  
- Presupuesto e inventarios  
- Gráficos de desempeño de empleados
**Tip para recordarlo:**  
MIS = “Resumen de lo que pasa adentro de la empresa” → ideal para gerentes que toman decisiones basadas en datos internos.

### 📈 **3. DSS – Sistemas de Soporte a Decisiones**
**¿Qué hacen?**  
Analizan datos **internos y externos** para ayudar a tomar **decisiones complejas**. Usan modelos, análisis de escenarios y comparaciones.
**Ejemplos:**
- Analizar si conviene abrir una nueva sucursal  
- Comparar proveedores  
- Evaluar costos vs. beneficios  
- Simular “¿qué pasaría si…?”
**Tip para recordarlo:**  
DSS = “Tomo decisiones difíciles” → me ayuda a elegir la mejor opción usando muchos datos y análisis.

### 🧠 **4. EIS – Sistemas de Información Ejecutiva**
**¿Qué hacen?**  
Brindan información **clave y estratégica** (interna y externa) a los **altos directivos** para que tengan una visión general rápida de la empresa.
**Ejemplos:**
- Dashboards con indicadores clave  
- Comparaciones entre regiones o áreas  
- Tendencias del mercado y situación económica o política
**Tip para recordarlo:**  
EIS = “Vista desde arriba” → para ejecutivos que necesitan saber **cómo va todo**, sin meterse en los detalles.

---

## 📦 **Almacenamiento de Datos**
El **almacenamiento de datos** es el proceso de **guardar y conservar información digital**, ya sea en **dispositivos físicos** 
(como discos duros) o en la **nube** (almacenamiento remoto a través de internet).

## 🔍 **Tipos de Almacenamiento de Datos**
### 1. 🗂️ **Almacenamiento de Archivos**
- **Definición**: Organiza los datos en un sistema jerárquico de archivos y carpetas.  
- **Funcionamiento**:  
  - Datos → Archivos  
  - Archivos → Carpetas  
  - Carpetas → Directorios/Subdirectorios  
- **Uso común**: Entornos donde los usuarios acceden a archivos específicos de forma manual, como documentos, imágenes, PDFs, etc.
### 2. 🧱 **Almacenamiento en Bloque**
- **Definición**: Divide los datos en bloques individuales, cada uno con un identificador único.  
- **Ventajas**:  
  - Alta velocidad  
  - Mayor eficiencia  
  - Confiabilidad en transferencias de datos  
- **Uso común**:  
  - Bases de datos  
  - Aplicaciones empresariales críticas  
  - Máquinas virtuales
### 3. 🧩 **Almacenamiento de Objetos**
- **Definición**: Ideal para manejar grandes volúmenes de datos **no estructurados**.  
- **Ejemplos de datos no estructurados**:
  - Correos electrónicos  
  - Videos y fotos  
  - Archivos de audio  
  - Páginas web  
  - Datos de sensores  
- **Ventajas**: Escalabilidad, accesibilidad y eficiencia en el manejo de contenido multimedia y web.

## ☁️ **Nota adicional: Almacenamiento en la Nube**
- **La nube** permite almacenar cualquier tipo de dato en servidores remotos accesibles desde internet.  
- Puede incorporar cualquiera de los tres tipos anteriores (archivos, bloques, objetos), según el proveedor y el caso de uso.

---

## 🔎 **Diferencia entre Datos e Información**
### 📊 **Datos**
- Son **elementos básicos**, sin procesar.  
- Por sí solos **no tienen significado**.  
- Ejemplo: `32°C` (sin contexto, solo un número con unidad).
### 💡 **Información**
- Es el resultado de **procesar, organizar y contextualizar** los datos.  
- Tiene **sentido, relevancia y utilidad** para quien la interpreta.  
- Debe ser:  
  ✅ Útil  
  ✅ Actual  
  ✅ Confiable  
- Ejemplo: `32°C en Buenos Aires el 15 de enero a las 14 hs` → ahora **sabemos** el clima en un lugar y momento específico.

## ⚙️ **Relación entre datos e información**
- Los **datos** son la materia prima.  
- La **información** es el producto final tras el procesamiento de esos datos.  
- Todo sistema informático busca **administrar los datos** para generar **información útil**, que apoye la **toma de decisiones**.

## 📌 **Ejemplo práctico**

| Dato | Información |
|------|-------------|
| 32°C | Temperatura actual en Ciudad de México a las 13:00 hrs |
| 1013 hPa | Presión atmosférica para análisis meteorológico |
| 80% | Humedad relativa para prever condiciones climáticas |

---

# **Base de Datos**
Es un conjunto organizado de datos almacenados de forma estructurada en un sistema informático. La estructura de la base de datos permite 
almacenar, gestionar y recuperar información de manera eficiente. Existen diferentes modelos de bases de datos, como el relacional 
(organizado en tablas), no relacional (almacena datos sin un esquema fijo, como en documentos o claves-valor) y orientado a objetos 
(donde los datos se representan como objetos), que definen cómo se organizan, almacenan y acceden a los datos.

## 🗄️ **Tipos de Bases de Datos**
Las bases de datos pueden clasificarse según **la variabilidad** de los datos o según **el contenido** que manejan.

### 📌 **Según su Variabilidad**
#### 1. 🧊 **Bases de Datos Estáticas**
- **Características**:  
  - Los datos **no se modifican**.  
  - Diseñadas para **consulta y lectura**.  
  - Se utilizan para:  
    - Almacenar **datos históricos**.  
    - Realizar **análisis estadísticos**.  
    - **Apoyar la toma de decisiones**.
#### 2. 🔁 **Bases de Datos Dinámicas**
- **Características**:  
  - Los datos **se pueden actualizar** (agregar, modificar o eliminar).  
  - Permiten el trabajo con **información en tiempo real**.  
  - Se usan en **sistemas activos**, como sitios web, aplicaciones, etc.

### 📌 **Según su Contenido**
Se clasifican de acuerdo con el tipo de información que priorizan.

- Bases de datos jerárquicas: Organizan los datos en una estructura de árbol, con relaciones padre-hijo. Cada hijo tiene un único padre.
- Bases de datos de red: Similar a las jerárquicas, pero permiten relaciones más complejas: un hijo puede tener varios padres.
- Bases de datos deductivas: Permiten realizar inferencias lógicas a partir de los datos almacenados, usando reglas y hechos.
- Bases de datos multidimensionales: Diseñadas para analizar grandes volúmenes de datos desde distintas perspectivas (por ejemplo, ventas por región, tiempo, producto).
- Bases de datos bibliográficas: Almacenan referencias a documentos como libros, artículos, tesis, etc., sin contener el texto completo.
- Bases de datos de texto completo: Almacenan documentos en su totalidad, permitiendo búsquedas dentro del contenido textual.
- Bases de datos relacionales: Organizan los datos en tablas relacionadas entre sí mediante claves. Es el modelo más común en aplicaciones actuales.
