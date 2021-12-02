class Glissade:
    def __init__(self, nom, arrondissement, cle, date_maj, ouvert,
                 deblaye, condition):
        self.nom = nom
        self.arrondissement = arrondissement
        self.cle = cle
        self.date_maj = date_maj
        self.ouvert = ouvert
        self.deblaye = deblaye
        self.condition = condition

    def to_dict(self):
        return {
            'nom': self.nom,
            'arrondissement': self.arrondissement,
            'cle': self.cle,
            'date_maj': self.date_maj,
            'ouvert': self.ouvert,
            'deblaye': self.deblaye,
            'condition': self.condition
        }

    def min_info(self):
        return {
            'nom': self.nom
        }
