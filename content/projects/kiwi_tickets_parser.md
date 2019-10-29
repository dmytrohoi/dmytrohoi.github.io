Title: Kiwi Tickets Parser
Date: 2019-01-31 11:01
Modified: 2019-02-02 18:30
Tags: parser, python, tkinter, requests, projects, lang:russian
Slug: kiwi_tickets_parser
Summary: Скрипт с интерфейсом для создания партнерских ссылок на покупку билетов с сайта Kiwi.com.


## Цель

Создать скрипт, который бы в автоматическом режиме находил самые дешевые билеты
и создавал партнерские ссылки на них для публикации в Telegram канале на тему
туризма (travel-channel).

-----

## Инструментарий

Основной язык: Python 3.6

Библиотеки:

- requests - отправка запроса на сервер по REST API;

- json - преобразование JSON ответа от сервера в объект Python;

- tkinter - создание интерфейса для программы.

-----

## Алгоритм

Скрипт отправляет запрос, в зависимости от потребностей пользователя (меню настройки запроса), и выдает полученную инфомацию о билетах, в заложенном в скрипте виде, для каждого авиарейса с сайта Kiwi.com. Внутри используется requests запрос который по API получает информацию в JSON о авиарейсах и переведя этот json в объект Python из этого объекта выбирается нужная информация.

![Интерфейс программы Kiwi Tickets Parser](/images/projects/kiwi_tickets_parser.jpg)

-----

## Код

Ниже представлено часть кода программы:

    headers = { 'apiKey': settings.API_KEY }
    URL = 'https://kiwicom-prod.apigee.net/v2/search'

    request = get(URL, params=payload, headers=headers)
    content = request.json()

    text.delete(1.0, END)
    text.insert(END, '\n\tОновлено: ' + datetime.now().strftime('%H:%M'))

    if not content.get('data'):
        return text.insert(END, f'\n\n\tВозникла ошибка! \n\n\t{
            (content.get("fault") if content.get("fault") else content.get("message"))
        }')

    affilid = settings.AFFILID

    CURR_SYMBOL = {
        'EUR': '€',
        'UAH': '₴',
        'USD': '$'
    }

    curr = CURR_SYMBOL.get(payload['curr'], payload['curr'])

__Иная информация защищена авторскими правами..__