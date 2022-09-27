from datetime import datetime
# eel
import eel
# Импортируем модуль connect
from show_ip_cisco_l3.connect_to_device import connect
# Импортируем декоратор
from show_ip_cisco_l3.decorators.save_dataset import save_dataset
#
path = '/home/asumin/web-app/eel_app/show_ip_cisco_l3/dataset/save_dataset'
eel.init('web')
#
@save_dataset
def run(save_file: str):
    # создаем экземпляр кдасса Device
    dev = connect.Device('linux', '127.0.0.1', 'asumin', 'demon')
    # Получаем dataset
    dataset = dev.runCommands(['lsof -i'])
    return dataset
#
@eel.expose
def getDataPy(ip_device, mac):
    if len(mac) != 0:
        dt = datetime.now().replace(microsecond=0)  # Убираем микросекунды
        # создаем экземпляр кдасса Device
        dev = connect.Device('cisco', ip_device, 'admin', '2xm9sD')
        # Получаем dataset
        dataset = dev.runCommands([f'sh arp | i {mac}'])
        if len(dataset.strip()) == 0:
            # Передаем аргументы и вызываем ф-цию из JS
            return eel.getDataJs(dataset.strip(), mac)
        else:
            # Сохраняем в файл
            with open(path, 'a') as file:
                file.write(f"[{dt}]\n{dataset}\n\n")
            print(f"[ok] -> Сохранено в {path}")
            # Передаем аргументы и вызываем ф-цию из JS
            return eel.getDataJs(dataset.strip(), mac)
    else:
        # Передаем аргументы и вызываем ф-цию из JS
        return eel.getDataJs('', '???')
#
eel.start('index.html', mode="chrome", size=(1000, 320))
#
if __name__ == '__main__':
    pass