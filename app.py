import streamlit as st
import ollama
from PyPDF2 import PdfReader


st.set_page_config(page_title="Llama Özetleyici", page_icon="📄")

st.title("📄 Belge Özetleme Asistanı")
st.markdown("---")

# Dosya Yükleme
uploaded_file = st.file_uploader("Özetlenecek PDF veya Metin dosyasını seç", type=['pdf', 'txt'])

def extract_text(file):
    if file.type == "text/plain":
        return file.read().decode("utf-8")
    elif file.type == "application/pdf":
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

if uploaded_file is not None:
    content = extract_text(uploaded_file)
    st.write("Dosya başarıyla okundu, ilk 100 karakter:", content[:100])
    
    if st.button("Özetle"):
        with st.spinner("Llama dökümanı inceliyor (Arka planda API çalışıyor)..."):
            try:
                # Ollama API Portu üzerinden modelle konuşuyoruz
                response = ollama.chat(model='llama3', messages=[
                    {'role': 'system', 'content': 'Sen bir döküman analiz uzmanısın. Sana verilen metni başka soru sormadan direkt Türkçe özetlemelisin.'},
                    {'role': 'user', 'content': f"Aşağıdaki metni analiz et ve Türkçe özetle. Metin şudur: \n\n {content}"} 
                ])
                
                st.subheader("📝 Özet Sonucu")
                st.success(response['message']['content'])
                
            except Exception as e:
                st.error(f"API Bağlantı Hatası: {e}. Ollama'nın çalıştığından emin ol.")

st.sidebar.info("API Server Port: 11434\nModel: Llama3")