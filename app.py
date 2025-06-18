from models.translate_model import tokenizer,model  

import streamlit as st

# Title
st.set_page_config(page_title="Machine Translation App", layout="centered")
st.title("🈂️ Machine Translation App")

# Description
st.markdown("Translate text from English to Hindi (or any other supported languages).")

# Input text
input_text = st.text_area("Enter sentence to translate:", height=150)

# Dummy translation function (replace with actual model call)
def translate_text(text):
    tokens = tokenizer(text,return_tensors='pt',padding=True)
    translated = model.generate(**tokens)
    output = tokenizer.decode(translated[0],skip_special_tokens=True)
    return output

# Translate button
if st.button("Translate"):
    if input_text.strip() != "":
        translation = translate_text(input_text)
        st.markdown("### Translated Sentence:")
        st.success(translation)
    else:
        st.warning("Please enter a sentence to translate.")
