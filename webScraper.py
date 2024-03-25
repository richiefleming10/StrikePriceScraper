import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all('div', {'class': class_path})
    try:
        spans = web_content_div[1].find_all('span')
        texts = [span.get_text() for span in spans]
    except IndexError:
        texts = []
    return texts


def real_time_price(stock_code):
    url = 'https://money.cnn.com/quote/quote.html?utm_source=quote_search&symb=' + stock_code

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = web_content_div(web_content, 'clearfix')
        if texts != []:
            price, change = texts[0], texts[3]
        else:
            price, change = [], []
    except ConnectionError:
        price, change = [], []
    return price, change

def get_strike_price(stock_code):
    url = 'https://money.cnn.com/quote/quote.html?utm_source=quote_search&symb=' + stock_code

    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = web_content_div(web_content, 'clearfix')
        if texts != []:
            strike = texts[0]
        else:
            strike = []
    except ConnectionError:
        strike
    return strike


# Top 10 on the SNP 500
print('APPL', real_time_price('AAPL'))
print('MSFT', real_time_price('MSFT'))
print('AMZN', real_time_price('AMZN'))
print('TSLA', real_time_price('TSLA'))
print('GOOGL', real_time_price('GOOGL'))
print('GOOG', real_time_price('GOOG'))
print('NVDA', real_time_price('NVDA'))
# print('BRKD', real_time_price('BRKB'))
# print('META', real_time_price('META'))
# print('UNH', real_time_price('UNH'))



