/*Событие на кнопку 'найти' */
const container_btn = document.querySelector('.container_btn');
const container_output = document.querySelector('.container_output');
const container_input = document.querySelector('.input');
const select_list = document.querySelector('.select_list')

/* */
cisco_l3 = {
    'AUK': 'iAUK-2-1-2',
    'PK1': 'PK1-1-3-1',
    'VNIIRA': 'VNIIRA-2-1-1',
    'VNRPSK': 'VNRPSK-3-1-1',
    'ABK4': 'ABK4-1-2-1',
    'RIRV': 'RIRV-2-1-1',
    'PK2': 'Node37-2',
    'UKS': 'Node37-3',
    '51': 'Node37-4',
    'OKS': 'Node37-5',
    'IK8': 'IK-1-1-1',
    '16 ЦЕХ': '16-1-1-1',
    '48 ЦЕХ': 'node4',
    '69 ЦЕХ': 'node5',
    'ГП': 'GP-0-1-1',
    'Бассейн': 'DS-3-1-1'
};

/* Заполняем  <select>..</select> */
let count = 1;
for (let [key, value] of Object.entries(cisco_l3)) {
    //addElement('option', '.select_list', 'op', `option_${count}`, NaN, `${key} -> ${value}`)
    let childElement = document.createElement('option')
    childElement.type = NaN
    childElement.id = 'op'
    childElement.className = `option_${count}`
    childElement.value = `${value}`
    childElement.innerHTML = `${key} -> ${value}`
    document.querySelector('.select_list').appendChild(childElement)
    count++
};
//

/* Обработчик события : выбираем коммутатор */
let btn = document.querySelector('.select_list')
//console.log(btn)
btn.addEventListener('change', function () {
    // выбираем <option>
    if (this.value == 0) {
        container_btn.style.display = 'none'
    }
    else {
        //console.log(this.value)
        container_btn.style.display = 'block'
    }
});
//

//
container_btn.addEventListener('click', () => {
    //console.log(container_btn.innerHTML)
    container_output.innerHTML = ''
    container_btn.innerHTML = 'Ищем..'

    // Отбираем коммутатор, mac -> передаем (python ф-цию)
    console.log(`${select_list.value}, ${container_input.value}`)

    /*Вызываем ф-цию  из python*/
    eel.getDataPy(`${select_list.value}`, `${container_input.value}`)
})
//

/* ! Подготавливаем ф-цию getData(data) для вызова из python  */
eel.expose(getDataJs)
function getDataJs(data, mac) {
    //console.log(data.length)
    if (data.length != 0) {
        result = data.split('\n').filter(Boolean)
        //container_output.innerHTML = `${data} <br> `
        result.forEach(element => {
            elem = element.split(' ').filter(Boolean)
            //console.log(elem[1], elem[3], elem[5])
            container_output.innerHTML += `${elem[1]}  ${elem[3]}  ${elem[5]} <br>`
        });

        container_btn.innerHTML = 'Найти'
    }
    else {
        container_output.innerHTML = `Ничего нет по адресу ${mac}`
        container_btn.innerHTML = 'Найти'
    }
};
/* */