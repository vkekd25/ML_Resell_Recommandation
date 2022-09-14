from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import urllib.request
from urllib.parse import quote
from selenium.webdriver.common.by import By
import time


# url 리스트
url_list = []


# 조건 : 최신순, 검색어: 애플워치
# i는 조건에 따른 페이지 넘버
# page number => range(79 ~ 90번)


for i in range(21,30,1) :
    url = f"https://m.bunjang.co.kr/search/products?order=date&page={i}&q=%EA%B0%A4%EB%9F%AD%EC%8B%9C%EC%9B%8C%EC%B9%98"
    url_list.append(url)


# 드라이버 불러오기
driver = webdriver.Chrome('c:/chromedriver.exe')


# 스크랩 함수
def scrap(df, idx) :

    print("스크래핑을 시작합니다.")

    ## range(1, 101) => 페이지당 노출되는 아이템 수(100개)
    for i in range(1,100) :
        time.sleep(3)
        driver.find_element(By.XPATH, f'//*[@id="root"]/div/div/div[4]/div/div[4]/div/div[{i}]/a').click()
        time.sleep(2)

        print(f"## 현재 DB의 index_number는 {len(df)} 입니다.")

        # bs로 html parser
        new_html = driver.page_source
        target = BeautifulSoup(new_html, 'html.parser')
    
        # 아티클 제목
        title = target.find_all("div", {"class" : "sc-iFUGim igvOwa"})
        title = str(title).split('">')[1].split('</')[0].strip()
        print(f"#{i}.") 
        print("제목: ", title)

        # 가격
        price = target.find_all("div", {"class" : "sc-clBsIJ gCydIg"})
        price = str(price).split('">')[1].split('<span>')[0]
        print("가격: ", price)

        # 좋아요
        like = target.find_all("div", {"class":"sc-jWxkHr entBTg"})
        like = str(like).split('">')[1].split('</div>')[0]
        print("좋아요: ", like)

        # 조회수
        view = target.find_all("div", {"class" : "sc-dPPMrM dwJvbh"})
        view = str(view).split('width="21"/>')[1].split('</div>')[0]
        print("조회수: ", view)

        # 지역
        location = target.find_all("div", {"class" : "sc-bJTOcE dqeWNg"})
        location = str(location).split("/>")[1].split("</")[0]
        print("지역: ", location)

        # 카테고리
        category = target.find_all("span", {'class':'sc-kMBllD kTXZyT'})
        category = str(category).split('">')[1].split("</span>")[0]
        print("카테고리: ", category)

        # 아티클
        article = target.find_all('p')
        article = str(article).split('width: 663px;">')[1].split('</p>')[0]
        print("아티클: ", article)

        now = time
        now_time = now.strftime('%Y-%m-%d %H:%M:%S')
        print("현재 시각:", now_time)
        print(" ")
        print(" ")

        # 페이지 url
        link = driver.current_url
        link = str(link)

        df.loc[idx] = [title, price, like, view, article, category, location, link]
        idx += 1

        ## 스크랩 100 단위마다 csv파일로 저장
        if idx % 100 == 0 :
            df.to_csv(f"test_{idx}.csv", encoding='utf-8-sig')
            print(f"{idx}번째 df를 저장하였습니다.")

        driver.back()
        time.sleep(2)
    return df, idx


# 값을 저장할 df, idx 만들기
df = pd.DataFrame(columns=('title', 'price', 'like', 'view', 'article', 'category', 'location', 'link'))
idx = 0

## 스크랩 시작!!

for i in url_list : 
    print("이동할 주소: ", i)
    time.sleep(3)
    driver.get(i)
    time.sleep(3)
    print("현재 df입니다.",  df)
    print(f"현재 idx는 {idx} 입니다.")
    df, idx = scrap(df, idx)
    time.sleep(2)

breakpoint()
