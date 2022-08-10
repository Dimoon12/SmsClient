import requests
#import token from file
messagerepeater=False
with open("token.txt", "r") as f:
    token = f.read()
while True:

    number = input("Номер:")
    while True:
        message = input("(YOU)")
        if message[0] == '/':
            if message == '/exit':
                break
            elif message == '/help':
                print("/exit - ввод номера")
                print("/help - помощь")
            else:
                print("Неизвестная команда")
        else:
            resp=requests.get(f"http://[201:a65e:753f:842e:d958:8487:edc7:ef9e]:8080/{message}@{number}@{token}", timeout=10)
            if not resp.text == "OK":
                print(f"Ошибка: {resp.text}")
                # сделать реакию на задокументированные ошибки а не только на сбой сети
                if messagerepeater == True:
                    while True:
                        try:
                          requests.get(f"http://[201:a65e:753f:842e:d958:8487:edc7:ef9e]:8080/{message}@{number}@{token}",timeout=10)
                        except:
                            print("Ошибка повторной отправки, пытаюсь снова")
                        else:
                            print("Повторная отправка прошла успешно")
                            break
                    break

