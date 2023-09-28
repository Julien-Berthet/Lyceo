import random
from data import NOMS, MATIERES

class Professeur:

    """
    # Classe Professeur
    ----------------
    Represente un professeur d'un lycée
    """

    def __init__(self, genre, nom, matiere):
        """
        # Attributs
        `genre`: Literal['M', 'F']
            Permet de savoir si l'ont doit appeler un prfesseur M. ou Mm.
        `nom`: str
            Permet de nommé un professeur
        `matiere`: str
            Permet de savoir la matiere que le professeur peut enseigner
        """
        if genre not in ('M', 'F'):
            raise Exception("Veuillez préciser votre genre en entrant \'M\' ou \'F\'")
            
        self.genre = genre
        self.nom = nom
        self.matiere = matiere

    def __repr__(self):
        return f'<Professeur: {self.affichage()}>'
    
    # Getters et Setters
    def get_genre(self):
        """
        Fonction getter pour l'attribut `genre`
        """
        return self.genre
    
    def set_genre(self, value):
        """
        Fonction setter pour l'attribut `genre`
        """
        self.genre = value
        
    def get_nom(self):
        """
        Fonction getter pour l'attribut `nom`
        """
        return self.nom
    
    def set_nom(self, value):
        """
        Fonction setter pour l'attribut `nom`
        """
        self.nom = value
        
    def get_matiere(self):
        """
        Fonction getter pour l'attribut `matiere`
        """
        return self.matiere
    
    def set_matiere(self, value):
        """
        Fonction setter pour l'attribut `matiere`
        """
        self.matiere = value
    
    # Méthodes Statiques
    @classmethod
    def generer(self):
        """
        Méthode Statique
        Génère un professeur avec des attributs aléatoires
        """
        genre = random.randint(0, 1)
        if genre:
            genre = 'M'
        else:
            genre = 'F'
        nom = random.choice(NOMS)
        matiere = random.choice(MATIERES)

        return Professeur(genre, nom, matiere)

    # Méthodes
    def affichage(self):
        """
        affiche le prefixe et le nom du professeur
        """
        prefixe = ''
        
        if self.genre == "M":
            prefixe = 'M. '
        else:
            prefixe = 'Mme. '
            
        return f'{prefixe}{self.nom.upper()}'