import streamlit as st
import openai

# Sayfa Ayarları
st.set_page_config(page_title="Evrensel Titreşim", page_icon="🔮")

# Şık Tasarım
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #f0e68c; }
    .stButton>button { background-color: #ffd700; color: black; border-radius: 10px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 Hoş geldin, Mustafa")
st.subheader("Evren bugün senin için ne fısıldıyor?")

# OpenAI Bağlantısı (Ayarlardan gizli olarak bağlayacağız)
if "OPENAI_API_KEY" in st.secrets:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
else:
    st.warning("Lütfen API anahtarını bağla.")

mood = st.text_area("Kalbindekileri dök, yıldızlar yol göstersin...", placeholder="Şu an ne hissediyorsun?")

if st.button("Mistik Mesajı Al"):
    if mood:
        with st.spinner('Yıldızlar hizalanıyor...'):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Sen Mistik Gezgin'sin. Bilge ve samimisin. Kullanıcıyı Mustafa (1987 Maraş doğumlu Akrep) olarak tanı ve mistik yorumlar yap."},
                        {"role": "user", "content": mood}
                    ]
                )
                st.success(response.choices[0].message.content)
            except Exception as e:
                st.error("Bir hata oluştu, muhtemelen API anahtarı henüz eklenmedi.")
    else:
        st.warning("Henüz bir şey yazmadın ruh kardeşim.")
