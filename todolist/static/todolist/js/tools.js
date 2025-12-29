function getCollectionFromUrl() {
    let url = new URL(window.location.href);
    let searchParams = url.searchParams;
    return searchParams.get('collection');
}