REPLACE_TRANSLATE_FUNCTS = {
    'hola_mundo': (id) => {
        $(`#${id}`).text(gettext('Hola Mundo'));
    },
    'pais': (id) => {
        $(`#${id}`).text(pgettext('país', 'Estado'));
    },
    'estatus': (id) => {
        $(`#${id}`).text(pgettext('estatus', 'Estado'));
    },
    'carrito': (id) => {
        var qty = $('#id_cantidad').val();
        var message = ''
        if($.isNumeric(qty))
            message = interpolate(
                ngettext('%s articulo agregado', '%s articulos agregados', qty),
                [qty]
            )
        else
            message = gettext('Ingresa un valor numérico')

        $('.response-area').append($('<p>', { text: message }));
        $('#id_cantidad').val('');
        console.log(`message: ${message}`);
    }
}

$('.replace_translate').on('click', function(event, elem){
    var id = $(this).attr('id');
    REPLACE_TRANSLATE_FUNCTS[id](id);
})
