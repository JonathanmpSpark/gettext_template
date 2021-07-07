from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _, ngettext

def agregar_al_carrito(request):
    cantidad = request.GET['cantidad']
    
    if str.isdigit(cantidad):
        cantidad = int(cantidad)
        message = ngettext('{cantidad} articulo agregado', '{cantidad} articulos agregados', cantidad).format(cantidad=cantidad)
    else:
        message = _('Ingresa un valor numérico')

        
    response = {
        'message': message,
    }

    return JsonResponse( response )