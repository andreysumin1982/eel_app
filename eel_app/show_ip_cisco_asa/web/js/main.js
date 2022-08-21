/*Событие на кнопку 'найти' */
const container_btn = document.querySelector('.container_btn')
const container_output = document.querySelector('.container_output')

let counter = 0
container_btn.addEventListener('click', ()=> {
    console.log(counter++)
    container_output.innerHTML = `${counter}`
})
