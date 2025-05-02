import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Simuler un extrait de manuel
manuel = """
Appuyez sur le bouton [REC] pour enregistrer.
Le bouton [LOOP] active l'enregistrement en boucle.
Branchez le clavier à l'ordinateur en USB pour utiliser le MIDI.
"""

st.title("Assistant KORG Go Keys 3 🎶")
question = st.text_input("Posez votre question sur le clavier :")

if question:
    prompt = f"""
Tu es un expert du clavier KORG Go Keys 3.
Réponds à la question suivante en utilisant uniquement les informations ci-dessous :

Manuel :
{manuel}

Question :
{question}
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    st.success(response.choices[0].message.content.strip())



