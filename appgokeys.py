from openai import OpenAI

import streamlit as st
import openai

# 🔑 Clé API OpenAI (ajoute-la dans Settings > Secrets)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ✅ Texte brut extrait du manuel utilisateur
manuel = """
Appuyez sur le bouton [REC] pour démarrer l'enregistrement.
Utilisez les boutons de catégorie pour changer de sons.
Le mode LOOP vous permet de superposer des parties de batterie, basse, accord et solo.
Branchez le clavier à l'ordinateur via USB (Type B) pour le connecter en MIDI.
... (tu peux compléter ce texte avec plus d’extraits du PDF)
"""

# 🎹 Interface utilisateur
st.title("Assistant KORG Go Keys 3 🎶")
question = st.text_input("Posez votre question sur le clavier :")

if question:
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Générer le prompt à partir de la question
prompt = f"""
Tu es un expert du clavier KORG Go Keys 3.
Réponds à la question suivante en utilisant uniquement les informations ci-dessous :

Manuel :
{manuel}

Question :
{question}
"""

# Appel API
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Affichage
st.success(response.choices[0].message.content.strip())

    with st.spinner("Recherche de la réponse..."):
       from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

st.success(response.choices[0].message.content.strip())



