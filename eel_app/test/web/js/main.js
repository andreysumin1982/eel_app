/* */
let res = eel.show_py(2,3)
/* */
eel.expose(get_data_js)
function get_data_js(data){
    document.querySelector('.container_output').innerHTML = `${data}`
}
