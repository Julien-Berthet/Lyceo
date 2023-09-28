import webbrowser
import random

from data import QUESTIONS, NOMS, MATIERES
from professeur import Professeur
from classe import Classe

class Lycee:
    """
    # Classe Lycee
    ----------------
    Représente un lycée sur l'application
    """
    def __init__(self, nom: str, site_web: str):
        """
        # Arguments
        `nom`: str
            Nom de l'établissement
        `site_web`: str
            Lien vers le site web de l'établissement
        """
        self.nom = nom
        self.site_web = site_web
        self.classes = []
        self.professeurs = []

    def _poser_question(self, component: dict):
        """
        Méthode protégée
        Pose une question lors de l'entretien dans la console
        ----------------
        # Arguments
        `component`: dict
            dictionnaire comportant les informations nécessaires
        """
        question = component['question']
        reponses = component['reponses']
        correct = component['correct']
        print(f'Question: {question}')

        for reponse in reponses:
            print(f'  {reponse}')

        guess = None
        while type(guess) != int:
            try:
                guess = int(input('Entrez 1, 2, ou 3: '))
            except ValueError:
                print('Veuillez entrer un nombre')
                guess = None

        return guess == correct

    # Getters et Setters
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
        
    def get_site_web(self):
        """
        Fonction getter pour l'attribut `site_web`
        """
        return self.site_web
    
    def set_site_web(self, value):
        """
        Fonction setter pour l'attribut `site_web`
        """
        self.site_web = value
        
    def get_classes(self):
        """
        Fonction getter pour l'attribut `classes`
        """
        return self.classes
    
    def set_classes(self, value):
        """
        Fonction setter pour l'attribut `classes`
        """
        self.classes = value
        
    def get_professeurs(self):
        """
        Fonction getter pour l'attribut `professeurs`
        """
        return self.professeurs
    
    def set_professeurs(self, value):
        """
        Fonction setter pour l'attribut `professeurs`
        """
        self.professeurs = value
    
    # Méthodes statiques
    @classmethod
    def generer(cls):
        """
        Méthode Statique
        Génère un lycée avec des attributs aléatoires
        """
        # Site Web par défaut: https://www.lycee-julesfroment.fr/
        site_web = 'https://www.lycee-julesfroment.fr/'
        nom = random.choice(NOMS)
        lycee = Lycee(nom, site_web)
        
        for _ in range(6):
            lycee.classes.append(Classe.generer())

        for m in MATIERES:
            prof = Professeur.generer()
            prof.matiere = m
            lycee.professeurs.append(prof)

        cls.mettre_a_jour_matieres(lycee)
        return lycee

    # Méthodes
    def ouvrir_site_web(self):
        """
        Ouvre le site du lycée dans un nouveau navigateur
        """
        webbrowser.open(self.site_web)
        
    def ajouter_classe(self, classe):
        """
        Ajoute la classe donnée dans le lycée
        ----------------
        # Arguments
        `classe`: Classe
            Classe à ajouter
        """
        self.classes.append(classe)
        self.mettre_a_jour_matieres()

    def recruter_professeur(self, professeur, ignorer_quizz = False):
        """
        Pose 3 question en rapport avec la matière du professeur
        Si 2 ou 3 bonnes réponses le professeur donné est recruté
        ----------------
        # Arguments
        `professeur`: Professeur
            Objet Professeur à recruter
        `ignorer_quiz`: bool
            Ignore le quizz de recrutement
        """
        if ignorer_quizz:
            self.professeurs.append(professeur)
            self.mettre_a_jour_matieres()
            return
        
        matiere = professeur.matiere
        questions = QUESTIONS[matiere]
        reponses_correctes = 0
        
        for q in questions:
            print('\n----------------')
            correct = self._poser_question(q)
            if correct:
                reponses_correctes += 1

        if reponses_correctes >= 2:
            print('')
            print(f"Vous avez eu {reponses_correctes} bonnes réponses")
            print(f"{professeur.affichage()} est recruté!")
            self.professeurs.append(professeur)

        else:
            print(f"Vous avez eu {reponses_correctes} bonnes réponses")
            print(f"{professeur.affichage()} n'est pas recruté...")
            
        self.mettre_a_jour_matieres()

    def eleves(self):
        """
        Itérateur qui permet de boucler à travers
        tous les élèves du lycée
        # Exemple
        for eleve in eleves():
            print(eleve)
        """
        for classe in self.classes:
            for eleve in classe.liste_eleve:
                yield eleve

    def ajouter_notes_aleatoires(self):
        """
        Remplit l'attribute "notes" de tous les elèves
        avec des notes aléatoires
        """
        for eleve in self.eleves():
            eleve.ajouter_notes_aleatoires()

    def mettre_a_jour_matieres(self):
        """
        Met a jour les matières éligibles à la notation en fonction des
        professeurs embauchés
        """
        matieres = set()
        for prof in self.professeurs:
            matieres.add(prof.matiere)

        for classe in self.classes:
            for eleve in classe.liste_eleve:
                for m in matieres:
                    if m not in eleve.notes.keys():
                        eleve.notes[m] = []

                for m in eleve.notes.keys():
                    if m not in matieres:
                        del eleve.notes[m]
                        
    def combat_lyceo(self):
        """
        Cree un combat aléatoire entre deux élèves du lycée
        """
        eleves = [e for e in self.eleves()]
        
        eleve1 = random.choice(eleves)
        eleve2 = random.choice(eleves)
        
        eleve1.ajouter_notes_aleatoires()
        eleve2.ajouter_notes_aleatoires()
        
        eleve1.combattre(eleve2)