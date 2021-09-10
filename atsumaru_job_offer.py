スクロールが必要な求人情報から求人情報を取得します。

from time import sleep,time
from selenium import webdriver 
import requests 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

d_list = []
options = webdriver.ChromeOptions()


# 2. シークレットモードでの使用
options.add_argument('--incognito')

# options.add_argument('--headless')

#step1 : driverを作成する
driver = webdriver.Chrome(
    executable_path='',
    options=options
)
driver.implicitly_wait(10)


driver.get('https://atsumaru.jp/area/7/list?sagid=all')
sleep(3)

# while True:
#     height = driver.execute_script('return document.body.scrollHeight')
#     driver.execute_script(f'window.scrollTo(0, {height})')
#     sleep(2)
#     height1 = driver.execute_script('return document.body.scrollHeight')
#     if height == height1:
#         break

soup = BeautifulSoup(driver.page_source, 'lxml')
company_urls = soup.select('span.exe a')
i = 1

for company_url in company_urls:
    company_url = "https://atsumaru.jp/" + company_url.get('href')
    # print(company_url)

    driver.get(company_url)
    sleep(3)

    button_tel = driver.find_element_by_css_selector('li.telBtn')
    button_tel.click()
    sleep(2)


    company_name = driver.find_element_by_css_selector('#detailBox h2').text
    if ('　' in company_name):
        company_name = company_name.replace('　', ' ')
    # company_name = soup.select('div.area .contsBox h2')
   

    print('='*30 , i , '='*30 )
    print(company_name)
    company_address = driver.find_element_by_css_selector('article:last-of-type > table > tbody > tr:last-of-type > td > p:first-of-type').text
    print(company_address)
    company_tel = driver.find_element_by_css_selector('div.telNo a').text
    print(company_tel)
    i += 1
    d_list.append({
            'company_name': company_name,
            'company_address': company_address,
            'company_tel': company_tel
        })
    print(d_list[-1])


df = pd.DataFrame(d_list)
df.to_csv('company_list.csv', index=None, encoding='utf-8-sig')




    # page_r = requests.get(company_url,timeout=3) 
    # page_r.raise_for_status()
    # page_soup = BeautifulSoup(page_r.content,'lxml')
    





