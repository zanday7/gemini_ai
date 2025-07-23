# gemini_ai.py
from colorama import init, Fore, Style
import google.generativeai as genai
import sys

init(autoreset=True)

# ===== API KEY =====
API_KEY = "AIzaSyDA2GJPS71Zh6UmJ33dGItP3e7NkY2oKZA"
genai.configure(api_key=API_KEY)

# ===== Inisialisasi model dan chat session =====
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat(history=[])

def ask_bot(prompt):
    try:
        response = chat.send_message(prompt)
        print("\n\033[1;32m================= Jawaban Chatbot =====================\033[0m\n")

        if hasattr(response, "parts"):
            for part in response.parts:
                print(f"{Fore.GREEN}{Style.BRIGHT}{part.text}")
        else:
            print(f"{Fore.GREEN}{Style.BRIGHT}{response.text}")
    except Exception as e:
        print(Fore.RED + "[ERROR] Terjadi kesalahan:")
        print(Fore.RED + str(e))

if __name__ == "__main__":
    print("Selamat datang di Chatbot Gemini!\nKetik 'exit' untuk keluar.\n")
    while True:
        user_input = input("Anda: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Bot: Sampai jumpa!")
            break
        ask_bot(user_input)
