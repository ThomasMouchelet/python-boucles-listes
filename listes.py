# =============================================================================
#                           TUTORIEL PYTHON : LES LISTES
# =============================================================================
# Les listes sont des collections ordonnées et modifiables d'éléments.
# Elles peuvent contenir des éléments de types différents.
# =============================================================================


# =============================================================================
# 1. CRÉATION DE LISTES
# =============================================================================

print("=" * 60)
print("1. CRÉATION DE LISTES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1.1 Différentes façons de créer une liste
# -----------------------------------------------------------------------------
print("\n--- 1.1 Création de listes ---")

# Liste vide
liste_vide = []
liste_vide2 = list()
print(f"Liste vide : {liste_vide}")

# Liste avec des éléments
nombres = [1, 2, 3, 4, 5]
print(f"Liste de nombres : {nombres}")

# Liste avec différents types
mixte = [1, "deux", 3.0, True, None]
print(f"Liste mixte : {mixte}")

# Liste de listes (liste imbriquée)
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrice : {matrice}")

# Création avec range()
de_zero_a_neuf = list(range(10))
print(f"Avec range(10) : {de_zero_a_neuf}")

# Création avec multiplication
cinq_zeros = [0] * 5
print(f"[0] * 5 : {cinq_zeros}")

# Création avec compréhension de liste
carres = [x**2 for x in range(1, 6)]
print(f"Carrés de 1 à 5 : {carres}")


# =============================================================================
# 2. ACCÈS AUX ÉLÉMENTS (INDEXATION)
# =============================================================================

print("\n" + "=" * 60)
print("2. ACCÈS AUX ÉLÉMENTS")
print("=" * 60)

# -----------------------------------------------------------------------------
# 2.1 Index positifs et négatifs
# -----------------------------------------------------------------------------
print("\n--- 2.1 Indexation ---")

fruits = ["pomme", "banane", "orange", "fraise", "kiwi"]
print(f"Liste : {fruits}")
print(f"Index :    0        1         2        3       4")
print(f"Index : -5       -4        -3       -2      -1")

print(f"\nfruits[0] = {fruits[0]}")       # Premier élément
print(f"fruits[2] = {fruits[2]}")         # Troisième élément
print(f"fruits[-1] = {fruits[-1]}")       # Dernier élément
print(f"fruits[-2] = {fruits[-2]}")       # Avant-dernier

# -----------------------------------------------------------------------------
# 2.2 Slicing (découpage)
# -----------------------------------------------------------------------------
print("\n--- 2.2 Slicing [debut:fin:pas] ---")

print(f"Liste originale : {fruits}")
print(f"fruits[1:4] = {fruits[1:4]}")       # Index 1, 2, 3
print(f"fruits[:3] = {fruits[:3]}")         # Du début à l'index 2
print(f"fruits[2:] = {fruits[2:]}")         # De l'index 2 à la fin
print(f"fruits[::2] = {fruits[::2]}")       # Un élément sur deux
print(f"fruits[::-1] = {fruits[::-1]}")     # Liste inversée

# Copie d'une liste avec slicing
copie = fruits[:]
print(f"\nCopie avec [:] : {copie}")


# =============================================================================
# 3. MODIFICATION DE LISTES
# =============================================================================

print("\n" + "=" * 60)
print("3. MODIFICATION DE LISTES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 3.1 Modifier un élément
# -----------------------------------------------------------------------------
print("\n--- 3.1 Modifier un élément ---")

animaux = ["chat", "chien", "oiseau"]
print(f"Avant : {animaux}")
animaux[1] = "lapin"
print(f"Après animaux[1] = 'lapin' : {animaux}")

# -----------------------------------------------------------------------------
# 3.2 Ajouter des éléments
# -----------------------------------------------------------------------------
print("\n--- 3.2 Ajouter des éléments ---")

# append() : ajoute à la fin
liste = [1, 2, 3]
print(f"Liste initiale : {liste}")

liste.append(4)
print(f"Après append(4) : {liste}")

# insert() : ajoute à une position spécifique
liste.insert(0, 0)  # Insère 0 à l'index 0
print(f"Après insert(0, 0) : {liste}")

liste.insert(2, 1.5)  # Insère 1.5 à l'index 2
print(f"Après insert(2, 1.5) : {liste}")

# extend() : ajoute plusieurs éléments
liste.extend([5, 6, 7])
print(f"Après extend([5, 6, 7]) : {liste}")

# Différence entre append et extend
print("\n--- Différence append vs extend ---")
liste_a = [1, 2]
liste_b = [1, 2]

liste_a.append([3, 4])
liste_b.extend([3, 4])

print(f"append([3, 4]) : {liste_a}")   # [1, 2, [3, 4]]
print(f"extend([3, 4]) : {liste_b}")   # [1, 2, 3, 4]

# -----------------------------------------------------------------------------
# 3.3 Supprimer des éléments
# -----------------------------------------------------------------------------
print("\n--- 3.3 Supprimer des éléments ---")

lettres = ["a", "b", "c", "d", "e", "f"]
print(f"Liste initiale : {lettres}")

# remove() : supprime la première occurrence d'une valeur
lettres.remove("c")
print(f"Après remove('c') : {lettres}")

# pop() : supprime et retourne l'élément à un index
element = lettres.pop()  # Dernier élément par défaut
print(f"Après pop() : {lettres} (élément retiré : '{element}')")

element = lettres.pop(1)  # Index spécifique
print(f"Après pop(1) : {lettres} (élément retiré : '{element}')")

# del : supprime par index ou par slice
del lettres[0]
print(f"Après del lettres[0] : {lettres}")

# clear() : vide la liste
lettres.clear()
print(f"Après clear() : {lettres}")


# =============================================================================
# 4. OPÉRATIONS SUR LES LISTES
# =============================================================================

print("\n" + "=" * 60)
print("4. OPÉRATIONS SUR LES LISTES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 4.1 Concaténation et répétition
# -----------------------------------------------------------------------------
print("\n--- 4.1 Concaténation et répétition ---")

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

# Concaténation avec +
concatenee = liste1 + liste2
print(f"{liste1} + {liste2} = {concatenee}")

# Répétition avec *
repetee = [0] * 3
print(f"[0] * 3 = {repetee}")

# -----------------------------------------------------------------------------
# 4.2 Longueur et appartenance
# -----------------------------------------------------------------------------
print("\n--- 4.2 Longueur et appartenance ---")

nombres = [10, 20, 30, 40, 50]
print(f"Liste : {nombres}")
print(f"len(nombres) = {len(nombres)}")
print(f"30 in nombres = {30 in nombres}")
print(f"35 in nombres = {35 in nombres}")
print(f"35 not in nombres = {35 not in nombres}")

# -----------------------------------------------------------------------------
# 4.3 Minimum, maximum, somme
# -----------------------------------------------------------------------------
print("\n--- 4.3 min, max, sum ---")

valeurs = [15, 8, 23, 4, 42, 16]
print(f"Liste : {valeurs}")
print(f"min(valeurs) = {min(valeurs)}")
print(f"max(valeurs) = {max(valeurs)}")
print(f"sum(valeurs) = {sum(valeurs)}")
print(f"Moyenne = {sum(valeurs) / len(valeurs):.2f}")


# =============================================================================
# 5. MÉTHODES DE LISTE
# =============================================================================

print("\n" + "=" * 60)
print("5. MÉTHODES DE LISTE")
print("=" * 60)

# -----------------------------------------------------------------------------
# 5.1 Recherche
# -----------------------------------------------------------------------------
print("\n--- 5.1 Recherche ---")

lettres = ["a", "b", "c", "b", "d", "b"]
print(f"Liste : {lettres}")

# index() : trouve l'index de la première occurrence
print(f"lettres.index('b') = {lettres.index('b')}")
print(f"lettres.index('b', 2) = {lettres.index('b', 2)}")  # Cherche à partir de l'index 2

# count() : compte les occurrences
print(f"lettres.count('b') = {lettres.count('b')}")
print(f"lettres.count('z') = {lettres.count('z')}")

# -----------------------------------------------------------------------------
# 5.2 Tri et inversion
# -----------------------------------------------------------------------------
print("\n--- 5.2 Tri et inversion ---")

nombres = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Liste originale : {nombres}")

# sort() : trie la liste en place (modifie l'original)
nombres.sort()
print(f"Après sort() : {nombres}")

nombres.sort(reverse=True)
print(f"Après sort(reverse=True) : {nombres}")

# sorted() : retourne une nouvelle liste triée (ne modifie pas l'original)
original = [3, 1, 4, 1, 5]
triee = sorted(original)
print(f"\noriginal : {original}")
print(f"sorted(original) : {triee}")

# reverse() : inverse la liste en place
nombres = [1, 2, 3, 4, 5]
nombres.reverse()
print(f"\nAprès reverse() : {nombres}")

# reversed() : retourne un itérateur inversé
print(f"list(reversed([1, 2, 3])) : {list(reversed([1, 2, 3]))}")

# -----------------------------------------------------------------------------
# 5.3 Tri avec clé personnalisée
# -----------------------------------------------------------------------------
print("\n--- 5.3 Tri avec clé personnalisée ---")

mots = ["python", "java", "c", "javascript", "go"]
print(f"Liste originale : {mots}")

# Tri par longueur
mots_par_longueur = sorted(mots, key=len)
print(f"Tri par longueur : {mots_par_longueur}")

# Tri alphabétique insensible à la casse
noms = ["Alice", "bob", "Charlie", "david"]
noms_tries = sorted(noms, key=str.lower)
print(f"Tri insensible à la casse : {noms_tries}")

# -----------------------------------------------------------------------------
# 5.4 copy() : copie superficielle
# -----------------------------------------------------------------------------
print("\n--- 5.4 Copie de listes ---")

original = [1, 2, 3]
copie1 = original.copy()
copie2 = original[:]
copie3 = list(original)

print(f"Original : {original}")
print(f"copy() : {copie1}")
print(f"[:] : {copie2}")
print(f"list() : {copie3}")

# Attention aux listes imbriquées !
print("\n--- Attention : copie superficielle ---")
original = [[1, 2], [3, 4]]
copie = original.copy()
copie[0][0] = 999
print(f"Après modification de la copie :")
print(f"  Original : {original}")  # Aussi modifié !
print(f"  Copie : {copie}")

# Solution : copie profonde avec copy.deepcopy()
import copy
original = [[1, 2], [3, 4]]
copie_profonde = copy.deepcopy(original)
copie_profonde[0][0] = 999
print(f"\nAvec deepcopy :")
print(f"  Original : {original}")  # Non modifié
print(f"  Copie : {copie_profonde}")


# =============================================================================
# 6. COMPRÉHENSIONS DE LISTE
# =============================================================================

print("\n" + "=" * 60)
print("6. COMPRÉHENSIONS DE LISTE")
print("=" * 60)

# -----------------------------------------------------------------------------
# 6.1 Syntaxe de base
# -----------------------------------------------------------------------------
print("\n--- 6.1 Syntaxe de base ---")
print("Syntaxe : [expression for element in iterable]")

# Exemple : carrés des nombres de 1 à 5
carres = [x**2 for x in range(1, 6)]
print(f"Carrés : {carres}")

# Exemple : convertir en majuscules
mots = ["hello", "world", "python"]
majuscules = [mot.upper() for mot in mots]
print(f"Majuscules : {majuscules}")

# -----------------------------------------------------------------------------
# 6.2 Avec condition (filtrage)
# -----------------------------------------------------------------------------
print("\n--- 6.2 Avec condition ---")
print("Syntaxe : [expression for element in iterable if condition]")

# Nombres pairs
pairs = [x for x in range(1, 11) if x % 2 == 0]
print(f"Nombres pairs de 1 à 10 : {pairs}")

# Filtrer les mots longs
mots = ["a", "bb", "ccc", "dddd", "eeeee"]
longs = [mot for mot in mots if len(mot) > 2]
print(f"Mots de plus de 2 caractères : {longs}")

# -----------------------------------------------------------------------------
# 6.3 Avec expression conditionnelle
# -----------------------------------------------------------------------------
print("\n--- 6.3 Expression conditionnelle ---")
print("Syntaxe : [expr_si_vrai if condition else expr_si_faux for element in iterable]")

# Pair ou impair
nombres = [1, 2, 3, 4, 5]
parite = ["pair" if n % 2 == 0 else "impair" for n in nombres]
print(f"Parité : {parite}")

# Valeur absolue manuelle
valeurs = [-3, -1, 0, 2, 4]
absolues = [x if x >= 0 else -x for x in valeurs]
print(f"Valeurs absolues : {absolues}")

# -----------------------------------------------------------------------------
# 6.4 Compréhensions imbriquées
# -----------------------------------------------------------------------------
print("\n--- 6.4 Compréhensions imbriquées ---")

# Aplatir une matrice
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplatie = [element for ligne in matrice for element in ligne]
print(f"Matrice : {matrice}")
print(f"Aplatie : {aplatie}")

# Créer une matrice
matrice_3x3 = [[i * 3 + j for j in range(3)] for i in range(3)]
print(f"Matrice 3x3 : {matrice_3x3}")


# =============================================================================
# 7. LISTES ET FONCTIONS UTILES
# =============================================================================

print("\n" + "=" * 60)
print("7. FONCTIONS UTILES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 7.1 enumerate()
# -----------------------------------------------------------------------------
print("\n--- 7.1 enumerate() ---")

fruits = ["pomme", "banane", "orange"]
print("Parcours avec enumerate :")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

print("\nAvec start=1 :")
for num, fruit in enumerate(fruits, start=1):
    print(f"  {num}. {fruit}")

# -----------------------------------------------------------------------------
# 7.2 zip()
# -----------------------------------------------------------------------------
print("\n--- 7.2 zip() ---")

noms = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print("Combinaison avec zip :")
for nom, score in zip(noms, scores):
    print(f"  {nom}: {score}")

# Créer un dictionnaire avec zip
dictionnaire = dict(zip(noms, scores))
print(f"\nDictionnaire : {dictionnaire}")

# -----------------------------------------------------------------------------
# 7.3 map()
# -----------------------------------------------------------------------------
print("\n--- 7.3 map() ---")

nombres = [1, 2, 3, 4, 5]

# Appliquer une fonction à chaque élément
carres = list(map(lambda x: x**2, nombres))
print(f"Carrés avec map : {carres}")

# Conversion de types
chaines = ["1", "2", "3", "4", "5"]
entiers = list(map(int, chaines))
print(f"Conversion en int : {entiers}")

# -----------------------------------------------------------------------------
# 7.4 filter()
# -----------------------------------------------------------------------------
print("\n--- 7.4 filter() ---")

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrer les nombres pairs
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(f"Nombres pairs avec filter : {pairs}")

# Filtrer les valeurs non nulles
valeurs = [0, 1, "", "hello", None, [], [1, 2]]
non_vides = list(filter(None, valeurs))
print(f"Valeurs non vides : {non_vides}")

# -----------------------------------------------------------------------------
# 7.5 any() et all()
# -----------------------------------------------------------------------------
print("\n--- 7.5 any() et all() ---")

notes = [15, 12, 8, 18, 14]
print(f"Notes : {notes}")

# any() : au moins un élément vérifie la condition
au_moins_un_excellent = any(note >= 18 for note in notes)
print(f"Au moins une note >= 18 : {au_moins_un_excellent}")

# all() : tous les éléments vérifient la condition
tous_reussis = all(note >= 10 for note in notes)
print(f"Toutes les notes >= 10 : {tous_reussis}")


# =============================================================================
# 8. EXERCICES PRATIQUES
# =============================================================================

print("\n" + "=" * 60)
print("8. EXERCICES PRATIQUES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Exercice 1 : Inverser une liste sans reverse()
# -----------------------------------------------------------------------------
print("\n--- Exercice 1 : Inverser une liste ---")
original = [1, 2, 3, 4, 5]
inversee = original[::-1]
print(f"Original : {original}")
print(f"Inversée : {inversee}")

# -----------------------------------------------------------------------------
# Exercice 2 : Supprimer les doublons (en gardant l'ordre)
# -----------------------------------------------------------------------------
print("\n--- Exercice 2 : Supprimer les doublons ---")
avec_doublons = [1, 2, 2, 3, 4, 3, 5, 1, 6]
sans_doublons = []
for element in avec_doublons:
    if element not in sans_doublons:
        sans_doublons.append(element)
print(f"Avec doublons : {avec_doublons}")
print(f"Sans doublons : {sans_doublons}")

# Méthode avec dict.fromkeys() (Python 3.7+)
sans_doublons2 = list(dict.fromkeys(avec_doublons))
print(f"Avec dict.fromkeys() : {sans_doublons2}")

# -----------------------------------------------------------------------------
# Exercice 3 : Trouver le deuxième plus grand
# -----------------------------------------------------------------------------
print("\n--- Exercice 3 : Deuxième plus grand ---")
nombres = [5, 2, 8, 1, 9, 3, 7]
uniques = list(set(nombres))
uniques.sort(reverse=True)
deuxieme = uniques[1]
print(f"Liste : {nombres}")
print(f"Deuxième plus grand : {deuxieme}")

# -----------------------------------------------------------------------------
# Exercice 4 : Fusionner deux listes triées
# -----------------------------------------------------------------------------
print("\n--- Exercice 4 : Fusionner deux listes triées ---")
liste1 = [1, 3, 5, 7]
liste2 = [2, 4, 6, 8]
fusionnee = sorted(liste1 + liste2)
print(f"Liste 1 : {liste1}")
print(f"Liste 2 : {liste2}")
print(f"Fusionnée : {fusionnee}")

# -----------------------------------------------------------------------------
# Exercice 5 : Rotation de liste
# -----------------------------------------------------------------------------
print("\n--- Exercice 5 : Rotation de liste ---")
original = [1, 2, 3, 4, 5]
n = 2  # Nombre de positions à décaler

# Rotation vers la droite
rotation_droite = original[-n:] + original[:-n]
print(f"Original : {original}")
print(f"Rotation droite de {n} : {rotation_droite}")

# Rotation vers la gauche
rotation_gauche = original[n:] + original[:n]
print(f"Rotation gauche de {n} : {rotation_gauche}")


# =============================================================================
# RÉSUMÉ
# =============================================================================
print("\n" + "=" * 60)
print("RÉSUMÉ")
print("=" * 60)
print("""
CRÉATION :
  - [] ou list()
  - [1, 2, 3] ou list(range(n))
  - [x for x in iterable]

ACCÈS :
  - liste[index] (positif ou négatif)
  - liste[debut:fin:pas] (slicing)

MODIFICATION :
  - append(x), insert(i, x), extend(iterable)
  - remove(x), pop(), pop(i), del, clear()

MÉTHODES UTILES :
  - sort(), reverse(), copy()
  - index(x), count(x)
  - len(), min(), max(), sum()

FONCTIONS :
  - sorted(), reversed()
  - enumerate(), zip()
  - map(), filter()
  - any(), all()

COMPRÉHENSION :
  - [expr for x in iterable]
  - [expr for x in iterable if condition]
  - [expr1 if cond else expr2 for x in iterable]
""")
