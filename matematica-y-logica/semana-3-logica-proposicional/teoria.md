## Elementos de Lógica y Lógica Proposicional

La **lógica** es el estudio del razonamiento y la argumentación, centrándose en los principios de **inferencia válida** y el **buen juicio**. Nos ayuda a comprender cómo pensar y razonar de forma estructurada y sistemática.

En particular, la **lógica matemática** se ocupa del **razonamiento formal**, aplicando reglas y estructuras matemáticas para analizar proposiciones y argumentos. Este enfoque busca llegar a **conclusiones correctas y verificables**, lo cual es esencial en áreas como la informática, la inteligencia artificial, las bases de datos y los lenguajes de programación.

La **lógica proposicional** considera como unidades básicas a las **proposiciones**, las cuales pueden combinarse mediante **conectivos lógicos** para formar **argumentos válidos**. Una **proposición** es una **sentencia declarativa** que puede evaluarse como **verdadera (V) o falsa (F)**, pero no ambas al mismo tiempo. Este valor se conoce como **valor de verdad**.

Es importante señalar que las sentencias exclamativas, interrogativas o imperativas no son proposiciones, ya que no pueden ser calificadas como verdaderas o falsas. En lógica, las proposiciones suelen representarse mediante letras minúsculas como p, q o r. Estas pueden ser **simples** (sin conectivos) o **compuestas** (formadas por varias proposiciones mediante conectivos lógicos).

## Conectivos Lógicos

Los **conectivos lógicos** permiten combinar enunciados para formar proposiciones más complejas. Estos conectivos expresan relaciones entre proposiciones y son fundamentales para construir estructuras lógicas formales.

* La **negación (¬ o ㄱ)** es un operador **unitario** que invierte el valor de verdad de una proposición. Si una proposición p es verdadera, ¬p es falsa, y viceversa. En teoría de conjuntos, se asocia con el complemento: Aᶜ = {x | ¬(x ∈ A)}.

* La **conjunción (∧)** combina dos proposiciones, y el resultado es verdadero sólo si ambas lo son. Representa la intersección en teoría de conjuntos: A ∩ B = {x | x ∈ A ∧ x ∈ B}.

* La **disyunción (∨)** también combina dos proposiciones, pero es verdadera si al menos una de ellas lo es. Existen dos tipos:

  * **Disyunción inclusiva**: falsa solo si ambas proposiciones son falsas. Equivale a la unión en conjuntos: A ∪ B = {x | x ∈ A ∨ x ∈ B}.
  * **Disyunción exclusiva**: verdadera si solo una de las proposiciones es verdadera.

* La **implicación (⇒ o ⟶)** se expresa como “si p, entonces q”, donde p es el **antecedente** y q el **consecuente**. Es verdadera en todos los casos excepto cuando p es verdadera y q es falsa. Es clave distinguir entre la implicación y sus variantes:

  * **Recíproca**: q ⇒ p
  * **Inversa**: ¬p ⇒ ¬q
  * **Contrarrecíproca**: ¬q ⇒ ¬p (equivalente lógicamente a la implicación original)

* El **bicondicional (⇔)** indica que dos proposiciones son verdaderas o falsas al mismo tiempo. Se interpreta como “p si y solo si q” y equivale a la conjunción de la implicación y su recíproca: (p ⇒ q) ∧ (q ⇒ p).

Los conectivos lógicos poseen propiedades fundamentales como la **conmutatividad**, **asociatividad** y **distributividad**, además de estar relacionados con las **leyes de De Morgan**, que permiten transformar expresiones mediante negaciones. También se aplican **reglas de precedencia** para evitar ambigüedades: primero ¬, luego ∧, ∨, ⇒ y finalmente ⇔.

## Tablas de Verdad

Las **tablas de verdad** permiten visualizar de forma sistemática cómo se comporta una proposición compuesta en función de los valores de verdad de sus componentes. Son especialmente útiles para evaluar proposiciones complejas y verificar equivalencias lógicas.

Cada conectivo tiene su propia tabla, desde la negación hasta el bicondicional, incluyendo variaciones como la contrarrecíproca. Al listar todas las combinaciones posibles de valores de verdad, se puede verificar la validez de argumentos o demostrar tautologías.

## Formas Normales: Conjuntiva y Disyuntiva

Las **formas normales** son representaciones estandarizadas de proposiciones compuestas. Facilitan su análisis lógico, especialmente en procesos de automatización y en lógica computacional.

* La **forma normal conjuntiva (FNC)** es una conjunción de disyunciones. Por ejemplo:
  (p ∨ q) ∧ (¬r ∨ s)

* La **forma normal disyuntiva (FND)** es una disyunción de conjunciones. Por ejemplo:
  (p ∧ ¬q) ∨ (r ∧ s)

Ambas formas permiten estructurar expresiones complejas de manera que puedan ser manipuladas de forma más sistemática. Existen algoritmos para convertir proposiciones arbitrarias a su forma normal equivalente.

## Validez

Un **argumento válido** es aquel cuya **conclusión se deriva lógicamente de las premisas**. La lógica proposicional proporciona un marco riguroso para evaluar esta validez.

En matemáticas, los enunciados como teoremas o lemas requieren **demostraciones** que aseguren que si las hipótesis son ciertas, la conclusión también lo es. Estas demostraciones pueden ser **directas** (se parte de las premisas y se llega a la conclusión) o **indirectas** (se asume la negación de la conclusión y se busca una contradicción).

Además, para refutar una afirmación general (especialmente cuando incluye cuantificadores), puede usarse un **contraejemplo**, es decir, un caso en el que las hipótesis se cumplen pero la conclusión no.
