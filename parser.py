import requests,lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_html(base_url):
    r=requests.get(base_url)
    return r.text
def get_page_data(html):
    href_company=[]
    soup = BeautifulSoup(html, 'lxml')
    company=soup.find('ul',class_='indexList').find_all('li',class_='indexList_item')

    for i in company:
        href_company.append(i.find('a').get('href'))



    return href_company

def get_html_company(href_company):
    content_dict=[]
    data_content={}
    for i in href_company:
        content=get_html(i)
        content_dict.append(content)

    data_content={'photograph':content_dict[0],
                  'videograph':content_dict[1],
                  'photo_studio':content_dict[2],
                  'vedyhie':content_dict[3],
                  'organizatorbl':content_dict[4],
                  'oformiteli':content_dict[5],
                  'stilistbl':content_dict[6],
                  'ZAGSS':content_dict[7],
                  'banket_room':content_dict[8],
                  'cars':content_dict[9],
                  'long_cars':content_dict[10],
                  'platb9':content_dict[11],
                  'rings':content_dict[12],
                  'byketbl':content_dict[13],
                  'aksessyarbl':content_dict[14],
                  'photobydki':content_dict[15],
                  'registrators':content_dict[16],
                  'mysikantbl' : content_dict[17],
                  'artists':content_dict[18],
                  'feierverki':content_dict[19],
                  'DJ':content_dict[20],
                  'horeographs':content_dict[21],
                  'keitering':content_dict[22],
                  'cooks':content_dict[23],
                  'place_for_walk':content_dict[24],
                  'other':content_dict[25]}
    href_human_list=[]
    for j in dict.values(data_content):
        soup=BeautifulSoup(j,'lxml')
        div_human=soup.find_all('div',class_='userCard')
        for k in div_human:
            href_human=k.find_all('a',class_='userCard_name')
            for v in href_human:
                href_human_list.append(v.get('href'))
    for n in dict.values(data_content):
        soup=BeautifulSoup(n,'lxml')
        div_human=soup.find_all('div',class_='userCard-pro')
        for s in div_human:
            href_human=s.find_all('a',class_='userCard_name')
            for l in href_human:
                href_human_list.append(l.get('href'))
    href_human_list = sorted(href_human_list)
    return href_human_list



def main():
    base_url = 'https://ufa.gorko.ru/'

    html=get_html(base_url)
    data=get_page_data(html)
    content_html=get_html_company(data)

    print(content_html)








if __name__=='__main__':
    main()