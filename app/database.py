import sqlite3
from .glissade import *
from .patinoire import *
from .piscine import *


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('app/db/db.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def inserer_piscine(self, id_uev, type, nom, arrondissement, adresse,
                        propriete, gestion, point_x, point_y, equipement,
                        longitude, latitude):
        connexion = self.get_connection()
        curseur = self.get_connection().cursor()
        curseur.execute(("insert or replace into piscine("
                         "id_uev, type, nom, arrondissement, adresse,"
                         "propriete, gestion, point_x, point_y, equipement,"
                         "longitude, latitude)"
                         "values(?,?,?,?,?,?,?,?,?,?,?,?)"),
                        (id_uev, type, nom, arrondissement, adresse,
                         propriete, gestion, point_x, point_y, equipement,
                         longitude, latitude))
        connexion.commit()

    def inserer_patinoire(self, arrondissement, nom, date, ouvert, deblaye,
                          arrose, resurface):
        connexion = self.get_connection()
        curseur = self.get_connection().cursor()
        curseur.execute(("insert or replace into patinoire("
                         "arrondissement, nom, date, ouvert, deblaye,"
                         "arrose, resurface)"
                         "values(?,?,?,?,?,?,?)"),
                        (arrondissement, nom, date, ouvert, deblaye,
                         arrose, resurface))
        connexion.commit()

    def inserer_glissade(self, nom, arrondissement, cle, date_maj, ouvert,
                         deblaye, condition):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        curseur.execute(("insert or replace into glissade("
                        "nom, arrondissement, cle, date_maj, ouvert,"
                         "deblaye, condition)"
                         "values(?,?,?,?,?,?,?)"),
                        (nom, arrondissement, cle, date_maj, ouvert,
                        deblaye, condition))
        connexion.commit()

    def inserer_utilisateur(self, utilisateur):
        connexion = self.get_connection()
        connexion.execute("insert into utilisateur"
                          "(nom, courriel, mdp, liste_arr)"
                          "values(?, ?, ?, ?)",
                          (utilisateur.nom, utilisateur.courriel,
                           utilisateur.mdp, utilisateur.liste_arr))
        connexion.commit()
        return utilisateur

    def get_arrondissements(self):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        curseur.execute(("""select distinct arrondissement 
                        from piscine order by arrondissement"""))
        liste_arr = curseur.fetchall()
        return liste_arr

    def get_glissades_arrondissement(self, arrondissement):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        curseur.execute(
            ("select * from glissade where arrondissement = ?"),
            (arrondissement,))
        glissades = curseur.fetchall()
        return (Glissade(g[1], g[2], g[3], g[4], g[5], g[6], g[7])
                for g in glissades)

    def get_patinoires_arrondissement(self, arrondissement):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        curseur.execute(
            ("select * from patinoire where arrondissement = ?"),
            (arrondissement,))
        patinoires = curseur.fetchall()
        return (Patinoire(p[1], p[2], p[3], p[4], p[5], p[6], p[7])
                for p in patinoires)

    def get_piscines_arrondissement(self, arrondissement):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        curseur.execute(
            ("select * from piscine where arrondissement = ?"),
            (arrondissement,))
        piscines = curseur.fetchall()
        return (Piscine(p[1], p[2], p[3], p[4], p[5], p[6],
                        p[7], p[8], p[9], p[10], p[11], p[12])
                for p in piscines)

    def get_glissades_nom_ins(self, nom):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        curseur.execute(
            ("select * from glissade where nom = ?"), (nom,))
        glissades = curseur.fetchall()
        return (Glissade(g[1], g[2], g[3], g[4], g[5], g[6], g[7])
                for g in glissades)

    def get_patinoires_nom_ins(self, nom):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        curseur.execute(
            ("select * from patinoire where nom = ?"), (nom,))
        patinoires = curseur.fetchall()
        return (Patinoire(p[1], p[2], p[3], p[4], p[5], p[6], p[7])
                for p in patinoires)

    def get_piscines_nom_ins(self, nom):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        curseur.execute(
            ("select * from piscine where nom = ?"), (nom,))
        piscines = curseur.fetchall()
        return (Piscine(p[1], p[2], p[3], p[4], p[5], p[6], p[7],
                        p[8], p[9], p[10], p[11], p[12])
                for p in piscines)

    def get_nom_installations(self):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        curseur.execute(("select nom from glissade"))
        glissades = curseur.fetchall()
        curseur.execute(("select nom from patinoire"))
        patinoires = curseur.fetchall()
        curseur.execute(("select nom from piscine"))
        piscines = curseur.fetchall()

        nom_installations = []
        nom_installations.extend(glissades)
        nom_installations.extend(patinoires)
        nom_installations.extend(piscines)
        return nom_installations

    def get_nombre_piscines(self):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        curseur.execute("select count(*) from piscine")
        nombre_piscines = curseur.fetchone()[0]
        return nombre_piscines

    def get_nombre_patinoires(self):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        curseur.execute("select count(*) from patinoire")
        nombre_patinoires = curseur.fetchone()[0]
        return nombre_patinoires

    def get_nombre_glissades(self):
        connexion = self.get_connection()
        curseur = connexion.cursor()
        curseur.execute("select count(*) from glissade")
        nombre_glissades = curseur.fetchone()[0]
        return nombre_glissades

    def get_nouvelles_installations(self, nombre_glissades,
                                    nombre_patinoires, nombre_piscines):
        cursor = self.get_connection().cursor()
        cursor.execute(
            ("select * from glissade where id > ?"), (nombre_glissades,))
        glissades = cursor.fetchall()
        cursor.execute(
            ("select * from patinoire where id > ?"), (nombre_patinoires,))
        patinoires = cursor.fetchall()
        cursor.execute(
            ("select * from piscine where id > ?"), (nombre_piscines,))
        piscines = cursor.fetchall()
        nouvelles_installations = [glissades, patinoires, piscines]
        return nouvelles_installations
