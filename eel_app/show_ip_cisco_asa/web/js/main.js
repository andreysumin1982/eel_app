/*Событие на кнопку 'найти' */
const container_btn = document.querySelector('.container_btn')
const container_output = document.querySelector('.container_output')
const container_input = document.querySelector('.input')

container_btn.addEventListener('click', () => {
    console.log(container_input.value)

    let res = eel.showip(container_input.value)
})
/* Вызов ф-цию из python  */
eel.expose(getData)
function getData(data) {
    console.log(data)
}