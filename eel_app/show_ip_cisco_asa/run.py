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
        sw = Cisco('ip', '***', '***')
        command = [f"sh arp | i {mac}"]
        dataset = sw.setCommands(command)
        sw.saveFile(dataset, save_file)
        return pricessing(save_file, mac)
    except Exception as error:
        print(f"[ERROR] -> {error}")
#
def pricessing(save_file, mac: str) -> list:
    try:
        with open(save_file) as file:
            result = list(map(lambda x : [x.split()[1], x.split()[-3], x.split()[-1]], file.readlines()))
            print(f"[OK] -> {result}"); return eel.getData(result)
    except Exception as ERROR:
        print(f"[INFO] -> Ничего нет по адресу {mac}")
        dateTime = datetime.now().replace(microsecond=0)  # Убираем микросекунды
        with open(error_file, 'a') as file_error:
            file_error.write(f"{dateTime}\n[ERROR] -> {ERROR}\n\n")

#
eel.start('index.html', mode="chrome", size=(1000, 320))
#
if __name__ == '__main__':
    pass
    #save_file = '/home/asumin/web-app/eel_app/show_ip_cisco_asa/dataset/dataset.txt'
    #run()
    #pricessing(save_file)
    #showip('41')
