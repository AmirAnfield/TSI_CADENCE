import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Configuration des autorisations
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("Credentials/tsi-cadence-678df727045f.json", scopes=scope)
client = gspread.authorize(creds)

# Ouvrir la feuille de calcul
sheet = client.open("TSI_CADENCE").sheet1  # Utilise le nom de ta feuille ici

# Fonction pour le calcul des cadences
def calculer_cadences(dossiers):
    cadences = {
        "REQ FR": 10,
        "REQ IT": 0.6,
        "PEP / SL": 16,
        "SCT IN": 28,
        "SCT OUT": 24,
        "Swift in": 44,
        "Arkéa": 14,
        "Point AIC": 1 / 60  # Conversion en dossier par minute
    }
    temps_mails = 7 * 60  # 7 heures en minutes

    # Calculer le total des dossiers
    total_dossiers = sum(dossiers.values())
    
    # Calculer le temps à allouer aux mails
    temps_mails_alloues = temps_mails - total_dossiers

    return temps_mails_alloues

# Interface Streamlit
st.title("Calculateur de Cadences")
dossiers = {}
for key in ["REQ FR", "REQ IT", "PEP / SL", "SCT IN", "SCT OUT", "Swift in", "Arkéa", "Point AIC"]:
    dossiers[key] = st.number_input(f"Nombre de dossiers pour {key}", min_value=0)

if st.button("Calculer"):
    temps_mails = calculer_cadences(dossiers)
    st.write(f"Temps à allouer aux mails : {temps_mails} minutes")
