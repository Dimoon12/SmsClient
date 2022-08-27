import asyncio
import requests
from aioconsole import ainput

numbers = []
version = "1.0.0"
###
# Переключите на True и вам будут совать ссылки на справку по ошибке которая выскочила
linkon = False

####

# import token from file
with open("token.txt", "r") as f:
    token = f.read()


def response(serverresponse):
    if serverresponse == "OK":
        print("Отправлено")
        return "ok"
    elif serverresponse == "F_ASS_DIED":
        fault("Ошибка отправки, пытаюсь повторно", "DEBG", "F_ASS_DIED")
        return "repeat"
    else:
        fault(f"Ошибка отправки. Прерываюсь", "WARN", f"{serverresponse}")
        return "fail"


# обработка команд
def command(command):
    if command == "/exit":
        return False
    elif command == "/help":
        print("/exit - ввод номера")
        print("/help - помощь")
    else:
        print("Неизвестная команда")


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


async def sendtask():
    await asyncio.sleep(5)
    print("loop running")
    if numbers != []:
        tempnumber = numbers[0].split(":")
        number = tempnumber[0]
        message = tempnumber[1]
        responseraw = requests.get(f"http://[201:a65e:753f:842e:d958:8487:edc7:ef9e]:8080/{message}@{number}@{token}",
                                   timeout=2)
        if response(responseraw.text) == "OK":
            numbers.remove(numbers[0])
            print(f"Отправлено {message} на {number}")


async def main():
   while True:
       exitloop = False
       number = await ainput("Номер ")
       while True:
           if exitloop == True: break
           exitloop = False
           message = await ainput(">>> ")
           checkinet()
           if message[0] == "/" and command(message) == False:
               exitloop = True
               break
           else:
               numbers.append(f"{number}:{message}")
asyncio.run(sendtask())
asyncio.run(main())