import hashlib
import os
from urllib.parse import urljoin

import requests


class MyIterator:
    def __init__(self, url: str):
        self.url = url
        self.wiki_base_link = 'https://en.wikipedia.org/wiki/'
        self.response = requests.get(self.url)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.response.json())

    def create_country_link(self):
        for country in self.response.json():
            created_country_link = urljoin(self.wiki_base_link, str(country['name']['common'])).replace(' ', '_')
            yield created_country_link

    def creating_generator_object(self):
        generator_for_further_writing_in_file = (i for i in self.create_country_link())
        return generator_for_further_writing_in_file


def write_country_countrylink_in_file():
    file_path = os.path.join(os.getcwd(), 'country - country_link.txt')
    with open(file_path, 'w') as file:
        for i in exemplar_of_class_my_iterator.creating_generator_object():
            file.write(f'{i[30:]} - {i}\n')


def show_md5_hash_from_each_file_row():
    file_path = os.path.join(os.getcwd(), 'country - country_link.txt')
    with open(file_path) as file:
        for row_ in file:
            yield hashlib.md5(row_.encode('utf8')).hexdigest().lower()


if __name__ == '__main__':
    exemplar_of_class_my_iterator = MyIterator(
        'https://raw.githubusercontent.com/mledoze/countries/master/countries.json')

    write_country_countrylink_in_file()

    for line in show_md5_hash_from_each_file_row():
        print(line)

# ________________________________________________________
# |||||||||||| a variant without classes ||||||||||||

# def get_list_of_links_to_wiki():
#     training_link_with_data_for_parse = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
#     wiki_base_link = 'https://en.wikipedia.org/wiki/'
#     response = requests.get(training_link_with_data_for_parse)
#     for country in response.json():
#         create_country_link = urljoin(wiki_base_link, str(country['name']['common'])).replace(' ', '_')
#         yield create_country_link
#
#
# # for i in get_list_of_links_to_wiki():
# #     pprint(i)
#
#
# file_path = os.path.join(os.getcwd(), 'country - country_link.txt')
# with open(file_path, 'w') as file:
#     for i in get_list_of_links_to_wiki():
#         file.write(f'{i[30:]} - {i}\n')
