from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import yaml


def envoyer_courriel(destinataire, courriel_installations):
    sujet = "Nouvelles installations de la ville de Montreal"
    adresse = "installationsmontreal@gmail.com"
    contenu = courriel_installations
    msg = MIMEMultipart()
    msg['Subject'] = sujet
    msg['From'] = adresse
    msg['To'] = ', '.join(destinataire)
    msg['ReplyTo'] = adresse
    msg.attach(MIMEText(contenu, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(adresse, "inf5190h2021")
    text = msg.as_string()
    server.sendmail(adresse, destinataire, text)
    server.quit()


def envoyer_nouvelles_installations(courriel_installations):
    destinataires = get_destinataires()
    for d in destinataires:
        envoyer_courriel(d, courriel_installations)


def get_destinataires():
    with open('config.yaml') as f:
        yaml_doc = yaml.full_load(f)
        email = yaml_doc['email_list']
        return email
