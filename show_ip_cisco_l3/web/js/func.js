//
function addElement(child, parent = 'body', id = 'no_id', classChild = 'no_class', type = NaN, text = '') {
    /*Ф-ция создает элемент на странице:
        На вход подаются 1 обязятельный элемент и 3 не обязательных:
     Дочерний (div, p, li ...), класс для дочернего элемента , родительский элемент - ('.classname'), тип дочернего элемента.
     По умолчинию все элементы создаются в теле документа body.
     */
    let childElement = document.createElement(child)
    childElement.type = type
    childElement.id = id
    childElement.className = classChild
    childElement.innerHTML = text
    document.querySelector(parent).appendChild(childElement)
};
//
function addButton(child, parent = 'body', id = 'no_id', classChild = 'no_class', type = NaN, value = '') {
    /*Ф-ция создает элемент на странице:
        На вход подаются 1 обязятельный элемент и 3 не обязательных:
     Дочерний (div, p, li ...), класс для дочернего элемента , родительский элемент - ('.classname'), тип дочернего элемента.
     По умолчинию все элементы создаются в теле документа body.
     */
    let childElement = document.createElement(child)
    childElement.type = type
    childElement.id = id
    childElement.className = classChild
    childElement.value = value
    document.querySelector(parent).appendChild(childElement)
};
