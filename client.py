import requests

token = "Your token here"

while 1 == 1:

    number = input("Номер:")
    while True:
        message = input("(YOU)")
        if message[0] == '/':
            if message == '/exit':
                break
            elif message == '/help':
                print("/exit - выход")
                print("/help - помощь")
            else:
                print("Неизвестная команда")
        else:
            resp=requests.get(f"http://[201:a65e:753f:842e:d958:8487:edc7:ef9e]:8080/{message}@{number}@{token}", timeout=5)
            if not resp.text == "OK":
                print(f"Ошибка: {resp.text}")
