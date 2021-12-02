class Patinoire:
    def __init__(self, arrondissement, nom, date, ouvert, deblaye,
                 arrose, resurface):
        self.nom = nom
        self.arrondissement = arrondissement
        self.date = date
        self.ouvert = ouvert
        self.deblaye = deblaye
        self.arrose = arrose
        self.resurface = resurface

    def to_dict(self):
        return {
            'nom': self.nom,
            'arrondissement': self.arrondissement,
            'date': self.date,
            'ouvert': self.ouvert,
            'deblaye': self.deblaye,
            'arrose': self.arrose,
            'resurface': self.resurface
        }

    def min_info(self):
        return {
            'nom': self.nom
        }
