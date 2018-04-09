$(function(context) {
    return function() {
        $('.small-image').on('mouseenter', event => {
            let src = $(event.currentTarget).find('img').attr('src');
            let alt = $(event.currentTarget).find('img').attr('alt');
            $('img.big-image').attr({
                'src': src,
                'alt': alt,
            });
        });
    };
}(DMP_CONTEXT.get()));
