function getCollectionFromUrl() {
    let url = new URL(window.location.href);
    let searchParams = url.searchParams;
    return searchParams.get('collection');
}

function setCurrentCollectionTitle () {
    buttons = document.querySelectorAll(".todolist-collection-button");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            let title = document.body.getElementsByClassName("todolist-current-collection")[0];
            title.innerText = button.innerText;
            console.log("click");
        })            
    });
}