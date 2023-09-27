from newspaper import Article

url = 'https://www.hankyung.com/society/article/2023060146561'
a = Article(url, language='ko')
a.download()
a.parse()


print(a.title)

