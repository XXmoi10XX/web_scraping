# virtualenv env　仮想か
from time import sleep 
from bs4 import BeautifulSoup

import re 
import requests 
import pandas as pd 

url = 'https://doda.jp/DodaFront/View/JobSearchList.action?pr=13&pic=1&ds=0&oc=0112M%2C0113M%2C010401S%2C010402S%2C010404S&so=50&tp=1&usrclk_searchList=PC-logoutJobSearchList_searchResultFooterArea_pagination_pos-1'
r = requests.get(url,timeout=3)
r.raise_for_status()


soup = BeautifulSoup(r.content, 'lxml')


d_list = []
for i in range(2,67):
    for under in soup.find_all('div', class_='under'):
        post_url = under.find('a',class_= '_JobListToDetail').get('href')
        sleep(2)

        #1回目
        sleep(3)
        post_r = requests.get(post_url, timeout=3)
        r.raise_for_status()
        post_soup = BeautifulSoup(post_r.content,'lxml')
        #求人詳細
        

        if post_soup.find('a', class_='_canonicalUrl'):
            post_soup.find('a', class_='_canonicalUrl').get('href')
            post_url = post_soup.find('a', class_='_canonicalUrl').get('href')

            sleep(3)

            post_r = requests.get(post_url, timeout=3)
            r.raise_for_status()
            post_soup = BeautifulSoup(post_r.content,'lxml')

        

        # print('求人詳細:',post_url)
        #会社名取得
        job_title = post_soup.find('p', class_='job_title').text
        print('会社名:', job_title)
        
        
        #会社url取得
        if post_soup.find('a', target='_blank'): 
            job_url = post_soup.find('a', target='_blank').get('href')
            print('会社url:', job_url)
            d = {
                'name': job_title,
                'url': job_url
            }
        else:
            d = {
                'name': job_title,
            }
        d_list.append(d)

    url = 'https://doda.jp/DodaFront/View/JobSearchList.action?pr=13&pic=1&ds=0&oc=0112M%2C0113M%2C010401S%2C010402S%2C010404S&so=50&tp=1&page={}&usrclk_searchList=PC-logoutJobSearchList_searchResultFooterArea_pagination_pos-{}'

    target_url = url.format(i,i)

    print(target_url)
    sleep(2)
    r = requests.get(target_url)
    soup = BeautifulSoup(r.content, 'lxml')

df = pd.DataFrame(d_list)
print(df)

df.to_csv('python_web_posts.csv', index=None, encoding = 'utf-8-sig')
df.to_excel('python_web_posts.xlsx', index=None, encoding = 'utf-8-sig')
        # for target in post_soup.find_all('table', id='company_profile_table'):
        #     print(target.find('a').get('href'))




        

