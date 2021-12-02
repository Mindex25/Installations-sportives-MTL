window.onload = () => {
    document.getElementById("inscription").addEventListener('submit', function (event) {
        event.preventDefault();
        document.getElementById("msg-erreur").innerText = "";
        var nom = document.getElementById("champ-nom").value;
        var courriel = document.getElementById("champ-courriel").value;
        var mdp = document.getElementById("champ-mdp").value;
        const selected = document.querySelectorAll('#form-liste_arr option:checked');
        console.log(selected);
        const liste_arr = Array.from(selected).map(el => el.value);
        if (nom == "" | courriel == "" | mdp == "" | liste_arr == "") {
            document.getElementById("msg-erreur").innerText = "Tous les champs sont obligatoires.";
            document.getElementById("msg-erreur").style.color = "red";
        } else {
            var utilisateur = new FormData();
            utilisateur.append("nom", nom);
            utilisateur.append("courriel", courriel);
            utilisateur.append("mdp", mdp);
            utilisateur.append("liste_arr", liste_arr);
            (async () => {
                const rawResponse = await fetch('/api/utilisateur', {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(Object.fromEntries(utilisateur))
                });
                const content = await rawResponse.json();
                console.log(content);
                var reponse = rawResponse.status;
                if (reponse == 404) {
                    document.getElementById("msg-retour").innerText = content;
                    document.getElementById("msg-retour").style.color = "red";
                }
                if (reponse == 201) {
                    document.getElementById("msg-retour").innerText = "Votre compte a été crée avec succès. \n"
                    document.getElementById("msg-retour").style.color = "green";
                }
            })();

        }

    })
};