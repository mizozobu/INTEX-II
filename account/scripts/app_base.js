$(function(context) {
    return function() {
        //log in dropdown
        $('.dropdown-toggle').on('click', () => {
            $('.dropdown-menu').toggle();
        });

        let hilighted = false;
        for (i = 0; i < $('.cat').length; i++) {
            if($($('.cat')[i]).css('backgroundColor') == 'rgb(242, 242, 242)') {
                hilighted = true;
                break;
            };
        };
        if(!hilighted && document.location.href.includes('catalog/index')) {
            $('#all-product').addClass('active');
        };
    };
}(DMP_CONTEXT.get()));
