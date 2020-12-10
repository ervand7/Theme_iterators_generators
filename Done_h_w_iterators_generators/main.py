from Done_h_w_iterators_generators.class_My_iterator import MyIterator
import os
import hashlib


def write_country_link_in_file():
    """Creating and writing data in format: Aruba - https://en.wikipedia.org/wiki/Aruba.
    Here we use creating_generator_object() function from file 'class_MyIterator'"""
    file_path = os.path.join(os.getcwd(), 'country - country_link.txt')
    with open(file_path, 'w') as file:
        for i in exemplar_of_class_my_iterator.creating_generator_object():
            file.write(f'{i[30:]} - {i}\n')


def show_md5_hash_from_each_file_row():
    """Here we execute the second paragraph from H/w"""
    file_path = os.path.join(os.getcwd(), 'country - country_link.txt')
    with open(file_path) as file:
        for row_ in file:
            yield hashlib.md5(row_.encode('utf8')).hexdigest().lower()


if __name__ == '__main__':
    exemplar_of_class_my_iterator = MyIterator(
        'https://raw.githubusercontent.com/mledoze/countries/master/countries.json')

    write_country_link_in_file()

    for line in show_md5_hash_from_each_file_row():
        print(line)
