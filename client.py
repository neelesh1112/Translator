import streamlit as st
from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit app
st.title("Language Translator")

text = st.text_area("Enter the text you want to translate")
target_language = st.selectbox("Select the target language", ["french", "spanish", "itailian", "japanese", "hindi"])

if st.button("Translate"):
    if text:
        translated_text = translate_text(text, target_language)
        st.write("Translated text:", translated_text)
    else:
        st.write("Please enter some text to translate.")