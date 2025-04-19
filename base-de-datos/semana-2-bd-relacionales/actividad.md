# Diseño de Base de Datos: Sistema Gestor de Ventas y Stock

## Consigna

Continuamos nuestro camino en el diseño de bases de datos, y esta semana nos enfocaremos en identificar los componentes fundamentales: las entidades y sus atributos.

Para esta actividad, los invito a pensar en un sistema de información sencillo que conozcan bien o que les resulte interesante. Describan brevemente este sistema y uno de sus procesos principales en no más de 10 renglones.

Luego, identifiquen y listen las entidades principales que participan en ese sistema, junto con algunos de los atributos relevantes que describen a cada una de esas entidades.

---

## Descripción del Sistema

Este sistema está diseñado para gestionar las ventas de productos en una tienda, así como el control de su inventario. Un proceso clave es el registro de las ventas realizadas por los vendedores, donde se asocia cada venta con un producto específico y se actualiza automáticamente el stock disponible. Además, se calcula la comisión correspondiente a cada vendedor en función de sus ventas.

## Entidades y Atributos

A continuación, se presentan las entidades principales del sistema, junto con algunos de sus atributos relevantes:

### Vendedores
- **ID_Vendedor** (clave primaria)
- **Nombre**
- **Apellido**
- **Comision**
- **Vacaciones**

### Productos
- **ID_Producto** (clave primaria)
- **Nombre**
- **Kg**
- **Precio**
- **Stock**

### Ventas
- **ID_Venta** (identificador)
- **ID_Vendedor** (clave foránea)
- **ID_Producto** (clave foránea)
- **Unidades**
- **Fecha_Venta**
- **Total**

