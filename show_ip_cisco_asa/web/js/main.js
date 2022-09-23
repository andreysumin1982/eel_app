/*Событие на кнопку 'найти' */
const container_btn = document.querySelector('.container_btn');
const container_output = document.querySelector('.container_output');
const container_input = document.querySelector('.input');
/* */

container_btn.addEventListener('click', () => {
    //console.log(container_btn.innerHTML)
    container_output.innerHTML = ''
    container_btn.innerHTML = 'Ищем..'
    /*Вызываем ф-цию showip из python*/
    eel.showip(container_input.value)
    //console.log(result)
});

/* Вызов ф-цию getData(data) из python  */
eel.expose(getData)
function getData(data, mac = NaN) {
    console.log(data.length)
    if (data.length != 0) {
        data.forEach(element => {
            // console.log(element)
            console.log(`${element[0]} ${element[1]} ${element[2]}`)
            container_output.innerHTML += `${element[0]} ${element[1]} ${element[2]} <br> `
        });
        container_btn.innerHTML = 'Найти'
    }
    else {
        container_output.innerHTML = `Ничего нет по адресу ${mac}`
        container_btn.innerHTML = 'Найти'
    }
};
/* */