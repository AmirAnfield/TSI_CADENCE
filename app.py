import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# Utiliser les API Google Drive et Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Charger le fichier JSON des identifiants
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials/tsi-cadence-678df727045f.json', scope)

# Authentifier le client gspread
client = gspread.authorize(credentials)

# Ouvrir la feuille Google Sheets par son nom
sheet = client.open("TSI_CADENCE").sheet1  # Utilise le nom de ta feuille ici

# Fonction pour ajouter des données à Google Sheets
def ajouter_donnees(data):
    sheet.append_row(data)

# Interface Streamlit
st.title("Suivi des Cadences")

# Saisie des données
date = st.date_input("Date")
req_fr = st.number_input("REQ FR", min_value=0)
req_it = st.number_input("REQ IT", min_value=0)
pep_sl = st.number_input("PEP / SL", min_value=0)
sct_in = st.number_input("SCT IN", min_value=0)
sct_out = st.number_input("SCT OUT", min_value=0)
swift_in = st.number_input("Swift in", min_value=0)
arkea = st.number_input("Arkéa", min_value=0)
point_aic = st.number_input("Point AIC", min_value=0)

# Bouton pour ajouter les données
if st.button("Ajouter les données"):
    data = [str(date), req_fr, req_it, pep_sl, sct_in, sct_out, swift_in, arkea, point_aic]
    ajouter_donnees(data)
    st.success("Données ajoutées avec succès !")
