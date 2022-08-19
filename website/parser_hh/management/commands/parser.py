import pprint
import random
import requests
import json
import time
from tqdm import tqdm

"""
Структура базы:
address - адрес собрать с компанией вместе
alternate_url - адрес страницы
contacts - контакты, могут быть None
- employer - name - название компании
name - название вакансии
- salary - зарплата от до и валюта, может не быть - собрать в один str
- schedule - name - Полный день - график работы
snippet - requirement - Что нужно 
snippet - responsibility - чем придется заниматься
description - описание компании
- employment - name - Стажировка
- experience - name - Нет опыта 
- key_skills множественное name  
- professional_roles - профессиональная роль
- specializations - множественное name - специализация
"""


def treatment_str(data):
    """
    Убираем ненужные символы в строковых данных.
    :param data: Строка.
    :return: Строка.
    """
    deleted_words = ['<p>', '<strong>', '</p>', '</strong>', '<ul>', '<li>',
                     '</li>', '</ul>', '<highlighttext>', '</highlighttext>',
                     '\r', '\r\n', '<br />', '</ol>', '<ol>', '&quot;']
    for i_str in deleted_words:
        if isinstance(data, str):
            data = data.replace(i_str, '')
    return data


def get_id_area(region, regions):
    """
    Получаем код региона для поиска.
    :param region: Интересующий регион или город.
    :param regions: Список всех городов и регионов РФ с id.
    :return: Номер id города или региона.
    """
    region = region.lower()
    for places in regions:
        if region == places['name'].lower():
            return int(places['id'])
        for place in places['areas']:
            if region == place['name'].lower():
                return int(place['id'])
    return 11  # иначе вся Россия


def data_processing(data, pattern_external, pattern_inner):
    """
    Обрабатываем данные вакансии, выбираем нужные и формируем словарь.
    :param data: Вакансия
    :param pattern_external: Список нужных ключей вакансии.
    :param pattern_inner: Список нужных ключей внутри ключей.
    :return: Словарь со списками в значениях
    """
    # TODO если нет данных, заполняем нулями
    result = {}
    for keys, items in data.items():
        new_value = list()
        if keys in pattern_external:
            if isinstance(items, str):
                new_value.append(treatment_str(items))
                result[keys] = new_value
            elif isinstance(items, dict):
                for key, item in items.items():
                    if key in pattern_inner:
                        new_data = treatment_str(item) if isinstance(item, str)\
                            else item
                        new_value.append(new_data)
                result[keys] = new_value
            elif isinstance(items, list):
                for values in items:
                    for key, value in values.items():
                        if key in pattern_inner:
                            new_value.append(value)
                result[keys] = new_value
            else:
                new_value.append('No data')
                result[keys] = new_value
    return result


if __name__ == '__main__':
    params_file = 'parser_hh/management/commands/params.json'
    # params_file = 'params.json'
    result_file = 'database.json'
    request_address = f'https://api.hh.ru/vacancies'
    page = 0
    with open(params_file, 'r') as get_params:
        data_params = json.load(get_params)
    params = {
        'area': 113,
        'page': page
    }
    areas_address = f'https://api.hh.ru/areas/'
    id_areas = requests.get(areas_address).json()[0]['areas']
    id_1 = get_id_area(data_params['area'], id_areas)

    if data_params.get('text'):
        params['text'] = data_params['text']
    if data_params.get('area'):
        params['area'] = get_id_area(data_params['area'], id_areas)
    if data_params.get('employment'):
        params['employment'] = data_params['employment']
    if data_params.get('schedule'):
        params['schedule'] = data_params['schedule']

    counter_vacancies = 0
    columns_one = [
        "snippet", "alternate_url", "employer", "schedule", "area",
        "name", "salary", "address", "contacts"
    ]
    domestic_columns_one = [
        "name", "requirement", "responsibility", "from", "to", "currency", "raw"
    ]
    columns_two = [
        "description", "employment", "experience", "key_skills",
        "professional_roles", "specializations"
    ]
    domestic_columns_two = [
        "name"
    ]
    db = {}
    # pages = requests.get(request_address, params=params).json()['pages']
    pages = 1
    for page in tqdm(range(pages)):
        params['page'] = page
        next_page = requests.get(request_address, params=params).json()
        for data_job in tqdm(next_page['items']):
            time.sleep(1 + random.random())
            # Обработка одой вакансии
            id_address = f'https://api.hh.ru/vacancies/{data_job["id"]}'
            data_further = requests.get(id_address).json()
            part_one = data_processing(data_job, columns_one,
                                       domestic_columns_one)
            part_two = data_processing(data_further, columns_two,
                                       domestic_columns_two)

            vacancy = part_one | part_two
            db[counter_vacancies] = vacancy
            counter_vacancies += 1

    with open('database.json', 'w') as database:
        json.dump(db, database)
