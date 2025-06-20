from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import markdown2
from dotenv import load_dotenv
import os

api_key = os.getenv('GEMINI_KEY')

def hitGemini(lokasi, budget):
    prompt = f"""
Bertindaklah sebagai konsultan bisnis profesional yang memahami tren pasar lokal di berbagai daerah Indonesia. User akan memberikan lokasi dan jumlah budget mereka. Tugasmu adalah memberikan ide usaha yang potensial, relevan dengan lokasi tersebut, dan realistis dengan budget yang mereka miliki.

Jawaban kamu **harus selalu diawali dengan kalimat: "Hai soldier, selamat datang di aplikasi LBE (Let's Become Entrepreneurs)."**

Setelah itu, jelaskan:
1. Rekomendasi jenis usaha yang cocok
2. Alasan kenapa usaha tersebut potensial di lokasi tersebut
3. Perkiraan biaya awal dan distribusinya
4. Potensi keuntungan per bulan
5. Tips sukses menjalankan usaha tersebut

Berikan jawaban yang bersahabat namun profesional, tidak terlalu panjang, dan mudah dipahami. Juga berikan heading markdown yang konsisten untuk memformat jawaban. dan tolong jangan mengubah budget, harus sesuai dengan yang diberikan user.

Lokasi: {lokasi}
Budget: {budget}
    """
    genai.configure(api_key='AIzaSyCT0XJaAalXXmL1eA_rcM5MBM5wlF_fFUc')
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return markdown2.markdown(response.text)

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    rekomendasi = None
    if request.method == 'POST':
        lokasi = request.form.get('lokasi')
        budget = request.form.get('budget')
        if lokasi and budget:
            rekomendasi = hitGemini(lokasi, budget)
        else:
            rekomendasi = "Mohon masukkan lokasi dan budget yang valid."
    return render_template('index.html', rekomendasi=rekomendasi)

if __name__ == '__main__':
    app.run(debug=True)