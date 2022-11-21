import requests
from bs4 import BeautifulSoup

def get_movie():
    ret_list = []
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&date=20221120'

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tbody = soup.select_one('tbody')
        titles = tbody.select('div.tit3 > a')
        for rank, title in enumerate(titles):
            #print(f"{rank+1}위 {title.get_text()}")
            ret_list.append((rank+1, title.get_text()))
    else : 
        print(response.status_code)

    return ret_list

    #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
    #old_content > table
    #old_content > table > tbody > tr:nth-child(3) > td.title > div > a
    #old_content > table > tbody
    #div.tit3

    #s_content > div.section > ul > li:nth-child(1) > dl > dt > a