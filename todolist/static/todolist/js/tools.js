function getCollectionFromUrl() {
    let url = new URL(window.location.href);
    let searchParams = url.searchParams;
    return searchParams.get('collection');
}


function setCurrentCollectionTitle () {
    let buttons = document.querySelectorAll(".todolist-nav-button");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            let title = document.body.getElementsByClassName("todolist-current-collection")[0];
            title.innerText = button.innerText;
            console.log("click");
        });            
    });
}


function setEmptyFields () {
    let buttons = document.querySelectorAll(".todolist-button-add");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            let inputFields = document.body.getElementsByClassName("todolist-input-add");
            console.log(inputFields);
            Array.prototype.forEach.call(inputFields, (input) => {
                input.value = "";
            })
        });
    });
}