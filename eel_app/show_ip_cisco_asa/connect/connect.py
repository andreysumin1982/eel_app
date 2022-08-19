#
from netmiko import (ConnectHandler,
                     NetmikoTimeoutException,
                     NetmikoAuthenticationException)
import time
import json
#import re
#
class Cisco:
    def __init__(self, ip, username, password = None, secret = None):
        self.ip = ip
        self.username = username
        self.password = password or None
        self.secret = secret or None
    #
    def setCommands(self, commands: list):
        # Параметры подключения
        cisco = {
            'device_type': 'cisco_ios',
            'host': f'{self.ip}',
            'user': f'{self.username}',
            'password': f'{self.password}',
            'secret': f'{self.secret}'
            }
        # Подключаемся к коммутатору
        with ConnectHandler(device_type=cisco['device_type'],
                            ip=cisco['host'],
                            username=cisco['user'],
                            password=cisco['password'],
                            secret=cisco['secret']) as ssh:
            # Выполняем
            time.sleep(1)  # Пауза
            output = {}
            for command in commands:
                result = ssh.send_command(command)
                output[f"{command}"] = result.split('\n')
                time.sleep(1)
        return output
    #
    def saveFile(self, dataset: dict, save_file) -> json:
        with open(save_file, 'w') as file:
            json.dump(dataset, file)


#
if __name__ == '__main__':
    pass