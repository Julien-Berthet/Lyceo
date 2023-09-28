from eleve import Eleve
from professeur import Professeur
from classe import Classe
from lycee import Lycee
from main import Lyceo

# --------------------- #
# EXEMPLE 3             #
# --------------------- #

# On peut ensuite, faire se combattre deux élèves
# Le système de combat fonctionne de la manière suivante

# On crée deux élèves dans un lycée
lycee = Lycee.generer()

eleveA = Eleve.generer()
eleveB = Eleve.generer()

classe = Classe([ eleveA, eleveB ], 'TGΩ')
lycee.ajouter_classe(classe)

# Et on lance un combat qui se joue dans la console
eleveA.combattre(eleveB)

# L'élève avec la meilleure moyenne générale commence
# A chaque tour on choisit d'attaquer ou de déclarer forfait
# Si l'on attaque on doit choisir un matière dans laquelle attaquer

# Admettons que l'attaquant attaque avec de la NSI: alors
# Ses dégats seront plus puissants en si la moyenne de NSI est élevée
# Et l'ennemi subira plus de dégats si sa moyenne de NSI et faible

# Un elève vaincu est supprimé

# On peut egalement mettre le paramètre `manuel` de la méthode
# `combattre()` à True pour ne pas avoir d'interface et combattre
# en utilisant les méthodes `attaquer()`, `attaque_aleatoire()`,
# ou `arreter_le_combat()`

# Durant un combat, on peut récuperer la vie d'un elève avec l'attribut `vie`
# On peut également récuperer son adversaire dans l'attribut `ennemi`