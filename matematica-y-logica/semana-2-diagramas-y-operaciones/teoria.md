## 🔵 Diagrama de Venn

Los **diagramas de Venn** son representaciones gráficas utilizadas para mostrar las relaciones entre conjuntos. Cada conjunto se representa como una figura cerrada (generalmente círculos), y las zonas de superposición indican los elementos comunes.

Ejemplo:  
- Si A = {1, 2, 3} y B = {3, 4, 5}, el diagrama mostrará el "3" en la intersección de los conjuntos A y B.

## 🔶 Subconjuntos

Un **subconjunto** es un conjunto cuyas partes están incluidas totalmente en otro conjunto.

- Si todos los elementos de A están en B, se dice que A ⊆ B.
- Si A tiene al menos un elemento que no está en B, entonces A ⊄ B.

### 🔸 Intervalos de Números Reales

Los **intervalos** son subconjuntos de los números reales ℝ que contienen todos los números comprendidos entre dos extremos.

- Intervalo **abierto**: (a, b) → no incluye extremos.
- Intervalo **cerrado**: [a, b] → incluye ambos extremos.
- Semiabiertos o semicerrados: (a, b], [a, b)
- Intervalos infinitos: (−∞, b), [a, ∞), etc.

### 🔸 El Conjunto de Partes

El **conjunto de partes** (o conjunto potencia) de un conjunto A, denotado como 𝒫(A), es el conjunto de todos los subconjuntos posibles de A, incluyendo el conjunto vacío ∅ y el conjunto A mismo.

- Si A tiene *n* elementos, entonces 𝒫(A) tiene 2ⁿ subconjuntos.

Ejemplo:
- A = {x, y} → 𝒫(A) = {∅, {x}, {y}, {x, y}}

## 🟢 Operaciones entre Conjuntos

### 🔹 Unión (A ∪ B)

Reúne todos los elementos que están en A, en B o en ambos.

Ejemplo:  
A = {1, 2}, B = {2, 3} → A ∪ B = {1, 2, 3}

### 🔹 Intersección (A ∩ B)

Incluye solo los elementos que están tanto en A como en B.

Ejemplo:  
A = {1, 2}, B = {2, 3} → A ∩ B = {2}

### 🔹 Complemento (Aᶜ)

El complemento de A es el conjunto de elementos que están en el universo U pero **no** en A.

Ejemplo:  
U = {1, 2, 3, 4}, A = {1, 3} → Aᶜ = {2, 4}

### 🔹 Diferencia (A − B)

Incluye los elementos que están en A pero no en B.

Ejemplo:  
A = {1, 2, 3}, B = {2, 3, 4} → A − B = {1}

## 📐 Propiedades de las Operaciones

- **Conmutativa**:  
  A ∪ B = B ∪ A  
  A ∩ B = B ∩ A

- **Asociativa**:  
  A ∪ (B ∪ C) = (A ∪ B) ∪ C  
  A ∩ (B ∩ C) = (A ∩ B) ∩ C

- **Distributiva**:  
  A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)  
  A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)

- **Ley de De Morgan**:  
  (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ  
  (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ

## 🧮 Producto Cartesiano

El **producto cartesiano** de dos conjuntos A y B, denotado A × B, es el conjunto de todos los pares ordenados (a, b) donde a ∈ A y b ∈ B.

Ejemplo:  
Si A = {1, 2} y B = {a, b} →  
A × B = {(1, a), (1, b), (2, a), (2, b)}

Se utiliza, por ejemplo, para representar relaciones entre elementos y en la definición de funciones.
