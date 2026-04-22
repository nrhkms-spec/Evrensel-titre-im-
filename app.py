
import streamlit as st
import google.generativeai as genai

# Sayfa başlığı
st.title("🔮 Hoş geldin, Mustafa")
st.subheader("Evren bugün senin için ne fısıldıyor?")

# KİLİT BURADA: Kasadaki (Secrets) anahtarı kontrol et
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
else:
    st.warning("Lütfen API anahtarını bağla.")
    st.stop()

# Kullanıcı girişi
user_input = st.text_area("Kalbindekileri dök...")

if st.button("Mistik Mesajı Al"):
    if user_input:
        try:
            # Fal yorumu
            response = model.generate_content(f"Sen mistik bir falcısın. Mustafa'ya şu konuda bilgece bir cevap ver: {user_input}")
            st.success(response.text)
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
    else:
        st.warning("Lütfen bir şeyler yaz.")
