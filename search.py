import json
import re

from bs4 import BeautifulSoup
from requests import get

from yandex_geocoder import Client, YandexGeocoderException


client = Client("ВАШ IP ключ")

headers = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

LIST_KV_VT = {
  "type": "FeatureCollection",
  "features": []
}


def search_in_page(page):
    bn_ru = f'https://www.bn.ru/kvartiry-vtorichka/?sorting=6&page={page}'
    response = get(bn_ru, headers=headers)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    house_containers = html_soup.find_all('div', class_="catalog-item__container")
    for house_container in house_containers:
        dict_kv_vt = {"type": "Feature",
                      "id": 0,
                      "geometry": {
                          "type": "Point",
                          "coordinates": []},
                      "properties": {
                          "balloonContentHeader": "<font size=3><b><a target='_blank' href='https://yandex.ru'>Здесь может быть ваша ссылка</a></b></font>",
                          "balloonContentBody": "<p>Ваше имя: <input name='login'></p><p><em>Телефон в формате 2xxx-xxx:</em>  <input></p><p><input type='submit' value='Отправить'></p>",
                          "balloonContentFooter": "<font size=1>Информация предоставлена: </font> <strong>этим балуном</strong>",
                          "clusterCaption": "<strong><s>Еще</s> одна</strong> метка",
                          "hintContent": "<strong>Текст  <s>подсказки</s></strong>"}}
        try:
            id = int(house_container.find_all('div', class_="catalog-item__id")[0].text[2:])
            # dict_kv_vt['url'] = 'https://www.bn.ru' + house_container.find_all('a')[2]['href']
            # dict_kv_vt['details'] = house_container.find_all('div', class_="catalog-item__headline")[0].text.replace("  ", '')
            # dict_kv_vt['rooms'] = int(dict_kv_vt['details'][0])
            address = house_container.find_all('div', class_="catalog-item__address")[0].text
            print(address)
            # try:
            decimal_coord = client.coordinates(address)
            coordinates = [float(decimal_coord[0]), float(decimal_coord[1])]
            # except YandexGeocoderException:
            #     continue
            # dict_kv_vt['properties']['balloonContent'] = int(house_container.find_all('div', class_="catalog-item__price catalog-item__price-with-icon")[
            #                 0].text.replace(" ", ''))
            # dict_kv_vt['district'] = house_container.find_all('div', class_="catalog-item__district")[0].text
            # dict_kv_vt['type_of_sale'] = house_container.find_all('div', class_="catalog-item__sub-headline")[0].text
            # description_data = house_container.find_all('span', class_="catalog-item__param")
            # dict_kv_vt['description'] = list(' '.join(v.text.split()) for v in description_data)
            # dict_kv_vt['metro_name'] = house_container.find_all('span', class_="catalog-item__metro-name")[0].text.replace('\xa0', '')
            # LIST_KV_VT['features'].append(dict_kv_vt)
            dict_kv_vt['id'] = id
            dict_kv_vt['geometry']['coordinates'] = coordinates
            LIST_KV_VT['features'].append(dict_kv_vt)
            print(id, coordinates)

        except IndexError:
            continue

        except ValueError:
            continue


def search_all_kv_vt():
    for i in range(4, 5):
        search_in_page(i)
    # return LIST_KV_VT


def write_all_kv_vr_to_json():
    with open('static/json_path/new_json_content.json', 'w', encoding='utf-8') as f:
        json.dump(LIST_KV_VT, f, indent=4)


# search_all_kv_vt()
# write_all_kv_vr_to_json()

