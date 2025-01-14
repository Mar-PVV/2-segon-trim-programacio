# Pràctica 2: Temps de Càlcul del Màxim Comú Divisor

En aquesta pràctica programarem una aplicació en Python per representar gràficament el temps de càlcul del **màxim comú divisor (MCD)** entre parelles de nombres enters utilitzant l'[algorisme d'Euclides](https://ca.wikipedia.org/wiki/Algorisme_d%27Euclides). Utilitzarem llibreries gràfiques per visualitzar el nombre d’iteracions necessàries per calcular el MCD com una funció dels dos nombres, utilitzant diferents colors per indicar el nombre de passos.

## Objectius

- Implementar una funció per calcular el MCD entre dos nombres que també compti el nombre d'iteracions necessàries utilitzant l'algorisme d'Euclides.
- Emmagatzemar i gestionar dades en llistes per representar informació gràfica.
- Utilitzar la llibreria `matplotlib` per crear un gràfic de dispersió (`scatter plot`) que visualitzi el temps de càlcul.
- Modularitzar el codi en diferents funcions. Cada funció té la seva pròpia funcionalitat.
- Escriure codi Python comentat.
- Optimitzar l'eficiència del codi.

## Enunciat

### Funcionalitat bàsica

1. Escriviu una funció que, donats dos nombres enters, `a` i `b`, calculi el MCD i retorni el nombre d’iteracions necessàries. (Funció `iteracions_MCD_Euclides(a,b)`)
2. Executeu la funció per totes les parelles de nombres enters `(i, j)` per valors de `i` i `j` entre `0` i `10`. Emmagatzemeu:
   - Els valors de `i` en una llista `x`
   - Els valors de `j` en una llista `y`
   - El nombre d’iteracions per cada parella en una llista `z`
3. Utilitzeu la funció `plt.scatter(x, y, c=z)` per representar gràficament el resultat.

4. Repetiu els càlculs amb una malla més gran (per exemple, valors de `i` i `j` entre `0` i `20`, `0` i `50`...).

5. Observeu i analitzeu la distribució dels punts i els patrons visibles segons el nombre d'iteracions.

## Estructura del projecte

### Fitxer `main.py`

- Importa les funcions des del fitxer `funcions.py`.
- Crida les funcions `iteracions_MCD_Euclides(a,b)` i `plt.scatter(x, y, c=z)`
- Defineix la lògica per calcular el MCD per totes les parelles de nombres en un rang donat.

### Fitxer `funcions.py`

- Conté la funció `iteracions_MCD_Euclides(a,b)` que calcula el MCD utilitzant l'algorisme d'Euclides i retorni el nombre d'iteracions.
