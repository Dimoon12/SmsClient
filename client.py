import time

import requests

#######
# Переключите на true и вам будут совать ссылки на справку по ошибке которая выскочила
linkon = False
#######

def fault(fault,type):
    if type == "CRIT":
        print(f"[КРИТ] Программа будет закрыта Т.К восстановить работоспособность не удалось. Ошибка: ({fault})")
        if linkon == True:
            print(f"https://github.com/Dimoon12/SmsClient/wiki/{fault}")
        exit()
    elif type == "WARN":
        print(f"[ПРЕД] Предупреждение, проверьтие проблему ({fault}). продолжаем работу")
        if linkon == True:
            print(f"https://github.com/Dimoon12/SmsClient/wiki/{fault}")

def checkinet():
    try:
        requests.get("http://[21e:a51c:885b:7db0:166e:927:98cd:d186]", timeout=4)
        return True
    except:
        fault("Yggdrasil_unavaible", "CRIT")

#import token from file
messagerepeater=True
with open("token.txt", "r") as f:
    token = f.read()
while True:
    checkinet()
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
                if messagerepeater == True:
                    while True:
                        reqloop=requests.get(f"http://[201:a65e:753f:842e:d958:8487:edc7:ef9e]:8080/{message}@{number}@{token}",timeout=10)
                        if reqloop.text == "OK":
                            print("Отправлено")
                            break
                        else:
                            print(f"Ошибка, пытаемся снова ({reqloop.text})")
                            time.sleep(3)

