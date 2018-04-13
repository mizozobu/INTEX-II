$(function(context) {
    return function() {
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

        //ajax and page number
        let current_page = Number($('#current-page').text());
        if (current_page === 1){
            $('#left-arrow').hide();
        }
        else if (current_page === Number($('#last-page').text())){
            $('#right-arrow').hide();
        }

        $('#left-arrow').on('click', () => {
            let URL = "/catalog/index.products/" + context.category_id_js + "/";
            let current_page = Number($('#current-page').text());
            current_page -= 1;
            URL += current_page;
            $('#products').load(URL);
            $('#current-page').text(current_page );
            $('#right-arrow').show();
            if (current_page === 1){
                $('#left-arrow').hide();
            }
        });

        $('#right-arrow').on('click', () => {
            let URL = "/catalog/index.products/" + context.category_id_js + "/";
            let current_page = Number($('#current-page').text());
            current_page += 1;
            URL += current_page;
            $('#products').load(URL);
            $('#current-page').text(current_page);
            $('#left-arrow').show();
            if (current_page === Number($('#last-page').text())){
                $('#right-arrow').hide();
            }
        });
    };
}(DMP_CONTEXT.get()));
