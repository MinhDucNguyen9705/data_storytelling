import json 
import requests
from bs4 import BeautifulSoup 
from unidecode import unidecode

# Perform web scraping to get data
url_1 = 'https://tdkmart.com/danh-sach-cac-quan-huyen-cua-64-tinh-thanh-viet-nam-link-1'
data = requests.get(url_1)
soup = BeautifulSoup(data.content, 'html.parser') 
s = soup.find('div', class_="module-content") 
content = s.find_all('p') 
string = str(content[2])
district_list=[]
district_dict=dict()
city_map = dict()
lst = string.split('\n')[1:-1]
for line in lst:
    input_string = line
    split_string = input_string.split('\xa0\xa0 \xa0')
    if len(split_string) >= 2:
        city, district = split_string[1].split('\xa0\xa0 \xa0')[0].strip(), split_string[3].split('<br/>')[0].strip()
        result_tuple = (city, district)
        district_list.append(unidecode(district).lower())
        district_dict[unidecode(district).lower()] = city
        city_map[unidecode(city).lower()]=city
    else:
        line = ()

url_2 = 'https://tdkmart.com/danh-sach-cac-quan-huyen-cua-64-tinh-thanh-viet-nam-link-2'
data = requests.get(url_2)
soup = BeautifulSoup(data.content, 'html.parser') 
s = soup.find('div', class_="module-content") 
content = s.find_all('p') 
string = str(content[1])
lst = string.split('\n')[1:-1]
for line in lst:
    input_string = line
    split_string = input_string.split('\xa0\xa0 \xa0')
    if len(split_string) >= 2:
        city, district = split_string[1].split('\xa0\xa0 \xa0')[0].strip(), split_string[3].split('<br/>')[0].strip()
        result_tuple = (city, district)
        district_list.append(unidecode(district).lower())
        district_dict[unidecode(district).lower()] = city
        city_map[unidecode(city).lower()]=city
    else:
        line = ()

# print(district_list)
# print(district_dict)
# print(city_map)
        
import pandas as pd 

df = pd.read_csv('da_nang_data.csv')
avenues_list = df.iloc[:,1].to_list()
for i in range (len(avenues_list)):
    temp = ' '.join(avenues_list[i].split('\xa0'))
    avenues_list[i] = unidecode(temp).lower()
# print(avenues_list)