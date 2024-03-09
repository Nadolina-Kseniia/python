from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    url = 'https://web.archive.org/web/20231202034433/https://omgtu.ru/general_information/the-structure/the-department-of-university.php' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div', class_ = "main__content") # находим  контейнер с нужным классом
    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('a'): # находим тег <a>
            description += data.text # записываем в переменную содержание тега

    # оформляем красивый список
    description = description.split('\n')
    description = [0 if x=='' else x for x in description]
    while 0 in description:
        description.remove(0)
    description[-1] = description[-1].replace(' ','',1)
    description = '\n'.join(description)

    # записываем результат в файл
    with open('kaphedry.txt', 'w') as file:
        file.write(description)
    file.close

parse();
