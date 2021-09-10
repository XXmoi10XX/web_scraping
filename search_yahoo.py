''' 
 yahooニュースで「機械学習」と調べた際にもっと見るボタンを押して最下層まで
スクロールするプログラムです 

'''

from time import sleep,time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()


# 2. シークレットモードでの使用
options.add_argument('--incognito')


#step1 : driverを作成する
driver = webdriver.Chrome(
    executable_path='',
    options=options
)
driver.implicitly_wait(10)


driver.get('https://news.yahoo.co.jp')
sleep(3)

# 検索

search_box = driver.find_element_by_css_selector('input.sc-kgoBCf')
sleep(3)


search_box.send_keys('機械学習')
sleep(5)

search_box.submit()
sleep(3)


            

while True:
    height = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script(f'window.scrollTo(0, {height})')
    sleep(2)
    button_tag = driver.find_elements_by_css_selector('div.newsFeed > div > span > button')
    if button_tag:
        button_tag[0].click() 
    else:
        # news_title = driver.find_elements_by_css_selector('.newsFeed_item_title')
        # news_url =  driver.find_elements_by_css_selector('div.newsFeed > ol > li a.newsFeed_item_link')
        break

start = time()
soup = BeautifulSoup(driver.page_source, 'lxml')
news_title = soup.select('.newsFeed_item_title')
news_url =  soup.select('div.newsFeed > ol > li a.newsFeed_item_link')


# selenium
# ==============================
# 9.095846891403198
# ==============================
# start = time()
# news_title = driver.find_elements_by_css_selector('.newsFeed_item_title')
# news_url =  driver.find_elements_by_css_selector('div.newsFeed > ol > li a.newsFeed_item_link')



# for i in range(len(news_title)):
            
#             print('='*30 , i+1 , '='*30 )
#             print(news_title[i].text)
#             print(news_url[i].get_attribute('href'))
        

# BeautifulSoup
# ==============================
# 0.5261411666870117
# ==============================
for i in range(len(news_title)):
            
            print('='*30 , i+1 , '='*30 )
            print(news_title[i].text)
            print(news_url[i].get('href'))
        
print('='*30)
print(time() - start)
print('='*30)











