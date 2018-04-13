// update button
$('#server-time-button').click(function() {
    $('.server-time').load('/homepage/ajax/gettime/');
});
