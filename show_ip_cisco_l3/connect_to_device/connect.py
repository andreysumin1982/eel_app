#
from netmiko import (ConnectHandler, SSHDetect,
                     NetmikoTimeoutException,
                     NetmikoAuthenticationException)
import time
from datetime import datetime
#
error_file = '/home/asumin/web-app/eel_app/show_ip_cisco_l3/error/error.txt'
#
class Device:
    def __init__(self, device, ip, username, password = None, secret = None):
        self.device = device
        self.ip = ip
        self.username = username
        self.password = password or None
        self.secret = secret or None
    #
    def runCommands(self, commands: list) -> str:
        # Параметры подключения
        device_type = {'linux': 'linux', 'cisco': 'cisco_ios', 'cisco_asa': 'cisco_asa'}
        device_param = {
            'device_type': None,
            'host': f'{self.ip}',
            'user': f'{self.username}',
            'password': f'{self.password}',
            'secret': f'{self.secret}'
            }
        # Подключаемся к Устройству
        try:
            if self.device in device_type:
                device_param['device_type'] = device_type[self.device]
            #
            with ConnectHandler(device_type=device_param['device_type'],
                                ip=device_param['host'],
                                username=device_param['user'],
                                password=device_param['password'],
                                secret=device_param['secret']) as ssh:
                time.sleep(1)  # Пауза
                dataset = ''
                # Выполняем
                for command in commands:
                    result = ssh.send_command(command)
                    dataset += (f"{result}\n")
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
        print(f"[dataset] -> {dataset}")
        with open(save_file, 'w') as file:
            for item in dataset:
                file.write(''.join(item) + '\n')
#

#
if __name__ == '__main__':
    pass
