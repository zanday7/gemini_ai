# gemini_ai.py
from colorama import init, Fore, Style
import google.generativeai as genai
import sys
import requests

# ===== Masukkan API Key Gemini langsung di sini =====
API_KEY = "AIzaSyDA2GJPS71Zh6UmJ33dGItP3e7NkY2oKZA"

# ===== Konfigurasi model Gemini =====
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def ask_bot(prompt):
    response = model.generate_content(prompt)
    print("\n\033[1;32m================= Jawaban Chatbot =====================\033[0m\n")
    print(f"{Fore.GREEN}{Style.BRIGHT}{response.text}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Masukkan prompt sebagai argumen!")
    else:
        user_input = " ".join(sys.argv[1:])
        ask_bot(user_input)
