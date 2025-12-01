# =============================================================================
#                           TUTORIEL PYTHON : LES BOUCLES
# =============================================================================
# Les boucles permettent de répéter des instructions plusieurs fois.
# Python propose deux types de boucles : for et while
# =============================================================================


# =============================================================================
# 1. LA BOUCLE FOR
# =============================================================================
# La boucle for permet de parcourir une séquence (liste, chaîne, range, etc.)

print("=" * 60)
print("1. LA BOUCLE FOR")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1.1 Parcourir une séquence de nombres avec range()
# -----------------------------------------------------------------------------
print("\n--- 1.1 La fonction range() ---")

# range(n) génère les nombres de 0 à n-1
print("range(5) : nombres de 0 à 4")
for i in range(5):
    print(i, end=" ")
print()  # Retour à la ligne

# range(debut, fin) : de debut à fin-1
print("\nrange(2, 7) : nombres de 2 à 6")
for i in range(2, 7):
    print(i, end=" ")
print()

# range(debut, fin, pas) : avec un pas personnalisé
print("\nrange(0, 10, 2) : nombres pairs de 0 à 8")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Compte à rebours avec un pas négatif
print("\nrange(10, 0, -1) : compte à rebours de 10 à 1")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# -----------------------------------------------------------------------------
# 1.2 Parcourir une chaîne de caractères
# -----------------------------------------------------------------------------
print("\n--- 1.2 Parcourir une chaîne ---")

mot = "Python"
print(f"Parcours de '{mot}' lettre par lettre :")
for lettre in mot:
    print(lettre, end=" ")
print()

# -----------------------------------------------------------------------------
# 1.3 Parcourir une liste
# -----------------------------------------------------------------------------
print("\n--- 1.3 Parcourir une liste ---")

fruits = ["pomme", "banane", "orange", "fraise"]
print("Liste des fruits :")
for fruit in fruits:
    print(f"  - {fruit}")

# -----------------------------------------------------------------------------
# 1.4 enumerate() : obtenir l'index et la valeur
# -----------------------------------------------------------------------------
print("\n--- 1.4 enumerate() : index + valeur ---")

print("Fruits avec leur index :")
for index, fruit in enumerate(fruits):
    print(f"  {index} : {fruit}")

# Commencer l'index à 1
print("\nAvec enumerate(fruits, start=1) :")
for numero, fruit in enumerate(fruits, start=1):
    print(f"  {numero}. {fruit}")

# -----------------------------------------------------------------------------
# 1.5 zip() : parcourir plusieurs séquences en parallèle
# -----------------------------------------------------------------------------
print("\n--- 1.5 zip() : parcours parallèle ---")

noms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
villes = ["Paris", "Lyon", "Marseille"]

print("Informations combinées :")
for nom, age, ville in zip(noms, ages, villes):
    print(f"  {nom}, {age} ans, habite à {ville}")


# =============================================================================
# 2. LA BOUCLE WHILE
# =============================================================================
# La boucle while répète tant qu'une condition est vraie

print("\n" + "=" * 60)
print("2. LA BOUCLE WHILE")
print("=" * 60)

# -----------------------------------------------------------------------------
# 2.1 Boucle while simple
# -----------------------------------------------------------------------------
print("\n--- 2.1 Boucle while simple ---")

compteur = 0
print("Compteur de 0 à 4 :")
while compteur < 5:
    print(compteur, end=" ")
    compteur += 1  # IMPORTANT : ne pas oublier d'incrémenter !
print()

# -----------------------------------------------------------------------------
# 2.2 Boucle while avec condition complexe
# -----------------------------------------------------------------------------
print("\n--- 2.2 Condition complexe ---")

nombre = 1
print("Puissances de 2 inférieures à 100 :")
while nombre < 100:
    print(nombre, end=" ")
    nombre *= 2
print()

# -----------------------------------------------------------------------------
# 2.3 Boucle infinie contrôlée avec break
# -----------------------------------------------------------------------------
print("\n--- 2.3 Simulation d'entrée utilisateur ---")

# Simulation : on utilise une liste de réponses prédéfinies
reponses_simulees = ["continuer", "encore", "stop"]
index_reponse = 0

print("Simulation de saisie utilisateur :")
while True:
    reponse = reponses_simulees[index_reponse]
    print(f"  Réponse : {reponse}")
    if reponse == "stop":
        print("  -> Sortie de la boucle")
        break
    index_reponse += 1


# =============================================================================
# 3. CONTRÔLE DE FLUX : break, continue, else
# =============================================================================

print("\n" + "=" * 60)
print("3. CONTRÔLE DE FLUX")
print("=" * 60)

# -----------------------------------------------------------------------------
# 3.1 break : sortir immédiatement de la boucle
# -----------------------------------------------------------------------------
print("\n--- 3.1 break ---")

print("Recherche du premier nombre divisible par 7 entre 50 et 100 :")
for n in range(50, 100):
    if n % 7 == 0:
        print(f"  Trouvé : {n}")
        break

# -----------------------------------------------------------------------------
# 3.2 continue : passer à l'itération suivante
# -----------------------------------------------------------------------------
print("\n--- 3.2 continue ---")

print("Nombres de 1 à 10 (sauf les multiples de 3) :")
for n in range(1, 11):
    if n % 3 == 0:
        continue  # Saute les multiples de 3
    print(n, end=" ")
print()

# -----------------------------------------------------------------------------
# 3.3 else : exécuté si la boucle se termine normalement (sans break)
# -----------------------------------------------------------------------------
print("\n--- 3.3 else dans les boucles ---")

print("Recherche de 15 dans [1, 5, 10, 20] :")
nombres = [1, 5, 10, 20]
for n in nombres:
    if n == 15:
        print("  15 trouvé !")
        break
else:
    print("  15 non trouvé dans la liste")

print("\nRecherche de 10 dans [1, 5, 10, 20] :")
for n in nombres:
    if n == 10:
        print("  10 trouvé !")
        break
else:
    print("  10 non trouvé dans la liste")


# =============================================================================
# 4. BOUCLES IMBRIQUÉES
# =============================================================================

print("\n" + "=" * 60)
print("4. BOUCLES IMBRIQUÉES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 4.1 Table de multiplication
# -----------------------------------------------------------------------------
print("\n--- 4.1 Table de multiplication (1 à 5) ---")

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()  # Nouvelle ligne après chaque rangée

# -----------------------------------------------------------------------------
# 4.2 Motif avec des étoiles
# -----------------------------------------------------------------------------
print("\n--- 4.2 Triangle d'étoiles ---")

for i in range(1, 6):
    print("*" * i)

print("\n--- Triangle inversé ---")
for i in range(5, 0, -1):
    print("*" * i)


# =============================================================================
# 5. COMPRÉHENSIONS DE LISTE (List Comprehensions)
# =============================================================================
# Syntaxe compacte pour créer des listes avec une boucle

print("\n" + "=" * 60)
print("5. COMPRÉHENSIONS DE LISTE")
print("=" * 60)

# -----------------------------------------------------------------------------
# 5.1 Syntaxe de base
# -----------------------------------------------------------------------------
print("\n--- 5.1 Syntaxe de base ---")

# Méthode classique
carres_classique = []
for x in range(1, 6):
    carres_classique.append(x ** 2)
print(f"Méthode classique : {carres_classique}")

# Avec compréhension de liste
carres = [x ** 2 for x in range(1, 6)]
print(f"Compréhension    : {carres}")

# -----------------------------------------------------------------------------
# 5.2 Avec condition (filtrage)
# -----------------------------------------------------------------------------
print("\n--- 5.2 Avec condition ---")

# Nombres pairs de 1 à 10
pairs = [x for x in range(1, 11) if x % 2 == 0]
print(f"Nombres pairs de 1 à 10 : {pairs}")

# Mots de plus de 4 lettres
mots = ["chat", "chien", "oiseau", "rat", "éléphant"]
longs_mots = [mot for mot in mots if len(mot) > 4]
print(f"Mots de plus de 4 lettres : {longs_mots}")

# -----------------------------------------------------------------------------
# 5.3 Avec transformation
# -----------------------------------------------------------------------------
print("\n--- 5.3 Avec transformation ---")

# Mettre en majuscules
mots_majuscules = [mot.upper() for mot in mots]
print(f"En majuscules : {mots_majuscules}")

# Condition ternaire dans la compréhension
parite = ["pair" if x % 2 == 0 else "impair" for x in range(1, 6)]
print(f"Parité de 1 à 5 : {parite}")


# =============================================================================
# 6. EXERCICES PRATIQUES
# =============================================================================

print("\n" + "=" * 60)
print("6. EXERCICES PRATIQUES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Exercice 1 : Somme des nombres de 1 à 100
# -----------------------------------------------------------------------------
print("\n--- Exercice 1 : Somme de 1 à 100 ---")
somme = 0
for i in range(1, 101):
    somme += i
print(f"Somme de 1 à 100 = {somme}")

# Version avec sum() et range()
print(f"Vérification avec sum() : {sum(range(1, 101))}")

# -----------------------------------------------------------------------------
# Exercice 2 : Factorielle
# -----------------------------------------------------------------------------
print("\n--- Exercice 2 : Factorielle de 5 ---")
n = 5
factorielle = 1
for i in range(1, n + 1):
    factorielle *= i
print(f"{n}! = {factorielle}")

# -----------------------------------------------------------------------------
# Exercice 3 : Fibonacci
# -----------------------------------------------------------------------------
print("\n--- Exercice 3 : Suite de Fibonacci (10 premiers) ---")
a, b = 0, 1
fibonacci = []
for _ in range(10):
    fibonacci.append(a)
    a, b = b, a + b
print(f"Fibonacci : {fibonacci}")

# -----------------------------------------------------------------------------
# Exercice 4 : Trouver les nombres premiers jusqu'à 50
# -----------------------------------------------------------------------------
print("\n--- Exercice 4 : Nombres premiers jusqu'à 50 ---")
premiers = []
for n in range(2, 51):
    est_premier = True
    for diviseur in range(2, int(n ** 0.5) + 1):
        if n % diviseur == 0:
            est_premier = False
            break
    if est_premier:
        premiers.append(n)
print(f"Nombres premiers : {premiers}")


# =============================================================================
# RÉSUMÉ
# =============================================================================
print("\n" + "=" * 60)
print("RÉSUMÉ")
print("=" * 60)
print("""
BOUCLE FOR :
  - for element in sequence:
  - range(n), range(debut, fin), range(debut, fin, pas)
  - enumerate() pour avoir l'index
  - zip() pour parcourir plusieurs séquences

BOUCLE WHILE :
  - while condition:
  - Attention aux boucles infinies !

CONTRÔLE DE FLUX :
  - break : sortir de la boucle
  - continue : passer à l'itération suivante
  - else : exécuté si pas de break

COMPRÉHENSION DE LISTE :
  - [expression for element in sequence]
  - [expression for element in sequence if condition]
""")
