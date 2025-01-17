import sqlite3
import requests
from bs4 import BeautifulSoup

connection = sqlite3.connect('sites.db')
cur = connection.cursor()

# cur.execute("CREATE TABLE Shop_of_machin (name TEXT);")
# connection.commit()

def add_sites():
    cur.execute('DELETE FROM sites')
    connection.commit()

    sites = ['https://allo.ua/', 'https://www.samsung.com', 'https://www.foxtrot.com.ua/']

    for site in sites:
        cur.execute('INSERT INTO sites (url) VALUES (?)', (site,))
    connection.commit()

def count_word_on_site(url, word):
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()

        word_count = text.lower().count(word.lower())
        return word_count
    except Exception as e:
        print(f"Не вдалося обробити сайт {url}: {e}")
        return 0

def search_word():
    try:
        word = input("Введіть слово, яке вас цікавить - ")
    except:
        raise TypeError(f"проблема з введенням тексту")

    cur.execute('SELECT url FROM sites')
    sites = cur.fetchall()
    results = []

    for site in sites:
        url = site[0]
        count = count_word_on_site(url, word)
        results.append((url, count))

    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

    print(f"Результати пошуку для слова '{word}':")
    for url, count in sorted_results:
        print(f"Сайт: {url} — Знайдено слів: {count}")

    connection.close()


if __name__ == "__main__":
    add_sites()
    search_word()
else:
    print("Error")