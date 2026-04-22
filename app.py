
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Mistik Mesaj", page_icon="🔮")
st.title("🔮 Hoş geldin, Mustafa")

# Anahtar Kontrolü
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # EN GARANTİ MODEL: gemini-1.0-pro
    model = genai.GenerativeModel('gemini-1.0-pro')
else:
    st.error("API Anahtarı eksik!")
    st.stop()

st.info("Eski ve bilge model bağlandı. Şimdi deneme vakti!")

user_input = st.text_area("Kalbindekileri dök...")

if st.button("Mistik Mesajı Al"):
    if user_input:
        try:
            with st.spinner('Evrenle bağ kuruluyor...'):
                response = model.generate_content(f"Sen bilge birisin. Mustafa '{user_input}' diyor. Ona Türkçe kısa bir moral ver.")
                st.success(response.text)
                st.balloons()
        except Exception as e:
            st.error(f"Hata oluştu: {e}")
    else:
        st.warning("Lütfen bir mesaj yaz.")
