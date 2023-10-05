// selectors
const Entry = document.querySelector('.todo');
const Button = document.querySelector('.Add');
const List = document.querySelector('.todo-list');
const Save = document.querySelector('.save')




// Event Listeners
Button.addEventListener('click', addtodo);
List.addEventListener('click', DeletCheck);








// functions
function addtodo(event) {
    event.preventDefault();
    // todo div
    const tododiv = document.createElement("div");
    tododiv.classList.add("todo-div")
    //  creat li
    const newtodo = document.createElement("li")
    newtodo.innerText = Entry.value;
    newtodo.classList.add("todo-item")
    tododiv.appendChild(newtodo)

    // check mark button
    const checkButton = document.createElement("button");
    checkButton.innerText = "Done";
    checkButton.classList.add("check-btn")
    tododiv.appendChild(checkButton)
    // check mark button
    const trashButton = document.createElement("button");
    trashButton.innerText = "Trash";
    trashButton.classList.add("trash-btn")
    tododiv.appendChild(trashButton)

    // append to list
    List.appendChild(tododiv);
    // clear to do input
    Entry.value = ""
};

function DeletCheck(e) {
    const item = e.target;
    // const tododiv = document.querySelector('.todo-div')
    // delet to do
    if (item.classList[0] === "trash-btn") {
        const todo = item.parentElement;
        todo.classList.add("fall")
        todo.addEventListener("transitionend", function(){
            todo.remove();
        });
    }


    if (item.classList[0] === "check-btn") {
        const todo = item.parentElement;
        todo.classList.toggle("Completed");
    }
};
