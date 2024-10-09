import streamlit as st
import requests
import json
from datetime import datetime

# Titre de l'application
st.title("Suivi des Cadences Professionnelles")

# Saisie des données
st.header("Saisissez les informations de vos dossiers")
nombre_dossiers = st.number_input("Nombre de dossiers traités", min_value=0)
date = st.date_input("Date", value=datetime.today())

# Bouton pour soumettre les données
if st.button("Soumettre"):
    # Préparer les données à sauvegarder
    data = {
        "date": date.isoformat(),
        "nombre_dossiers": nombre_dossiers
    }

    # URL pour l'API GitHub
    token = "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"
    repo_name = "tsi-cadence"
    file_name = f"cadences_{date.isoformat()}.json"
    url = f"https://api.github.com/repos/YOUR_USERNAME/{repo_name}/contents/{file_name}"

    # Vérification de l'existence du fichier
    response = requests.get(url, headers={"Authorization": f"token {token}"})
    
    if response.status_code == 200:
        # Fichier existe déjà, mettre à jour
        sha = response.json()["sha"]
        existing_data = json.loads(requests.get(url).json()["content"])
        existing_data.append(data)
        content = json.dumps(existing_data)

        # Mettre à jour le fichier
        requests.put(url, headers={
            "Authorization": f"token {token}",
            "Content-Type": "application/json"
        }, json={
            "message": "Mise à jour des cadences",
            "sha": sha,
            "content": content,
            "branch": "main"
        })
    else:
        # Créer un nouveau fichier
        content = json.dumps([data])

        requests.put(url, headers={
            "Authorization": f"token {token}",
            "Content-Type": "application/json"
        }, json={
            "message": "Création du fichier de cadences",
            "content": content,
            "branch": "main"
        })

    st.success("Données enregistrées avec succès !")
