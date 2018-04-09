$(function(){
    $('.bulk').parent().hide()
    $('.rental').parent().hide()
    $('#id_type').change(function(){
        $('.bulk').parent().hide()
        $('.rental').parent().hide()

        if ($('#id_type').val() == '1') {
            $('.bulk').parent().show()
        }
        else if ($('#id_type').val() == '2') {
            $('.individual').parent().show()
        }
        else if ($('#id_type').val() == '3') {
            $('.rental').parent().show()
        }
    })
})
