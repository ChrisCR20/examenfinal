from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.contrib import messages
from .forms import CompraForm
from compra.models import Usuario, Compra

def compra_nueva(request):
    if request.method == "POST":
        formulario = CompraForm(request.POST)
        if formulario.is_valid():
            compra = Usuario.objects.create(nombre=formulario.cleaned_data['nombre'], dpi = formulario.cleaned_data['dpi'])
            for producto_id in request.POST.getlist('productos'):
                compra = Compra(producto_id=producto_id, usuario_id = compra.id)
                compra.save()
            messages.add_message(request, messages.SUCCESS, 'Compra Realizada Exitosamente')
    else:
        formulario = CompraForm()
    return render(request, 'compra/compra_editar.html', {'formulario': formulario})
