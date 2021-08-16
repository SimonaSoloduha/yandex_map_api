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
                          "balloonContentHeader": "",
                          "balloonContentBody": "",
                          "balloonContentFooter": "",
                          "clusterCaption": "",
                          "hintContent": ""}}
        try:
            id = int(house_container.find_all('div', class_="catalog-item__id")[0].text[2:])
            url = 'https://www.bn.ru' + house_container.find_all('a')[2]['href']
            details = house_container.find_all('div', class_="catalog-item__headline")[0].text.replace("  ", '')
            rooms = int(details[0])
            address = house_container.find_all('div', class_="catalog-item__address")[0].text
            decimal_coord = client.coordinates(address)
            coordinates = [float(decimal_coord[1]), float(decimal_coord[0])]

            price = int(house_container.find_all('div', class_="catalog-item__price catalog-item__price-with-icon")[
                            0].text.replace(" ", ''))
            district = house_container.find_all('div', class_="catalog-item__district")[0].text
            type_of_sale = house_container.find_all('div', class_="catalog-item__sub-headline")[0].text
            description_data = house_container.find_all('span', class_="catalog-item__param")
            description = list(' '.join(v.text.split()) for v in description_data)
            metro_name = house_container.find_all('span', class_="catalog-item__metro-name")[0].text.replace('\xa0', '')
            dict_kv_vt['id'] = id
            dict_kv_vt['geometry']['coordinates'] = coordinates
            dict_kv_vt['properties']['balloonContentHeader'] = f"<a target='_blank' href='{url}'</a></b></font>"
            dict_kv_vt['properties']['balloonContentBody'] = description
            dict_kv_vt['properties']['hintContent'] = f'{type_of_sale} Цена: {price}, Метро: {metro_name}'
            LIST_KV_VT['features'].append(dict_kv_vt)

        except IndexError:
            continue

        except ValueError:
            continue


def search_all_kv_vt():
    for i in range(4, 5):
        search_in_page(i)
    # return LIST_KV_VT


def write_all_kv_vr_to_json():
    with open('static/json_path/json_2.json', 'w', encoding='utf-8') as f:
        json.dump(LIST_KV_VT, f, indent=4)



