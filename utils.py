#!/usr/bin/env python3

from requests import *
from bs4 import BeautifulSoup
import pandas as pd
import httpx
import time
from pymongo import MongoClient
from datetime import datetime, timedelta
from bson import json_util


# url = 'https://breachforums.st/Thread-DATABASE-Lockerim-co-il-CSV'
# _cookies = {'cf_clearance':'VG0zNJEQ5tIdeYo8CIdmPy7H6Cew5atCI2fWP7aLin8-1714416038-1.0.1.1-hkhQpdYKA3eyJeh5dweI3WEuoYisb6VslCo6X8yzWmYGm7xx.rm1dX2hFiBkKACflzTSev.K86qj0BzMoLE4_A',
#             'loginattempts':'1',
#             'mybb[announcements]':'0',
#             'mybb[lastactive]':'1714416183',
#             'mybb[lastvisit]':'1714416085',
#             'mybbuser':'195220_2VCGScwBl6Npou4h1XgN1NjpDkTtxrOUdy4QMfWma4BnsUpIkL',
#             'sid':'0c12297edda54129969e000a86040dbb'}
# page = get(url, cookies=_cookies)
def hackernews() -> None:

    url = 'https://thehackernews.com/search?max-results=100&by-date=true'
    page = get(url=url)

    soup = BeautifulSoup(page.text, 'html.parser')

    posts = soup.find_all('div', class_='body-post clear')
    for _post in posts:
        data = {}
        data['link'] = _post.find('a', class_='story-link').attrs['href'].strip()
        data['title'] = _post.find('h2', class_ = 'home-title').text.strip()
        data['date'] = datetime.strptime( _post.find('span', class_ = 'h-datetime').text[1:], "%b %d, %Y").strftime('%Y-%m-%d')
        data['desc'] = _post.find('div', class_ = 'home-desc').text.strip()
        data['type'] = 'news'
        db_insert(data)
    
    # df = pd.DataFrame(all_data)
    # print(df)

def seconline() -> None:

    url = 'https://securityonline.info/page/1/'
    page = get(url=url)

    # print(page.text)

    soup = BeautifulSoup(page.text, 'html.parser')

    posts = soup.find_all('div', class_='post-content')
    # print(posts)
    for _post in posts:
        data = {}
        data['link'] = _post.find('h2', class_ = 'post-title entry-title').find('a').attrs['href'].strip()
        data['title'] = _post.find('h2', class_ = 'post-title entry-title').text.strip()
        data['date'] = datetime.strptime(_post.find('p', class_ = 'post-date').text.split("\xa0by")[0].strip(), '%B %d, %Y').strftime('%Y-%m-%d')
        data['desc'] = _post.find('div', class_ = 'entry excerpt entry-summary').find('p').text.strip()
        data['type'] = 'news'
        db_insert(data)
    
    # df = pd.DataFrame(all_data)
    # print(df)

def bleepcomp() -> None:
    client = httpx.Client(http2=True)
    url = 'https://www.bleepingcomputer.com/news/security/'
    page = client.get(url=url)

    # print(page.text)

    soup = BeautifulSoup(page.text, 'html.parser')

    posts = soup.find_all('div', class_ = 'bc_latest_news_text')
    # print(posts[0])
    for _post in posts:
        data = {}
        data['link'] = _post.find('h4').find('a').attrs['href'].strip()
        data['title'] = _post.find('h4').find('a').text.strip()
        data['date'] = datetime.strptime(_post.find('ul').find('li', class_ = 'bc_news_date').text.strip(), '%B %d, %Y').strftime('%Y-%m-%d')
        data['desc'] = _post.find('p').text.strip()
        data['type'] = 'news'
        db_insert(data)    

    # df = pd.DataFrame(all_data)
    # print(df)

def exploitdb() -> None:
    time_ = round(time.time() * 1000) - 704110
    url = f'https://www.exploit-db.com/?draw=1&columns%5B0%5D%5Bdata%5D=date_published&columns%5B0%5D%5Bname%5D=date_published&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=download&columns%5B1%5D%5Bname%5D=download&columns%5B1%5D%5Bsearchable%5D=false&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=application_md5&columns%5B2%5D%5Bname%5D=application_md5&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=verified&columns%5B3%5D%5Bname%5D=verified&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=description&columns%5B4%5D%5Bname%5D=description&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=type_id&columns%5B5%5D%5Bname%5D=type_id&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=platform_id&columns%5B6%5D%5Bname%5D=platform_id&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=author_id&columns%5B7%5D%5Bname%5D=author_id&columns%5B7%5D%5Bsearchable%5D=false&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=code&columns%5B8%5D%5Bname%5D=code.code&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=id&columns%5B9%5D%5Bname%5D=id&columns%5B9%5D%5Bsearchable%5D=false&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=9&order%5B0%5D%5Bdir%5D=desc&start=0&length=15&search%5Bvalue%5D=&search%5Bregex%5D=false&author=&port=&type=&tag=&platform=&_={time_}'
    page = get(url=url, headers={'User-Agent':'Mozilla/5.0', 'Accept':'application/json, text/javascript', 'X-Requested-With': 'XMLHttpRequest'})
    # print(url)
    data_ = page.json()['data']


    # soup = BeautifulSoup(page.text, 'html.parser')

    # posts = soup.find('table')
    # print(posts)
    for i in data_:
        data = {}
        data['link'] = 'https://www.exploit-db.com/exploits/' + i['id'].strip()
        data['title'] = i['description'][1].strip()
        data['date'] = i['date_published']
        data['desc'] = i['description'][1].strip()
        data['type'] = 'exploit'
        db_insert(data)    

    # df = pd.DataFrame(all_data)
    # print(df)

def cvedetails() -> None:
    date_ = datetime.now()
    url = 'https://www.cvedetails.com/vulnerability-search.php?f=1&publishdatestart=' + (date_ - timedelta(days=1)).strftime('%Y-%m-%d') + '&publishdateend=' + date_.strftime('%Y-%m-%d')
    page = get(url=url, headers={'User-Agent':'Mozilla/5.0'})

    soup = BeautifulSoup(page.text, 'html.parser')

    posts = soup.find_all('div', {'data-tsvfield': 'cveinfo'})
    for _post in posts:
        data = {}
        data['link'] = 'https://www.cvedetails.com' + _post.find('a').attrs['href'].strip()
        data['title'] = _post.find('a').text.strip()
        data['date'] = _post.find('div', {'data-tsvfield': 'publishDate'}).text.strip()
        data['desc'] = _post.find('div', {'data-tsvfield': 'summary'}).text.strip()
        data['type'] = 'cve'
        db_insert(data)

def snykio() -> None:
    url = 'https://security.snyk.io/disclosed-vulnerabilities/'
    page = get(url=url, headers={'User-Agent':'Mozilla/5.0'})

    soup = BeautifulSoup(page.text, 'html.parser')

    posts = soup.find_all('li', {'data-snyk-test': 'ProprietaryVulns: item'})
    for _post in posts:
        data = {}
        data['link'] = 'https://security.snyk.io' + _post.find('a').attrs['href'].strip()
        data['title'] = ' '.join( [i.strip() for i in _post.find('p').text.split('\n')] )
        data['date'] = datetime.strptime( _post.find('div', {'data-snyk-test': 'ProprietaryVulns: publicationTime'}).text.strip(), '%d %b %Y').strftime('%Y-%m-%d')
        
        desc = get(url=data['link'], headers={'User-Agent':'Mozilla/5.0'})
        desc_soup = BeautifulSoup(desc.text, 'html.parser')

        data['desc'] = desc_soup.find_all('div', class_ = 'markdown-section')[1].find('div', class_ = 'markdown-description').text.strip()
        data['type'] = 'vuln'
        db_insert(data)

def rapid7() -> None:
    url = 'https://www.rapid7.com/db/?q=&type=metasploit'
    page = get(url=url, headers={'User-Agent':'Mozilla/5.0'})

    soup = BeautifulSoup(page.text, 'html.parser')

    posts = soup.find_all('a', class_ = 'vulndb__result resultblock')
    for _post in posts:
        data = {}
        data['link'] = 'https://www.rapid7.com' + _post.attrs['href'].strip()
        data['title'] = _post.find('div', class_ = 'resultblock__info-title').text.strip()
        data['date'] = datetime.strptime( _post.find('div', class_ = 'resultblock__info-meta').text.strip().split('Disclosed: ')[1], '%B %d, %Y').strftime('%Y-%m-%d')
        
        desc = get(url=data['link'], headers={'User-Agent':'Mozilla/5.0'})
        desc_soup = BeautifulSoup(desc.text, 'html.parser')

        data['desc'] = desc_soup.find_all('div', class_ = 'vulndb__detail-content')[0].find('p').text.strip()
        data['type'] = 'exploit'
        db_insert(data)
    
def packetstorm() -> None:
    url = 'https://packetstormsecurity.com/files/'
    page = get(url=url, headers={'User-Agent':'Mozilla/5.0'})

    soup = BeautifulSoup(page.text, 'lxml')

    posts = soup.find_all('dl', class_ = 'file')
    for _post in posts:
        data = {}
        data['link'] = 'https://packetstormsecurity.com' + _post.find('a').attrs['href'].strip()
        data['title'] = _post.find('a').text.strip()
        data['date'] = datetime.strptime( _post.find('dd', class_ = 'datetime').find('a').text.strip(), '%b %d, %Y').strftime('%Y-%m-%d')
        data['desc'] = _post.find('dd', class_ = 'detail').text.strip()
        data['type'] = 'exploit'
        db_insert(data)
    
def cxsec() -> None:
    url = 'https://cxsecurity.com/wlb/rss/all/'
    page = get(url=url, headers={'User-Agent':'Mozilla/5.0'})

    soup = BeautifulSoup(page.text, 'xml')

    posts = soup.find_all('item')
    for _post in posts:
        data = {}
        data['link'] = _post.find('link').text.strip()
        data['title'] = _post.find('title').text.strip()
        data['date'] = _post.find('lastBuildDate').text.split(' ')[0] #datetime.strptime( _post.find('dd', class_ = 'datetime').find('a').text.strip(), '%b %d, %Y').strftime('%Y-%m-%d')
        data['desc'] = _post.find('description').text.split(' Text:')[0]
        data['type'] = 'exploit'
        db_insert(data)

def zerodtoday() -> None:
    url = 'https://en.0day.today/'
    headers={'User-Agent':'Mozilla/5.0'}
    page = get(url=url, headers=headers)
    cookie_val = page.cookies.get('PHPSESSID')
    headers['Cookie'] = 'PHPSESSID=' + cookie_val
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    page = post(url=url, data='agree=Yes%2C+I+agree', headers=headers)
    page = get(url=url, headers=headers)

    soup = BeautifulSoup(page.text, 'html.parser')

    # all_data = []

    posts = soup.find_all('div', class_ = 'ExploitTableContent')
    # print(posts)
    for _post in posts:
        data = {}
        data['link'] = 'https://en.0day.today' + _post.find('h3').find('a').attrs['href'].strip()
        data['title'] = _post.find('h3').text.strip()
        data['date'] = datetime.strptime( _post.find('a').text.strip(), '%d-%m-%Y').strftime('%Y-%m-%d')
        
        desc = get(url=data['link'], headers=headers)
        desc_soup = BeautifulSoup(desc.text, 'html.parser')

        try:
            data['desc'] = desc_soup.find('div', string='Description').find_next().text.strip()
        except:
            data['desc'] = data['title']

        data['type'] = 'exploit'
        # all_data.append(data)
        db_insert(data)
    
    # df = pd.DataFrame(all_data)
    # print(df)    
    # print(all_data[0])

def db_insert(data_: dict) -> None:

    client = MongoClient("mongodb://localhost:27017/")

    # Access the database (it will be created if it doesn't exist)
    db = client["mydatabase"]

    # Access the collection (it will be created if it doesn't exist)
    collection = db["mycollection"]

    # Insert a document
    # collection.insert_many(exploitdb())

    query = {'link': ''}
    query['link'] = data_['link'].strip()
    if not collection.find_one(query):
        collection.insert_one(data_)

def db_fetch() -> str:
    client = MongoClient("mongodb://localhost:27017/")

    db = client["mydatabase"]
    collection = db["mycollection"]

    all_data = collection.find().sort('date', -1)

    return json_util.dumps(all_data)
    # for data in all_data:
    #     print(data['link'] + '-->' + data['date'])

def db_test():
    client = MongoClient("mongodb://localhost:27017/")

    # Access the database (it will be created if it doesn't exist)
    db = client["mydatabase"]

    # Access the collection (it will be created if it doesn't exist)
    collection = db["mycollection"]

    test_dic = {'link': 'linktest', 'title': 'titletest', 'date': '2024-07-01', 'desc': 'literally description', 'tags': ['vuln', 'exploit', 'news']}

    # collection.insert_one(test_dic)

    res = collection.delete_many({})
    print(res.deleted_count)
    print('\n###\n')

    # doc = collection.find()
    # print(len(list(doc)))

    # for doci in doc:
    #     print(doci['desc'])
    #     if doci.get('tags'):
    #         print(doci['tags'][1])

def scrape() -> None:
    print('[*] 1')
    hackernews()
    print('[*] 2')
    seconline()
    print('[*] 3')
    bleepcomp()
    print('[*] 4')
    exploitdb()
    print('[*] 5')
    cvedetails()
    print('[*] 6')
    snykio()
    print('[*] 7')
    rapid7()
    print('[*] 8')
    packetstorm()
    print('[*] 9')
    cxsec()
    print('[*] 10')
    zerodtoday()
    print('[+] Done')

# scrape()
# print(db_fetch())

# hackernews()
# bleepcomp()
# seconline()
# exploitdb()

# db_test()