# yandex_map_api

Приложение yandex_map_api наносит на карту Яндекс объекты с сайта поиска недвижимости. 

## Запуск проекта:

Откройте консоль

Перейдите в папку, в которой будет храниться проект

cd <путь до папки>

Склонируйте проект
https://github.com/SimonaSoloduha/yandex_map_api

перейдите в папку проекта
cd flask

Создайте виртуальное окружение venv
python3 -m venv venv

Активируйте виртуальное окружение venv
source venv/bin/activate

Установите необходимые пакеты:
pip3 install -r requirements.txt

(Все используемые библиотеки представлены в файле requirements.txt)

При необходимости обновите pip

(Если получите сообщение: WARNING: You are using pip version 20.2.3; however, version 21.2.1 is available. You should consider upgrading via the '..... flask/venv/bin/python3 -m pip install --upgrade pip' command.)

Добавьте в код свой ключ (в файл search.py (10-я строка) и в файл /templates/index.html (10-я строка)

Запустите проект через конлось 

python3 app.py runserver 

Перейдете по ссыке
http://127.0.0.1:5000/

