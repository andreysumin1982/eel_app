#
from connect.connect import Cisco
#
def run():
    commands = ['sh version', 'sh int des', 'sh int counters']
    #
    sw = Cisco('iVNRa-8-1-2', 'admin', '2xm9sD')
    ssh_result = sw.setCommands(commands)
    #
    sw.saveFile(ssh_result, save_file)
#
def pricessing(file_json):
    with open(file_json) as file:
        res = file.readlines()
    for item in res:
        print(item)

#
if __name__ == '__main__':
    save_file = '/home/asumin/web-app/eel_app/show_ip_cisco_asa/dataset/dataset.txt'
    #run()
    pricessing(save_file)