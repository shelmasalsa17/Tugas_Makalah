from bm import boyer_moore
from suara import *

# Database pertanyaan dan jawaban
questions = ["Apa itu wanita?", "Halo siri", "Hai siri bisakah membantu saya", 
"Selamat Pagi"]
answers = ["Wanita adalah makhluk ciptaan Tuhan.", 
"Hai. selamat menggunakan saya", "Halo saya bisa membantu anda", "Pagi juga"]

# Rekam suara
input = rekam().lower()  # Mengubah input menjadi huruf kecil

# Pencocokan pertanyaan dan jawaban (case-insensitive)
for i, question in enumerate(questions):
    if (boyer_moore(question.lower(), input) != -1):  # Mengubah pertanyaan menjadi huruf kecil
        convert_suara(answers[i])
        break
