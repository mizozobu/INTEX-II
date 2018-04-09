$(function(context){
    return function(){
        var content = $('#democontainer')
        content.load('/catalog/demo.inner')
    }
}(DMP_CONTEXT.get()))
