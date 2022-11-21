import requests
from bs4 import BeautifulSoup

def get_melon():
    ret_list = []
    url = 'https://www.melon.com/chart/'
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tbody = soup.select_one('tbody')
        titles = tbody.select('td > div > div > div.ellipsis.rank01 > span > a')
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

    ##lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
    ##lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
    ##lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
    ##lst50