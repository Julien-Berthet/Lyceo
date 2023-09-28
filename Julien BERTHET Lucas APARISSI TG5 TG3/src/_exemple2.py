from eleve import Eleve
from professeur import Professeur
from classe import Classe
from lycee import Lycee
from main import Lyceo

# --------------------- #
# EXEMPLE 2             #
# --------------------- #

# On commence par creer une nouvelle instance de l'application Lyceo
lyceo = Lyceo()

# Puis on génère un lycée aléatoirement avec la méthode statique `generer()`
# Ce lycée aura des classes aléatoires contenant des élèves aléatoires
# et des professeurs aléatoires dans chaque matière
lycee = Lycee.generer()

lyceo.ajouter_lycee(lycee)

# Notons que la plupart des classes on également cette méthode tel que
Classe.generer()
Professeur.generer()
Eleve.generer()

# Outre cela on peut generer des notes aléatoire pour l'élève
eleve = Eleve.generer()
eleve.ajouter_notes_aleatoires()

# Si l'on veut parcourir les élèves d'un lycée on peut utiliser
# le générateur (itérateur) `eleves()` avec un boucle for
for e in lycee.eleves():
    e.ajouter_notes_aleatoires()
    print(f'Moyenne Générale de {e}:', e.get_moyenne_generale())