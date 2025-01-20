# Pràctica 3: Comptar i Ordenar

En aquesta pràctica desenvoluparem un programa en Python per generar una llista de nombres aleatoris, comptar quantes vegades apareix cada nombre, i ordenar la llista en ordre creixent sense repeticions, **sense utilitzar funcions predefinides com `list.count` o `sort`**. Implementarem aquestes funcionalitats manualment.

## Objectius

- Aprendre a gestionar llistes i bucles per analitzar i manipular dades.
- Desenvolupar habilitats per desenvolupar algorismes i optimitzar-los.

## Enunciat

### Generar llista aleatoria

Creeu la funció `genera_llista(rang, longitud)`. Aquesta crea una llista de nombres enters aleatoris dins d'un rang determinat i amb una longitud especificada. Podeu utilitzar la llibreria `random` per a aquesta part.

### Comptatge de repeticions

Creeu la funció `compta_repeticions(llista)`. Aquesta compata quantes vegades apareix cada element en la llista. Una mica d'indicacions:

- Recorreu la llista amb un bucle `for` per comptar quantes vegades apareix cada nombre.
- Utilitzeu un segon bucle per recórrer la llista completament per a cada element, comptant les repeticions. Això us portarà a tenir un **bucle dins d’un bucle** amb dos índexs diferents.
- Per ajudar-vos, imprimiu per pantalla el nombre i el seu recompte a mesura que es descobreix. Després podeu borrar aquests prints.
- Retorna dues llistes una amb els elements sense repetir i una altra amb el nombre de repeticcions corresponent a cada element de la primera llista.

```python
return llista_elements, num_repeticions
```

Exemple:

```python
llista = [1, 1, 3, 2, 3, 3, 3]

llista_elements, num_repeticions = compta_repeticions(llista)

# llista_elements = [1, 3, 2]
# num_repeticions = [2, 4, 1]

```

### Millorem el recompte

Modifiqueu el programa per assegurar-vos que cada nombre només es compta una vegada, encara que aparegui diverses vegades. D'aquesta manera s'optimitza el codi de manera que evitem tornar a comptar els nombres repetits i que ja han estat comtpats.

### Ordenació manual

Creeu la funció `ordena_manual(llista)` que retorna la llista ordenada, tant si hi ha elements repetits com si no. Aquesta ha d'ordenar la llista resultant en ordre creixent sense utilitzar la funció `sort`. Per ajudar-vos, imprimiu per pantalla la llista ordenada, sense repeticions. Després podeu borrar aquests prints.

### Ampliació

Modifica la funció anterior de manera que puguis indicar si vols que s'ordeni de manera creixent o decreixent. Ara la funció serà `ordena_manual(llista, creix)` on tu tries quin tipus de variable pot ser `creix` per tal d'indicar el tipus d'ordenació.

## Estructura del projecte

### Fitxer `main.py`

- Executa el programa principal. Importa funcions des del fitxer `funcions.py`.
- Conté la lògica per generar la llista, comptar els elements i ordenar-los.

### Fitxer `funcions.py`

Defineix les funcions següents:

- `genera_llista(rang, longitud)`: genera una llista de nombres aleatoris.
- `compta_repeticions(llista)`: compta les repeticions sense utilitzar `count`.
- `ordena_manual(llista)`: ordena la llista sense utilitzar `sort`.

## Exemples d'execució

### En el `main.py`

```python
rang = 3 # Els nombres poden anar de l'1 al 3.
longitud = 5 # La llista estarà composta per 5 elements.

llista = genera_llista(rang, longitud)

print(f'La llista inicial és: {llista}')

llista_elements, num_repeticions = compta_repeticions(llista)

print(f'Elements que formen la llista: {llista_elements}')
print(f'Nombre de repeticions de cada element de la llista: {num_repeticions}')

llista_ordenada = ordena_manual(llista_elements)

print(f'Llista d\'elements ordenada: {llista_ordenada}')

llista_ordenada = ordena_manual(llista_elements)

print(f'Llista ordenada: {llista_ordenada}')
```

### Sortida per pantalla

```bash
La llista inicial és: [3, 3, 2, 1, 2]
Elements que formen la llista: [3, 2, 1]
Nombre de repeticions de cada element de la llista: [2, 2, 1]
Llista d'elements ordenada: [1, 2, 3]
Llista ordenada: [1, 2, 2, 3, 3]
```
