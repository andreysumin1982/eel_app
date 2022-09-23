#
import eel
#
eel.init('web')
#
@eel.expose
def show_py(a,b):
    print ((a+b)*10)

def summ(*args):
    result = 0
    for item in args:
        result += item * 0.5
    return result

eel.get_data_js(summ(300,5,890,122,234,556,1,0.5,500,2324))

eel.start('index.html', mode="chrome", size=(1000, 320))