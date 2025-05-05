# 1. Conceptos Fundamentales

## 1.1 Código Fuente

* Considerado un **activo valioso** en el desarrollo de software.
* Es la **materialización del conocimiento, creatividad y experiencia** del equipo de desarrollo.
* Su **calidad y estructura** son críticas para el mantenimiento y la evolución de un producto.

**Importancia:**

* **Motor de Innovación:** Permite implementar nuevas ideas y soluciones.
* **Mantenimiento y Evolución:** Facilita la corrección de errores, adición de características y adaptación a cambios.
* **Reutilización y Eficiencia:** Puede ser aprovechado en múltiples proyectos.
* **Protección Intelectual:** Ofrece una ventaja competitiva.
* **Colaboración y Escalabilidad:** Permite a varios desarrolladores trabajar simultáneamente.

## 1.2 Control de Código Fuente

* Es el **proceso o práctica para gestionar y registrar cambios** en el código fuente.
* Fundamental para la **integridad y evolución del software**, especialmente en equipos colaborativos.
* Steve McConnell lo considera **esencial para el éxito** de cualquier proyecto.

**Ventajas:**

* **Registro Histórico:** Mantiene un historial detallado de todos los cambios.
* **Preservación de Conocimiento:** Conserva el contexto (quién, qué, por qué) de los cambios.
* **Acceso a Versiones Anteriores:** Permite revertir a estados pasados.
* **Trabajo Colaborativo:** Facilita la gestión de contribuciones de varios miembros.
* **Seguridad y Protección:** Protege el código contra pérdidas y asegura copias de cada versión.

## 1.3 Sistemas de Control de Versiones (VCS)

* Son **herramientas** que gestionan y registran los cambios en el código fuente.
* Esenciales para el **trabajo colaborativo y mantener la integridad** del software.

**Características de los VCS modernos:**

* **Distribución y Descentralización**
* **Ramas y Fusiones Eficientes**
* **Alta Trazabilidad**
* **Seguridad y Respaldo**
* **Colaboración**
* **Integración con Otras Herramientas**

# 2. Git en Detalle

## 2.1 Introducción a Git

* **Sistema de control de versiones distribuido**.
* Creado por **Linus Torvalds** en 2005.
* Ideal para **desarrollo paralelo, seguimiento de cambios e integridad** del código.
* Popularizado por **GitHub, GitLab y Bitbucket**.
* **Características:**
  * **Distribución completa**
  * **Ramas eficientes**
  * **Trazabilidad con SHA-1**
  * **Alta integridad**
  * **Colaboración efectiva**

## 2.2 Repositorios en Git

* Son **directorios con historial completo del código fuente**.

**Tipos de repositorio:**

* **Local:** Trabajar sin conexión.
* **Remoto:** Colaboración y respaldo (GitHub, etc.).

**Comandos:**

* `git init`: Inicializa nuevo repositorio vacío.
* `git clone`: Clona uno existente desde remoto.

## 2.3 Flujo de Trabajo y Áreas de Git

**Áreas principales:**

1. **Área de Trabajo:** Donde editas archivos.
2. **Staging Area (INDEX):** Lista de cambios listos para confirmar.
3. **Repositorio Local (HEAD):** Almacena confirmaciones.
4. **Repositorio Remoto:** Copia segura y compartida.

**Comandos:**

* `git status`, `git add`, `git reset`, `git commit`, `git push`, `git pull`

## 2.4 Cómo Guardar (Confirmar) Cambios

1. Realizar cambios.
2. Agregar al área de preparación (`git add`).
3. Confirmar con `git commit`.
4. Enviar al remoto con `git push` (opcional).

## 2.5 Cómo Inspeccionar Cambios

* `git status`: Ver estado del proyecto.
* `git log`: Historial de commits.

**Opciones útiles:**

* `--oneline`, `--pretty=format`, `--author`, `--since`, `--grep`, `-n`

## 2.6 Cómo Deshacer Cambios

### `git reset`

* Para cambios **locales** no compartidos.
* Tipos:
  * `--soft`: Mantiene en staging.
  * `--mixed`: Mantiene en área de trabajo.
  * `--hard`: Borra todo (**irreversible**).

### `git revert`

* Para deshacer **cambios compartidos**.
* Crea un commit que revierte otro.
* Mantiene historial intacto.

## 2.7 Cómo Reescribir el Historial

### `git commit --amend`

* Modifica el último commit.
* Útil para correcciones rápidas.

### `git rebase`

* Reorganiza o limpia historial.
* `git rebase -i`: Interactivo, permite:
  * `pick`, `reword`, `edit`, `squash`, `drop`
* Mejora legibilidad del historial.

---

# 3. Tabla Resumen de Comandos Clave

| Comando Git         | Propósito principal                             | ¿Destruye historial? | Uso común                         |
|---------------------|--------------------------------------------------|----------------------|------------------------------------|
| `git add`           | Agregar cambios al staging                      | No                   | Preparar archivos para commit     |
| `git commit`        | Guardar cambios en el repositorio local         | No                   | Confirmar una versión             |
| `git reset`         | Retroceder a un estado anterior (destructivo)   | Sí (a veces)         | Corregir commits locales          |
| `git revert`        | Crear un commit que revierte otro               | No                   | Deshacer cambios compartidos      |
| `git rebase`        | Reescribir historial de manera lineal           | Sí (con cuidado)     | Limpiar o reorganizar historial   |
| `git push`          | Enviar cambios al repositorio remoto            | No                   | Compartir código con el equipo    |
| `git pull`          | Traer y combinar cambios del repositorio remoto | No                   | Mantener actualizado el local     |
| `git log`           | Ver historial de commits                        | No                   | Auditoría y trazabilidad          |
| `git status`        | Ver estado actual del área de trabajo           | No                   | Saber qué falta confirmar         |
