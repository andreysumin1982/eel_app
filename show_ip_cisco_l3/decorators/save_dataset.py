#
from datetime import datetime

# Создаем декоратор для сохранения dataset в файл.
def save_dataset(func):
    path = '/home/asumin/web-app/eel_app/show_ip_cisco_l3/dataset/save_dataset'
    def inner(*args, **kwargs):
        dt = datetime.now().replace(microsecond=0)  # Убираем микросекунды
        result = func(*args, **kwargs)
        with open(path, 'a') as file:
            file.write(f"[{dt}]{result}\n\n")
        print(f"[ok] -> Сохранено в {path}")
        return result

    return inner
#

#
if __name__ == '__main__':
    pass