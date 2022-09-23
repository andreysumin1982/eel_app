#
from datetime import datetime

# Создаем декоратор для сохранения dataset в файл.
def save_dataset(func):

    def inner(*args, **kwargs):
        dt = datetime.now().replace(microsecond=0)  # Убираем микросекунды
        result = func(*args, **kwargs)
        with open(args[0], 'a') as file:
            file.write(f"[{dt}]{result}\n\n")
        print(f"[ok] -> Сохранено в {args[0]}")
        return result

    return inner
#

#
if __name__ == '__main__':
    pass