from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask_bcrypt import Bcrypt
from flask_json_schema import JsonSchema
from .donnees import *
from .glissade import *
from .patinoire import *
from .piscine import *
from .utilisateur import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
schema = JsonSchema(app)
app.config['SECRET_KEY'] = "87e7812695e54ee4e18c0904fd183ad8"
bcrypt = Bcrypt(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route('/', methods=["GET", "PUT"])
def index():
    nom_installations = get_db().get_nom_installations()
    liste_installations = []
    for installation in nom_installations:
        liste_installations.append(installation[0])
    return render_template("index.html", nomsInstallations=liste_installations)


@app.route('/doc')
def documentation():
    return render_template('doc.html')


@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'GET':
        arrondissements = get_db().get_arrondissements()
        return render_template(
            'inscription.html', arrondissements=arrondissements)
    else:
        nom = request.form["nom"]
        courriel = request.form["courriel"]
        mdp = request.form["mdp"]
        liste_arr = request.form["liste_arr"]
        if nom == "" or courriel == "" or mdp == "" or liste_arr == "":
            return render_template(
                "inscription.html",
                error="Vous devez remplir tous les champs.")
        return redirect("/succes")


@app.route('/api/installations', methods=["GET"])
def get_installations():
    arrondissement = request.args.get('arrondissement')

    if arrondissement is not None:
        glissades = get_db().get_glissades_arrondissement(arrondissement)
        patinoires = get_db().get_patinoires_arrondissement(arrondissement)
        piscines = get_db().get_piscines_arrondissement(arrondissement)

        if not glissades and not patinoires and not piscines:
            message_aucune_installation = {
                "message_erreur:": "Aucun résultat pour cet arrondissement"
            }
            return jsonify(message_aucune_installation), 404
        else:
            nom_glissades = []
            nom_patinoires = []
            nom_piscines = []
            for glissade in glissades:
                nom_glissades.append(glissade.nom)
            for patinoire in patinoires:
                nom_patinoires.append(patinoire.nom)
            for piscine in piscines:
                nom_piscines.append(piscine.nom)

            installations = {
                'glissades': nom_glissades,
                'patinoires': nom_patinoires,
                'piscines': nom_piscines}

            return jsonify(installations)
    else:
        return render_template('404.html'), 404


@app.route('/api/info', methods=["GET"])
def get_installations_nom():
    nom = request.args.get('nom')

    glissades = get_db().get_glissades_nom_ins(nom)
    patinoires = get_db().get_patinoires_nom_ins(nom)
    piscines = get_db().get_piscines_nom_ins(nom)
    if not glissades and not patinoires and not piscines:
        message_aucune_installation = {
            "message_erreur:": "Aucun résultat pour cet installation"
        }
        return jsonify(message_aucune_installation), 404
    else:
        glissade_info = [glissade.to_dict() for glissade in glissades]
        patinoire_info = [patinoire.to_dict() for patinoire in patinoires]
        piscines_info = [piscine.to_dict() for piscine in piscines]

        info = glissade_info
        info.extend(patinoire_info)
        info.extend(piscines_info)
        info = jsonify(info)

        return info


@app.route('/api/utilisateur', methods=["POST"])
@schema.validate(create_user_schema)
def creer_utilisateur():
    data = request.get_json()
    mdp_hashed = bcrypt.generate_password_hash(data["mdp"]).decode('utf-8')
    utilisateur = Utilisateur(
        data["nom"], data["courriel"], mdp_hashed, data["liste_arr"])
    utilisateur = get_db().inserer_utilisateur(utilisateur)
    return jsonify(utilisateur.min_info()), 201
