$(function(context) {
    return function() {
        //log in dropdown
        $('.dropdown-toggle').on('click', () => {
            $('.dropdown-menu').toggle();
        });
    };
}(DMP_CONTEXT.get()));
