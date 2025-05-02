import streamlit as st
import openai
from PyPDF2 import PdfReader

# 🔑 Clé OpenAI (à sécuriser dans Streamlit Cloud)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 📘 Charger le manuel PDF
@st.cache_data
def charger_manuel(path):
    reader = PdfReader(path)
    texte = ""
    for page in reader.pages:
        texte += page.extract_text() + "\n"
    return texte

# Charger le manuel
manuel = charger_manuel("GOKEYS_Reference_fra01_W.pdf")

# Interface utilisateur
st.title("🎹 Assistant KORG Go Keys 3")
question = st.text_input("Posez votre question :")

if question:
    prompt = f'''
Tu es un expert du clavier Roland KORG Go Keys 3.
Réponds à la question de manière claire et simple, en utilisant uniquement les informations de ce manuel.

Manuel :
{manuel[:20000]}

Question :
{question}
'''
    with st.spinner("Recherche de la réponse..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.success(response.choices[0].message.content.strip())
