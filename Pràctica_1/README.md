# Pràctica 1: Càlcul del mcm i MCD

En aquesta pràctica programarem una aplicació en Python que permeti calcular el **mínim comú múltiple (mcm)** i el **Màxim Comú Divisor (MCD)** de dos o més nombres a partir de la seva **descomposició en factors primers**.

## Objectius

- Implementar un algorisme per descompondre nombres en factors primers.
- Utilitzar els factors primers per calcular el mcm i el MCD.
- Modularitzar el codi en diferents funcions. Cada funció té la seva pròpia funcionalitat.
- Escriure codi Python comentat.
- Optimitzar l'eficiència del codi.

## Enunciat

### Funcionalitat bàsica

Escriviu un programa que calculi el mcm i MCD de dos nombres. Aquests s'han de definir a partir d'una variable nombres. NO s'han de demanar a l'usuari. Exemple de la variable:

```python
nombres = [3,5]
```

Si cal, busca com calcular el mcm i MCD.

### Ampliació

Modifiqueu el programa perquè es calculi el mcm i el MCD de una llista amb una quantitat qualsevol de nombres.

## Estructura del projecte

- **Fitxer `main.py`:**
  - Importa les funcions del fitxer `funcions.py`.
  - Defineix una llista amb els nombres per calcular el mcm i el MCD.
  - Crida les funcions implementades i mostra els resultats.

- **Fitxer `funcions.py`:**
  - Conté les funcions necessàries.

## Exemples d’execució

### Funcionalitat bàsica (dos nombres)

**Entrada:**

```python
nombres = [12, 18]
```

**Sortida:**

```python
Donats els nombres 12 i 18, el seu mcm i MCD són:
mcm(12, 18) 36
MCD(12, 18) = 6
```
