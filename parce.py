# Парсер заточен под quote.rbc.ru. В URL нужно только поменять номер тикета,
# и будет отслеживаться цена нужной валюты. Уровень цен задается любой, какой нужен.
# Время повторной проверки 15 минут.
# Tkinter позволяет вывести сообщение в случае срабатывания поверх всех окон.


import time
import requests
from tkinter import Tk
from tkinter import messagebox
from bs4 import BeautifulSoup


class Parcer:
    def __init__(self, url, url2):
        self.url = url
        self.url2 = url2

    def geturl(self):
        response = requests.get(self.url)
        response2 = requests.get(self.url2)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes_price = soup.find_all('span', class_='chart__info__sum')
        soup2 = BeautifulSoup(response2.text, 'lxml')
        quotes_price2 = soup2.find_all('span', class_='chart__info__sum')
        headers = []
        headers2 = []
        # Переборка полиметалл
        for i in quotes_price:
            for _ in list(i):
                title = i.text
                headers.append(title)
        h1 = str(headers[0])
        h1 = h1.replace(',', '.')
        h1_2 = float(h1[1:-1])

        # Переборка РосАгро
        for i in quotes_price2:
            for _ in list(i):
                title = i.text
                headers2.append(title)
        h2 = str(headers2[0])
        h2 = h2.replace(',', '.')
        h2_1 = float(h2[1:-1])
        top = Tk()
        top.geometry('300x200')

        if h1_2 > 1300:  # Проверка цены полиметалл
            print(h1_2)
            print('Цена пробила уровень 1300')
            messagebox.showinfo('Внимание!!!', f'Внимание! Цена Полиметалл пробила уровень 1300 цена сейчас: {h1_2}')
        if h2_1 > 1100:  # Проверка цена РосАгро
            print(h2_1)
            print('Цена пробила уровень 1100')
            messagebox.showinfo('Внимание!!!', f'Внимание! Цена РосАгро пробила уровень 1100 цена сейчас: {h2_1}')
        else:
            print('Цены ни одной из акций не вышли на уровень')
            print('Poly: ' + str(h1_2) + ' rub')
            print('RosAgro: ' + str(h2_1) + ' rub')
            time.sleep(900)
            st.geturl()


st = Parcer('https://quote.rbc.ru/ticker/59408', 'https://quote.rbc.ru/ticker/77501')
st.geturl()
