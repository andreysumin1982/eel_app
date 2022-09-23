/*Событие на кнопку 'найти' */
const container_btn = document.querySelector('.container_btn');
const container_output = document.querySelector('.container_output');
const container_input = document.querySelector('.input');
const select_list = document.querySelector('.select_list')

/* */
cisco_l3 = {
    'AUK': 'AUK-2-1-1.oz.ru',
    'PK1': 'PK1-1-3-1',
    'VNIIRA': 'VNIIRA-2-1-1',
    'VNRPSK': 'VNRPSK-3-1-1.oz.ru',
    'ABK4': 'ABK4-1-2-1',
    'RIRV': 'RIRV-2-1-1',
    'PK2': 'Node37-2',
    'UKS': 'Node37-3',
    '51': 'Node37-4',
    'OKS': 'Node37-5',
    'IK8': 'IK-1-1-1',
    '16 ЦЕХ': '16-1-1-1',
    '48 ЦЕХ': 'node4.oz.ru',
    '69 ЦЕХ': 'node5.oz.ru',
    'ГП': 'GP-0-1-1',
    'Бассейн': 'DS-3-1-1.oz.ru'
};

/* Заполняем  <select>..</select> */
let count = 1;
for (let [key, value] of Object.entries(cisco_l3)) {
    //console.log(`${key}, ${value}`)
    addElement('option', '.select_list', `opt select_${count}`, NaN, `${key} -> ${value}`)
    count++
};

/* Обработчик события: выбираем коммутатор */
let opt = document.querySelectorAll('.opt')
opt.forEach(elem => {
    elem.addEventListener('click', () => {
        if (elem.value == 0) {
            container_btn.style.display = 'none'
        }
        else {
            console.log(elem.innerText)
            container_btn.style.display = 'block'
            container_btn.addEventListener('click', () => {
                //console.log(container_btn.innerHTML)
                container_output.innerHTML = ''
                container_btn.innerHTML = 'Ищем..'

                // Отбираем коммутатор, mac -> передаем (python ф-цию)
                console.log(`${(select_list.value).split(' -> ')[1]}, ${container_input.value}`)

                /*Вызываем ф-цию  из python*/
                //eel.showip(container_input.value)
                //eel.showNetstat()
                //eel.showCommand(container_input.value)
                //console.log(result)
            });
        }
    })
});



/* */
// container_btn.addEventListener('click', () => {
//     //console.log(container_btn.innerHTML)
//     container_output.innerHTML = ''
//     container_btn.innerHTML = 'Ищем..'

//     // Отбираем коммутатор, mac -> передаем (python ф-цию)
//     console.log(`${(select_list.value).split(' -> ')[1]}, ${container_input.value}`)

//     /*Вызываем ф-цию  из python*/
//     //eel.showip(container_input.value)
//     //eel.showNetstat()
//     //eel.showCommand(container_input.value)
//     //console.log(result)
// });

/* ! Подготавливаем ф-цию getData(data) для вызова из python  */
//eel.expose(getData)
function getData(data, mac = NaN) {
    console.log(data.length)
    if (data.length != 0) {
        data.forEach(element => {
            // console.log(element)
            //console.log(`${element[0]} ${element[1]} ${element[2]}`)
            console.log(`${element}`)
            container_output.innerHTML += `${element} <br> `
        });
        container_btn.innerHTML = 'Найти'
    }
    else {
        container_output.innerHTML = `Ничего нет по адресу ${mac}`
        container_btn.innerHTML = 'Найти'
    }
};
/* */