def get_district_list():
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
    lst = string.split('\n')[1:-1]
    for line in lst:
        input_string = line
        split_string = input_string.split('\xa0\xa0 \xa0')
        if len(split_string) >= 2:
            city, district = split_string[1].split('\xa0\xa0 \xa0')[0].strip(), split_string[3].split('<br/>')[0].strip()
            district_list.append(unidecode(district).lower())
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
            district_list.append(unidecode(district).lower())
        else:
            line = ()
    return district_list

def get_district_dict():
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
    district_dict=dict()
    lst = string.split('\n')[1:-1]
    for line in lst:
        input_string = line
        split_string = input_string.split('\xa0\xa0 \xa0')
        if len(split_string) >= 2:
            city, district = split_string[1].split('\xa0\xa0 \xa0')[0].strip(), split_string[3].split('<br/>')[0].strip()
            district_dict[unidecode(district).lower()] = city
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
            district_dict[unidecode(district).lower()] = city
        else:
            line = ()
    return district_dict

def get_city_map():
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
    city_map = dict()
    lst = string.split('\n')[1:-1]
    for line in lst:
        input_string = line
        split_string = input_string.split('\xa0\xa0 \xa0')
        if len(split_string) >= 2:
            city, district = split_string[1].split('\xa0\xa0 \xa0')[0].strip(), split_string[3].split('<br/>')[0].strip()
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
            city_map[unidecode(city).lower()]=city
        else:
            line = ()
    return city_map
        
def get_avenues_list():
    import pandas as pd 
    import numpy as np
    from unidecode import unidecode
    df = pd.read_csv('da_nang_data.csv')
    column_dict = {column: df[column].to_list() for column in df.columns[1:-1]}
    avenues_map = dict()
    avenues_list = []
    for key, values in column_dict.items():
        for value in values:
            if value is not np.NaN:
                # avenues_map[unidecode(key).lower()].append(unidecode(' '.join(value.split('\xa0'))).lower())
                if 'Đường' in value or 'Phường' in value or 'Xã' in value:
                    avenues_map[' '.join(unidecode(' '.join(value.split('\xa0'))).lower().split()[1:])]=unidecode(key).lower()
                    avenues_list.append(' '.join(unidecode(' '.join(value.split('\xa0'))).lower().split()[1:]))
                else:
                    avenues_map[unidecode(' '.join(value.split('\xa0'))).lower()]=unidecode(key).lower()
                    avenues_list.append(unidecode(' '.join(value.split('\xa0'))).lower())
    return avenues_list

def get_avenues_map():
    import pandas as pd 
    import numpy as np
    from unidecode import unidecode
    df = pd.read_csv('da_nang_data.csv')
    column_dict = {column: df[column].to_list() for column in df.columns[1:-1]}
    avenues_map = dict()
    avenues_list = []
    for key, values in column_dict.items():
        for value in values:
            if value is not np.NaN:
                # avenues_map[unidecode(key).lower()].append(unidecode(' '.join(value.split('\xa0'))).lower())
                if 'Đường' in value or 'Phường' in value or 'Xã' in value:
                    avenues_map[' '.join(unidecode(' '.join(value.split('\xa0'))).lower().split()[1:])]=unidecode(key).lower()
                    avenues_list.append(' '.join(unidecode(' '.join(value.split('\xa0'))).lower().split()[1:]))
                else:
                    avenues_map[unidecode(' '.join(value.split('\xa0'))).lower()]=unidecode(key).lower()
                    avenues_list.append(unidecode(' '.join(value.split('\xa0'))).lower())
    return avenues_map

if __name__ == '__main__':
    print(get_avenues_map())