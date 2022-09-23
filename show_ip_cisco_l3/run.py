# eel
import eel
# Импортируем модуль connect
from show_ip_cisco_l3.connect_to_device import connect
# Импортируем декоратор
from show_ip_cisco_l3.decorators.save_dataset import save_dataset
#
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
eel.start('index.html', mode="chrome", size=(1000, 320))
#
if __name__ == '__main__':
    save = '/home/asumin/web-app/eel_app/show_ip_cisco_l3/dataset/save_dataset'
    pass
    #print(run(save))