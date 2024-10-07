import streamlit as st

# Titre de l'application
st.title("Calcul des Cadences Professionnelles")

# Cadences attendues par activité
cadences = {
    "REQ FR": 10,
    "REQ IT": 0.6,
    "PEP / SL": 16,
    "SCT IN": 28,
    "SCT OUT": 24,
    "Swift in": 44,
    "Arkéa": 14,
    "Point AIC": 60  # 1 par minute = 60 par heure
}

# Formulaire pour entrer les nombres de dossiers traités
st.header("Saisissez le nombre de dossiers traités pour chaque activité")

req_fr = st.number_input("Nombre de REQ FR traités", min_value=0, value=0)
req_it = st.number_input("Nombre de REQ IT traités", min_value=0, value=0)
pep_sl = st.number_input("Nombre de PEP / SL traités", min_value=0, value=0)
sct_in = st.number_input("Nombre de SCT IN traités", min_value=0, value=0)
sct_out = st.number_input("Nombre de SCT OUT traités", min_value=0, value=0)
swift_in = st.number_input("Nombre de Swift in traités", min_value=0, value=0)
arkea = st.number_input("Nombre d'Arkéa traités", min_value=0, value=0)
point_aic = st.number_input("Nombre de points AIC traités (en minutes)", min_value=0, value=0)

# Calcul du temps passé pour chaque activité
temps_total = (
    req_fr / cadences["REQ FR"] +
    req_it / cadences["REQ IT"] +
    pep_sl / cadences["PEP / SL"] +
    sct_in / cadences["SCT IN"] +
    sct_out / cadences["SCT OUT"] +
    swift_in / cadences["Swift in"] +
    arkea / cadences["Arkéa"] +
    point_aic / cadences["Point AIC"]
)

# Affichage du temps total calculé et gestion des mails
st.write(f"Temps total passé sur les activités : {temps_total:.2f} heures")

# Calcul du temps restant pour les mails
temps_mails = max(0, 7 - temps_total)
st.write(f"Temps à allouer aux mails : {temps_mails:.2f} heures")
