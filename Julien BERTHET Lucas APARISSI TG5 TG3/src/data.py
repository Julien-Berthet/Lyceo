"""
Fichier dans lequel sont importés les données du dossier 'data'
au format JSON (JavaScript Object Notation) avec le module built-in
json. Ces données sont ensuite importées dans des constantes.
"""
import json

with open("src/data/matieres.json") as file:
    MATIERES = json.load(file)

with open("src/data/questions.json") as file:
    QUESTIONS = json.load(file)

with open("src/data/noms.json") as file:
    noms = json.load(file)
    PRENOMS_MASCULINS = noms['M']
    PRENOMS_FEMININS = noms['F']
    NOMS = noms['NOM']
