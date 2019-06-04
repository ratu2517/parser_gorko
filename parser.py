import requests,lxml,re,csv,itertools
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
    return data_content
def href_human(content_html):
    href_human_list=[]
    for j in dict.values(content_html):
        soup=BeautifulSoup(j,'lxml')
        div_human=soup.find_all('div',class_='userCard')
        for k in div_human:
            href_human=k.find_all('a',class_='userCard_name')
            for v in href_human:
                href_human_list.append(v.get('href'))
    return href_human_list
def href_human_pro(content_html):
    href_human_list_pro=[]

    for n in dict.values(content_html):
        soup=BeautifulSoup(n,'lxml')
        div_human=soup.find_all('div',class_='userCard-pro')
        for s in div_human:
            href_human_pro=s.find_all('a',class_='userCard_name')
            for l in href_human_pro:
                href_human_list_pro.append(l.get('href'))


    return href_human_list_pro
def get_html_human_pro(human_pro):
    get_html_human_pro_list=[]
    for i in human_pro:
        r=requests.get(i)
        get_html_human_pro_list.append(r.text)
    return get_html_human_pro_list
def get_html_human(human):
    get_html_human=[]
    for i in human:
        r=requests.get(i)
        get_html_human.append(r.text)
    return get_html_human


def get_phone_number_pro(html_human_pro):
    nomer_pro=[]
    for i in html_human_pro:
        soup=BeautifulSoup(i,'lxml')
        phone=soup.find_all('div',class_='content_l')
        for j in phone:
            nomer_pro.append(j.find('div',id='meta_info').find('div',text=re.compile('\+79')).text)
    return nomer_pro
def get_phone_nomer(html_human):
    nomer = []
    for i in html_human:
        soup = BeautifulSoup(i, 'lxml')
        phone = soup.find_all('div', class_='content_l')
        try:
            for j in phone:
                nomer.append(j.find('div', id='meta_info').find('div', text=re.compile('\+79')).text)
        except:
            continue


    return nomer
def get_name_company_pro(content_html):
    href_human_list_pro = []

    for n in dict.values(content_html):
        soup = BeautifulSoup(n, 'lxml')
        div_human = soup.find_all('div', class_='userCard-pro')
        for s in div_human:
            href_human = s.find_all('a', class_='userCard_name')
            for l in href_human:
                href_human_list_pro.append(l.get('href').split('/')[3])

    return href_human_list_pro
def get_name_company(content_html):
    href_human_list = []
    for j in dict.values(content_html):
        soup = BeautifulSoup(j, 'lxml')
        div_human = soup.find_all('div', class_='userCard')
        for k in div_human:
            href_human = k.find_all('a', class_='userCard_name')
            for v in href_human:
                href_human_list.append(v.get('href').split('/')[3])
    return href_human_list
def get_name_human(content_html):
    names_human_list = []

    for n in dict.values(content_html):
        soup = BeautifulSoup(n, 'lxml')
        div_human = soup.find_all('div', class_='userCard')
        for s in div_human:
            href_human = s.find_all('a', class_='userCard_name')
            for l in href_human:
                names_human_list.append(l.text)

    return names_human_list

def get_name_human_pro(content_html):
    names_human_list_pro = []

    for n in dict.values(content_html):
        soup = BeautifulSoup(n, 'lxml')
        div_human = soup.find_all('div', class_='userCard-pro')
        for s in div_human:
            href_human = s.find_all('a', class_='userCard_name')
            for l in href_human:
               names_human_list_pro.append(l.text)

    return names_human_list_pro
# def csv_write(name_human_pro,name_company_pro,get_phone_nomer_pro):
#     dnp=[]
#     dnk=[]
#     dph=[]
#
#     for i in name_human_pro:
#         dnp.append(str(i))
#     for j in name_company_pro:
#         dnk.append(str(j))
#     for v in get_phone_nomer_pro:
#         dph.append(str(v))
#
#         d={'name':dnp,
#            'company':dnk,
#            'phone':dph}

def csv_write(name_human_pro, name_company_pro, get_phone_nomer_pro,name_human,name_company,phone_nomer):
    with open('gorko.csv', 'w', encoding='utf-8', ) as file:
        writer = csv.writer(file)
        writer.writerow(['Имя-про', 'Компания-про', 'Номер-про','Имя','Компания','Номер'])
        writer.writerows(itertools.zip_longest(name_human_pro, name_company_pro, get_phone_nomer_pro,name_human,name_company,phone_nomer,fillvalue='-'))

def main():
    base_url = 'https://ufa.gorko.ru/'
    html=get_html(base_url)
    data=get_page_data(html)
    content_html=get_html_company(data)
    human=href_human(content_html)
    html_human=get_html_human(human)
    name_company=get_name_company(content_html)
    phone_nomer=get_phone_nomer(html_human)
    name_human=get_name_human(content_html)

    human_pro = href_human_pro(content_html)
    html_human_pro = get_html_human_pro(human_pro)
    name_company_pro = get_name_company_pro(content_html)
    get_phone_nomer_pro = get_phone_number_pro(html_human_pro)
    name_human_pro = get_name_human_pro(content_html)
    csv_write(name_human_pro,name_company_pro,get_phone_nomer_pro,name_human,name_company,phone_nomer)

if __name__=='__main__':
    main()