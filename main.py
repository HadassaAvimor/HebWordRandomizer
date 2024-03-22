import requests
from bs4 import BeautifulSoup
import random
import tkinter as tk


def get_random_hebrew_word():
    url = "https://he.wikipedia.org/wiki/%D7%A2%D7%9E%D7%95%D7%93_%D7%A8%D7%90%D7%A9%D7%99"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')

    hebrew_words = []

    for paragraph in paragraphs:
        words = paragraph.text.split()
        hebrew_words.extend(
            [word.strip('.,') for word in words if any(char in 'אבגדהוזחטיכלמנסעפצקרשת' for char in word)])

    random_word = random.choice(hebrew_words)
    return random_word


def show_random_hebrew_word():
    def generate_new_word():
        random_word = get_random_hebrew_word()
        word_label.config(text=random_word)

    root = tk.Tk()
    root.title("מילה עברית אקראית מוויקיפדיה")

    word_label = tk.Label(root, text="", font=("Helvetica", 24))
    word_label.pack(padx=20, pady=20)

    generate_button = tk.Button(root, text="מילה חדשה", command=generate_new_word, bg="#4CAF50", fg="white", font=("Helvetica", 12), padx=10, pady=5)
    generate_button.pack(padx=20, pady=10)

    generate_new_word()

    root.mainloop()


if __name__ == "__main__":
    show_random_hebrew_word()
