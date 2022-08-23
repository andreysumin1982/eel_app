#
import eel
from datetime import datetime
from connect.connect import Cisco
#
eel.init('web')
#
save_file = '/home/asumin/web-app/eel_app/show_ip_cisco_asa/dataset/dataset.txt'
error_file = '/home/asumin/web-app/eel_app/show_ip_cisco_asa/error/error.txt'
#
@eel.expose
def showip(mac: str):
    try:
        sw = Cisco('192.168.220.254', '***', '***')
        command = [f"sh arp | i {mac}"]
        dataset = sw.setCommands(command)
        sw.saveFile(dataset, save_file)
        return pricessing(save_file, mac)
    except Exception as ERROR:
        print(f"[ERROR] -> {ERROR}")
        dateTime = datetime.now().replace(microsecond=0)  # Убираем микросекунды
        with open(error_file, 'a') as file_error:
            file_error.write(f"{dateTime}\n[ERROR] -> {ERROR}\n\n")
#
def pricessing(save_file, mac: str) -> list:
    try:
        with open(save_file) as file:
            dataset = list(map(lambda x : [x.split()[1], x.split()[-3], x.split()[-1]], file.readlines()))
            print(f"[OK] -> {dataset}"); return eel.getData(dataset) # Передаем аргументы и вызываем ф-цию из JS
    except Exception as ERROR:
        print(f"[INFO] -> Ничего нет по адресу '{mac}'")
        dateTime = datetime.now().replace(microsecond=0)  # Убираем микросекунды
        with open(error_file, 'a') as file_error:
            file_error.write(f"{dateTime}\n[ERROR] -> {ERROR}\n\n")
        eel.getData([], mac)  # Передаем аргументы и вызываем ф-цию из JS

#
eel.start('index.html', mode="chrome", size=(1000, 320))
#
if __name__ == '__main__':
    pass
    #save_file = '/home/asumin/web-app/eel_app/show_ip_cisco_asa/dataset/dataset.txt'
    #run()
    #pricessing(save_file)
    #showip('41')
