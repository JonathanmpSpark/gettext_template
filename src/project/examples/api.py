from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _, ngettext

def add_to_cart(request):
    qty = request.GET['qty']
    
    if str.isdigit(qty):
        qty = int(qty)
        message = ngettext('{qty} articulo agregado', '{qty} articulos agregados', qty).format(qty=qty)
    else:
        message = _('Ingresa un valor numérico')

        
    response = {
        'message': message,
    }

    return JsonResponse( response )