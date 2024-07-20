import requests
from bs4 import BeautifulSoup

# URL сайта для парсинга
url = 'https://www.drom.ru/reviews/haval/h5/1444113/'

try:
    # Отправляем GET-запрос на сайт с увеличенным временем ожидания
    response = requests.get(url, timeout=10)

    # Проверяем успешность запроса
    if response.status_code == 200:
        print("Успешно получили данные с сайта.")

        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        # Находим все элементы с классом 'item'
        title = soup.find_all(class_='item')

        if title:
            # Печатаем текст каждого элемента
            for idx, item in enumerate(title, 1):
                print(item.text.strip())
        else:
            print("Элементы с классом 'item' не найдены. Возможно, изменились классы элементов.")

        # Находим все элементы с классом 'b-fix-wordwrap'

        review = soup.find(class_='b-fix-wordwrap')

        if review:
            print("Найден первый элемент с классом 'b-fix-wordwrap'.")
            print(review.text.strip())
        else:
            print("Элементы с классом 'b-fix-wordwrap' не найдены. Возможно, изменились классы элементов.")

        # Находим все элементы с классом 'b-flex__item b-text_size_default'
        published = soup.find_all(class_='b-flex__item b-text_size_default')

        if published:
            # Печатаем текст каждого элемента
            for idx, flex_item in enumerate(published, 1):
                print(flex_item.text.strip())
        else:
            print(
                "Элементы с классом 'b-flex__item b-text_size_default' не найдены. Возможно, изменились классы элементов.")
    else:
        print(f"Не удалось получить данные с сайта. Статус-код: {response.status_code}")
except requests.exceptions.Timeout:
    print("Запрос превысил максимальное время ожидания.")
except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка при выполнении запроса: {e}")
