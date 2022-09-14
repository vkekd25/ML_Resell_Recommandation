from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
from tqdm import tqdm


num = int(input(' 데이터 갯수 : 6 + 12 * num -> 데이터 범위 설정하기 num 설정:'))
data_num = 6 + num * 12
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


# 브라우저 생성
driver = webdriver.Chrome('/Users/byungwookkang/Documents/chromedriver', options=options)

# 웹사이트 열기
url = "https://www.daangn.com/search/%EC%95%A0%ED%94%8C%EC%9B%8C%EC%B9%98"
driver.get(url)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


## 빈 리스트 지정
area_ls = []
manner_degree_ls = [] 
title_ls = []
price_ls = [] 
like_ls = [] 
chat_ls = []
view_ls = []
category_ls = []
time_ls = []
tap_ls = []
article_ls = []
total_area = []


#변수가 생겼을시(인터넷 이슈, 해당사이트 에러등) 데이터 중단하고 데이터 저장
try:
    # num이 0이상의 정수일시 실행
    if num > 0:
        # tqdm() for문 시간 측정
        for j in range(num): 
            ## 더보기 클릭
            driver.find_element(By.XPATH, '//*[@id="result"]/div[1]/div[2]').click()
            time.sleep(1)
            

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        # 사이드 사이트 추출
        div = soup.find('div', class_ = 'articles-wrap')
        articles = soup.findAll("article", class_ = 'flea-market-article flat-card')


        # 리스트에 사이드 사이트 담기
        for article in articles:
            tap = 'https://www.daangn.com' + article.find('a')['href']
            tap_ls.append(tap)

        area = soup.find_all('p', class_ = 'article-region-name')
        for areas in area:
            total_area.append(areas.text.split('\n')[1].lstrip())
        

        # 더보기 누른 후 12개 증가하는 데이터 수만큼 반복문 실행
        for i in tqdm(range(6 + num * 12)):

            # 해당 데이터로 새탭 열기
            driver.execute_script(f'window.open("{tap_ls[i]}");')

            # 새로운 사이트로 이동
            driver.switch_to.window(driver.window_handles[-1])
            
            # 해당 사이트 page_source
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            # 숨겨진 article시 닫고 이전 탭으로 이동
            no_article = soup.find('p', id = 'no-article')
            # price가 아닌 나눔상품일경우 닫고 이전 탭으로 이동
            price_nanum = soup.find('p', id = 'article-price-nanum')
            if (no_article != None) or (price_nanum != None):
                # 새탭 닫기
                driver.close()
                # 이전탭으로 이동
                driver.switch_to.window(driver.window_handles[-1])
                # 이전 사이트 지역 제거
                total_area[i] = None
                # tap_ls[i] = None
                continue

            # if namum_article:
            #     # 새탭 닫기
            #     driver.close()
            #     # 이전탭으로 이동
            #     driver.switch_to.window(driver.window_handles[-1])

            #지역, 매너온도, 제목, 가격, 관심수, 채팅수, 조회수, 카테고리, 시간, 기사 크롤링
            region_name = soup.find(id = "region-name")
            manner_degree = soup.find('dl', id = 'temperature-wrap')
            title = soup.find('h1', id = 'article-title')
            price = soup.find('p', id = 'article-price')
            like_chat_view = soup.find('p', id = 'article-counts')
            category = soup.find('p', id = "article-category")
            time_ = soup.find('p', id = "article-category")
            article = soup.find('div', id = "article-detail")
            # nanum_article = soup.find('p', id = 'article-price-nanum')


            # 지역, 매너온도, 제목, 가격, 관심수, 채팅수, 조회수, 카테고리, 시간, 기사 텍스트 추출
            region_name = region_name.text
            manner_degree = manner_degree.text.split('\n')[3].lstrip()
            title = title.text
            # 해당 당근마켓 price가격이 없는 경우 price = None
            if price.text != None:
                price = price.text.split('\n')[1].lstrip()
            else:
                price = None
            like = like_chat_view.text.split('\n')[1].lstrip()
            chat = like_chat_view.text.split('\n')[2].lstrip()
            view = like_chat_view.text.split('\n')[4].lstrip()
            category = category.text.split('\n')[1].lstrip()
            time_ = time_.text.split('\n')[3].lstrip()
            article = article.text

            # 리스트에 지역, 매너온도, 제목, 가격, 관심수, 채팅수, 조회수, 카테고리, 시간 담기
            area_ls.append(region_name)
            manner_degree_ls.append(manner_degree)
            title_ls.append(title)
            price_ls.append(price) 
            like_ls.append(like)
            chat_ls.append(chat)
            view_ls.append(view)
            category_ls.append(category)
            time_ls.append(time_)
            article_ls.append(article)
            
            # 새탭 닫기
            driver.close()
            
            # 이전탭으로 이동
            driver.switch_to.window(driver.window_handles[-1])

#예상치 못한 변수 생길시 남은 데이터 df로 만든 뒤 csv파일 저장
except:
    area = pd.Series(area_ls)
    manner_degree = pd.Series(manner_degree_ls)
    title = pd.Series(title_ls)
    price = pd.Series(price_ls)
    like = pd.Series(like_ls)
    chat = pd.Series(chat_ls)
    view = pd.Series(view_ls)
    title = pd.Series(title_ls)
    price = pd.Series(price_ls)
    category = pd.Series(category_ls)
    time_ = pd.Series(time_ls)
    total_area = pd.Series(total_area)
    article = pd.Series(article_ls)
    # link = pd.Series(tap_ls)

    df = pd.DataFrame({"area": area, "manner_degree":manner_degree, "title":title, 
                    "price":price, 'like':like, 'chat':chat, 'view':view,
                    "category" : category, "time" : time_, "total_area" : total_area,
                    "article" : article},
                    columns=("area", "manner_degree", "title", "price", 
                    'like', 'chat', 'view', 'category', 'time', 'total_area', 'article'))



    df.to_csv('data2.csv')


area = pd.Series(area_ls)
manner_degree = pd.Series(manner_degree_ls)
title = pd.Series(title_ls)
price = pd.Series(price_ls)
like = pd.Series(like_ls)
chat = pd.Series(chat_ls)
view = pd.Series(view_ls)
title = pd.Series(title_ls)
price = pd.Series(price_ls)
category = pd.Series(category_ls)
time_ = pd.Series(time_ls)
total_area = pd.Series(total_area)
article = pd.Series(article_ls)
# link = pd.Series(tap_ls)


df = pd.DataFrame({"area": area, "manner_degree":manner_degree, "title":title, 
                    "price":price, 'like':like, 'chat':chat, 'view':view,
                    "category" : category, "time" : time_, "total_area" : total_area,
                    "article" : article},
                    columns=("area", "manner_degree", "title", "price", 
                    'like', 'chat', 'view', 'category', 'time', 'total_area', 'article'))

# csv파일 만들기
df.to_csv('data_applewatch.csv')
