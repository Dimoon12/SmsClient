import time
import requests

###
# Переключите на True и вам будут совать ссылки на справку по ошибке которая выскочила
linkon = False
####

# обработка ошибок
def fault(failuretext, errortype, errcode):
    if errortype == "CRIT":
        print(f"[КРИТ] Программа будет закрыта Т.К восстановить работоспособность не удалось. ({failuretext})")
        if linkon:
            print(f"https://github.com/Dimoon12/SmsClient/wiki/{errcode}")
        exit()
    elif errortype == "WARN":
        print(f"[ПРЕД] Предупреждение, {failuretext}")
        if linkon:
            print(f"https://github.com/Dimoon12/SmsClient/wiki/{errcode}")

# проверка яжки и инета
def checkinet():
    try:
        requests.get("http://[21e:a51c:885b:7db0:166e:927:98cd:d186]", timeout=4)
        return True
    except Exception:
        fault("сетевой Yggdrasil сервис недоступен", "CRIT", "Yggdrasil_unavaible")


# import token from file
with open("token.txt", "r") as f:
    token = f.read()
while True:
    checkinet()
    number = input("Номер:")
    while True:
        message = input("(YOU)")
        if message[0] == "/":
            if message == "/exit":
                break
            elif message == "/help":
                print("/exit - ввод номера")
                print("/help - помощь")
            else:
                print("Неизвестная команда")
        else:
            resp = requests.get(f"http://[201:a65e:753f:842e:d958:8487:edc7:ef9e]:8080/{message}@{number}@{token}", timeout=10)
            if not resp.text == "OK":
                 while True:
                    reqloop = requests.get(f"http://[201:a65e:753f:842e:d958:8487:edc7:ef9e]:8080/{message}@{number}@{token}", timeout=10)
                    if reqloop.text == "OK":
                        print("Отправлено")
                        break
                    elif reqloop.text == "F_ASS_DIED":
                        fault(f"Ошибка сервера, повторяем попытку", "WARN", f"{reqloop.text}")
                        time.sleep(3)
                    else:
                        fault(f"проверьте ввод ({reqloop.text})", "WARN", f"{reqloop.text}")
                        break
