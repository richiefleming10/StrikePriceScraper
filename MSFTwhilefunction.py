import webScraper
import msvcrt, time
from selenium import webdriver

# webScraper.web_content_div()

def test(x):
    flag = 1
    while flag != 0:
        print(test(webScraper.real_time_price()))
        if msvcrt.getwche() == '\r':
            break
        time.sleep(5)

# test('AAPL')
  
    