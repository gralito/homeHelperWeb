setCurrentCollectionTitle();
document.body.addEventListener("htmx:load", function(event) {
    setCurrentCollectionTitle();
})