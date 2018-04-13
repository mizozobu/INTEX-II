$(function() {
    //fade effect
    $('.cover-container').hide();

    $('.product').on('mouseenter', event => {
        name = $(event.currentTarget).find('.name').text()
        $(event.currentTarget).find('.price').fadeOut();
        $(event.currentTarget).animate({
            opacity: '0.5',
        });
        $(event.currentTarget).find('.cover-container').slideDown();
    })
    $('.product').on('mouseleave', event => {
        $(event.currentTarget).find('.price').fadeIn();
        $(event.currentTarget).animate({
            opacity: '1',
        });
        $(event.currentTarget).find('.cover-container').slideUp();
    })
});
