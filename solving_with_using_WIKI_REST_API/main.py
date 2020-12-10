from solving_with_using_WIKI_REST_API.list_of_countries import get_list_of_countries
from solving_with_using_WIKI_REST_API.class_Wiki import Wiki
import hashlib

if __name__ == '__main__':
    for i in get_list_of_countries():
        wiki_user = Wiki(i)
        print(
            f'{i} - {wiki_user.get_wiki_data()} - {hashlib.md5(wiki_user.get_wiki_data().encode()).hexdigest().lower()}')
