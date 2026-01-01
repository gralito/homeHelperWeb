setCurrentCollectionTitle();
// setEmptyFields();

document.body.addEventListener("htmx:load", function(event) {
    setCurrentCollectionTitle();
    setEmptyFields();
})

