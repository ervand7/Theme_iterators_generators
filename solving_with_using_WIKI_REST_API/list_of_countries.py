import requests


def get_list_of_countries():
    my_list = []
    training_link_with_data_for_parse = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
    response = requests.get(training_link_with_data_for_parse)
    for i in response.json():
        my_list.append(i['name']['common'])
    return my_list
