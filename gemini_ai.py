# gemini_ai.py
import google.generativeai as genai
import sys

# ===== Masukkan API Key Gemini langsung di sini =====
API_KEY = "AIzaSyDA2GJPS71Zh6UmJ33dGItP3e7NkY2oKZA"

# ===== Konfigurasi model Gemini =====
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    print("\n=== Jawaban Chatbot ===\n")
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Masukkan prompt sebagai argumen!")
    else:
        user_input = " ".join(sys.argv[1:])
        ask_gemini(user_input)
