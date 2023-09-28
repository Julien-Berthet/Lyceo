from eleve import Eleve
import random

class Classe:
    """
    # Classe Classe
    ----------------
    Représente une classe du lycée
    """

    def __init__(self, liste_eleve, nom_classe):
        """
        # Attributs
        `liste_eleve`: list
            Liste de tous les lycéens de la classe
        `nom_classe`: str
            Nom donné à la classe
        """
        self.liste_eleve = liste_eleve
        self.nom_classe = nom_classe

    def __repr__(self):
        return f'<class Classe: {self.nom_classe}>'

    # Getters et Setters
    def get_liste_eleve(self):
        """
        Fonction getter pour l'attribut `liste_eleve`
        """
        return self.liste_eleve
    
    def set_liste_eleve(self, value):
        """
        Fonction setter pour l'attribut `liste_eleve`
        """
        self.liste_eleve = value
        
    def get_nom_classe(self):
        """
        Fonction getter pour l'attribut `nom_classe`
        """
        return self.nom_classe
    
    def set_nom_classe(self, value):
        """
        Fonction setter pour l'attribut `nom_classe`
        """
        self.nom_classe = value
    
    # Méthodes Statiques
    @classmethod
    def generer(cls):
        """
        Genere un classe aléatoirement
        """
        liste_eleves = [Eleve.generer() for _ in range(10)]
        prefixe_class = [
            "S", "PT", "PG", "TT", "TG"
        ]
        prefixe = random.choice(prefixe_class)
        numero = random.randint(1, 9)
        nom = f"{prefixe}{numero}"
        return Classe(liste_eleves, nom)
    
    # Méthodes
    def ajouter_un_eleve(self, eleve):
        """
        Ajoute un eleve dans la classe
        ----------------
        # Arguments
        `eleve`: Eleve
            Infos sur l'eleve
        """
        self.liste_eleve.append(eleve)

    def liste_appel(self):
        """
        Renvoie la liste d'appel sur un fichier texte
        """
        appel = self.liste_eleve
        affichage = []
        appel.sort(key=lambda x: x.nom)
        
        for e in appel:
            affichage.append(f'{e.nom.upper()} {e.prenom}')
            
        affichage = "\n".join(affichage)

        with open(self.nom_classe + '.txt', 'w') as file:
            file.write(affichage)
            
        print('La liste a été exportée')