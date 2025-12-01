# =============================================================================
#                    ATELIER PRATIQUE : LES BOUCLES
# =============================================================================
# Exercices pratiques pour mettre en application les notions de base
# sur les boucles for et while.
#
# Instructions :
# - Complétez chaque exercice le commentaire par votre code
# - Exécutez le fichier pour vérifier vos réponses
# - Les résultats attendus sont indiqués dans les commentaires
# =============================================================================


# =============================================================================
# EXERCICE 1 : Afficher les nombres de 1 à 10
# =============================================================================
# Utilisez une boucle for avec range() pour afficher les nombres de 1 à 10
# Résultat attendu : 1 2 3 4 5 6 7 8 9 10

print("=" * 60)
print("EXERCICE 1 : Nombres de 1 à 10")
print("=" * 60)

# Votre code ici :


# =============================================================================
# EXERCICE 2 : Compte à rebours
# =============================================================================
# Affichez un compte à rebours de 10 à 1, puis "Décollage !"
# Résultat attendu : 10 9 8 7 6 5 4 3 2 1 Décollage !

print("\n" + "=" * 60)
print("EXERCICE 2 : Compte à rebours")
print("=" * 60)

# Votre code ici :


# =============================================================================
# EXERCICE 3 : Table de multiplication
# =============================================================================
# Affichez la table de multiplication de 7 (de 1 à 10)
# Résultat attendu :
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

print("\n" + "=" * 60)
print("EXERCICE 3 : Table de multiplication de 7")
print("=" * 60)

# Votre code ici :


# =============================================================================
# EXERCICE 4 : Somme des nombres
# =============================================================================
# Calculez la somme des nombres de 1 à 50
# Résultat attendu : La somme de 1 à 50 est : 1275

print("\n" + "=" * 60)
print("EXERCICE 4 : Somme de 1 à 50")
print("=" * 60)

somme = 0
# Votre code ici :

# print(f"La somme de 1 à 50 est : {somme}")


# =============================================================================
# EXERCICE 5 : Parcourir une chaîne
# =============================================================================
# Affichez chaque lettre du mot "PYTHON" avec son index
# Résultat attendu :
# Position 0 : P
# Position 1 : Y
# ...

print("\n" + "=" * 60)
print("EXERCICE 5 : Parcourir une chaîne")
print("=" * 60)

mot = "PYTHON"
# Votre code ici (utilisez enumerate) :


# =============================================================================
# EXERCICE 6 : Nombres pairs
# =============================================================================
# Affichez tous les nombres pairs entre 2 et 20 (inclus)
# Résultat attendu : 2 4 6 8 10 12 14 16 18 20

print("\n" + "=" * 60)
print("EXERCICE 6 : Nombres pairs de 2 à 20")
print("=" * 60)

# Votre code ici (deux méthodes possibles : avec range ou avec continue) :


# =============================================================================
# EXERCICE 7 : Boucle while - Devinette
# =============================================================================
# Utilisez une boucle while pour trouver le premier nombre divisible
# par 7 ET par 3 en partant de 1
# Résultat attendu : Le premier nombre divisible par 7 et 3 est : 21

print("\n" + "=" * 60)
print("EXERCICE 7 : Trouver un nombre (while)")
print("=" * 60)

nombre = 1
# Votre code ici :

# print(f"Le premier nombre divisible par 7 et 3 est : {nombre}")


# =============================================================================
# EXERCICE 8 : Compter les voyelles
# =============================================================================
# Comptez le nombre de voyelles dans la phrase donnée
# Résultat attendu : Nombre de voyelles : 11

print("\n" + "=" * 60)
print("EXERCICE 8 : Compter les voyelles")
print("=" * 60)

phrase = "Python est un langage genial"
voyelles = "aeiouyAEIOUY"
compteur = 0

# Votre code ici :
# for lettre in phrase:
#     if lettre in voyelles:
#         compteur += ...

# print(f"Nombre de voyelles : {compteur}")


# =============================================================================
# EXERCICE 9 : Triangle d'étoiles
# =============================================================================
# Créez un triangle d'étoiles de 5 lignes
# Résultat attendu :
# *
# **
# ***
# ****
# *****

print("\n" + "=" * 60)
print("EXERCICE 9 : Triangle d'étoiles")
print("=" * 60)

# Votre code ici :
# for i in range(1, ...):
#     print("*" * ...)


# =============================================================================
# EXERCICE 10 : FizzBuzz simplifié
# =============================================================================
# Pour les nombres de 1 à 20 :
# - Si le nombre est divisible par 3, affichez "Fizz"
# - Si le nombre est divisible par 5, affichez "Buzz"
# - Si le nombre est divisible par 3 ET 5, affichez "FizzBuzz"
# - Sinon, affichez le nombre
#
# Résultat attendu : 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz...

print("\n" + "=" * 60)
print("EXERCICE 10 : FizzBuzz")
print("=" * 60)

# Votre code ici :
# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz", end=" ")
#     elif ...
#     elif ...:
# print()


# =============================================================================
# EXERCICE 11 : Recherche avec break
# =============================================================================
# Trouvez le premier nombre supérieur à 100 qui est divisible par 17
# Utilisez break pour sortir de la boucle dès que trouvé
# Résultat attendu : Premier nombre > 100 divisible par 17 : 102

print("\n" + "=" * 60)
print("EXERCICE 11 : Recherche avec break")
print("=" * 60)

# Votre code ici :
# for n in range(101, 200):
#     if n % 17 == 0:
#         print(f"Premier nombre > 100 divisible par 17 : {n}")
#         ...
