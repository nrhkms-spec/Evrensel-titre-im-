
import streamlit as st
import google.generativeai as genai

# Sayfa yapılandırması
st.set_page_config(page_title="Mistik Mesaj", page_icon="🔮")

# Kasa (Secrets) kontrolü
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # MODELİ BURADA TANIMLIYORUZ - Kesinlikle gemini-1.5-flash
    model_name = 'gemini-1.5-flash'
    model = genai.GenerativeModel(model_name)
else:
    st.error("HATA: Secrets kısmına GEMINI_API_KEY eklenmemiş!")
    st.stop()

st.title("🔮 Hoş geldin, Mustafa")
st.info(f"Sistem şu an '{model_name}' modelini kullanıyor.") # Model adını ekrana yazdırdık

user_input = st.text_area("Kalbindekileri dök...", placeholder="Mesajını buraya yaz...")

if st.button("Mistik Mesajı Al"):
    if user_input:
        try:
            with st.spinner('Yıldızlarla konuşuyorum...'):
                response = model.generate_content(f"Sen bir falcısın. Mustafa diyor ki: {user_input}. Ona moral ver.")
                st.success(response.text)
                st.balloons()
        except Exception as e:
            st.error(f"Bir hata oluştu. Hata mesajı: {e}")
    else:
        st.warning("Lütfen bir şeyler yaz.")
