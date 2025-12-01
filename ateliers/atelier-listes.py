# =============================================================================
#                    ATELIER PRATIQUE : LES LISTES
# =============================================================================
# Exercices pratiques pour mettre en application les notions de base
# sur les listes en Python.
#
# Instructions :
# - Complétez chaque exercice en remplaçant les "..." par votre code
# - Exécutez le fichier pour vérifier vos réponses
# - Les résultats attendus sont indiqués dans les commentaires
# =============================================================================


# =============================================================================
# EXERCICE 1 : Créer et afficher une liste
# =============================================================================
# Créez une liste contenant les 5 premiers nombres impairs
# Résultat attendu : [1, 3, 5, 7, 9]

print("=" * 60)
print("EXERCICE 1 : Créer une liste de nombres impairs")
print("=" * 60)

# Votre code ici :
# impairs = [...]
# print(f"Nombres impairs : {impairs}")


# =============================================================================
# EXERCICE 2 : Accéder aux éléments
# =============================================================================
# À partir de la liste donnée, affichez :
# - Le premier élément
# - Le dernier élément
# - Le troisième élément

print("\n" + "=" * 60)
print("EXERCICE 2 : Accéder aux éléments")
print("=" * 60)

fruits = ["pomme", "banane", "orange", "fraise", "kiwi"]
print(f"Liste : {fruits}")

# Votre code ici :
# print(f"Premier élément : {fruits[...]}")
# print(f"Dernier élément : {fruits[...]}")
# print(f"Troisième élément : {fruits[...]}")


# =============================================================================
# EXERCICE 3 : Slicing (découpage)
# =============================================================================
# À partir de la liste nombres, extrayez :
# - Les 3 premiers éléments
# - Les 3 derniers éléments
# - Les éléments d'index 2 à 5 (exclus)

print("\n" + "=" * 60)
print("EXERCICE 3 : Slicing")
print("=" * 60)

nombres = [10, 20, 30, 40, 50, 60, 70]
print(f"Liste : {nombres}")

# Votre code ici :
# print(f"3 premiers : {nombres[...]}")
# print(f"3 derniers : {nombres[...]}")
# print(f"Index 2 à 5 : {nombres[...]}")


# =============================================================================
# EXERCICE 4 : Modifier une liste
# =============================================================================
# Modifiez la liste pour remplacer "python" par "Python"
# Résultat attendu : ['html', 'css', 'Python', 'javascript']

print("\n" + "=" * 60)
print("EXERCICE 4 : Modifier un élément")
print("=" * 60)

langages = ["html", "css", "python", "javascript"]
print(f"Avant : {langages}")

# Votre code ici :
# langages[...] = "Python"

# print(f"Après : {langages}")


# =============================================================================
# EXERCICE 5 : Ajouter des éléments
# =============================================================================
# Ajoutez "mangue" à la fin de la liste
# Puis insérez "cerise" en position 2
# Résultat attendu : ['pomme', 'banane', 'cerise', 'orange', 'mangue']

print("\n" + "=" * 60)
print("EXERCICE 5 : Ajouter des éléments")
print("=" * 60)

fruits = ["pomme", "banane", "orange"]
print(f"Liste initiale : {fruits}")

# Votre code ici :
# fruits.append(...)
# fruits.insert(..., ...)

# print(f"Liste finale : {fruits}")


# =============================================================================
# EXERCICE 6 : Supprimer des éléments
# =============================================================================
# Supprimez "banane" de la liste avec remove()
# Puis supprimez le dernier élément avec pop()
# Résultat attendu : ['pomme', 'orange', 'fraise']

print("\n" + "=" * 60)
print("EXERCICE 6 : Supprimer des éléments")
print("=" * 60)

fruits = ["pomme", "banane", "orange", "fraise", "kiwi"]
print(f"Liste initiale : {fruits}")

# Votre code ici :
# fruits.remove(...)
# fruits.pop()

# print(f"Liste finale : {fruits}")


# =============================================================================
# EXERCICE 7 : Concaténation et répétition
# =============================================================================
# Créez une nouvelle liste en concaténant liste1 et liste2
# Puis créez une liste avec [0] répété 5 fois

print("\n" + "=" * 60)
print("EXERCICE 7 : Concaténation et répétition")
print("=" * 60)

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

# Votre code ici :
# concatenee = liste1 ... liste2
# zeros = [0] ... 5

# print(f"Concaténée : {concatenee}")
# print(f"Zéros : {zeros}")


# =============================================================================
# EXERCICE 8 : Opérations sur les listes
# =============================================================================
# À partir de la liste notes, calculez :
# - La longueur de la liste
# - La note minimale
# - La note maximale
# - La somme des notes
# - La moyenne des notes

print("\n" + "=" * 60)
print("EXERCICE 8 : Opérations sur les listes")
print("=" * 60)

notes = [15, 12, 18, 9, 14, 16]
print(f"Notes : {notes}")

# Votre code ici :
# print(f"Nombre de notes : {len(...)}")
# print(f"Note minimale : {min(...)}")
# print(f"Note maximale : {max(...)}")
# print(f"Somme : {sum(...)}")
# print(f"Moyenne : {sum(...) / len(...):.2f}")


# =============================================================================
# EXERCICE 9 : Tri de liste
# =============================================================================
# Triez la liste dans l'ordre croissant
# Puis triez-la dans l'ordre décroissant

print("\n" + "=" * 60)
print("EXERCICE 9 : Tri de liste")
print("=" * 60)

nombres = [42, 17, 8, 99, 23, 56]
print(f"Liste initiale : {nombres}")

# Votre code ici :
# nombres.sort()
# print(f"Tri croissant : {nombres}")

# nombres.sort(reverse=...)
# print(f"Tri décroissant : {nombres}")


# =============================================================================
# EXERCICE 10 : Recherche dans une liste
# =============================================================================
# Trouvez l'index de "orange" dans la liste
# Comptez combien de fois "pomme" apparaît
# Vérifiez si "mangue" est dans la liste

print("\n" + "=" * 60)
print("EXERCICE 10 : Recherche dans une liste")
print("=" * 60)

fruits = ["pomme", "banane", "orange", "pomme", "fraise", "pomme"]
print(f"Liste : {fruits}")

# Votre code ici :
# print(f"Index de 'orange' : {fruits.index(...)}")
# print(f"Nombre de 'pomme' : {fruits.count(...)}")
# print(f"'mangue' dans la liste : {'mangue' ... fruits}")


# =============================================================================
# EXERCICE 11 : Parcourir avec enumerate
# =============================================================================
# Affichez chaque fruit avec son numéro (commençant à 1)
# Résultat attendu :
# 1. pomme
# 2. banane
# 3. orange

print("\n" + "=" * 60)
print("EXERCICE 11 : Parcourir avec enumerate")
print("=" * 60)

fruits = ["pomme", "banane", "orange"]

# Votre code ici :
# for num, fruit in enumerate(fruits, start=...):
#     print(f"{num}. {fruit}")


# =============================================================================
# EXERCICE 12 : Compréhension de liste - Base
# =============================================================================
# Créez une liste des doubles de chaque nombre
# Résultat attendu : [2, 4, 6, 8, 10]

print("\n" + "=" * 60)
print("EXERCICE 12 : Compréhension de liste - Base")
print("=" * 60)

nombres = [1, 2, 3, 4, 5]

# Votre code ici :
# doubles = [... for x in nombres]
# print(f"Doubles : {doubles}")


# =============================================================================
# EXERCICE 13 : Compréhension de liste - Avec filtre
# =============================================================================
# Créez une liste contenant uniquement les nombres pairs
# Résultat attendu : [2, 4, 6, 8, 10]

print("\n" + "=" * 60)
print("EXERCICE 13 : Compréhension de liste - Avec filtre")
print("=" * 60)

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Votre code ici :
# pairs = [x for x in nombres if ...]
# print(f"Nombres pairs : {pairs}")


# =============================================================================
# EXERCICE 14 : Inverser une liste
# =============================================================================
# Inversez la liste sans utiliser reverse()
# Résultat attendu : [5, 4, 3, 2, 1]

print("\n" + "=" * 60)
print("EXERCICE 14 : Inverser une liste")
print("=" * 60)

nombres = [1, 2, 3, 4, 5]

# Votre code ici (utilisez le slicing) :
# inversee = nombres[...]
# print(f"Inversée : {inversee}")


# =============================================================================
# EXERCICE 15 : Combiner deux listes avec zip
# =============================================================================
# Combinez les deux listes pour afficher nom : note
# Résultat attendu :
# Alice : 15
# Bob : 12
# Charlie : 18

print("\n" + "=" * 60)
print("EXERCICE 15 : Combiner avec zip")
print("=" * 60)

noms = ["Alice", "Bob", "Charlie"]
notes = [15, 12, 18]

# Votre code ici :
# for nom, note in zip(..., ...):
#     print(f"{nom} : {note}")