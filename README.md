# SmsClient - Офигеть, но смс клиент!
Клиент для смс сервера, только для моих человеков.
Прост как картошка, сами научитесь пользоваться

# Как открыть этого зверя?
Ставить зависимости:
pip3 install requests

Создать текстовик и засунуть туда токен

Запуск: python3 client.py

Бахнуть пива

# Для очкариков

структура запроса: http://[IPV6_Яжки]/сообщение@номер@токен

## Ответы:

OK - все найс, может сервак дохлый, пока что никак такое не задетектить

F_CRITICAL_FAULT - неведомый пиздец

F_NUMBER_WHITELIST_FAILED - номер не в вайт листе, попросите меня добавить, вынужденая мера чтоб не писали хуйню бедным кожаным мешкам.

F_TOKEN_TRIES_EXAUSTED - у токена кончились попытки, первого числа все будет найс

F_TOKEN_AUTH_FAILED - вместо токена дичь, сударь!
