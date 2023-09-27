import requests
from bs4 import BeautifulSoup

from newspaper import Article

import pandas as pd


def search_naver_news(query):
    # 네이버 뉴스 검색 URL
    url = "https://search.naver.com/search.naver?where=news&query={}"
    #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}

    # https://www.dt.co.kr/contents.html?article_no=2023060802109931820004&ref=naver
    
     # HTTP GET 요청 보내기
    response = requests.get(url.format(query))
 
    
    # 응답을 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 뉴스 기사 링크 찾기
    news_links = soup.select(".news_area > a")
    
    
    if not news_links:
        print("뉴스 기사를 찾을 수 없습니다.")
        return
    
    # 첫 번째 뉴스 기사 링크 선택
    first_news_link = news_links[0]["href"]
    print(first_news_link)

    a = Article(first_news_link, language='ko')
    a.download()
    a.parse()
    
    # 기사 제목
    print(a.title)
    print("==============")

    # 기사내용
    print(a.text)
   

if __name__ == "__main__":
    query = input("뉴스 기사 제목을 입력하세요: ")
    search_naver_news(query)
