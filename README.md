# Публикация комиксов

Данный проект публикует рандомный комикс автора xkcd на стену вашего сообщества

### Как установить
Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)

### Получение нужных данных для работы
Для начала создаём [standalone-приложение](https://vk.com/editapp?act=create) для своего сообщества и получаем client id
Далее вводим его в файл .env в строке с CLIENT_ID

```
CLIENT_ID=ВашClientId
GROUP_ID=
ACCESS_TOKEN=
API_VERSION=5.131
```

Открываем консоль и пишем
```
python get_access_token.py
```
Переходим по полученой ссылке и получаем access_token из ссылки на страницу, на которую перешли
`https://oauth.vk.com/blank.html# --> access_token=ВашAccesToken <-- &expires_in=число&user_id=ВашUserId`

Далее вносим его в файл .env в строке с ACCESS_TOKEN
```
CLIENT_ID=ВашClientId
GROUP_ID=
ACCESS_TOKEN=ВашAccessToken
API_VERSION=5.131
```

Так-же нам нужно получить [group id своей группы и свой id](https://regvk.com/id/)
Далее вносим его в файл .env в строке с ACCESS_TOKEN
```
CLIENT_ID=ВашClientId
GROUP_ID=ВашGroupId
OWNER_ID=ВашOwnerId
ACCESS_TOKEN=ВашAccessToken
API_VERSION=5.131
```

### Как запустить
Открываем консоль и пишем
```
python main.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).