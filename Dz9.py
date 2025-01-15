import requests
from bs4 import BeautifulSoup
response = requests.get("https://minfin.com.ua/ua/currency/nbu/")

print(response)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class":"sc-1x32wa2-9"})
    res = soup_list[0]
    print(f"Курс Долара станом на сьогодні - {res.text}$")
else:
    print("error")


a = input("Вам потрібно розміняти гривні чи долари? - ")
if a == "Гривні":
    aa = float(input("Введіть курс Долара -"))
    ab = float(input("Введіть суму грн, яку ви хочете розміняти -"))
    ac = ab/aa
    print(f"Ваша сума в Доларах - {ac}$")
elif a == "Долари":
    ba = float(input("Введіть суму доларів, яку ви хочете розміняти -"))
    bc = float(input("Введіть курс Долара -"))
    bb = ba*bc
    print(f"Ваша сума в Гривнях - {bb}грн")
