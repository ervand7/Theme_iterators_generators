import requests
from urllib.parse import urljoin


class MyIterator:
    def __init__(self, url: str):
        self.url = url
        self.wiki_base_link = 'https://en.wikipedia.org/wiki/'
        self.response = requests.get(self.url)

    def __iter__(self):
        """If we have not this function, we can't iterate and use __next__() magic method"""
        return self

    def __next__(self):
        """We need exactly response in json format for readable and convenience"""
        return next(self.response.json())

    def create_country_link(self):
        """Here we join https://en.wikipedia.org/wiki/ with name of country
        from https://raw.githubusercontent.com/mledoze/countries/master/countries.json"""
        for country in self.response.json():
            created_country_link = urljoin(self.wiki_base_link, str(country['name']['common'])).replace(' ', '_')
            yield created_country_link

    def creating_generator_object(self):
        """In further we will write line by line from (i for i in self.create_country_link())
        to file 'country - country_link.txt'"""
        generator_for_further_writing_in_file = (i for i in self.create_country_link())
        return generator_for_further_writing_in_file
