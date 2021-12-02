import csv
from datetime import datetime
from flask import g
import requests
from xml.etree import ElementTree
from .database import Database


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


def importer_piscines():
    url = "https://data.montreal.ca/dataset/4604afb7-a7c4-4626-a3ca-e136158133f2/resource/cbdca706-569e-4b4a-805d-9af73af03b14/download/piscines.csv"
    reponse = requests.get(url)
    if reponse.status_code == 200:
        decoded_content = reponse.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        piscines = list(cr)
        premiere_ligne = True
        for row in piscines:
            if premiere_ligne:
                premiere_ligne = False
            else:
                get_db().inserer_piscine(row[0], row[1], row[2],
                                         uniformiser_arrondissement(row[3]),
                                         row[4], row[5], row[6], row[7],
                                         row[8], row[9], row[10], row[11])


def importer_patinoires():
    url = "https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0/download/l29-patinoire.xml"
    reponse = requests.get(url)
    if reponse.status_code == 200:
        racine = ElementTree.fromstring(reponse.content)

        for patinoire in racine:
            arrondissement = patinoire[0].text.strip()
            nom = patinoire[1][0].text.strip()
            derniere_date = datetime.fromisoformat("2000-01-01 00:00:00")
            for condition in patinoire[1].iter('condition'):
                if datetime.fromisoformat(
                        condition[0].text.strip()) > derniere_date:

                    date = condition[0].text.strip()
                    ouvert = condition[1].text.strip()
                    deblaye = condition[2].text.strip()
                    arrose = condition[3].text.strip()
                    resurface = condition[4].text.strip()
                    derniere_date = datetime.fromisoformat(
                        condition[0].text.strip())
            get_db().inserer_patinoire(arrondissement, nom, date, ouvert,
                                       deblaye, arrose, resurface)


def importer_glissades():
    url = "http://www2.ville.montreal.qc.ca/services_citoyens/pdf_transfert/L29_GLISSADE.xml"
    reponse = requests.get(url)
    if reponse.status_code == 200:
        racine = ElementTree.fromstring(reponse.content)

        for glissade in racine.findall('glissade'):
            nom = glissade.find('nom').text
            nom_arrondissement = glissade.find('arrondissement')
            arrondissement = nom_arrondissement.find('nom_arr').text
            cle = nom_arrondissement.find('cle').text
            date_maj = nom_arrondissement.find('date_maj').text
            ouvert = glissade.find('ouvert').text
            deblaye = glissade.find('deblaye').text
            condition = glissade.find('condition').text
            get_db().inserer_glissade(nom, arrondissement, cle,
                                      date_maj, ouvert, deblaye, condition)


def importer_donnees():
    importer_piscines()
    importer_patinoires()
    importer_glissades()


def uniformiser_arrondissement(arrondissement):
    if "Ahuntsic" in arrondissement:
        return "Ahuntsic - Cartierville"
    elif "Côte-des-Neiges" in arrondissement:
        return "Côte-des-Neiges - Notre-Dame-de-Grâce"
    elif "L'Île-Bizard" in arrondissement:
        return "L'Île-Bizard - Sainte-Geneviève"
    elif "Mercier" in arrondissement:
        return "Mercier - Hochelaga-Maisonneuve"
    elif "Pierrefonds" in arrondissement:
        return "Pierrefonds - Roxboro"
    elif "Rivière-des-Prairies" in arrondissement:
        return "Rivière-des-Prairies - Pointe-aux-Trembles"
    elif "Rosemont" in arrondissement:
        return "Rosemont - La Petite-Patrie"
    elif "Villeray" in arrondissement:
        return "Villeray-Saint-Michel - Parc-Extension"
    else:
        return arrondissement
