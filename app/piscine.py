class Piscine:
    def __init__(self, id_uev, type, nom, arrondissement, adresse, propriete,
                 gestion, point_x, point_y, equipement, longitude, latitude):
        self.id_uev = id_uev
        self.type = type
        self.nom = nom
        self.arrondissement = arrondissement
        self.adresse = adresse
        self.propriete = propriete
        self.gestion = gestion
        self.point_x = point_x
        self.point_y = point_y
        self.equipement = equipement
        self.longitude = longitude
        self.latitude = latitude

    def to_dict(self):
        return {
            'id_uev': self.id_uev,
            'type': self.type,
            'nom': self.nom,
            'arrondissement': self.arrondissement,
            'adresse': self.adresse,
            'propriete': self.propriete,
            'gestion': self.gestion,
            'point_x': self.point_x,
            'point_y': self.point_y,
            'equipement': self.equipement,
            'longitude': self.longitude,
            'latitude': self.latitude
        }

    def min_info(self):
        return {
            'nom': self.nom
        }


def liste_piscines(self):
    return {
        'piscines': self.piscines
    }
