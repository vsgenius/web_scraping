import requests
import bs4
HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ru,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_ym_uid=1646540977817391266; _ym_d=1646540977; _ga=GA1.2.927992289.1646540978; hl=ru; fl=ru; _gid=GA1.2.127829036.1646670520; _ym_isad=2; visited_articles=654651; habr_web_home_feed=/all/',
'Host': 'habr.com',
'Referer': 'https://www.yandex.ru/clck/jsredir?from=yandex.ru;suggest;browser&text=',
'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="96", "Yandex";v="22"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "macOS",
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 YaBrowser/22.1.0.2500 Yowser/2.5 Safari/537.36'}
KEYWORDS = set(['дизайн', 'фото', 'web', 'python','Sberfight','ребенка'])
response = requests.get('https://habr.com/ru/all/',headers=HEADERS)
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all('a', class_="tm-article-snippet__hubs-item-link")
    tags = [hub.find('span').text for hub in hubs]
    title = article.find('a', class_="tm-article-snippet__title-link")
    if (KEYWORDS & set(tags) or KEYWORDS & set(map(str.lower,tags))) or \
            KEYWORDS & set(title.find('span').text.split()) or KEYWORDS & set(article.text.split()):
        date = article.find('time').attrs['title']
        href = 'https://habr.com' + title.attrs['href']
        print(date, title.find('span').text, href)