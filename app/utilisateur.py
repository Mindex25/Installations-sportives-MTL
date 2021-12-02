from .database import *


class Utilisateur:
    def __init__(self, nom, courriel, mdp, liste_arr):
        self.nom = nom
        self.courriel = courriel
        self.mdp = mdp
        self.liste_arr = liste_arr

    def min_info(self):
        return {
            "nom": self.nom,
            "email": self.courriel,
            "mdp": self.mdp,
            "liste_arr": self.liste_arr
        }


create_user_schema = {
    "type": "object",
    "required": ["nom", "courriel", "mdp", "liste_arr"],
    "properties": {
        "nom": {
            "type": "string"
        },
        "courriel": {
            "type": "string", "format": "email"
        },
        "mdp": {
            "type": "string"
        },
        "liste_arr": {
            "type": "string"
        }
    },
    "additionalProperties": False
}
