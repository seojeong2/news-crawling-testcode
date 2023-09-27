import requests
from bs4 import BeautifulSoup

import pandas as pd
import time
import re


def search_news(query):


    # 검색어 입력
    search_query = query

    # 네이버 뉴스 검색 URL
    search_url = f"https://search.naver.com/search.naver?where=news&query={search_query}"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36'}

    # HTTP GET 요청을 보내서 검색 결과 페이지 가져오기
    response = requests.get(search_url, headers=headers)
    time.sleep(5)

    # HTTP 요청이 성공했는지 확인
    if response.status_code == 200:


        # 검색 결과 페이지를 파싱하기 위해 BeautifulSoup 객체 생성
        soup = BeautifulSoup(response.text, 'html.parser')

        # 검색 결과에서 뉴스 기사 제목과 링크 추출
        # news_titles = soup.find_all('a', {'class': 'news_tit'})

        first_link = soup.find('a', {'class': 'news_tit'})
        
        if first_link:
            new_link = first_link['href']
        else:
            new_link = "no link"

        # print(new_link)
        return new_link
    else:
        print('검색 결과 페이지를 가져올 수 없습니다.')
        return '검색 결과 페이지를 가져올 수 없습니다.'


        
    #     # 검색 결과 중 첫 번째 기사 선택 (변경 가능)
    #     first_news = news_titles[0]

    #     # 뉴스 기사 제목과 링크 출력
    #     news_title = first_news.get_text()
    #     news_link = first_news['href']
    #     print('뉴스 기사 제목:', news_title)
    #     print('뉴스 기사 링크:', news_link)

    #     # 뉴스 기사 링크로 이동하여 기사 본문 내용 가져오기
    #     article_response = requests.get(news_link)
    #     if article_response.status_code == 200:
    #         article_soup = BeautifulSoup(article_response.text, 'html.parser')

    #         # 기사 본문 내용 추출
    #         article_content = article_soup.find('div', {'id': 'articleBodyContents'}).get_text()

    #         # 기사 본문 출력
    #         print('뉴스 기사 본문:')
    #         print(article_content)
    #     else:
    #         print('뉴스 기사 링크에 접근할 수 없습니다.')
    # else:
    #     print('검색 결과 페이지를 가져올 수 없습니다.')

def clean_text(text):
    # 정규 표현식을 사용하여 문자열에서 특수 문자와 공백을 제거
    cleaned_text = re.sub(r'[^a-zA-Z0-9가-힣\s]', '', text)
    # 쌍따옴표 제거
    cleaned_text = cleaned_text.replace('"', '')
    # 중복 공백 제거
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text



def getData():

    data3 = []

    data = pd.read_csv("/Users/seojeong/Desktop/news.csv")
    data2 = data["기사제목"].tolist()

    for i in data2:
        tmp = clean_text(i)
        data3.append(tmp)

    return data3
    

        

if __name__ == "__main__":

    temp_list = []

    f = open("log.txt", "w")
 
    data = getData()
    for idx, i in enumerate(data):
        print(idx)
        f.write(str(idx)+"\n")
        ret = search_news(i)
        temp_list.append(ret)
        f.write(ret+"\n")
        # temp_list.append(search_news(i))
     

    df = pd.DataFrame(temp_list)
    df.to_csv('output.csv',index=False)


