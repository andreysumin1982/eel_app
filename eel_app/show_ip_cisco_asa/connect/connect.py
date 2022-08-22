#
from netmiko import (ConnectHandler,
                     NetmikoTimeoutException,
                     NetmikoAuthenticationException)
import time
from datetime import datetime
#
error_file = '/home/asumin/web-app/eel_app/show_ip_cisco_asa/error/error.txt'
#
class Cisco:
    def __init__(self, ip, username, password = None, secret = None):
        self.ip = ip
        self.username = username
        self.password = password or None
        self.secret = secret or None
    #
    def setCommands(self, commands: list) -> list:
        # Параметры подключения
        cisco = {
            'device_type': 'cisco_ios',
            'host': f'{self.ip}',
            'user': f'{self.username}',
            'password': f'{self.password}',
            'secret': f'{self.secret}'
            }
        # Подключаемся к коммутатору
        try:
            with ConnectHandler(device_type=cisco['device_type'],
                                ip=cisco['host'],
                                username=cisco['user'],
                                password=cisco['password'],
                                secret=cisco['secret']) as ssh:
                time.sleep(1)  # Пауза
                dataset = []
                # Выполняем
                for command in commands:
                    result = ssh.send_command(command)
                    dataset.append(result)
                    time.sleep(1)
            return dataset
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as ERROR:
            print(f"[ERROR] -> {ERROR}");
            dateTime = datetime.now().replace(microsecond=0)  # Убираем микросекунды
            with open(error_file, 'a') as file_error:
                file_error.write(f"{dateTime}\n[ERROR] -> {ERROR}\n\n")
        exit(0)
    #
    def saveFile(self, dataset, save_file: str):
        with open(save_file, 'w') as file:
            for item in dataset:
                file.write(''.join(item) + '\n')


#
if __name__ == '__main__':
    pass
