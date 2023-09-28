from eleve import Eleve
from professeur import Professeur
from classe import Classe
from lycee import Lycee
from main import Lyceo

# --------------------- #
# EXEMPLE 1             #
# --------------------- #

# On commence par creer une nouvelle instance de l'application Lyceo
lyceo = Lyceo()

# Puis on crée un nouveau lycée qu'on inscrit sur l'application
froment = Lycee('Jules Froment', 'https://www.lycee-julesfroment.fr/')
lyceo.ajouter_lycee(froment)

# Puis on crée une classe qu'on ajoute dans le lycée avec des élèves
eleve1 = Eleve('Julien', 'Berthet', 'M', 2007)
eleve2 = Eleve('Lucas', 'Aparissi', 'M', 2008)
classe = Classe([ eleve1, eleve2 ], 'TG5+3i')

# On ajoute la classe dans le lycée
froment.ajouter_classe(classe)

# Puis on ajoute des professeurs
prof1 = Professeur('M', 'MATT', 'Mathematiques')
prof2 = Professeur('F', 'ENESSI', 'NSI')

# Ces professeurs peuvent être recrutés avec la méthode `recruter_professeur()` qui créera un
# quizz de recrutement dans la console. Cependant on passera ici la valeur
# True dans `ignorer_quizz` afin d'ignorer ce quizz pour les biens de l'exemple
froment.recruter_professeur(prof1, ignorer_quizz=True)
froment.recruter_professeur(prof2, ignorer_quizz=True)

# On peut ensuite attribuer des notes a un elève
# A condition que au moins un professeur qui enseigne la matière ait été recruté
eleve2.ajouter_note('Mathematiques', 16)
eleve2.ajouter_note('Mathematiques', 17)
eleve2.ajouter_note('Mathematiques', 15)
eleve2.ajouter_note('Mathematiques', 19)

# Puis on peut calculer sa moyenne
print('Moyenne de Mathématiques:', eleve2.get_moyenne('Mathematiques'))
print('Moyenne Générale:', eleve2.get_moyenne_generale())