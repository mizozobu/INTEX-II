function onReady(callback) {
    var intervalID = window.setInterval(checkReady, 1000);

    function checkReady() {
        if (document.getElementsByTagName('body')[0] !== undefined) {
            window.clearInterval(intervalID);
            callback.call(this);
        }
    }
}

function show(id, value) {
    document.getElementById(id).style.display = value ? 'block' : 'none';
}

function showtag(tag, value) {
    document.getElementsByTagName(tag)[0].style.display = value ? 'block' : 'none';
}

onReady(function () {
    show('page', true);
    show('loader-container', false);
    showtag('footer', true);
});
