from datetime import datetime
import random
import time

from data import *

class Eleve:
    """
    # Classe Eleve
    ----------------
    Représente un eleve inscrit sur Lyceo
    """
    def __init__(self, prenom: str, nom: str, genre: str, annee_de_naissance: int):
        """
        # Attributs
        `prenom`: str
            Prénom de l'élève
        `nom`: str
            Nom de l'élève
        `genre`: Literal['M', 'F']
            Genre de l'élève. Soit M (Masculin) soit F (Féminin)
        `annee_de_naissance`: int
            Année de naissance de l'élève
        """
        self.prenom = prenom
        self.nom = nom
        self.genre = genre
        self.annee_de_naissance = annee_de_naissance
        self.notes: dict[str, list[float]] = {}
        self.vie = 100
        self.en_combat = False
        self.ennemi = None
        
        if self.genre not in ('M', 'F'):
            raise Exception(f"Le genre '{self.genre}' n'est pas défini")

    def __repr__(self):
        return f"{self.prenom} {self.nom.upper()}"

    # Méthodes protégées
    def _convertir_matiere(self, matiere: str):
        """
        Méthode Protégée
        Converti d'éventuelles ambiguités sur le nom des matières
        Revoie une erreur si la matière spécifiée n'existe pas
        ----------------
        # Arguments
        `matiere`: str
            Matière à convertir
        """
        matiere = matiere.lower()
        
        accents = {
            "é": "e",
            "è": "e",
            "ç": "c"
        }
        
        for k, v in accents.items():
            matiere = matiere.replace(k, v)
        
        if matiere in ('mathematiques', 'mathematique', 'maths', 'm'):
            return 'Mathematiques'
        
        if matiere in ('anglais', 'a'):
            return 'Anglais'
        
        if matiere in ('histoire-geo', 'histoire', 'geo',
                      'histoire-geographie', 'emc', 'hg', 'h'):
            return 'Histoire-Geographie'
        
        if matiere in ('francais', 'fr', 'f'):
            return 'Francais'
        
        if matiere in ('nsi', 'numerique et sciences informatiques', 'n'):
            return 'NSI'

        # PEP 8 non respéctée car message trop long
        raise Exception("La matière spécifiée n\'est pas supporté car ce lycée n'a pas de professeur")

    def _moyenne(self, liste):
        """
        Methode Protégée
        Renvoie la moyenne d'une liste de nombres
        ----------------
        # Arguments
        `liste`: list[float]
            Liste de nombre d'où l'on doit récuperer la moyenne
        """
        if len(liste) == 0:
            return 10
        return round(sum(liste) / len(liste), 2)
    
    # Getters et Setters
    def get_prenom(self):
        """
        Fonction getter pour l'attribut `prenom`
        """
        return self.prenom
    
    def set_prenom(self, value):
        """
        Fonction setter pour l'attribut `prenom`
        """
        self.prenom = value
        
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
        
    def get_annee_de_naissance(self):
        """
        Fonction getter pour l'attribut `annee_de_naissance`
        """
        return self.annee_de_naissance
    
    def set_annee_de_naissance(self, value):
        """
        Fonction setter pour l'attribut `annee_de_naissance`
        """
        self.annee_de_naissance = value
        
    def get_notes(self):
        """
        Fonction getter pour l'attribut `notes`
        """
        return self.notes
    
    def set_notes(self, value):
        """
        Fonction setter pour l'attribut `notes`
        """
        self.notes = value
        
    def get_vie(self):
        """
        Fonction getter pour l'attribut `vie`
        """
        return self.notes
    
    def set_vie(self, value):
        """
        Fonction setter pour l'attribut `vie`
        """
        self.vie = value
        
    def get_en_combat(self):
        """
        Fonction getter pour l'attribut `en_combat`
        """
        return self.en_combat
    
    def set_en_combat(self, value):
        """
        Fonction setter pour l'attribut `en_combat`
        """
        self.en_combat = value
        
    def get_ennemi(self):
        """
        Fonction getter pour l'attribut `ennemi`
        """
        return self.ennemi
    
    def set_ennemi(self, value):
        """
        Fonction setter pour l'attribut `ennemi`
        """
        self.ennemi = value

    # Méthodes Statiques
    @classmethod
    def generer(cls):
        """
        Méthode Statique
        Génère un eleve avec des attributs aléatoires
        """
        genre = random.randint(0, 1)
        if genre:
            genre = 'M'
            prenom = random.choice(PRENOMS_MASCULINS)
        else:
            genre = 'F'
            prenom = random.choice(PRENOMS_FEMININS)
        nom = random.choice(NOMS)

        return Eleve(prenom, nom, genre, random.randint(2005, 2010))

    # Méthodes
    def get_age(self):
        """
        Renvoie l'age de l'élêve en fonction de l'année courante
        ----------------
        """
        annee_actuelle = datetime.now().year
        return annee_actuelle - self.annee_de_naissance

    def ajouter_note(self, matiere: str, note: float):
        """
        Ajoute une note dans une matière donnée
        ----------------
        # Arguments
        `matiere`: str
            La matière dans laquelle ajouter la note
        `note`: float
            La note à ajouter
        """
        matiere = self._convertir_matiere(matiere)
        self.notes[matiere].append(note)

    def get_moyenne(self, matiere: str):
        """
        Renvoie la moyenne de l'élève de la matière spécifiée
        ----------------
        # Arguments
        `matiere`: str
            Matière d'où l'on doit récuperer la moyenne
        """
        matiere = self._convertir_matiere(matiere)
        notes = self.notes[matiere]
        return self._moyenne(notes)

    def get_moyenne_generale(self):
        """
        Renvoie la moyenne générale de l'élève
        -----------------
        """
        moyennes = []
        for notes in self.notes.values():
            if notes == []:
                continue
            moyennes.append(self._moyenne(notes))
        return self._moyenne(moyennes)

    def ajouter_notes_aleatoires(self):
        """
        Remplit l'attribute "notes" de l'élève avec des notes
        aléatoires
        """
        for m in self.notes.keys():
            for _ in range(random.randint(1, 10)):
                self.notes[m].append(random.randint(0, 20))

    def combattre(self, ennemi, manuel = False):
        """
        Fais se combattre deux élèves
        Voir système de comabat dans le document explicatif
        ----------------
        # Arguments
        `ennemi`: Eleve
            Objet eleve avec lequel simuler un combat
        `manuel`: bool
            Active le mode manuel, forcant l'utilisation des fonctions
            manuellement
        """
        print(f"Un combat à débuté entre {self} et {ennemi}!")
        if ennemi.en_combat:
            print(f'{ennemi} est déjà en combat!')
            return

        if self.nom == ennemi.nom and self.prenom == ennemi.prenom:
            print('\n=> Vous avez trouvé un secret')
            print('|| Combattre un miroir ||\n')

        self.en_combat = True
        self.ennemi = ennemi
        self.ennemi.en_combat = True
        self.ennemi.ennemi = self
        
        if manuel:
            return

        # Celui avec la meilleure moyenne générale commence
        moyenne_generale_self = self.get_moyenne_generale()
        moyenne_generale_ennemi = self.ennemi.get_moyenne_generale()

        attaquant = 'self'
        if moyenne_generale_ennemi >= moyenne_generale_self:
            attaquant = 'ennemi'
            print(f'{self.ennemi} commence')
        else:
            print(f'{self} commence')

        while self.en_combat:

            if attaquant == 'self':
                print('\n----------------')
                print('Choisir une action:')
                print('  1. Attaquer avec un attaque Mathématique')
                print('  2. Attaquer avec un attaque d\'Histoire-Geo')
                print('  3. Attaquer avec un attaque de Français')
                print('  4. Attaquer avec un attaque Anglais')
                print('  5. Attaquer avec un attaque NSI')
                print('  6. Déclarer forfait')

                choix = ''
                while choix not in ['1', '2', '3', '4', '5', '6']:
                    choix = input("Inserez 1, 2, 3, 4, 5 ou 6: ")

                choix = int(choix)

                if choix == 1:
                    self.attaquer('mathematiques')
                elif choix == 2:
                    self.attaquer('histoire-geo')
                elif choix == 3:
                    self.attaquer('francais')
                elif choix == 4:
                    self.attaquer('anglais')
                elif choix == 5:
                    self.attaquer('nsi')
                elif choix == 6:
                    print(f'{self} à déclaré forfait!')
                    self.arreter_le_combat()
                    break
                attaquant = 'ennemi'

            else:
                print('\n----------------')
                self.ennemi.attaque_aleatoire()
                attaquant = 'self'

            time.sleep(1.0)

        print('COMBAT TERMINE')

    def arreter_le_combat(self):
        """
        Met fin au combat en cours et retablit la vie
        des protagonistes
        """
        # PEP 8 non respéctée car message trop long
        print(f"Le combat entre {repr(self)} et {repr(self.ennemi)} s'est arrêté")
        self.vie = 100
        self.ennemi.vie = 100
        self.ennemi.en_combat = False
        self.en_combat = False
        self.ennemi = None

    def attaquer(self, matiere: str):
        """
        Attaque l'enemi du combat en cours avec une attaque
        dans la matière spécifiée
        ----------------
        # Arguments
        `matiere`: str
            Matière dans laquelle attaquer
        """
        if not self.en_combat:
            print('Vous devez être en combat pour attaquer!')
            return False

        matiere = self._convertir_matiere(matiere)

        degats = 20

        note_self = self.get_moyenne(matiere)
        degats *= (note_self / 40)

        note_ennemi = self.ennemi.get_moyenne(matiere)
        degats /= (note_ennemi / 40) + 0.01 # On evite la ZeroDivisionError en ajoutant 0.01 au dénominateur

        degats = round(degats, 1)

        print('\n----------------')

        if degats > 2:
            print(f'{self} a infligé {degats} dégats à {self.ennemi}!')
            self.ennemi.vie -= degats

            if self.ennemi.vie > 0:
                print(f'{int(self.ennemi.vie)}/100 points de vie restants')

        else:
            print(f'{self} a râté son attaque contre {self.ennemi}...')

        if self.ennemi.vie <= 0.0:
            print(f"{self} à vaincu {self.ennemi}!")
            self.arreter_le_combat()
            del self.ennemi

    def attaque_aleatoire(self):
        """
        Crée une attaque aléatoire dans une matière aléatoire
        A 1/20 de déclarer forfait
        """
        rng = random.randint(1, 20)
        if rng == 1:
            print(f'{self} à déclaré forfait!')
            self.arreter_le_combat()

        rng = random.randint(1, 5)
        if rng == 1:
            self.attaquer('mathematiques')
        elif rng == 2:
            self.attaquer('histoire-geo')
        elif rng == 3:
            self.attaquer('francais')
        elif rng == 4:
            self.attaquer('anglais')
        elif rng == 5:
            self.attaquer('nsi')