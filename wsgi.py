from app.courriel import envoyer_nouvelles_installations
from app.app import *
from apscheduler.schedulers.background import BackgroundScheduler

app = getApp()

def maj_donnees():
    with app.app_context():
        nombre_glissades_avant_maj = get_db().get_nombre_glissades()
        nombre_patinoires_avant_maj = get_db().get_nombre_patinoires()
        nombre_piscines_avant_maj = get_db().get_nombre_piscines()
        importer_donnees()
        nouvelles_installations = get_db().get_nouvelles_installations(
                nombre_glissades_avant_maj, nombre_patinoires_avant_maj,
                nombre_piscines_avant_maj)
        courriel_installations = '\n'.join(map(str, nouvelles_installations))
        envoyer_nouvelles_installations(courriel_installations)

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(maj_donnees, 'cron', hour=0)
scheduler.start()


if __name__ == "__main__":
    # Pour la correction
    # maj_donnees()
    app.run()