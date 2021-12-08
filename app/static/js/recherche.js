window.onload = () => {
    const chercherarrondissement = document.getElementById("recherche-arrondissement");
    chercherarrondissement.addEventListener("click", (event) => {
        event.preventDefault();
        var arrondissement = document.getElementById("arrondissement").value
        if (arrondissement == "") {
            document.getElementById("msgErreur").innerText = "Veuillez donner un nom d'arrondissement.";
            document.getElementById("msgErreur").style.color = "red";
        }
        else {
            document.getElementById("msgErreur").innerText = "";
            (async () => {
                const reponse = await fetch('/api/installations?arrondissement=' + arrondissement)
                const contenu = await reponse.json();
                if (reponse.status == 404) {
                    document.getElementById("liste-installations").innerHTML = contenu.message;
                } else {
                    let table = document.getElementById("liste-installations");
                    document.getElementById("liste-installations").innerHTML = "";
                    table = document.getElementById("liste-installations");
                    document.getElementById("informations").innerHTML = "";

                    let data = Object.keys(contenu);
                    creerEnTeteTableauInstallations(table, data);
                    creerTableauInstallations(table, contenu);
                }
            })();
        }
    });

    function creerEnTeteTableauInstallations(table, data) {
        table.innerHtml = "";
        let thead = table.createTHead();
        let row = thead.insertRow();
        for (let key of data) {
            let th = document.createElement("th");
            let text = document.createTextNode(key);
            th.appendChild(text);
            row.appendChild(th);
        }
    }

    const chercherinstallation = document.getElementById("recherche-installation");
    chercherinstallation.addEventListener("click", (event) => {
        event.preventDefault();
        var nom = document.getElementById("nomsInstallations").value
        if (nom == "") {
            document.getElementById("msgErreur").innerText = "Veuillez sélectionner un nom d'installation.";
            document.getElementById("msgErreur").style.color = "red";
        }
        else {
            (async () => {
                const reponse = await fetch('/api/info?nom=' + nom)
                const contenu = await reponse.json();
                if (reponse.status == 404) {
                    document.getElementById("informations").innerHTML = content.message;
                } else {
                    var informations = contenu;
                    let tableau = document.getElementById("informations");
                    document.getElementById("informations").innerHTML = "";
                    document.getElementById("liste-installations").innerHTML = "";
                    table = document.getElementById("liste-installations");
                    creerEnTeteTableauInformations(tableau, informations);
                    creerTableauInformations(tableau, informations);
                }
            })();
        }
    });

    function creerEnTeteTableauInformations(table, data) {
        table.innerHtml = "";
        let thead = table.createTHead();
        let row = thead.insertRow();
        let th = document.createElement("th");
        let text = document.createTextNode("Attribut");
        th.appendChild(text);
        row.appendChild(th);
        th = document.createElement("th");
        text = document.createTextNode("Valeur");
        th.appendChild(text);
        row.appendChild(th);
    }

    function creerTableauInformations(tableau, informations) {
        for (let clef in informations[0]) {
            let row = tableau.insertRow();
            let cell = row.insertCell();
            let text;
            text = document.createTextNode(clef);
            cell.appendChild(text);
            cell = row.insertCell();
            text = document.createTextNode(informations[0][clef]);
            cell.appendChild(text);
            cell = row.insertCell();
        }
    }

    function creerTableauInstallations(table, contenu) {
        let max = Math.max(contenu['glissades'].length, contenu['patinoires'].length, contenu['piscines'].length);
        for (let i = 0; i < max; i++) {
            let row = table.insertRow();
            let cell = row.insertCell();
            let text;
            if (contenu['glissades'][i]) {
                text = document.createTextNode(contenu['glissades'][i]);
                cell.appendChild(text);
                cell = row.insertCell();
            } else {
                text = document.createTextNode("");
                cell.appendChild(text);
                cell = row.insertCell();
            }
            if (contenu['patinoires'][i]) {
                text = document.createTextNode(contenu['patinoires'][i]);
                cell.appendChild(text);
                cell = row.insertCell();
            } else {
                text = document.createTextNode("");
                cell.appendChild(text);
                cell = row.insertCell();
            }
            if (contenu['piscines'][i]) {
                text = document.createTextNode(contenu['piscines'][i]);
                cell.appendChild(text);
                cell = row.insertCell();
            } else {
                text = document.createTextNode("");
                cell.appendChild(text);
                cell = row.insertCell();
            }
        }
    }

}
