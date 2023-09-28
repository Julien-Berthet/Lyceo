"""
Projet NSI
Lycéo

Par Julien BERTHET et Lucas APARISSI
    TG5               TG3
    
Voir les fichiers dans le dossier "exemples" pour une initiation
A noter que toutes les fonctions ne sont pas présentes dans les exemples
"""

__author__ = ['Julien BERTHET', 'Lucas APARISSI']

class Lyceo:
    """
    # Classe Lyceo
    ----------------
    Représente une application de gestion d'établissement scolaire
    comme EcoleDirecte
    """
    def __init__(self):
        self.lycees = []

    def __repr__(self):
        return f'<class Classe: "{self.nom}">'
    
    # Getters et Setters
    def get_lycees(self):
        """
        Fonction getter pour l'attribut `lycees`
        """
        return self.lycees
    
    def set_lycees(self, value):
        """
        Fonction setter pour l'attribut `lycees`
        """
        self.lycees = value

    # Méthodes
    def ajouter_lycee(self, name: str):
        """
        Inscrit un lycée sur l'application
        ----------------
        # Arguments
        `name`: str
            Nom du lycée
        """
        self.lycees.append(name)

