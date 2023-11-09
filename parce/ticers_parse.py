from bs4 import BeautifulSoup
import json

cn_name: list = []
tkr_name: list = []

with open('3_OOP/C5_Finaly_progect_OOP/FINAL_Progect_CurrencyBot/parce/tikers_and_coins.html', 'r') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

coin_name: BeautifulSoup = soup.find_all("div", class_="center")

for item in coin_name:
    coin = item.find(
        "span", class_="tw-text-blue-500 tw-font-bold lg:tw-block tw-hidden")
    tiker = item.find(
        "span", class_="tw-text-blue-500 tw-font-bold lg:tw-hidden")
    if coin != None and tiker != None:
        cn = coin.text.lower().replace(' ', '_')
        cn_name.append(cn)
        tkr_name.append(tiker.text)

all_currency = {}


for index in range(len(cn_name)):
    all_currency[cn_name[index]] = tkr_name[index]


# with open('3_OOP/C5_Finaly_progect_OOP/FINAL_Progect_CurrencyBot/coins_tikers.json', 'w') as file:
#     json.dump(all_currency, file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    print(all_currency)
