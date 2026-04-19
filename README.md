# 📄 Yerel Doküman Özetleyici (Local LLM Summarizer)

Bu proje, **Ollama API** ve **Llama 3** modeli kullanılarak geliştirilmiş, tamamen yerel makinede çalışan gizlilik odaklı bir belge analiz aracıdır.

---

### 🛡️ Proje Tanımı ve Özellikler

Özellikle veri gizliliğinin kritik olduğu alanlar (savunma sanayii, akademik araştırmalar vb.) için tasarlanmıştır. Verileriniz asla internete veya üçüncü taraf bulut servislerine gönderilmez.

* **Yerel Yapay Zeka:** Ollama aracılığıyla Llama 3 modelini kullanarak %100 çevrimdışı analiz.
* **Modern Arayüz:** Kullanıcı dostu, hızlı ve etkileşimli Streamlit arayüzü.
* **Geniş Format Desteği:** PDF ve TXT dosyalarını analiz edebilir.
* **Gizlilik ve Güvenlik:** Veri sızıntısı riskini yerel çalışma prensibiyle sıfıra indirir.
* **Güvenli Kodlama:** Döküman içeriği ve kullanıcı girdileri işlenirken SQL Injection gibi yaygın zafiyetlere karşı savunmacı kodlama prensipleri gözetilmiştir.

#### 🛠️ Kullanılan Teknolojiler
| Teknoloji | Kullanım Amacı |
| :--- | :--- |
| **Python** | Ana Programlama Dili |
| **Streamlit** | Web Arayüzü ve Kullanıcı Etkileşimi |
| **Ollama API** | Yerel LLM (Llama 3) Entegrasyonu (Port: 11434) |
| **pdfplumber** | PDF Veri Madenciliği |

---

### 🚀 Kurulum ve Kullanım

Projeyi kendi makinenizde ayağa kaldırmak için aşağıdaki adımları sırasıyla takip edebilirsiniz:

#### 1. Ön Hazırlık (Ollama)
Bilgisayarınızda Ollama'nın kurulu ve modelin indirilmiş olması gerekir:
1.  [ollama.com](https://ollama.com) adresinden Ollama'yı indirin.
2.  Terminali açın ve modeli çekin:
    ```bash
    ollama pull llama3
    ```

#### 2. Kütüphanelerin Kurulumu
Proje klasörüne gidin ve gerekli Python kütüphanelerini yükleyin:
```bash
pip install -r requirements.txt3. Uygulamayı Çalıştırma
Arayüzü şu komutla başlatabilirsiniz:

Bash
streamlit run app.py
⚠️ Önemli Notlar
Güvenlik Uyarısı: Proje geliştirilirken notlarda belirtilen SQL Injection risklerine karşı dikkatli olunmuştur. Eğer projeye bir veritabanı modülü eklenirse, döküman içeriklerini kaydederken mutlaka parameterized queries (parametreleştirilmiş sorgular) kullanılması zorunludur.
