
import streamlit as st
import google.generativeai as genai

# Sayfa Ayarları
st.set_page_config(page_title="Mistik Mesaj", page_icon="🔮")
st.title("🔮 Hoş geldin, Mustafa")

# Anahtar Kontrolü
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # BURADA GÜNCELLEME YAPTIK:
    model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')
else:
    st.error("API Anahtarı eksik!")
    st.stop()

st.info("Sistem güncellendi. Hadi Mustafa, şimdi dene!")

user_input = st.text_area("Kalbindekileri dök...")

if st.button("Mistik Mesajı Al"):
    if user_input:
        try:
            with st.spinner('Yıldızlar cevap veriyor...'):
                # En garanti metot
                response = model.generate_content(user_input)
                st.success(response.text)
                st.balloons()
        except Exception as e:
            st.error(f"Hata: {e}")
    else:
        st.warning("Lütfen bir şeyler yaz.")
