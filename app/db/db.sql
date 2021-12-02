create table piscine(
    id integer primary key autoincrement,
    id_uev varchar(50),
    type varchar(50),
    nom varchar(50),
    arrondissement varchar(50),
    adresse varchar(50),
    propriete varchar(50),
    gestion varchar(50),
    point_x varchar(50),
    point_y varchar(50),
    equipement varchar(50),
    longitude varchar(50),
    latitude varchar(50),
    unique(nom)
);

create table patinoire(
    id integer primary key autoincrement,
    arrondissement varchar(50),
    nom varchar(50),
    date varchar(50),
    ouvert varchar(10),
    deblaye varchar(10),
    arrose varchar(10),
    resurface varchar(10),
    unique(nom)
);

create table glissade(
    id integer primary key autoincrement,
    nom varchar(50),
    arrondissement varchar(50),
    cle varchar(50),
    date_maj varchar(10),
    ouvert varchar(10),
    deblaye varchar(10),
    condition varchar(100),
    unique(nom)
);

CREATE TABLE utilisateur (
    nom VARCHAR(50),
    courriel VARCHAR(50),
    mdp VARCHAR(50),
    liste_arr TEXT,
    unique(courriel)
);